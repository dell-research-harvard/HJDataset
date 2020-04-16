---
layout: post
show_nav: false
title: Reading Orders And Content Hierarchy
---

You can easily construct content dependency graphs or reading order graph based on the information provided in the annotations. As shown in the figure below, we generate these graphs for an example `main` page. 

- On the top right is the Hierarchical Relationship. Each node denotes a layout element, and the nodes are colored according to their categories, and the element IDs are annotated on top of the nodes. A directed edge shows the parental relationship (child element -> parent relationship). As the `page-frame` region does not  have a parent, we use `-1` to represent the end of the content tree. We can clearly observe the document structure based on the relationship figure. 
- The bottom left figure illustrates the reading order of contents. The directed edges are the sequential reading orders. For the last element on the given page, it points to `-1`, which is reserved for the *page end*. The reading order for `row` and `page frame` elements are generated separately from the other 5 types of contents. 

![](/assets/Reading Order and Dependency.png)