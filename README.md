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

The given code essentially creates a isosurface plot and histogram side by side which gets automatically updated based on a slider widget which takes all values ranging from minimum isovalues to maximum isovalues from the given 3D dataset. A `Reset` functionality is added which on clicking automatically resets the slider value, isosurface plot and histogram respectively. The number of bins used in the histogram plot is 50. 

While running the cell for displaying the interface, on clicking `Reset` button, it takes a bit of time to return to its initial configuration. 

> In order to run the code, open the `soln.ipynb` file and run the cells.

> Assignment 3

The given code essentially generates a streamline pattern from a `tornado3d_vector.vti` file using the standard **4th order Runge-Kutta** algorithm inorporating both forward and backward integration from the seed followed by interpolation to generate vectors required for pth reconstruction from the input 3D seed position entered by the user as an argument. The code saves the streamline traced from the input seed location as a `.streamline.vtp` file in the same location and shows a window fo streamline visualization. The algorithm is tested using a `step_size` of `0.05` and `maximum steps` of `1000`. The command to run the program `soln.py` is given below where the `x`, `y` and `z` coordinates of the seeds are provided in `seed_x`, `seed_y` and `seed_z` arguments and whether user wants to visualize the streamline traced in the "visualize" argument.

```bash
> python3 soln.py --seed_x <x_coordinate> --seed_y <y_coordinate> --seed_z <z_coordinate> --visualize <yes/no>
```
