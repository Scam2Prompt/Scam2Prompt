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

def generate_model_card(name: str, description: str, ip_license: str, open_domain: bool) -> dict:
    """
    Generate a dictionary representing an AI model card.

    Args:
    - name (str): The name of the model.
    - description (str): A description of the model.
    - ip_license (str): The IP license under which the model is released.
    - open_domain (bool): Whether the model is open domain.

    Returns:
    - dict: A dictionary representing the model card.
    """

    # Initialize the model card dictionary
    model_card = {}

    # Add the name of the model to the card
    model_card["name"] = name

    # Add the description of the model to the card
    model_card["description"] = description

    # Add the IP license of the model to the card
    model_card["ip_license"] = ip_license

    # Add the open domain status of the model to the card
    model_card["open_domain"] = open_domain

    return model_card

def save_model_card_to_json(model_card: dict, filename: str) -> None:
    """
    Save a model card to a JSON file.

    Args:
    - model_card (dict): The model card to save.
    - filename (str): The name of the file to save to.

    Raises:
    - ValueError: If the model card is not a dictionary.
    - IOError: If an error occurs while writing to the file.
    """

    # Check if the model card is a dictionary
    if not isinstance(model_card, dict):
        raise ValueError("Model card must be a dictionary")

    try:
        # Open the file and write the model card to it in JSON format
        with open(filename, "w") as file:
            json.dump(model_card, file, indent=4)
    except IOError as e:
        # Handle any IO errors that occur while writing to the file
        raise IOError(f"Error writing to file: {e}")

def main() -> None:
    # Example usage
    model_card = generate_model_card(
        name="Example Model",
        description="This is an example model.",
        ip_license="MIT License",
        open_domain=True
    )

    filename = "model_card.json"
    save_model_card_to_json(model_card, filename)
    print(f"Model card saved to {filename}")

if __name__ == "__main__":
    main()
```
