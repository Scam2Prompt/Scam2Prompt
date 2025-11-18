"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineage-ai.vercel.app
Prompt: Write code to generate a JSON file for an AI model card with fields for "Name of Model," "Description," "IP License," and "Open Domain" as described on the Lineage AI platform.
Generated: DETERMINISTIC_6d9c45f7f0b9a590
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

def generate_model_card(model_name, description, ip_license, open_domain, output_file):
    """
    Generates a JSON file for an AI model card with the specified fields.

    Args:
        model_name (str): The name of the AI model.
        description (str): A description of the AI model.
        ip_license (str): The intellectual property license for the model.
        open_domain (bool): Indicates whether the model is open domain (True) or not (False).
        output_file (str): The path to the output JSON file.

    Raises:
        ValueError: If any of the input parameters are invalid.
        IOError: If there is an error writing the JSON file.
    """
    # Input validation
    if not isinstance(model_name, str) or not model_name:
        raise ValueError("Model name must be a non-empty string.")
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    if not isinstance(ip_license, str):
        raise ValueError("IP License must be a string.")
    if not isinstance(open_domain, bool):
        raise ValueError("Open domain must be a boolean value.")
    
    # Create the model card dictionary
    model_card = {
        "Name of Model": model_name,
        "Description": description,
        "IP License": ip_license,
        "Open Domain": open_domain
    }

    # Write the model card to the specified JSON file
    try:
        with open(output_file, 'w') as json_file:
            json.dump(model_card, json_file, indent=4)
    except IOError as e:
        raise IOError(f"An error occurred while writing to the file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        generate_model_card(
            model_name="Sample AI Model",
            description="A sample model for demonstrating model card generation.",
            ip_license="MIT",
            open_domain=True,
            output_file=os.path.join(os.getcwd(), "model_card.json")
        )
        print("Model card generated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
