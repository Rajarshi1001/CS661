# CS661 (Big Data Visual Analytics)

> Assignment 1

The assignment consists of two problems, the first one involving creation of the *isocontour extraction* algorithm from a 2D scalar data of the Hurricane based on the `isovalue` provided by the user and storing it as `isocontour.vtp` polydata object in the same folder. The second problem involves rendering a 3D scalar field of the Hurricane using a custom *transfer function*, *opactiy* and optional *Phong Illumination* with the specified parameters. 

1. Question 1
```py
$ python3 soln1.py --isovalue <user_input> --visualize <yes/no>
```

2. Question 2
```py
$ python3 soln2.py --phong <yes/no>
```
> Assignment 2

he given code essentially creates a isosurface plot and histogram side by side which gets automatically updated based on a slider widget which takes all values ranging from minimum isovalues to maximum isovalues from the given 3D dataset. A `Reset` functionality is added which on clicking automatically resets the slider value, isosurface plot and histogram respectively. The number of bins used in the histogram plot is 50. 

While running the cell for displaying the interface, on clicking `Reset` button, it takes a bit of time to return to its initial configuration. 

> In order to run the code, open the `soln.ipynb` file and run the cells.
