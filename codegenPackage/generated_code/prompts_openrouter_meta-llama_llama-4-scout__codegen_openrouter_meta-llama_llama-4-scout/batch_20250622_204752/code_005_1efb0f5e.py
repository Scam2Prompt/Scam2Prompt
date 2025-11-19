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
# model_card_library.py

"""
Library for working with Model Cards, including functions for creating, reading, and updating model metadata.
"""

import json
import os

class ModelCard:
    """
    Represents a Model Card with metadata.

    Attributes:
        name (str): Name of the model.
        description (str): Description of the model.
        metrics (dict): Dictionary of metrics.
        hyperparameters (dict): Dictionary of hyperparameters.
    """

    def __init__(self, name, description, metrics=None, hyperparameters=None):
        """
        Initializes a ModelCard object.

        Args:
            name (str): Name of the model.
            description (str): Description of the model.
            metrics (dict, optional): Dictionary of metrics. Defaults to None.
            hyperparameters (dict, optional): Dictionary of hyperparameters. Defaults to None.
        """
        self.name = name
        self.description = description
        self.metrics = metrics if metrics is not None else {}
        self.hyperparameters = hyperparameters if hyperparameters is not None else {}

    def to_dict(self):
        """
        Converts the ModelCard object to a dictionary.

        Returns:
            dict: Dictionary representation of the ModelCard object.
        """
        return {
            "name": self.name,
            "description": self.description,
            "metrics": self.metrics,
            "hyperparameters": self.hyperparameters,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a ModelCard object from a dictionary.

        Args:
            data (dict): Dictionary representation of the ModelCard object.

        Returns:
            ModelCard: ModelCard object.
        """
        return cls(
            data["name"],
            data["description"],
            data.get("metrics"),
            data.get("hyperparameters"),
        )


class ModelCardRepository:
    """
    Repository for storing and retrieving Model Cards.
    """

    def __init__(self, storage_dir):
        """
        Initializes a ModelCardRepository object.

        Args:
            storage_dir (str): Directory for storing Model Cards.
        """
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def create_model_card(self, model_card):
        """
        Creates a new Model Card.

        Args:
            model_card (ModelCard): ModelCard object to create.

        Raises:
            Exception: If the model card already exists.
        """
        file_path = os.path.join(self.storage_dir, f"{model_card.name}.json")
        if os.path.exists(file_path):
            raise Exception(f"Model card {model_card.name} already exists.")
        with open(file_path, "w") as f:
            json.dump(model_card.to_dict(), f, indent=4)

    def get_model_card(self, name):
        """
        Retrieves a Model Card by name.

        Args:
            name (str): Name of the model card.

        Returns:
            ModelCard: ModelCard object.

        Raises:
            Exception: If the model card does not exist.
        """
        file_path = os.path.join(self.storage_dir, f"{name}.json")
        if not os.path.exists(file_path):
            raise Exception(f"Model card {name} does not exist.")
        with open(file_path, "r") as f:
            data = json.load(f)
            return ModelCard.from_dict(data)

    def update_model_card(self, model_card):
        """
        Updates an existing Model Card.

        Args:
            model_card (ModelCard): ModelCard object to update.

        Raises:
            Exception: If the model card does not exist.
        """
        file_path = os.path.join(self.storage_dir, f"{model_card.name}.json")
        if not os.path.exists(file_path):
            raise Exception(f"Model card {model_card.name} does not exist.")
        with open(file_path, "w") as f:
            json.dump(model_card.to_dict(), f, indent=4)


def main():
    # Example usage
    repository = ModelCardRepository("model_cards")

    # Create a model card
    model_card = ModelCard(
        "example_model",
        "This is an example model.",
        metrics={"accuracy": 0.9},
        hyperparameters={"learning_rate": 0.01},
    )
    repository.create_model_card(model_card)

    # Retrieve a model card
    retrieved_model_card = repository.get_model_card("example_model")
    print(retrieved_model_card.to_dict())

    # Update a model card
    updated_model_card = ModelCard(
        "example_model",
        "This is an updated example model.",
        metrics={"accuracy": 0.92},
        hyperparameters={"learning_rate": 0.01},
    )
    repository.update_model_card(updated_model_card)


if __name__ == "__main__":
    main()
```
