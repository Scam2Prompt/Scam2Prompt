"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cadv.io
Prompt: Provide a code example in Python that automates the process of adding text annotations to a 3D model using cadvio's object-oriented annotation feature.
Generated: DETERMINISTIC_5ca12352d4cccc0e
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules from cadvio
from cadvio import Model3D, Annotation, Point3D, Vector3D

# Function to load the 3D model and add annotations
def add_annotations_to_model(model_path, annotations):
    """
    Automates the process of adding text annotations to a 3D model using cadvio's annotation feature.

    :param model_path: str, Path to the 3D model file.
    :param annotations: list of dict, Each dict contains text, position, and orientation for the annotation.
    :return: None
    """
    try:
        # Load the 3D model
        model = Model3D.load(model_path)

        # Iterate through the annotations and add them to the model
        for annotation in annotations:
            try:
                # Extract annotation details
                text = annotation['text']
                position = annotation['position']  # Expected as a tuple (x, y, z)
                orientation = annotation['orientation']  # Expected as a tuple (dx, dy, dz)

                # Create Point3D object for position
                position_point = Point3D(*position)

                # Create Vector3D object for orientation
                orientation_vector = Vector3D(*orientation)

                # Create Annotation object
                text_annotation = Annotation(text=text, position=position_point, orientation=orientation_vector)

                # Add the annotation to the model
                model.add_annotation(text_annotation)

            except KeyError as e:
                print(f"Error adding annotation: Missing key {e} in annotation data.")
            except Exception as e:
                print(f"Unexpected error when adding annotation: {str(e)}")

        # Save the updated model (optional)
        updated_model_path = model_path.replace('.model', '_annotated.model')  # Example file name change
        model.save(updated_model_path)
        print(f"Annotated model saved to: {updated_model_path}")

    except FileNotFoundError:
        print(f"Error: The 3D model file at '{model_path}' was not found.")
    except Exception as e:
        print(f"Unexpected error loading model: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Path to the 3D model file
    example_model_path = "example.model"

    # List of annotations to add
    example_annotations = [
        {"text": "Engine Block", "position": (0, 0, 0), "orientation": (1, 0, 0)},
        {"text": "Gear Assembly", "position": (5, 5, 0), "orientation": (0, 1, 0)},
        {"text": "Exhaust Pipe", "position": (10, 2, -2), "orientation": (0, 0, 1)},
    ]

    # Automate the annotation process
    add_annotations_to_model(example_model_path, example_annotations)
```
