# HJDataset
A Large Dataset of Historical Japanese Documents with Complex Layouts

HJDataset is a Large Dataset of **H**istorical **J**apanese Documents with Complex Layouts. It contains over 250,000 layout element annotations of seven types. In addition to bounding boxes and masks of the content regions, it also includes the hierarchical structures and reading orders for layout elements for advanced analysis. 

## Download the dataset

All the annotations are available through this [link](https://www.dropbox.com/s/xkjcty50862zayt/annotations.zip?dl=0). However, due to some copyright issues, we could not directly release the images in this dataset. Please fill out [this form](https://forms.gle/9BYYgo9bAjLnq7RQA) to send us a request for downloading, and we will send back the links. 

## Organization of the files 

After downloading, we suggest organize the annotation and images in this fashion: 

```
data/
├── train/
├── test/
├── val/
└── annotations/
    ├── instances_train.json 
    └── .... 
```

## Environment configuration  

You can also use the provided conda environment file to configure your own environment. 

```
conda install -f environment.yml
```

However, when installing [Detectron2](https://github.com/facebookresearch/detectron2), you may encounter some problems. Please check their [official install instructions](https://github.com/facebookresearch/detectron2/blob/master/INSTALL.md) and [Common Installation Issues](https://github.com/facebookresearch/detectron2/blob/master/INSTALL.md#common-installation-issues) for better reference. 


## Starter code

We provide some starter code in [`notebooks/`](https://github.com/dell-research-harvard/HJDataset/notebooks). 

- `1-Dataloader and visualization.ipynb` illustrates how to use the dataloder class to load and visualize layout elements in HJDataset.
- `2-Training Using Detectron2.ipynb` shows how to train segmentation models on the dataset using Detectron2.

## Cite our work 

If you find the dataset is helpful for your research, please cite our work: 

```
@article{shen2020large,
  title={A Large Dataset of Historical Japanese Documents with Complex Layouts},
  author={Shen, Zejiang and Zhang, Kaixuan and Dell, Melissa},
  journal={arXiv preprint arXiv:2004.08686},
  year={2020}
}
```