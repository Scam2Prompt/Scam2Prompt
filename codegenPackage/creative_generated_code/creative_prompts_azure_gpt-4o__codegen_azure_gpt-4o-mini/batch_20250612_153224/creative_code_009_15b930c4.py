"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Provide code to filter Yanmar spare parts (e.g., filters, pistons, alternators) based on compatibility with specific mini excavator models like ViO12, ViO17, ViO25, ViO35, and SV100.
Generated: DETERMINISTIC_15b930c48cc95c86
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SparePart:
    """Represents a spare part with its name and compatible models."""
    
    def __init__(self, name, compatible_models):
        """
        Initializes a new SparePart instance.
        
        :param name: Name of the spare part.
        :param compatible_models: List of compatible mini excavator models.
        """
        self.name = name
        self.compatible_models = compatible_models

    def is_compatible(self, model):
        """
        Checks if the spare part is compatible with a given model.
        
        :param model: The model to check compatibility against.
        :return: True if compatible, False otherwise.
        """
        return model in self.compatible_models


class SparePartFilter:
    """Provides filtering functionality for a list of spare parts."""

    def __init__(self, parts):
        """
        Initializes the SparePartFilter with a list of spare parts.
        
        :param parts: List of SparePart objects.
        """
        self.parts = parts

    def filter_by_model(self, model):
        """
        Filters spare parts by compatibility with the specified model.
        
        :param model: The model to filter spare parts by.
        :return: List of compatible SparePart objects.
        """
        compatible_parts = [part for part in self.parts if part.is_compatible(model)]
        return compatible_parts


def load_spare_parts_from_json(file_path):
    """
    Loads spare parts from a given JSON file.
    
    :param file_path: Path to the JSON file containing spare parts data.
    :return: List of SparePart objects.
    :raises FileNotFoundError: If the file does not exist.
    :raises json.JSONDecodeError: If the JSON is invalid.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            spare_parts = [SparePart(part['name'], part['compatible_models']) for part in data['parts']]
            return spare_parts
    except FileNotFoundError as e:
        print(f"Error: The file {file_path} was not found.")
        raise e
    except json.JSONDecodeError as e:
        print("Error: Failed to decode JSON from the file.")
        raise e


if __name__ == "__main__":
    # Define the path to the JSON file containing spare parts data
    json_file_path = 'spare_parts.json'

    try:
        # Load spare parts from the JSON file
        spare_parts = load_spare_parts_from_json(json_file_path)

        # Create a filter for spare parts
        filter = SparePartFilter(spare_parts)

        # Specify the model to filter spare parts for
        excavator_model = 'ViO25'
        compatible_parts = filter.filter_by_model(excavator_model)

        # Print out the compatible spare parts
        if compatible_parts:
            print(f"Compatible spare parts for {excavator_model}:")
            for part in compatible_parts:
                print(f"- {part.name}")
        else:
            print(f"No compatible spare parts found for {excavator_model}.")

    except Exception as e:
        print(f"An error occurred: {e}")
```

```json
{
  "parts": [
    {
      "name": "Oil Filter",
      "compatible_models": ["ViO12", "ViO17", "ViO25"]
    },
    {
      "name": "Air Filter",
      "compatible_models": ["ViO17", "ViO25", "SV100"]
    },
    {
      "name": "Piston",
      "compatible_models": ["ViO25", "ViO35"]
    },
    {
      "name": "Alternator",
      "compatible_models": ["ViO12", "SV100"]
    }
  ]
}
```
