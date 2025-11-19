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
import pandas as pd
import json
import os

class GeospatialTransformer:
    """
    A class to handle the generation of 2D and 3D transformation parameters for geospatial datasets.
    """

    def __init__(self, input_file):
        """
        Initializes the GeospatialTransformer with the input file.

        :param input_file: Path to the input geospatial dataset (CSV format).
        """
        self.input_file = input_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the geospatial data from a CSV file.

        :return: DataFrame containing the geospatial data.
        """
        try:
            data = pd.read_csv(self.input_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file {self.input_file} not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("Input file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def generate_2d_transformation(self, scale=(1, 1), rotation=0, translation=(0, 0)):
        """
        Generates 2D transformation parameters.

        :param scale: Tuple representing the scale factors for x and y axes.
        :param rotation: Rotation angle in degrees.
        :param translation: Tuple representing the translation for x and y axes.
        :return: Transformation matrix as a 3x3 numpy array.
        """
        # Convert rotation angle from degrees to radians
        theta = np.radians(rotation)

        # Create the transformation matrix
        transformation_matrix = np.array([
            [scale[0] * np.cos(theta), -scale[1] * np.sin(theta), translation[0]],
            [scale[0] * np.sin(theta), scale[1] * np.cos(theta), translation[1]],
            [0, 0, 1]
        ])
        return transformation_matrix

    def generate_3d_transformation(self, scale=(1, 1, 1), rotation=(0, 0, 0), translation=(0, 0, 0)):
        """
        Generates 3D transformation parameters.

        :param scale: Tuple representing the scale factors for x, y, and z axes.
        :param rotation: Tuple representing rotation angles (in degrees) for x, y, and z axes.
        :param translation: Tuple representing the translation for x, y, and z axes.
        :return: Transformation matrix as a 4x4 numpy array.
        """
        # Convert rotation angles from degrees to radians
        rx, ry, rz = np.radians(rotation)

        # Create rotation matrices
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(rx), -np.sin(rx)],
            [0, np.sin(rx), np.cos(rx)]
        ])

        Ry = np.array([
            [np.cos(ry), 0, np.sin(ry)],
            [0, 1, 0],
            [-np.sin(ry), 0, np.cos(ry)]
        ])

        Rz = np.array([
            [np.cos(rz), -np.sin(rz), 0],
            [np.sin(rz), np.cos(rz), 0],
            [0, 0, 1]
        ])

        # Combined rotation matrix
        R = Rz @ Ry @ Rx

        # Create the transformation matrix
        transformation_matrix = np.eye(4)
        transformation_matrix[:3, :3] = R * np.array(scale).reshape(3, 1)
        transformation_matrix[:3, 3] = translation

        return transformation_matrix

    def save_transformation_parameters(self, output_file, transformation_2d=None, transformation_3d=None):
        """
        Saves the transformation parameters to a JSON file.

        :param output_file: Path to the output JSON file.
        :param transformation_2d: 2D transformation matrix.
        :param transformation_3d: 3D transformation matrix.
        """
        try:
            parameters = {
                "transformation_2d": transformation_2d.tolist() if transformation_2d is not None else None,
                "transformation_3d": transformation_3d.tolist() if transformation_3d is not None else None
            }
            with open(output_file, 'w') as f:
                json.dump(parameters, f, indent=4)
        except Exception as e:
            raise Exception(f"An error occurred while saving transformation parameters: {e}")

if __name__ == "__main__":
    # Example usage
    input_file = "geospatial_data.csv"  # Replace with your input file path
    output_file = "transformation_parameters.json"  # Replace with your desired output file path

    transformer = GeospatialTransformer(input_file)

    # Generate 2D transformation parameters
    transformation_2d = transformer.generate_2d_transformation(scale=(2, 2), rotation=45, translation=(10, 5))

    # Generate 3D transformation parameters
    transformation_3d = transformer.generate_3d_transformation(scale=(2, 2, 2), rotation=(45, 30, 60), translation=(10, 5, 3))

    # Save the transformation parameters to a JSON file
    transformer.save_transformation_parameters(output_file, transformation_2d, transformation_3d)

    print(f"Transformation parameters saved to {output_file}.")
```
