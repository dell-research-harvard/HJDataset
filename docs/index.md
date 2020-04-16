---
layout: project
show_nav: false

title: "HJDataset : A Large Dataset of Historical Japanese Documents with Complex Layouts"
authors: 
- {name: "Zejiang Shen", afffilation: "Harvard University", email: "zejiang_shen@g.harvard.edu", website: "www.zsj.io"}
- {name: "Kaixuan Zhang", afffilation: "Harvard University", email: "kaixuanzhang@fas.harvard.edu", website: ""}
- {name: "Melissa Dell", afffilation: "Harvard University", email: "melissadell@fas.harvard.edu", website: "https://scholar.harvard.edu/dell/home"}
short_name: HJDataset
teaser_fig: /assets/teaser.png
---


{% include project/teaser.html teaser_fig="/assets/teaser.png" caption="Examples of HJDataset document images and annotations. (a) to (d) show images of the four page categories, and (e) provides a simplified illustration of layout annotations for main pages. The seven types of hierarchically constructed layout elements are highlighted in different colors." %}


## Abstract 

Deep learning-based approaches for automatic document layout analysis and content extraction have the potential to unlock rich information trapped in historical documents on a large scale. One major hurdle is the lack of large datasets for training robust models. In particular, little training data exist for Asian languages. To this end, we present HJDataset, a Large Dataset of **H**istorical **J**apanese Documents with Complex Layouts. It contains over 250,000 layout element annotations of seven types. In addition to bounding boxes and masks of the content regions, it also includes the hierarchical structures and reading orders for layout elements. The dataset is constructed using a combination of human and machine efforts. A semi-rule based method is developed to extract the layout elements, and the results are checked by human inspectors. The resulting large-scale dataset is used to provide baseline performance analyses for text region detection using state-of-the-art deep learning models. And we demonstrate the usefulness of the dataset on real-world document digitization tasks. 

## Dataset 

***Notice:** We are sorry that the images are not available currently. We are working on the copyright issues and it should be released soon.*


Please check this [link](https://www.dropbox.com/s/xkjcty50862zayt/annotations.zip?dl=0) to download the dataset. You may also find the following quick notes helpful when using HJDataset.

- [Notes for Annotations](/annotation-notes.html)
- [Reading Orders And Content Hierarchy](/reading-orders-and-hierarchy.html)


## Pretained Models 

We pretrained three models over the HJDataset, namely, Faster RCNN, Mask RCNN, and RetinaNet. The implementation is based on [Detectron2](https://github.com/facebookresearch/detectron2). Besides the model weights, we also include the configuration files (`config.yml`) in the donwload links to improve reproducibility. 

| Model Name    | Faster R-CNN                                                 | Mask R-CNN                                                   | RetinaNet                                                    |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Download Link | [faster_rcnn_R_50_FPN_3x](https://www.dropbox.com/sh/jac1dtp0yogubmr/AABjWubt1PsCv88f6QjFngMAa?dl=0) | [mask_rcnn_R_50_FPN_3x](https://www.dropbox.com/sh/6wupiaqyzcyehia/AACpMiJ8eVR-Pe9yY5TMiNmga?dl=0) | [retinanet_R_50_FPN_3x](https://www.dropbox.com/sh/dtee77iapmg4ze7/AABblUG0ZXLuSkhfLDBlHUYCa?dl=0) |
| mAP (%)       | 81.991 | 81.343 | 75.223 |


## Copyright

- **Annotations** in the dataset are released under the [Community Data License Agreement – Permissive – Version 1.0 License](https://cdla.io/permissive-1-0/).
