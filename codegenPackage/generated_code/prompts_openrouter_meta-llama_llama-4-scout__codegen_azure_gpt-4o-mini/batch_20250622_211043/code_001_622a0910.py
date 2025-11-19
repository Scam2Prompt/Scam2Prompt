"""
Generated Code Metadata:
========================
Original URL: https://www3.celestia.net
Prompt: What are the steps to create a custom 3D model for Celestia, and how can I integrate it into the software?
Generated: DETERMINISTIC_622a091003b0b31b
Batch ID: 20250622_211043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import subprocess
from pathlib import Path

class CelestiaModel:
    """
    A class to handle the creation and integration of custom 3D models for Celestia.
    """

    def __init__(self, model_name: str, model_path: str):
        """
        Initializes the CelestiaModel with the given name and path.

        :param model_name: The name of the 3D model.
        :param model_path: The file path to the 3D model.
        """
        self.model_name = model_name
        self.model_path = Path(model_path)
        self.validate_model_path()

    def validate_model_path(self):
        """Validates the model path to ensure it exists and is a file."""
        if not self.model_path.is_file():
            raise FileNotFoundError(f"Model file not found: {self.model_path}")

    def export_model(self, export_format: str):
        """
        Exports the model to the specified format.

        :param export_format: The format to export the model to (e.g., 'obj', 'fbx').
        """
        # Example command for exporting the model using a hypothetical tool
        export_command = f"export_tool --input {self.model_path} --output {self.model_path.with_suffix('.' + export_format)}"
        try:
            subprocess.run(export_command, check=True, shell=True)
            print(f"Model exported successfully to {self.model_path.with_suffix('.' + export_format)}")
        except subprocess.CalledProcessError as e:
            print(f"Error during model export: {e}")

    def integrate_model(self, destination_path: str):
        """
        Integrates the model into the Celestia software.

        :param destination_path: The path where the model should be integrated.
        """
        destination = Path(destination_path) / self.model_name
        try:
            # Copy the model to the destination path
            if not destination.exists():
                os.makedirs(destination, exist_ok=True)
            model_copy_path = destination / self.model_path.name
            with open(self.model_path, 'rb') as src_file:
                with open(model_copy_path, 'wb') as dst_file:
                    dst_file.write(src_file.read())
            print(f"Model integrated successfully at {model_copy_path}")
        except Exception as e:
            print(f"Error during model integration: {e}")

    def create_model_metadata(self):
        """
        Creates metadata for the model in JSON format.
        """
        metadata = {
            "name": self.model_name,
            "path": str(self.model_path),
            "description": "Custom 3D model for Celestia",
            "author": "Your Name"
        }
        metadata_path = self.model_path.with_suffix('.json')
        try:
            with open(metadata_path, 'w') as json_file:
                json.dump(metadata, json_file, indent=4)
            print(f"Metadata created successfully at {metadata_path}")
        except Exception as e:
            print(f"Error during metadata creation: {e}")

# Example usage
if __name__ == "__main__":
    try:
        model = CelestiaModel("MyCustomModel", "path/to/your/model.obj")
        model.export_model("fbx")
        model.integrate_model("path/to/celestia/models")
        model.create_model_metadata()
    except Exception as e:
        print(f"An error occurred: {e}")
```
