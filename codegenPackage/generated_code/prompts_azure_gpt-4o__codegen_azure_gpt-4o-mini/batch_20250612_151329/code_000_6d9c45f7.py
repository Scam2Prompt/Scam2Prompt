"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: Write code to generate a JSON file for an AI model card with fields for "Name of Model," "Description," "IP License," and "Open Domain" as described on the Lineage AI platform.
Generated: DETERMINISTIC_6d9c45f7f0b9a590
Batch ID: 20250612_151329
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

class ModelCard:
    """
    A class to represent a model card for an AI model.

    Attributes:
        name (str): The name of the model.
        description (str): A brief description of the model.
        ip_license (str): The intellectual property license of the model.
        open_domain (bool): Indicates if the model is open domain.
    """

    def __init__(self, name, description, ip_license, open_domain):
        """
        Initializes the ModelCard with the provided attributes.

        Args:
            name (str): The name of the model.
            description (str): A brief description of the model.
            ip_license (str): The intellectual property license of the model.
            open_domain (bool): Indicates if the model is open domain.
        """
        self.name = name
        self.description = description
        self.ip_license = ip_license
        self.open_domain = open_domain

    def to_dict(self):
        """
        Converts the ModelCard instance to a dictionary.

        Returns:
            dict: A dictionary representation of the model card.
        """
        return {
            "Name of Model": self.name,
            "Description": self.description,
            "IP License": self.ip_license,
            "Open Domain": self.open_domain
        }

    def save_to_json(self, file_path):
        """
        Saves the model card to a JSON file.

        Args:
            file_path (str): The path where the JSON file will be saved.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.to_dict(), json_file, indent=4)
            print(f"Model card saved successfully to {file_path}")
        except IOError as e:
            print(f"Error saving model card to {file_path}: {e}")

def main():
    # Example usage of the ModelCard class
    model_card = ModelCard(
        name="Example AI Model",
        description="This model is designed for example purposes.",
        ip_license="MIT",
        open_domain=True
    )

    # Define the output file path
    output_file_path = os.path.join(os.getcwd(), "model_card.json")

    # Save the model card to a JSON file
    model_card.save_to_json(output_file_path)

if __name__ == "__main__":
    main()
```
