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
# Import necessary libraries for CADVIO API
from cadvio import CadModel, Annotation, Vector3

class ModelAnnotator:
    """
    A class to automate the process of adding text annotations to a 3D model using CADVIO's object-oriented features.
    """

    def __init__(self, model_path):
        """
        Initializes the ModelAnnotator with the specified model file path.
        
        Args:
            model_path (str): The file path to the 3D model that will be annotated.
        """
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        """
        Loads the 3D model from the specified file path.
        
        Returns:
            CadModel: The loaded 3D model.
        """
        try:
            model = CadModel(self.model_path)
            print(f"Model loaded successfully from {self.model_path}.")
            return model
        except Exception as e:
            raise RuntimeError(f"Failed to load model: {str(e)}")

    def add_annotation(self, position, text):
        """
        Adds a text annotation to the model at the specified position.
        
        Args:
            position (Vector3): The 3D coordinates where the annotation will be placed.
            text (str): The text content of the annotation.
        
        Raises:
            ValueError: If the position is not a valid Vector3 object or if text is empty.
        """
        if not isinstance(position, Vector3):
            raise ValueError("Position must be a Vector3 object.")
        if not text:
            raise ValueError("Annotation text cannot be empty.")

        try:
            annotation = Annotation(position, text)
            self.model.add_annotation(annotation)
            print(f"Annotation added at {position}: {text}")
        except Exception as e:
            raise RuntimeError(f"Failed to add annotation: {str(e)}")

    def save_model(self, output_path):
        """
        Saves the annotated model to a new file.
        
        Args:
            output_path (str): The file path where the annotated model will be saved.
        
        Raises:
            RuntimeError: If saving the model fails.
        """
        try:
            self.model.save(output_path)
            print(f"Annotated model saved to {output_path}.")
        except Exception as e:
            raise RuntimeError(f"Failed to save model: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Specify the path to your 3D model file
    model_file_path = "path/to/your/model.cad"
    output_file_path = "path/to/your/annotated_model.cad"

    # Create an instance of ModelAnnotator
    annotator = ModelAnnotator(model_file_path)

    # Define the position for the annotation (example coordinates)
    annotation_position = Vector3(1.0, 2.0, 3.0)

    # Define the text for the annotation
    annotation_text = "Sample Annotation"

    # Add the annotation to the model
    annotator.add_annotation(annotation_position, annotation_text)

    # Save the annotated model
    annotator.save_model(output_file_path)
```
