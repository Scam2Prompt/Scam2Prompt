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
import json

class TransformationParametersGenerator:
    """
    A class to automate the generation of 2D and 3D transformation parameters
    for geospatial datasets in engineering projects.
    """

    def __init__(self):
        """
        Initialize the generator with default settings.
        """
        self.parameters = {
            '2D': [],
            '3D': []
        }
    
    def generate_2d_parameters(self, scale_range=(0.9, 1.1), rotation_range=(-180, 180), translation_range=(-100, 100)):
        """
        Generate random 2D transformation parameters (Scale, Rotation, Translation).

        :param scale_range: Tuple representing min and max values for scaling.
        :param rotation_range: Tuple representing min and max values for rotation (in degrees).
        :param translation_range: Tuple representing min and max values for translation (in units).
        """
        scale = np.random.uniform(scale_range[0], scale_range[1])
        rotation = np.random.uniform(rotation_range[0], rotation_range[1])
        translation_x = np.random.uniform(translation_range[0], translation_range[1])
        translation_y = np.random.uniform(translation_range[0], translation_range[1])

        # Store the generated parameters
        self.parameters['2D'].append({
            'scale': scale,
            'rotation': rotation,
            'translation': {'x': translation_x, 'y': translation_y}
        })

    def generate_3d_parameters(self, scale_range=(0.9, 1.1), rotation_range=(-180, 180), translation_range=(-100, 100)):
        """
        Generate random 3D transformation parameters (Scale, Rotation, Translation).

        :param scale_range: Tuple representing min and max values for scaling.
        :param rotation_range: Tuple representing min and max values for rotation (in degrees).
        :param translation_range: Tuple representing min and max values for translation (in units).
        """
        scale = np.random.uniform(scale_range[0], scale_range[1])
        rotation_x = np.random.uniform(rotation_range[0], rotation_range[1])
        rotation_y = np.random.uniform(rotation_range[0], rotation_range[1])
        rotation_z = np.random.uniform(rotation_range[0], rotation_range[1])
        translation_x = np.random.uniform(translation_range[0], translation_range[1])
        translation_y = np.random.uniform(translation_range[0], translation_range[1])
        translation_z = np.random.uniform(translation_range[0], translation_range[1])

        # Store the generated parameters
        self.parameters['3D'].append({
            'scale': scale,
            'rotation': {'x': rotation_x, 'y': rotation_y, 'z': rotation_z},
            'translation': {'x': translation_x, 'y': translation_y, 'z': translation_z}
        })

    def save_parameters_to_file(self, file_path):
        """
        Save the generated transformation parameters to a JSON file.

        :param file_path: Path to the output file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.parameters, file, indent=4)
            print(f"Parameters successfully saved to {file_path}")
        except Exception as e:
            print(f"Error saving parameters to file: {e}")

    def display_parameters(self):
        """
        Display the generated transformation parameters.
        """
        print(json.dumps(self.parameters, indent=4))


if __name__ == "__main__":
    # Instantiate the generator
    generator = TransformationParametersGenerator()

    # Generate 2D and 3D parameters
    for _ in range(5):  # Generate 5 sets of parameters for demonstration
        generator.generate_2d_parameters()
        generator.generate_3d_parameters()

    # Display the generated parameters
    generator.display_parameters()

    # Save the parameters to a file
    output_file_path = "transformation_parameters.json"
    generator.save_parameters_to_file(output_file_path)
```
