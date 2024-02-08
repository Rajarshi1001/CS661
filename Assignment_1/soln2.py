import vtk
import argparse
import os
import faulthandler
faulthandler.enable()


DATA_PATH = os.path.join("Data", "Isabel_3D.vti")

def solve(enable_phong_shading):

    # loading the 3D data into the reader object
    reader = vtk.vtkXMLImageDataReader()
    reader.SetFileName(DATA_PATH)
    reader.Update()
    volume_data = reader.GetOutput()

    # initializing the color transfer function and opacity function
    tf = vtk.vtkColorTransferFunction()
    tf.AddRGBPoint(-4931.54, 0.0, 1.0, 1.0)
    tf.AddRGBPoint(-2508.95, 0.0, 0.0, 1.0)
    tf.AddRGBPoint(-1873.9, 0.0, 0.0, 0.5)
    tf.AddRGBPoint(-1027.16, 1.0, 0.0, 0.0)
    tf.AddRGBPoint(-298.031, 1.0, 0.4, 0.0)
    tf.AddRGBPoint(2594.97, 1.0, 1.0, 0.0)

    opf = vtk.vtkPiecewiseFunction()
    opf.AddPoint(-4931.54, 1.0)
    opf.AddPoint(101.815, 0.002)
    opf.AddPoint(2594.97, 0.0)

    # Creating the volume property mapper and adding the properties to it
    volumeprop = vtk.vtkVolumeProperty()
    volumeprop.SetColor(tf)
    volumeprop.SetScalarOpacity(opf)

    if enable_phong_shading:

        volumeprop.ShadeOn()
        volumeprop.SetAmbient(0.5)
        volumeprop.SetDiffuse(0.5)
        volumeprop.SetSpecular(0.5)
        volumeprop.SetSpecularPower(10)

    # volumeprop.SetInterpolationTypeToLinear()

    # Creating the volume Mapper
    volume_mapper = vtk.vtkSmartVolumeMapper()
    volume_mapper.SetInputData(volume_data)

    # Creating the volume actor
    volume = vtk.vtkVolume()
    volume.SetMapper(volume_mapper)
    volume.SetProperty(volumeprop)

    # Rendering the volume data
    renderer = vtk.vtkRenderer()
    render_window = vtk.vtkRenderWindow()
    render_window.SetSize(1000, 1000)
    render_window.AddRenderer(renderer)
    render_window_interactor = vtk.vtkRenderWindowInteractor()
    render_window_interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
    render_window_interactor.SetRenderWindow(render_window)
    renderer.SetBackground(0.5, 0.5, 0.5)
    renderer.AddVolume(volume)
    render_window.Render()
    render_window_interactor.Start()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--phongshading", type = str, choices = ["yes", "no"], default = "no")
    args = parser.parse_args()
    if args.phongshading == "yes":
        enable_phong_shading = True
    else: 
        enable_phong_shading = False
    
    solve(enable_phong_shading)

