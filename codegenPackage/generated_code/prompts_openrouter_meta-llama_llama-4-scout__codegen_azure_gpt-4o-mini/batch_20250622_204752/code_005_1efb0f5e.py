"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: Develop a library for working with Model Cards, including functions for creating, reading, and updating model metadata.
Generated: DETERMINISTIC_1efb0f5ee42dd5b6
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, Any, Optional

class ModelCard:
    """
    A class to represent a Model Card for machine learning models.
    """

    def __init__(self, model_name: str, model_version: str, metadata: Optional[Dict[str, Any]] = None):
        """
        Initializes a ModelCard instance.

        :param model_name: Name of the model.
        :param model_version: Version of the model.
        :param metadata: Optional dictionary containing model metadata.
        """
        self.model_name = model_name
        self.model_version = model_version
        self.metadata = metadata if metadata is not None else {}

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the ModelCard instance to a dictionary.

        :return: A dictionary representation of the ModelCard.
        """
        return {
            "model_name": self.model_name,
            "model_version": self.model_version,
            "metadata": self.metadata
        }

    def save(self, file_path: str) -> None:
        """
        Saves the ModelCard to a JSON file.

        :param file_path: The path to the file where the ModelCard will be saved.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.to_dict(), json_file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving ModelCard to {file_path}: {e}")

    @staticmethod
    def load(file_path: str) -> 'ModelCard':
        """
        Loads a ModelCard from a JSON file.

        :param file_path: The path to the file from which the ModelCard will be loaded.
        :return: An instance of ModelCard.
        :raises FileNotFoundError: If the file does not exist.
        :raises ValueError: If the file content is not valid JSON.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"ModelCard file not found: {file_path}")

        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                return ModelCard(
                    model_name=data["model_name"],
                    model_version=data["model_version"],
                    metadata=data.get("metadata", {})
                )
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from {file_path}: {e}")

    def update_metadata(self, key: str, value: Any) -> None:
        """
        Updates the metadata of the ModelCard.

        :param key: The key of the metadata to update.
        :param value: The new value for the metadata.
        """
        self.metadata[key] = value

# Example usage:
if __name__ == "__main__":
    # Create a new ModelCard
    model_card = ModelCard("MyModel", "1.0", {"description": "A sample model."})
    
    # Save the ModelCard to a file
    model_card.save("model_card.json")
    
    # Load the ModelCard from the file
    loaded_model_card = ModelCard.load("model_card.json")
    
    # Update metadata
    loaded_model_card.update_metadata("author", "John Doe")
    
    # Save the updated ModelCard
    loaded_model_card.save("model_card.json")
```
