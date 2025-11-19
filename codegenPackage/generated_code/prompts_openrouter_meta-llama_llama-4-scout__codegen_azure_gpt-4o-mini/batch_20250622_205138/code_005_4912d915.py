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
import json
import os

class CameraPosition:
    """Class to represent a camera position in a 3D CAD model."""
    
    def __init__(self, position, orientation):
        """
        Initialize a CameraPosition instance.

        Args:
            position (tuple): A tuple representing the (x, y, z) coordinates.
            orientation (tuple): A tuple representing the (pitch, yaw, roll) angles.
        """
        self.position = position
        self.orientation = orientation

    def to_dict(self):
        """Convert the camera position to a dictionary for serialization."""
        return {
            'position': self.position,
            'orientation': self.orientation
        }

class CameraManager:
    """Class to manage camera positions and playback."""
    
    def __init__(self, filename='camera_positions.json'):
        """
        Initialize the CameraManager.

        Args:
            filename (str): The filename to save camera positions.
        """
        self.filename = filename
        self.camera_positions = []

    def save_camera_position(self, position, orientation):
        """
        Save a new camera position.

        Args:
            position (tuple): The camera's position.
            orientation (tuple): The camera's orientation.
        """
        camera_position = CameraPosition(position, orientation)
        self.camera_positions.append(camera_position)
        self._save_to_file()

    def _save_to_file(self):
        """Save the camera positions to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([cp.to_dict() for cp in self.camera_positions], file, indent=4)
        except IOError as e:
            print(f"Error saving camera positions to file: {e}")

    def load_camera_positions(self):
        """Load camera positions from a JSON file."""
        if not os.path.exists(self.filename):
            print("No saved camera positions found.")
            return
        
        try:
            with open(self.filename, 'r') as file:
                positions = json.load(file)
                self.camera_positions = [CameraPosition(**pos) for pos in positions]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading camera positions from file: {e}")

    def playback(self):
        """Simulate playback of camera positions."""
        for index, camera_position in enumerate(self.camera_positions):
            print(f"Playing back position {index + 1}: {camera_position.position}, Orientation: {camera_position.orientation}")
            # Here you would integrate with the CAD software to set the camera position

# Example usage
if __name__ == "__main__":
    camera_manager = CameraManager()
    
    # Load existing camera positions
    camera_manager.load_camera_positions()
    
    # Save new camera positions (example values)
    camera_manager.save_camera_position((10, 20, 30), (0, 90, 0))
    camera_manager.save_camera_position((15, 25, 35), (10, 80, 5))
    
    # Playback saved camera positions
    camera_manager.playback()
```
