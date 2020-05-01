import numpy as np
import pandas as pd

import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle

import cv2
from pycocotools.coco import COCO
# You have to install COCO tools 

import os
import numpy as np
import torch
from PIL import Image

from copy import deepcopy

# If you want to draw the hierarchical graphs, you 
# have to install these two libs 

import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

_colors = [ (0,0,0),        # Black - Page Frame 
            (128,128,128),  # Grey  - Row 
            (255,127,80),   # Orange- Title Region
            (0,0,255),      # Blue  - Text Region 
            (255,0,0),      # Red   - Title
            (128,0,128),    # Pink  - Subtitle
            (124,252,0)     # Green - Other 
          ]

def _draw_graph(relations, labels, box_ids, title, figsize):
    G = nx.DiGraph()
    G.add_edges_from(relations)
    
    box2color = {box_id: label for box_id, label in zip(box_ids, labels)}
    node_color = []
    for node in G.nodes():
        color = PageDataset._color_map[box2color.get(node,1)]
        node_color.append(color)
        
    pos=graphviz_layout(G, prog='dot')
    plt.figure(figsize=figsize)
    nx.draw_networkx(G, pos=pos, node_color=node_color, with_labels=True)
    plt.title(title)
    plt.show() 
    
    
class PageDataset(object):
    _color_map = {i+1: tuple(map(lambda x: x/255, item)) for i, item in enumerate(_colors)}

    def __init__(self, img_root, anno_file, 
                 selected_cats=None, 
                 target_size=None):
        """The PageDataset 

        Args:
            img_root (str): The root of the image folder
            anno_file (str): The annotation file path
            selected_cats (list[int], optional): If not None, only load 
                layout elements of the specified categories. 
                Defaults to None.
            target_size (tuple, optional): If not None, resize the loaded 
                image and annotations to the target size (height, width). 
                Defaults to None.

        Examples:

        >>> dataset = PageDataset(image_root, anno_file)
        >>> image, label_info = dataset[0]
        >>> label_info['boxes']

        """
        
        self.root = img_root
        self.coco = COCO(anno_file)
        self.indices = list(self.coco.imgs.keys())        
        self.selected_cats = self.coco.getCatIds() if selected_cats == None \
                             else selected_cats

        self.target_size = target_size

    
    def obtain_target(self, img_info, scale_x=1, scale_y=1):
        
        anns_ids = self.coco.getAnnIds(imgIds=[img_info['id']], 
                            catIds=self.selected_cats, 
                            iscrowd=None)
        anns     = self.coco.loadAnns(anns_ids)
        
        # Obtain mask
        target_h = int(img_info['height']*scale_y)
        target_w = int(img_info['width']*scale_x)
        
        
        # Obtain bbox and labels
        boxes = []
        labels = []
        hierarchical_relations = []
        sequencial_relations = []
        box_ids = []
        for ann in anns:
            bbox = ann['bbox']
            xmin = (bbox[0])*scale_x
            xmax = (bbox[0] + bbox[2])*scale_x
            ymin = (bbox[1])*scale_y
            ymax = (bbox[1] + bbox[3])*scale_y
            box_ids.append(ann['id'])
            boxes.append([xmin, ymin, xmax, ymax])
            labels.append(ann['category_id'])
            hierarchical_relations.append((ann['id'], ann['parent_id']))
            sequencial_relations.append((ann['id'], ann['next_id']))
            
        return box_ids, boxes, labels, hierarchical_relations, sequencial_relations
    
    def __getitem__(self, idx):
        
        # load image info
        img_info = self.coco.loadImgs(ids=[self.indices[idx]])[0]
        
        # Determine Rescale
        if self.target_size != None:
            target_h, target_w = self.target_size
            source_h, source_w = img_info['height'], img_info['width']
            scale_x, scale_y = target_w/source_w, target_h/source_h
        else:
            target_h, target_w = img_info['height'], img_info['width']
            scale_x, scale_y = 1,1
        
        # Load image and resize 
        img = Image.open(f"{self.root}/{img_info['file_name']}").\
                    convert("RGB").resize((target_w, target_h))
        
        # Load masks and other meta info
        box_ids, boxes, labels, hierarchical_relations, sequencial_relations = \
                         self.obtain_target(img_info, scale_x, scale_y)
        
        boxes = np.array(boxes)
        areas = (boxes[:, 3] - boxes[:, 1]) * (boxes[:, 2] - boxes[:, 0])

        target = dict(box_ids = box_ids,
                      boxes = boxes,
                      labels = labels,
                      image_id = idx,
                      area = areas,
                      hierarchy = hierarchical_relations, 
                      order = sequencial_relations)

        return np.array(img), target

    def __len__(self):
        return len(self.indices)
                                
    def show_item(self, idx, show_hierarchy=False, show_order=False):
                                 
        plt.figure(figsize=(20,30))                 
        data_item = self[idx]
        
        plt.imshow(data_item[0])
        box_ids = data_item[1]['box_ids']
        boxes = data_item[1]['boxes']
        labels = data_item[1]['labels']
        hierarchy = data_item[1]['hierarchy']
        order = data_item[1]['order']
                         
        for i in range(len(boxes)):
            box = boxes[i]
            label = labels[i]
            if label == 2:
                rect = Rectangle((box[0]-5,box[1]-5),box[2]-box[0]+10,box[3]-box[1]+10,
                             linewidth=2, edgecolor=self._color_map[label],facecolor='none')
            else:
                rect = Rectangle((box[0],box[1]),box[2]-box[0],box[3]-box[1],
                             linewidth=2, edgecolor=self._color_map[label],facecolor='none')
            plt.gca().add_patch(rect)
            if show_hierarchy or show_order:
                plt.text(box[0]-10, box[1]-10, str(hierarchy[i][0]))
                         
                             
        plt.axis('off')
        plt.show()
        
        if show_hierarchy:
            _draw_graph(relations=hierarchy, 
                       figsize=(24,8),
                       labels=labels,
                       box_ids=box_ids,
                       title='Hierarchical Relation of Layout Elements')
                         
        if show_order:
             _draw_graph(relations=order, 
                       figsize=(20,20),
                       labels=labels,
                       box_ids=box_ids,
                       title='Reading Order of Layout Elements')