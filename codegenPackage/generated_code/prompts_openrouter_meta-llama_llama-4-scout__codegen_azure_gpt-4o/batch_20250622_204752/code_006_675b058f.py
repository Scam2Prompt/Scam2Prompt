"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: How can I use Model Cards to manage AI models with different licenses, such as free with attribution or paid with no attribution? Provide a code example.
Generated: DETERMINISTIC_675b058f826916db
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

class ModelCard:
    """
    A class to represent and manage AI model metadata, including licensing information.
    """

    def __init__(self, name, description, license_type, license_details):
        """
        Initialize a ModelCard instance.

        :param name: Name of the AI model.
        :param description: Description of the AI model.
        :param license_type: Type of license (e.g., 'Free with Attribution', 'Paid with No Attribution').
        :param license_details: Additional details about the license.
        """
        self.name = name
        self.description = description
        self.license_type = license_type
        self.license_details = license_details

    def to_dict(self):
        """
        Convert the ModelCard instance to a dictionary.

        :return: Dictionary representation of the model card.
        """
        return {
            "name": self.name,
            "description": self.description,
            "license_type": self.license_type,
            "license_details": self.license_details,
        }

    def save_to_file(self, file_path):
        """
        Save the ModelCard instance to a JSON file.

        :param file_path: Path to the file where the model card will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
            print(f"Model card saved successfully to {file_path}")
        except Exception as e:
            print(f"Error saving model card to file: {e}")

    @staticmethod
    def load_from_file(file_path):
        """
        Load a ModelCard instance from a JSON file.

        :param file_path: Path to the file containing the model card data.
        :return: ModelCard instance.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return ModelCard(
                name=data["name"],
                description=data["description"],
                license_type=data["license_type"],
                license_details=data["license_details"],
            )
        except Exception as e:
            print(f"Error loading model card from file: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Create a model card for a free model with attribution
    free_model_card = ModelCard(
        name="FreeModel",
        description="A free AI model requiring attribution.",
        license_type="Free with Attribution",
        license_details="You must credit the author when using this model."
    )

    # Save the model card to a file
    free_model_card.save_to_file("free_model_card.json")

    # Load the model card from the file
    loaded_model_card = ModelCard.load_from_file("free_model_card.json")
    if loaded_model_card:
        print("Loaded Model Card:")
        print(loaded_model_card.to_dict())

    # Create a model card for a paid model with no attribution
    paid_model_card = ModelCard(
        name="PaidModel",
        description="A paid AI model with no attribution required.",
        license_type="Paid with No Attribution",
        license_details="You must purchase a license to use this model."
    )

    # Save the model card to a file
    paid_model_card.save_to_file("paid_model_card.json")

    # Load the model card from the file
    loaded_paid_model_card = ModelCard.load_from_file("paid_model_card.json")
    if loaded_paid_model_card:
        print("Loaded Paid Model Card:")
        print(loaded_paid_model_card.to_dict())
```
