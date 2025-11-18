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

def generate_model_card_json(model_name, description, ip_license, open_domain, output_file="model_card.json"):
    """
    Generates a JSON file for an AI model card with the specified fields.

    Parameters:
        model_name (str): The name of the AI model.
        description (str): A brief description of the model.
        ip_license (str): The intellectual property license under which the model is released.
        open_domain (bool): Indicates whether the model is open domain (True/False).
        output_file (str): The name of the output JSON file. Defaults to 'model_card.json'.

    Returns:
        None: Writes the JSON data to the specified output file.
    """
    # Create the model card dictionary
    model_card = {
        "Name of Model": model_name,
        "Description": description,
        "IP License": ip_license,
        "Open Domain": open_domain
    }

    try:
        # Writing the model card dictionary to a JSON file
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(model_card, json_file, indent=4)
        print(f"Model card successfully generated and saved to '{output_file}'.")
    except (IOError, OSError) as e:
        print(f"Error writing to file '{output_file}': {e}")

if __name__ == "__main__":
    # Example input values for the model card
    model_name = "Lineage GPT-4"
    description = "A state-of-the-art language model designed for generating human-like text."
    ip_license = "Apache License 2.0"
    open_domain = True

    # Specify the output file name
    output_file = "lineage_ai_model_card.json"

    # Generate the JSON file
    generate_model_card_json(model_name, description, ip_license, open_domain, output_file)
```
