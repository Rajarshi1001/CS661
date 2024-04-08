## CS661 Assignment 3

The 3D data used for the solution is present in the folder

1. Question 1

The given code essentially generates a streamline pattern from a `tornado3d_vector.vti` file using the standard **4th order Runge-Kutta** algorithm inorporating both forward and backward integration from the seed followed by interpolation to generate vectors required for pth reconstruction from the input 3D seed position entered by the user as an argument. The code saves the streamline traced from the input seed location as a `.streamline.vtp` file in the same location and shows a window fo streamline visualization. The algorithm is tested using a `step_size` of `0.05` and `maximum steps` of `1000`. The command to run the program `soln.py` is given below where the `x`, `y` and `z` coordinates of the seeds are provided in `seed_x`, `seed_y` and `seed_z` arguments and whether user wants to visualize the streamline traced in the "visualize" argument.

```bash
> python3 soln.py --seed_x <x_coordinate> --seed_y <y_coordinate> --seed_z <z_coordinate> --visualize <yes/no>
```