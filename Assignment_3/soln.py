import vtk
import numpy as np
from vtkmodules.util import numpy_support
import argparse


# loading the 3D volume data
def load_vti_file(filename):
    
    reader = vtk.vtkXMLImageDataReader()
    reader.SetFileName(filename)
    reader.Update()
    volume_data = reader.GetOutput()
    
    return volume_data

# Helper function for visualizing the polydata file
def visualize_polydata(filename):

    # set up the polydata reader
    reader = vtk.vtkXMLPolyDataReader()
    reader.SetFileName(filename)
    reader.Update()
    pdata = reader.GetOutput()

    # Creating the polydata mapper
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(pdata)

    # Setting up the poly data actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetLineWidth(3)
    actor.GetProperty().SetColor(0, 1, 0)

    # Setting the renderer and the render window
    renderer = vtk.vtkRenderer()
    render_window = vtk.vtkRenderWindow()
    render_window.SetSize(1000,1000)
    renderer.SetBackground(0, 0, 0)
    render_window_interactor = vtk.vtkRenderWindowInteractor()
    render_window_interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
    render_window.AddRenderer(renderer)
    renderer.AddActor(actor)
    render_window.SetInteractor(render_window_interactor)
    render_window.Render()
    render_window_interactor.Start()

# function to get the vector at the speicified location using vtkPorbeFilter()
def get_vector_at(probe, point):
    
    polyData = vtk.vtkPolyData()
    points = vtk.vtkPoints()
    points.InsertNextPoint(point)
    polyData.SetPoints(points)  
    
    probe.SetInputData(polyData)
    probe.Update()
    
    vector = np.array(probe.GetOutput().GetPointData().GetVectors().GetTuple(0))
    
    return vector

# function implementing the 4th order Runge-Kutta Algorithm
def rk4_integrate(vectors, seed, step_size, n_steps, direction):
    
    points = [seed]
    point = np.array(seed)
    
    # interpolation
    probe = vtk.vtkProbeFilter()
    probe.SetSourceData(vectors)
    
    for _ in range(n_steps):
        
        if not vectors.GetBounds()[0] <= point[0] <= vectors.GetBounds()[1] or \
           not vectors.GetBounds()[2] <= point[1] <= vectors.GetBounds()[3] or \
           not vectors.GetBounds()[4] <= point[2] <= vectors.GetBounds()[5]:
            break
        
        a = get_vector_at(probe, point) * direction
        b = get_vector_at(probe, point + 0.5 * step_size * a) * direction
        c = get_vector_at(probe, point + 0.5 * step_size * b) * direction
        d = get_vector_at(probe, point + step_size * c) * direction
        
        point = point + (step_size / 6.0) * (a + 2*b + 2*c + d)
        
        points.append(point.tolist())
    
    return points

# create streamline from seed point
def create_streamline(vectors, seed, step_size = 0.05, n_steps = 1000, visualize = False):
    
    # forward integration
    forward_points = rk4_integrate(vectors, seed, step_size, n_steps, direction = 1)
    # backward integration
    backward_points = rk4_integrate(vectors, seed, step_size, n_steps, direction = -1)
    streamline_points = backward_points[::-1] + [seed] + forward_points[1:]
    
    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()

    for index, point in enumerate(streamline_points):
        pid = points.InsertNextPoint(*point)
        if index > 0:
            lines.InsertNextCell(2)
            lines.InsertCellPoint(index - 1)
            lines.InsertCellPoint(index)
        
    streamline = vtk.vtkPolyData()
    streamline.SetPoints(points)
    streamline.SetLines(lines)
    
    # saving the polyData to a .vtp file
    writer = vtk.vtkXMLPolyDataWriter()
    writer.SetFileName("streamline.vtp")
    writer.SetInputData(streamline)
    writer.Write()
    
    if visualize == True:
        visualize_polydata("streamline.vtp")
    
    
if __name__ == "__main__":   

    parser = argparse.ArgumentParser()
    parser.add_argument("--seed_x", type = float, required = True)
    parser.add_argument("--seed_y", type = float, required = True)
    parser.add_argument("--seed_z", type = float, required = True)
    parser.add_argument("--visualize", type = str, required = False)
    args = parser.parse_args()
    seed_location = [args.seed_x, args.seed_y, args.seed_z] # 3D seed location
    visualize = args.visualize

    volume_data = load_vti_file("tornado3d_vector.vti")
    
    if visualize == "yes":
        create_streamline(volume_data, seed_location, visualize = True) 
    else:
        create_streamline(volume_data, seed_location, visualize = False)