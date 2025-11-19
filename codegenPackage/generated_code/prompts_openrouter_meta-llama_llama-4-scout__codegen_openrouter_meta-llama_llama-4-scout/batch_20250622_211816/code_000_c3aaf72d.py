"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: "Write a Python script to perform 3D modelling and building information modelling (BIM) for a construction project using data from a UAV & Aerial Survey."
Generated: DETERMINISTIC_c3aaf72ddb5e03a7
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from pyproj import Transformer
import json

# Define a class for 3D point
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Define a class for BIM model
class BIMModel:
    def __init__(self):
        self.points = []
        self.faces = []

    def add_point(self, point):
        self.points.append(point)

    def add_face(self, face):
        self.faces.append(face)

# Load UAV & Aerial Survey data from JSON file
def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("File not found.")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return None

# Convert UAV & Aerial Survey data to 3D points
def convert_to_3d_points(data):
    points = []
    transformer = Transformer.from_crs(4326, 3857) # WGS84 to Web Mercator
    for feature in data['features']:
        x, y = transformer.transform(feature['geometry']['coordinates'][0], feature['geometry']['coordinates'][1])
        z = feature['properties']['elevation']
        points.append(Point3D(x, y, z))
    return points

# Create a 3D plot of the BIM model
def plot_bim_model(bim_model):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    points = bim_model.points
    x = [point.x for point in points]
    y = [point.y for point in points]
    z = [point.z for point in points]
    ax.scatter(x, y, z)
    for face in bim_model.faces:
        face_points = [points[i] for i in face]
        face_x = [point.x for point in face_points]
        face_y = [point.y for point in face_points]
        face_z = [point.z for point in face_points]
        face_x.append(face_points[0].x)
        face_y.append(face_points[0].y)
        face_z.append(face_points[0].z)
        ax.plot(face_x, face_y, face_z, 'b-')
    plt.show()

# Main function
def main():
    file_path = 'uav_data.json'
    data = load_data(file_path)
    if data:
        points = convert_to_3d_points(data)
        bim_model = BIMModel()
        for point in points:
            bim_model.add_point(point)
        # Example face: connect points 0, 1, 2
        bim_model.add_face([0, 1, 2])
        plot_bim_model(bim_model)

if __name__ == "__main__":
    main()
```

```json
// uav_data.json example file
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [12.456, 43.987]
            },
            "properties": {
                "elevation": 10.5
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [12.457, 43.988]
            },
            "properties": {
                "elevation": 11.2
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [12.458, 43.987]
            },
            "properties": {
                "elevation": 10.8
            }
        }
    ]
}
```
