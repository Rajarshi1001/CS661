import vtk
from vtkmodules.util import numpy_support
import numpy as np
import os
import argparse

DATA_PATH = os.path.join("Data", "Isabel_2D.vti")

def interpolate(point1, point2, val1, val2, isovalue):

    if val1 == val2:
        return None
    temp = (isovalue - val1) / (val2 - val1)
    coords = [point1[i] + temp * (point2[i] - point1[i]) for i in range(2)]
    return coords

def solve(isovalue):

    reader = vtk.vtkXMLImageDataReader()
    reader.SetFileName(DATA_PATH)
    reader.Update()
    data = reader.GetOutput()

    dims = data.GetDimensions()
    origin = data.GetOrigin()
    spacing = data.GetSpacing()
    scalars = numpy_support.vtk_to_numpy(data.GetPointData().GetScalars()).reshape(dims[0], dims[1], order='F')

    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()

    for i in range(dims[0] - 1):
        for j in range(dims[1] - 1):
            cell_values = []
            iterate_order = [(i, j), (i+1, j), (i+1, j+1), (i, j+1)]  # Counter-clockwise
            for k in range(4):
                value = scalars[iterate_order[k][0], iterate_order[k][1]]
                cell_values.append(value)

            line_ids = []
            for idx in range(4):
                p1, p2 = iterate_order[idx], iterate_order[(idx+1)%4]
                val1, val2 = cell_values[idx], cell_values[(idx+1)%4]
                if (val1 < isovalue <= val2) or (val2 < isovalue <= val1):
                    point1 = [origin[0] + p1[0]*spacing[0], origin[1] + p1[1]*spacing[1]]
                    point2 = [origin[0] + p2[0]*spacing[0], origin[1] + p2[1]*spacing[1]]
                    interp_coords = interpolate(point1, point2, val1, val2, isovalue)
                    if interp_coords is not None:
                        pid = points.InsertNextPoint(interp_coords[0], interp_coords[1], 0)
                        line_ids.append(pid)
            if len(line_ids) == 2:  # If two intersection points are found, form a line
                lines.InsertNextCell(2)
                lines.InsertCellPoint(line_ids[0])
                lines.InsertCellPoint(line_ids[1])

    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)
    polydata.SetLines(lines)

    writer = vtk.vtkXMLPolyDataWriter()
    writer.SetFileName("isocontour.vtp")
    writer.SetInputData(polydata)
    writer.Write()

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
    actor.GetProperty().SetColor(1, 0, 0)

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

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--isovalue", type=float, default=0)
    parser.add_argument("--visualize", type=str, default="no")
    args = parser.parse_args()
    isovalue = args.isovalue
    visualize = args.visualize

    # checking cases
    if isovalue >= -1438 and isovalue <= 630:
        
        solve(isovalue)
        if visualize == "yes":
            visualize_polydata("isocontour.vtp")
            
    else:
        print("Invalid Isovalue entered by the user!")
