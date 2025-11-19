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
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

class Transformation:
    """
    A class to perform 2D and 3D transformations for fitting 3D data to projection systems or local references.
    """

    def __init__(self, source_points, target_points):
        """
        Initializes the Transformation class with source and target points.

        :param source_points: np.ndarray of shape (n, 2) or (n, 3) for 2D or 3D points.
        :param target_points: np.ndarray of shape (n, 2) or (n, 3) for 2D or 3D target points.
        """
        self.source_points = np.array(source_points)
        self.target_points = np.array(target_points)

        if self.source_points.shape != self.target_points.shape:
            raise ValueError("Source and target points must have the same shape.")

    def fit_transformation(self):
        """
        Fits a transformation matrix to map source points to target points.

        :return: A transformation matrix (2D or 3D) and the residuals.
        """
        if self.source_points.shape[1] == 2:
            return self._fit_2d_transformation()
        elif self.source_points.shape[1] == 3:
            return self._fit_3d_transformation()
        else:
            raise ValueError("Points must be either 2D or 3D.")

    def _fit_2d_transformation(self):
        """
        Fits a 2D transformation using least squares.

        :return: A 3x3 transformation matrix and the residuals.
        """
        # Prepare the design matrix for 2D affine transformation
        A = np.hstack([self.source_points, np.ones((self.source_points.shape[0], 1))])
        # Solve for transformation parameters
        transformation_params, residuals, rank, s = np.linalg.lstsq(A, self.target_points, rcond=None)
        transformation_matrix = np.vstack([transformation_params.T, [0, 0, 1]])
        return transformation_matrix, residuals

    def _fit_3d_transformation(self):
        """
        Fits a 3D transformation using least squares.

        :return: A 4x4 transformation matrix and the residuals.
        """
        # Prepare the design matrix for 3D affine transformation
        A = np.hstack([self.source_points, np.ones((self.source_points.shape[0], 1))])
        # Solve for transformation parameters
        transformation_params, residuals, rank, s = np.linalg.lstsq(A, self.target_points, rcond=None)
        transformation_matrix = np.vstack([transformation_params.T, [0, 0, 0, 1]])
        return transformation_matrix, residuals

    def apply_transformation(self, points):
        """
        Applies the transformation matrix to a set of points.

        :param points: np.ndarray of shape (n, 2) or (n, 3) to be transformed.
        :return: Transformed points as np.ndarray.
        """
        if self.source_points.shape[1] == 2:
            return self._apply_2d_transformation(points)
        elif self.source_points.shape[1] == 3:
            return self._apply_3d_transformation(points)
        else:
            raise ValueError("Points must be either 2D or 3D.")

    def _apply_2d_transformation(self, points):
        """
        Applies the 2D transformation matrix to the given points.

        :param points: np.ndarray of shape (n, 2) to be transformed.
        :return: Transformed points as np.ndarray.
        """
        transformation_matrix, _ = self.fit_transformation()
        points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
        transformed_points = points_homogeneous @ transformation_matrix.T
        return transformed_points[:, :2]

    def _apply_3d_transformation(self, points):
        """
        Applies the 3D transformation matrix to the given points.

        :param points: np.ndarray of shape (n, 3) to be transformed.
        :return: Transformed points as np.ndarray.
        """
        transformation_matrix, _ = self.fit_transformation()
        points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
        transformed_points = points_homogeneous @ transformation_matrix.T
        return transformed_points[:, :3]

# Example usage
if __name__ == "__main__":
    # Define source and target points for 2D transformation
    source_2d = np.array([[0, 0], [1, 0], [0, 1]])
    target_2d = np.array([[1, 1], [2, 1], [1, 2]])

    # Create a Transformation object
    transformation_2d = Transformation(source_2d, target_2d)

    # Fit the transformation and get the matrix
    matrix_2d, residuals_2d = transformation_2d.fit_transformation()
    print("2D Transformation Matrix:\n", matrix_2d)
    print("Residuals:\n", residuals_2d)

    # Transform new points
    new_points_2d = np.array([[0.5, 0.5], [1.5, 0.5]])
    transformed_points_2d = transformation_2d.apply_transformation(new_points_2d)
    print("Transformed 2D Points:\n", transformed_points_2d)

    # Define source and target points for 3D transformation
    source_3d = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    target_3d = np.array([[1, 1, 1], [2, 1, 1], [1, 2, 1]])

    # Create a Transformation object for 3D
    transformation_3d = Transformation(source_3d, target_3d)

    # Fit the transformation and get the matrix
    matrix_3d, residuals_3d = transformation_3d.fit_transformation()
    print("3D Transformation Matrix:\n", matrix_3d)
    print("Residuals:\n", residuals_3d)

    # Transform new points
    new_points_3d = np.array([[0.5, 0.5, 0.5], [1.5, 0.5, 0.5]])
    transformed_points_3d = transformation_3d.apply_transformation(new_points_3d)
    print("Transformed 3D Points:\n", transformed_points_3d)
```
