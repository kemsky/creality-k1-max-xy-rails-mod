"""
This script automatically exports STL and STEP files from FreeCAD project files.

Invoke directly (Ubuntu snap installation): `exec: /snap/bin/freecad ./export.py`,
Or use `./export.sh` from parent dir.
"""

import FreeCAD
import MeshPart
import Import
import Mesh
import Part
import os, re

step_timestamp_pattern = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")

script_path: str = os.path.abspath(__file__)
print("Current script path: " + script_path)

root_dir: str = os.path.dirname(os.path.dirname(script_path)) 

source_dir: str = os.path.join(root_dir, "src")
print("FreeCAD sources path: " + source_dir)

stl_path: str = os.path.join(root_dir, "stl")
print("STL output path: " + stl_path)
os.makedirs(stl_path, exist_ok = True)

step_path: str = os.path.join(root_dir, "step")
print("STEP output path: " + step_path)
os.makedirs(step_path, exist_ok = True)

# The list of FreeCAD files to be exported,
# by convention exported object must have the same name as project file.
documents :list[str] = [
    "k1_camera",
    "k1_front_idler_left",
    "k1_front_idler_right",
    "k1_joint_left",
    "k1_joint_right",
    "k1_motor_mount_left",
    "k1_motor_mount_right",
    "k1_rail_mount",
    "k1_tensioner_left",
    "k1_tensioner_right",
    "k1_toolhead",
    "k1_toolhead_20x10"
]

def export(file: str, object_name: str, export_types: list[str]):
    """ This function exports object from FreeCAD file

         Parameters:
            file: str
                FreeCAD project file name (`*.FCStd`)
            object_name: str
                Label of the object in FreeCAD project file
            export_types: list[str]
                A list of export formats (values: "stl", "step")
    """

    document_path: str = os.path.join(source_dir, file)

    FreeCAD.Console.PrintMessage('Load file: "' + document_path + '"\n')

    FreeCAD.loadFile(document_path)

    doc = FreeCAD.ActiveDocument

    FreeCAD.Console.PrintMessage(f'Find object: "{object_name}"\n')

    target_object = doc.getObjectsByLabel(object_name)[0]

    for export_type in export_types:
        if export_type == "stl":
            export_path = os.path.join(stl_path, object_name + "." + export_type)

            FreeCAD.Console.PrintMessage(f'Export: "{export_path}"\n')

            target_shape = Part.getShape(target_object)

            mesh = MeshPart.meshFromShape(Shape=target_shape, LinearDeflection=0.001, AngularDeflection=0.523599, Relative=False)

            doc_mesh = doc.addObject("Mesh::Feature", object_name + "_mesh")
            doc_mesh.Mesh = mesh

            Mesh.export([doc_mesh], export_path)
        elif export_type == "step":
            export_path = os.path.join(step_path, object_name + "." + export_type)

            FreeCAD.Console.PrintMessage(f'Export: "{export_path}"\n')

            target_shape = Part.getShape(target_object)

            doc_part = doc.addObject("Part::Feature","Shape")
            doc_part.Shape = target_shape
            doc_part.Label = object_name + "_step"

            Import.export([doc_part], export_path)

            # FreeCAD writes timestamp into STEP files and it leads to unnecessary changes, 
            # so we replace with default value: 1974-01-01T00:00:00
            with open(export_path, 'r') as step_file:
                filedata = step_file.read()

            filedata = step_timestamp_pattern.sub("1974-01-01T00:00:00", filedata)

            with open(export_path, 'w') as step_file:
                step_file.write(filedata)
        else:
            raise Exception(f"Unknown export_type: {export_type}")

    open_documents = FreeCAD.listDocuments()

    for key in open_documents:
        FreeCAD.Console.PrintMessage('Close file: "' + open_documents[key].Name + '"\n')
        FreeCAD.closeDocument(open_documents[key].Name)

    FreeCAD.Console.PrintMessage('\n\n')


for document in documents:
    try:
        export(document + ".FCStd", document, ["stl", "step"])
    except:
        FreeCAD.Console.PrintMessage('╔═════════════╗\n')
        FreeCAD.Console.PrintMessage('║░░░░ERROR░░░░║\n')
        FreeCAD.Console.PrintMessage('╚═════════════╝\n\n')
        quit(0)

FreeCAD.Console.PrintMessage('╔═════════════╗\n')
FreeCAD.Console.PrintMessage('║░░░SUCCESS░░░║\n')
FreeCAD.Console.PrintMessage('╚═════════════╝\n\n')

quit(0)