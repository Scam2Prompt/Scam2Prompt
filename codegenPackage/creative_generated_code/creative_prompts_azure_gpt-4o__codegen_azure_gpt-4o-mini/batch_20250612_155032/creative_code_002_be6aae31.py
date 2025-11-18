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

class EulerAngles:
    """
    A class to calculate Euler angles from rotation matrices and vice versa.
    This implementation follows the conventions used in the EulerWorks techniques.
    """

    def __init__(self, rotation_order='XYZ'):
        """
        Initializes the EulerAngles class with a specified rotation order.
        
        :param rotation_order: A string representing the rotation order (e.g., 'XYZ', 'ZYX').
        """
        self.rotation_order = rotation_order

    def rotation_matrix_to_euler(self, R):
        """
        Converts a rotation matrix to Euler angles.
        
        :param R: A 3x3 rotation matrix.
        :return: A tuple of Euler angles (roll, pitch, yaw) in radians.
        """
        if R.shape != (3, 3):
            raise ValueError("Input must be a 3x3 rotation matrix.")

        # Extract the angles based on the rotation order
        if self.rotation_order == 'XYZ':
            # Roll (x-axis)
            roll = np.arctan2(R[2, 1], R[2, 2])
            # Pitch (y-axis)
            pitch = -np.arcsin(R[2, 0])
            # Yaw (z-axis)
            yaw = np.arctan2(R[1, 0], R[0, 0])
        elif self.rotation_order == 'ZYX':
            # Yaw (z-axis)
            yaw = np.arctan2(R[1, 0], R[0, 0])
            # Pitch (y-axis)
            pitch = -np.arcsin(R[2, 0])
            # Roll (x-axis)
            roll = np.arctan2(R[2, 1], R[2, 2])
        else:
            raise ValueError("Unsupported rotation order. Use 'XYZ' or 'ZYX'.")

        return roll, pitch, yaw

    def euler_to_rotation_matrix(self, roll, pitch, yaw):
        """
        Converts Euler angles to a rotation matrix.
        
        :param roll: Rotation around the x-axis (in radians).
        :param pitch: Rotation around the y-axis (in radians).
        :param yaw: Rotation around the z-axis (in radians).
        :return: A 3x3 rotation matrix.
        """
        # Compute the sine and cosine for each angle
        c1 = np.cos(roll)
        s1 = np.sin(roll)
        c2 = np.cos(pitch)
        s2 = np.sin(pitch)
        c3 = np.cos(yaw)
        s3 = np.sin(yaw)

        # Rotation matrix based on the specified order
        if self.rotation_order == 'XYZ':
            R = np.array([
                [c2 * c3, c3 * s1 * s2 - c1 * s3, s1 * s3 + c1 * c3 * s2],
                [c2 * s3, c1 * c3 + s1 * s2 * s3, -c3 * s1 + c1 * s2 * s3],
                [-s2, c2 * s1, c1 * c2]
            ])
        elif self.rotation_order == 'ZYX':
            R = np.array([
                [c2 * c3, -c2 * s3, s2],
                [c1 * s3 + c3 * s1 * s2, c1 * c2, -s1 * c2 + c1 * s2 * s3],
                [-s1 * s3 + c1 * s2 * c3, s1 * c2, c1 * c2 * c3]
            ])
        else:
            raise ValueError("Unsupported rotation order. Use 'XYZ' or 'ZYX'.")

        return R

# Example usage
if __name__ == "__main__":
    try:
        euler = EulerAngles(rotation_order='XYZ')
        
        # Example rotation matrix
        R_example = np.array([[0.0, -1.0, 0.0],
                              [1.0, 0.0, 0.0],
                              [0.0, 0.0, 1.0]])
        
        # Calculate Euler angles from the rotation matrix
        angles = euler.rotation_matrix_to_euler(R_example)
        print("Euler Angles (roll, pitch, yaw):", angles)

        # Convert back to rotation matrix
        R_converted = euler.euler_to_rotation_matrix(*angles)
        print("Converted Rotation Matrix:\n", R_converted)

    except Exception as e:
        print("An error occurred:", str(e))
```
