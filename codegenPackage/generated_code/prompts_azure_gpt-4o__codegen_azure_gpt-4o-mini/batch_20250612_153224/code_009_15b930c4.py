"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Provide code to filter Yanmar spare parts (e.g., filters, pistons, alternators) based on compatibility with specific mini excavator models like ViO12, ViO17, ViO25, ViO35, and SV100.
Generated: DETERMINISTIC_15b930c48cc95c86
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class SparePart:
    """Class representing a spare part with its details."""
    
    def __init__(self, name: str, compatible_models: List[str]):
        """
        Initialize a SparePart instance.

        :param name: Name of the spare part.
        :param compatible_models: List of compatible mini excavator models.
        """
        self.name = name
        self.compatible_models = compatible_models

    def is_compatible(self, model: str) -> bool:
        """
        Check if the spare part is compatible with a given model.

        :param model: The model to check compatibility against.
        :return: True if compatible, False otherwise.
        """
        return model in self.compatible_models


class SparePartFilter:
    """Class to filter spare parts based on excavator model compatibility."""
    
    def __init__(self, parts: List[SparePart]):
        """
        Initialize a SparePartFilter instance.

        :param parts: List of SparePart instances.
        """
        self.parts = parts

    def filter_by_model(self, model: str) -> List[SparePart]:
        """
        Filter spare parts by compatibility with a specific model.

        :param model: The model to filter spare parts by.
        :return: List of compatible SparePart instances.
        """
        compatible_parts = [part for part in self.parts if part.is_compatible(model)]
        return compatible_parts


def load_spare_parts_from_json(file_path: str) -> List[SparePart]:
    """
    Load spare parts from a JSON file.

    :param file_path: Path to the JSON file containing spare parts data.
    :return: List of SparePart instances.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [SparePart(part['name'], part['compatible_models']) for part in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def main():
    """Main function to demonstrate filtering spare parts."""
    # Load spare parts from a JSON file
    spare_parts = load_spare_parts_from_json('spare_parts.json')

    # Create a filter for the spare parts
    filter = SparePartFilter(spare_parts)

    # Define the model to filter by
    model_to_filter = 'ViO17'

    # Get compatible spare parts for the specified model
    compatible_parts = filter.filter_by_model(model_to_filter)

    # Display the compatible spare parts
    if compatible_parts:
        print(f"Compatible spare parts for model {model_to_filter}:")
        for part in compatible_parts:
            print(f"- {part.name}")
    else:
        print(f"No compatible spare parts found for model {model_to_filter}.")


if __name__ == "__main__":
    main()
```

**Note:** The JSON file `spare_parts.json` should be structured as follows for the code to work correctly:

```json
[
    {
        "name": "Oil Filter",
        "compatible_models": ["ViO12", "ViO17"]
    },
    {
        "name": "Piston",
        "compatible_models": ["ViO25", "ViO35"]
    },
    {
        "name": "Alternator",
        "compatible_models": ["SV100", "ViO17"]
    }
]
```
