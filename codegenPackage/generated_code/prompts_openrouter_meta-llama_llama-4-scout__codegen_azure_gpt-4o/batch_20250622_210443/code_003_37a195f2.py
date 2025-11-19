"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Develop a code to analyze and generate parameters of Transformación 2D and 3D for Ajuste de datos Tridimensionales a sistemas de proyecciones y/o referencias locales.
Generated: DETERMINISTIC_37a195f228cb4e78
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.optimize import minimize

class Transformation2D3D:
    """
    A class to analyze and generate parameters for 2D and 3D transformations.
    This includes fitting 3D data to projection systems or local reference systems.
    """

    def __init__(self):
        """
        Initialize the transformation class.
        """
        self.transformation_params = None

    def fit_3d_to_2d(self, points_3d, points_2d):
        """
        Fit 3D points to 2D projection using least squares optimization.

        :param points_3d: np.ndarray of shape (n, 3), 3D points
        :param points_2d: np.ndarray of shape (n, 2), corresponding 2D points
        :return: dict containing transformation parameters
        """
        if points_3d.shape[0] != points_2d.shape[0]:
            raise ValueError("Number of 3D points must match number of 2D points.")

        def projection_error(params):
            """
            Compute the error between projected 3D points and actual 2D points.

            :param params: Transformation parameters (scale, rotation, translation)
            :return: Sum of squared errors
            """
            scale, rx, ry, rz, tx, ty = params
            rotation_matrix = self._rotation_matrix(rx, ry, rz)
            projected_points = scale * (points_3d @ rotation_matrix.T)[:, :2] + np.array([tx, ty])
            return np.sum((projected_points - points_2d) ** 2)

        # Initial guess for parameters: scale=1, no rotation, no translation
        initial_params = [1, 0, 0, 0, 0, 0]

        # Minimize the projection error
        result = minimize(projection_error, initial_params, method='BFGS')

        if not result.success:
            raise RuntimeError("Optimization failed to converge.")

        self.transformation_params = {
            "scale": result.x[0],
            "rotation": result.x[1:4],
            "translation": result.x[4:6]
        }
        return self.transformation_params

    def transform_3d_to_2d(self, points_3d):
        """
        Apply the fitted transformation to 3D points to project them to 2D.

        :param points_3d: np.ndarray of shape (n, 3), 3D points
        :return: np.ndarray of shape (n, 2), projected 2D points
        """
        if self.transformation_params is None:
            raise ValueError("Transformation parameters have not been fitted yet.")

        scale = self.transformation_params["scale"]
        rx, ry, rz = self.transformation_params["rotation"]
        tx, ty = self.transformation_params["translation"]

        rotation_matrix = self._rotation_matrix(rx, ry, rz)
        projected_points = scale * (points_3d @ rotation_matrix.T)[:, :2] + np.array([tx, ty])
        return projected_points

    def _rotation_matrix(self, rx, ry, rz):
        """
        Generate a 3D rotation matrix from rotation angles.

        :param rx: Rotation around x-axis (radians)
        :param ry: Rotation around y-axis (radians)
        :param rz: Rotation around z-axis (radians)
        :return: np.ndarray of shape (3, 3), rotation matrix
        """
        cos_rx, sin_rx = np.cos(rx), np.sin(rx)
        cos_ry, sin_ry = np.cos(ry), np.sin(ry)
        cos_rz, sin_rz = np.cos(rz), np.sin(rz)

        # Rotation matrices for each axis
        rot_x = np.array([
            [1, 0, 0],
            [0, cos_rx, -sin_rx],
            [0, sin_rx, cos_rx]
        ])
        rot_y = np.array([
            [cos_ry, 0, sin_ry],
            [0, 1, 0],
            [-sin_ry, 0, cos_ry]
        ])
        rot_z = np.array([
            [cos_rz, -sin_rz, 0],
            [sin_rz, cos_rz, 0],
            [0, 0, 1]
        ])

        # Combined rotation matrix
        return rot_z @ rot_y @ rot_x


# Example usage:
if __name__ == "__main__":
    # Sample 3D points
    points_3d = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    # Corresponding 2D points
    points_2d = np.array([
        [1.1, 2.2],
        [4.3, 5.4],
        [7.5, 8.6]
    ])

    # Create transformation object
    transformer = Transformation2D3D()

    # Fit transformation parameters
    params = transformer.fit_3d_to_2d(points_3d, points_2d)
    print("Fitted Parameters:", params)

    # Transform 3D points to 2D
    projected_points = transformer.transform_3d_to_2d(points_3d)
    print("Projected Points:", projected_points)
```
