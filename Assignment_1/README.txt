CS661 Assignment 1

1. Question 1

The given code extracts all the cells and vertices from the 2D scalar data of the Hurricane and extracts the contour based on 
the isovalue provided by the user within a specified range, i.e (-1438, 630), thereby creating a PolyData object and storing it in as "isocontour.vtp" file in the same folder.
The script also has a helper function that may be executed to render the polydata object in a black blackground. The code to run the script
is mentioned below, where the user_input is the isovalue entered in the range (-1438, 630).

> python3 soln1.py --isovalue <user_input>

2. Question 2

The given code renders a 3D scalar field volume data of a Hurricane with optional Phong Shading feature. In order to run the script,
write the line specifying "yes" to the phong argument to enable phong shading with the mentioned ambient, diffuse and specular values or "no"
to disable phong shading.

> python3 soln2.py --phong <yes/no>