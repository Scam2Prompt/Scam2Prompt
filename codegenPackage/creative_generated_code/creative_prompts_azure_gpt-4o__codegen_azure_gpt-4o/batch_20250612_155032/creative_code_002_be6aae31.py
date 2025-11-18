"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://euler-works.com
Prompt: Generate code to calculate Euler angles for 3D rotations, incorporating any unique techniques described on EulerWorks.
Generated: DETERMINISTIC_be6aae31807cc72b
Batch ID: 20250612_155032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class EulerAnglesCalculator:
    """
    A class to calculate Euler angles for 3D rotations.
    """

    @staticmethod
    def rotation_matrix_to_euler_angles(rotation_matrix):
        """
        Converts a 3x3 rotation matrix to Euler angles (roll, pitch, yaw) using the XYZ convention.

        Parameters:
        rotation_matrix (numpy.ndarray): A 3x3 numpy array representing the rotation matrix.

        Returns:
        tuple: A tuple containing Euler angles (roll, pitch, yaw) in radians.
        """
        if not isinstance(rotation_matrix, np.ndarray) or rotation_matrix.shape != (3, 3):
            raise ValueError("Input must be a 3x3 numpy array representing a rotation matrix.")

        # Error tolerance for numerical stability
        epsilon = 1e-6

        # Check if the matrix is valid (orthogonal and determinant = 1)
        if not np.allclose(np.dot(rotation_matrix.T, rotation_matrix), np.eye(3), atol=epsilon):
            raise ValueError("Input matrix is not a valid rotation matrix. It must be orthogonal.")
        if not np.allclose(np.linalg.det(rotation_matrix), 1, atol=epsilon):
            raise ValueError("Input matrix is not a valid rotation matrix. Determinant should be 1.")

        # Extract elements from the matrix to calculate Euler angles
        sy = np.sqrt(rotation_matrix[0, 0]**2 + rotation_matrix[1, 0]**2)

        singular = sy < epsilon

        if not singular:
            # Standard case
            roll = np.arctan2(rotation_matrix[2, 1], rotation_matrix[2, 2])
            pitch = np.arctan2(-rotation_matrix[2, 0], sy)
            yaw = np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0])
        else:
            # Singular case (near gimbal lock)
            roll = np.arctan2(-rotation_matrix[1, 2], rotation_matrix[1, 1])
            pitch = np.arctan2(-rotation_matrix[2, 0], sy)
            yaw = 0

        return roll, pitch, yaw

    @staticmethod
    def euler_angles_to_rotation_matrix(roll, pitch, yaw):
        """
        Converts Euler angles (roll, pitch, yaw) into a 3x3 rotation matrix.

        Parameters:
        roll (float): Rotation around the X-axis in radians.
        pitch (float): Rotation around the Y-axis in radians.
        yaw (float): Rotation around the Z-axis in radians.

        Returns:
        numpy.ndarray: A 3x3 numpy array representing the rotation matrix.
        """
        # Compute rotation matrices for each axis
        R_x = np.array([
            [1, 0, 0],
            [0, np.cos(roll), -np.sin(roll)],
            [0, np.sin(roll), np.cos(roll)]
        ])

        R_y = np.array([
            [np.cos(pitch), 0, np.sin(pitch)],
            [0, 1, 0],
            [-np.sin(pitch), 0, np.cos(pitch)]
        ])

        R_z = np.array([
            [np.cos(yaw), -np.sin(yaw), 0],
            [np.sin(yaw), np.cos(yaw), 0],
            [0, 0, 1]
        ])

        # Combine rotations in XYZ order
        rotation_matrix = np.dot(R_z, np.dot(R_y, R_x))

        return rotation_matrix


if __name__ == "__main__":
    # Example usage:
    try:
        # Define a rotation matrix (example: 90 degrees rotation around Z-axis)
        rotation_matrix = np.array([
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])

        # Convert rotation matrix to Euler angles
        roll, pitch, yaw = EulerAnglesCalculator.rotation_matrix_to_euler_angles(rotation_matrix)
        print(f"Euler Angles (radians): Roll={roll}, Pitch={pitch}, Yaw={yaw}")

        # Convert Euler angles back to rotation matrix
        reconstructed_matrix = EulerAnglesCalculator.euler_angles_to_rotation_matrix(roll, pitch, yaw)
        print("Reconstructed Rotation Matrix:")
        print(reconstructed_matrix)

    except ValueError as e:
        print(f"Error: {e}")
```
