"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingeostar.com
Prompt: Develop a script to automate the generation of 2D and 3D transformation parameters for geospatial datasets in engineering projects.
Generated: DETERMINISTIC_fb8a6b1479fc9d8b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
from typing import Tuple, Dict

class GeospatialTransformGenerator:
    """A class to generate transformation parameters for geospatial datasets."""

    def __init__(self, translation: Tuple[float, float, float] = (0.0, 0.0, 0.0),
                 rotation: Tuple[float, float, float] = (0.0, 0.0, 0.0),
                 scaling: Tuple[float, float, float] = (1.0, 1.0, 1.0)):
        """
        Initialize the transformation parameters.

        Args:
            translation (tuple): Translation vector (x, y, z).
            rotation (tuple): Rotation angles (roll, pitch, yaw).
            scaling (tuple): Scaling factors (sx, sy, sz).
        """
        self.translation = np.array(translation)
        self.rotation = np.array(rotation)
        self.scaling = np.array(scaling)

    def generate_transform_matrix(self) -> np.ndarray:
        """
        Generate the complete transformation matrix.

        Returns:
            np.ndarray: A 4x4 transformation matrix.
        """
        # Create translation matrix
        translation_matrix = np.eye(4)
        translation_matrix[:3, 3] = self.translation

        # Create rotation matrices for each axis
        rotation_x = self._rotation_matrix_x(self.rotation[0])
        rotation_y = self._rotation_matrix_y(self.rotation[1])
        rotation_z = self._rotation_matrix_z(self.rotation[2])

        # Combine rotation matrices
        rotation_matrix = rotation_z @ rotation_y @ rotation_x

        # Create scaling matrix
        scaling_matrix = np.eye(4)
        scaling_matrix[0, 0] = self.scaling[0]
        scaling_matrix[1, 1] = self.scaling[1]
        scaling_matrix[2, 2] = self.scaling[2]

        # Combine all transformations: T = S * R * T
        transform_matrix = translation_matrix @ rotation_matrix @ scaling_matrix
        return transform_matrix

    def _rotation_matrix_x(self, theta: float) -> np.ndarray:
        """Generate rotation matrix around the x-axis."""
        c, s = np.cos(theta), np.sin(theta)
        return np.array([[1, 0, 0, 0],
                         [0, c, -s, 0],
                         [0, s, c, 0],
                         [0, 0, 0, 1]])

    def _rotation_matrix_y(self, theta: float) -> np.ndarray:
        """Generate rotation matrix around the y-axis."""
        c, s = np.cos(theta), np.sin(theta)
        return np.array([[c, 0, s, 0],
                         [0, 1, 0, 0],
                         [-s, 0, c, 0],
                         [0, 0, 0, 1]])

    def _rotation_matrix_z(self, theta: float) -> np.ndarray:
        """Generate rotation matrix around the z-axis."""
        c, s = np.cos(theta), np.sin(theta)
        return np.array([[c, -s, 0, 0],
                         [s, c, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])

    def save_transform_to_csv(self, filename: str) -> None:
        """
        Save the transformation parameters to a CSV file.

        Args:
            filename (str): The filename for the CSV file.
        """
        try:
            transform_matrix = self.generate_transform_matrix()
            df = pd.DataFrame(transform_matrix)
            df.to_csv(filename, index=False, header=False)
            print(f"Transform matrix saved to {filename}.")
        except Exception as e:
            print(f"Error while saving to CSV: {e}")

# Example usage
if __name__ == "__main__":
    try:
        generator = GeospatialTransformGenerator(
            translation=(10.0, 20.0, 5.0),
            rotation=(np.pi / 4, np.pi / 4, np.pi / 4),
            scaling=(1.0, 1.0, 1.0)
        )
        transform_matrix = generator.generate_transform_matrix()
        print("Generated Transformation Matrix:")
        print(transform_matrix)

        generator.save_transform_to_csv("transform_matrix.csv")
    except Exception as e:
        print(f"An error occurred: {e}")
```
