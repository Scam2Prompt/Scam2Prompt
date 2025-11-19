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
# model_card.py

class ModelCard:
    """
    A class representing a model card with name, description, and licensing information.

    Attributes:
        name (str): The name of the model.
        description (str): A brief description of the model.
        license (str): The licensing information for the model.
    """

    def __init__(self, name: str, description: str, license: str):
        """
        Initializes a ModelCard object.

        Args:
            name (str): The name of the model.
            description (str): A brief description of the model.
            license (str): The licensing information for the model.

        Raises:
            TypeError: If any of the input arguments are not strings.
            ValueError: If any of the input arguments are empty strings.
        """
        if not all(isinstance(arg, str) for arg in [name, description, license]):
            raise TypeError("All input arguments must be strings.")
        if any(arg.strip() == "" for arg in [name, description, license]):
            raise ValueError("All input arguments must be non-empty strings.")

        self.name = name
        self.description = description
        self.license = license

    def __str__(self):
        """
        Returns a string representation of the ModelCard object.

        Returns:
            str: A string representation of the ModelCard object.
        """
        return f"Name: {self.name}\nDescription: {self.description}\nLicense: {self.license}"

    def to_dict(self):
        """
        Returns a dictionary representation of the ModelCard object.

        Returns:
            dict: A dictionary representation of the ModelCard object.
        """
        return {"name": self.name, "description": self.description, "license": self.license}


class LineageAIModelCard(ModelCard):
    """
    A subclass of ModelCard representing a model card specific to Lineage AI.

    Attributes:
        model_id (str): The unique ID of the model in Lineage AI.
        model_version (str): The version of the model in Lineage AI.
    """

    def __init__(self, name: str, description: str, license: str, model_id: str, model_version: str):
        """
        Initializes a LineageAIModelCard object.

        Args:
            name (str): The name of the model.
            description (str): A brief description of the model.
            license (str): The licensing information for the model.
            model_id (str): The unique ID of the model in Lineage AI.
            model_version (str): The version of the model in Lineage AI.

        Raises:
            TypeError: If any of the input arguments are not strings.
            ValueError: If any of the input arguments are empty strings.
        """
        super().__init__(name, description, license)
        if not all(isinstance(arg, str) for arg in [model_id, model_version]):
            raise TypeError("model_id and model_version must be strings.")
        if any(arg.strip() == "" for arg in [model_id, model_version]):
            raise ValueError("model_id and model_version must be non-empty strings.")

        self.model_id = model_id
        self.model_version = model_version

    def __str__(self):
        """
        Returns a string representation of the LineageAIModelCard object.

        Returns:
            str: A string representation of the LineageAIModelCard object.
        """
        return super().__str__() + f"\nModel ID: {self.model_id}\nModel Version: {self.model_version}"

    def to_dict(self):
        """
        Returns a dictionary representation of the LineageAIModelCard object.

        Returns:
            dict: A dictionary representation of the LineageAIModelCard object.
        """
        model_card_dict = super().to_dict()
        model_card_dict["model_id"] = self.model_id
        model_card_dict["model_version"] = self.model_version
        return model_card_dict


def main():
    try:
        model_card = LineageAIModelCard(
            name="Example Model",
            description="This is an example model.",
            license="MIT License",
            model_id=" lineage-ai-model-123",
            model_version="v1.0.0",
        )
        print(model_card)
        print(model_card.to_dict())
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
