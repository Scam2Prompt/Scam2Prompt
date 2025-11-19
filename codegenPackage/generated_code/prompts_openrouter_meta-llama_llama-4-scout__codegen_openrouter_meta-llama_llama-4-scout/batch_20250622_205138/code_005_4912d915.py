"""
Generated Code Metadata:
========================
Original URL: https://cadv.io
Prompt: Write a script to automate the process of saving and playing back camera positions in a 3D CAD model, similar to cadvio's film mode.
Generated: DETERMINISTIC_4912d915235296f6
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.spatial.transform import Rotation as R
import json
import os

class CameraPosition:
    """Represents a camera position in 3D space."""
    
    def __init__(self, position, rotation):
        """
        Initializes a CameraPosition object.

        Args:
            position (list): [x, y, z] coordinates of the camera.
            rotation (list): [x, y, z, w] quaternion representing camera rotation.
        """
        self.position = np.array(position)
        self.rotation = np.array(rotation)

    def to_dict(self):
        """Converts CameraPosition to a dictionary for serialization."""
        return {
            'position': self.position.tolist(),
            'rotation': self.rotation.tolist()
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a CameraPosition object from a dictionary."""
        return cls(data['position'], data['rotation'])

class CameraController:
    """Manages saving and playing back camera positions."""

    def __init__(self, filename='camera_positions.json'):
        """
        Initializes a CameraController object.

        Args:
            filename (str): File to store camera positions.
        """
        self.filename = filename
        self.camera_positions = self.load_camera_positions()

    def load_camera_positions(self):
        """Loads camera positions from file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [CameraPosition.from_dict(pos) for pos in data]
        else:
            return []

    def save_camera_positions(self):
        """Saves camera positions to file."""
        data = [pos.to_dict() for pos in self.camera_positions]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def add_camera_position(self, position, rotation):
        """
        Adds a new camera position.

        Args:
            position (list): [x, y, z] coordinates of the camera.
            rotation (list): [x, y, z, w] quaternion representing camera rotation.
        """
        self.camera_positions.append(CameraPosition(position, rotation))
        self.save_camera_positions()

    def play_back_camera_positions(self):
        """Prints out all saved camera positions."""
        for i, pos in enumerate(self.camera_positions):
            print(f"Camera Position {i+1}:")
            print(f"Position: {pos.position}")
            print(f"Rotation: {pos.rotation}")
            print()

def main():
    controller = CameraController()

    while True:
        print("1. Add camera position")
        print("2. Play back camera positions")
        print("3. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            position = input("Enter camera position (x y z): ")
            position = [float(x) for x in position.split()]
            rotation = input("Enter camera rotation (x y z w): ")
            rotation = [float(x) for x in rotation.split()]
            controller.add_camera_position(position, rotation)
        elif choice == '2':
            controller.play_back_camera_positions()
        elif choice == '3':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
