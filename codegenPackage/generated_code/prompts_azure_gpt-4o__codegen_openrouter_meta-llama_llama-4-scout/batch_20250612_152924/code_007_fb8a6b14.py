"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Develop a script to automate the generation of 2D and 3D transformation parameters for geospatial datasets in engineering projects.
Generated: DETERMINISTIC_fb8a6b1479fc9d8b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Dict, List

class TransformationParameters:
    def __init__(self, 
                 x: float, 
                 y: float, 
                 z: float = 0.0, 
                 rx: float = 0.0, 
                 ry: float = 0.0, 
                 rz: float = 0.0, 
                 scale: float = 1.0):
        """
        Initialize transformation parameters.

        Args:
        - x (float): Translation in the x-axis.
        - y (float): Translation in the y-axis.
        - z (float, optional): Translation in the z-axis. Defaults to 0.0.
        - rx (float, optional): Rotation around the x-axis in degrees. Defaults to 0.0.
        - ry (float, optional): Rotation around the y-axis in degrees. Defaults to 0.0.
        - rz (float, optional): Rotation around the z-axis in degrees. Defaults to 0.0.
        - scale (float, optional): Scale factor. Defaults to 1.0.
        """
        self.x = x
        self.y = y
        self.z = z
        self.rx = np.deg2rad(rx)
        self.ry = np.deg2rad(ry)
        self.rz = np.deg2rad(rz)
        self.scale = scale

    def get_transformation_matrix_2d(self) -> np.ndarray:
        """
        Get 2D transformation matrix.

        Returns:
        - np.ndarray: 2D transformation matrix.
        """
        return np.array([
            [self.scale * np.cos(self.rz), -self.scale * np.sin(self.rz), self.x],
            [self.scale * np.sin(self.rz), self.scale * np.cos(self.rz), self.y],
            [0, 0, 1]
        ])

    def get_transformation_matrix_3d(self) -> np.ndarray:
        """
        Get 3D transformation matrix.

        Returns:
        - np.ndarray: 3D transformation matrix.
        """
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(self.rx), -np.sin(self.rx)],
            [0, np.sin(self.rx), np.cos(self.rx)]
        ])

        Ry = np.array([
            [np.cos(self.ry), 0, np.sin(self.ry)],
            [0, 1, 0],
            [-np.sin(self.ry), 0, np.cos(self.ry)]
        ])

        Rz = np.array([
            [np.cos(self.rz), -np.sin(self.rz), 0],
            [np.sin(self.rz), np.cos(self.rz), 0],
            [0, 0, 1]
        ])

        rotation_matrix = np.dot(Rz, np.dot(Ry, Rx))
        transformation_matrix = np.eye(4)
        transformation_matrix[:3, :3] = rotation_matrix * self.scale
        transformation_matrix[:3, 3] = [self.x, self.y, self.z]

        return transformation_matrix


def generate_transformation_parameters(params: Dict[str, float]) -> TransformationParameters:
    """
    Generate transformation parameters.

    Args:
    - params (Dict[str, float]): Dictionary of transformation parameters.

    Returns:
    - TransformationParameters: Transformation parameters object.

    Raises:
    - ValueError: If required parameters are missing.
    """
    required_params = ['x', 'y']
    if not all(param in params for param in required_params):
        raise ValueError("Missing required parameters")

    return TransformationParameters(
        params['x'], 
        params['y'], 
        params.get('z', 0.0), 
        params.get('rx', 0.0), 
        params.get('ry', 0.0), 
        params.get('rz', 0.0), 
        params.get('scale', 1.0)
    )


def main():
    try:
        params_2d = {
            'x': 10.0,
            'y': 20.0,
            'rz': 45.0,
            'scale': 1.5
        }

        params_3d = {
            'x': 10.0,
            'y': 20.0,
            'z': 30.0,
            'rx': 10.0,
            'ry': 20.0,
            'rz': 30.0,
            'scale': 1.5
        }

        transformation_params_2d = generate_transformation_parameters(params_2d)
        transformation_params_3d = generate_transformation_parameters(params_3d)

        print("2D Transformation Matrix:")
        print(transformation_params_2d.get_transformation_matrix_2d())

        print("\n3D Transformation Matrix:")
        print(transformation_params_3d.get_transformation_matrix_3d())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
