"""Check released STL topology, units, dimensions and R02 export equivalence."""
from pathlib import Path
import hashlib,json
import numpy as np
import trimesh
import networkx as nx
root=Path(__file__).resolve().parents[1]
reports=[]
for file in sorted((root/'stl').rglob('*.stl')):
    mesh=trimesh.load(file,force='mesh',process=True)
    graph=nx.Graph();graph.add_nodes_from(range(len(mesh.faces)))
    graph.add_edges_from(mesh.face_adjacency)
    bodies=nx.number_connected_components(graph)
    assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0 and bodies==1,file
    reports.append({'file':file.relative_to(root).as_posix(),'watertight':bool(mesh.is_watertight),
        'consistent_winding':bool(mesh.is_winding_consistent),'connected_face_components':bodies,
        'bounds_size_mm':mesh.extents.tolist(),'volume_mm3':float(mesh.volume),
        'sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
a=trimesh.load(root/'stl/v102-mount-r02-confirmed-fit.stl')
b=trimesh.load(root/'stl/v102-mount-r02-regenerated.stl')
assert np.allclose(a.extents,[48,6.8,24],atol=0.001)
assert np.allclose(a.bounds,b.bounds,atol=0.001)
assert abs(a.volume-b.volume)/a.volume<0.0001
result={'units':'mm','stl_count':len(reports),'meshes':reports,
    'r02_export_volume_difference_percent':100*abs(a.volume-b.volume)/a.volume,
    'note':'Digital topology/dimension checks only. Physical fit is owner-reported; no load or thermal validation.'}
(root/'verification/meshes.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
