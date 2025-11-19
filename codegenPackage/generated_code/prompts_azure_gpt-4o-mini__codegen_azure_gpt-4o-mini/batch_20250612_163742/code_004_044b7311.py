"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: Provide an example of a model card that includes a name, description, and licensing information based on the features of Lineage AI.
Generated: DETERMINISTIC_044b7311126f2fb9
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any

class ModelCard:
    """
    A class to represent a model card for machine learning models.
    
    Attributes:
        name (str): The name of the model.
        description (str): A brief description of the model.
        license_info (str): Licensing information for the model.
    """

    def __init__(self, name: str, description: str, license_info: str) -> None:
        """
        Initializes the ModelCard with the given name, description, and license information.

        Args:
            name (str): The name of the model.
            description (str): A brief description of the model.
            license_info (str): Licensing information for the model.
        """
        self.name = name
        self.description = description
        self.license_info = license_info

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the ModelCard instance to a dictionary.

        Returns:
            Dict[str, Any]: A dictionary representation of the model card.
        """
        return {
            "name": self.name,
            "description": self.description,
            "license_info": self.license_info
        }

    def to_json(self) -> str:
        """
        Converts the ModelCard instance to a JSON string.

        Returns:
            str: A JSON string representation of the model card.
        """
        return json.dumps(self.to_dict(), indent=4)

def create_model_card(name: str, description: str, license_info: str) -> ModelCard:
    """
    Creates a ModelCard instance with the provided parameters.

    Args:
        name (str): The name of the model.
        description (str): A brief description of the model.
        license_info (str): Licensing information for the model.

    Returns:
        ModelCard: An instance of ModelCard.

    Raises:
        ValueError: If any of the parameters are empty.
    """
    if not name or not description or not license_info:
        raise ValueError("Name, description, and license information must not be empty.")
    
    return ModelCard(name, description, license_info)

# Example usage
if __name__ == "__main__":
    try:
        model_card = create_model_card(
            name="Lineage AI Model",
            description="A model designed for lineage tracking in AI systems.",
            license_info="Apache 2.0 License"
        )
        print(model_card.to_json())
    except ValueError as e:
        print(f"Error creating model card: {e}")
```
