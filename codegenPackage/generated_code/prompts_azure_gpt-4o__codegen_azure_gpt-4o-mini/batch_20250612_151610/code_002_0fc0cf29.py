"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Generate code to validate packaging materials for table grapes using test data, inspired by Osku's testing and validation practices.
Generated: DETERMINISTIC_0fc0cf290d8a88a5
Batch ID: 20250612_151610
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

class PackagingMaterialValidator:
    """
    A class to validate packaging materials for table grapes.
    """

    def __init__(self, valid_materials: List[str]):
        """
        Initializes the validator with a list of valid packaging materials.

        :param valid_materials: A list of valid packaging materials.
        """
        self.valid_materials = valid_materials

    def validate(self, materials: List[str]) -> Dict[str, Any]:
        """
        Validates the provided packaging materials against the valid materials.

        :param materials: A list of packaging materials to validate.
        :return: A dictionary containing validation results.
        """
        results = {
            "valid_materials": [],
            "invalid_materials": [],
            "all_valid": True
        }

        for material in materials:
            if material in self.valid_materials:
                results["valid_materials"].append(material)
            else:
                results["invalid_materials"].append(material)
                results["all_valid"] = False

        return results

def load_test_data(file_path: str) -> List[str]:
    """
    Loads test data from a JSON file.

    :param file_path: The path to the JSON file containing test data.
    :return: A list of packaging materials.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get("packaging_materials", [])
    except FileNotFoundError:
        raise FileNotFoundError(f"Test data file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON from file: {file_path}")

def main():
    """
    Main function to execute the packaging material validation.
    """
    # Define valid packaging materials
    valid_materials = [
        "Cardboard Box",
        "Plastic Clamshell",
        "Wooden Crate",
        "Mesh Bag"
    ]

    # Load test data
    test_data_file = 'test_data.json'
    try:
        test_materials = load_test_data(test_data_file)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error loading test data: {e}")
        return

    # Create a validator instance
    validator = PackagingMaterialValidator(valid_materials)

    # Validate the test materials
    validation_results = validator.validate(test_materials)

    # Output the results
    print("Validation Results:")
    print(json.dumps(validation_results, indent=4))

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `test_data.json` file exists in the same directory as this script and contains a JSON object with a key `"packaging_materials"` that maps to a list of materials to be validated. For example:

```json
{
    "packaging_materials": [
        "Cardboard Box",
        "Plastic Clamshell",
        "Bubble Wrap",
        "Wooden Crate"
    ]
}
```
