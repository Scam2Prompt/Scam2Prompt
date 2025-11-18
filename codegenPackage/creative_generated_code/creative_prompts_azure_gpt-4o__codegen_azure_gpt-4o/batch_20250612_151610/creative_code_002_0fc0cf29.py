"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Generate code to validate packaging materials for table grapes using test data, inspired by Osku's testing and validation practices.
Generated: DETERMINISTIC_0fc0cf290d8a88a5
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Code to validate packaging materials for table grapes using test data.
Inspired by Osku's testing and validation practices.

This script checks the packaging material's compliance with defined specifications
such as weight, durability, and material composition using sample test data.
"""

import json

# Define Packaging Material Specifications
class PackagingSpecification:
    def __init__(self, max_weight, min_durability, allowed_materials):
        self.max_weight = max_weight  # Maximum weight (grams) the material can hold
        self.min_durability = min_durability  # Minimum durability rating (1-10)
        self.allowed_materials = allowed_materials  # List of allowed materials


# Sample Test Data
TEST_DATA = [
    {"id": 1, "name": "Plastic Box", "weight": 1500, "durability": 9, "material": "Plastic"},
    {"id": 2, "name": "Paper Carton", "weight": 1200, "durability": 6, "material": "Paper"},
    {"id": 3, "name": "Wooden Crate", "weight": 2000, "durability": 10, "material": "Wood"},
    {"id": 4, "name": "Metal Container", "weight": 2500, "durability": 8, "material": "Metal"},
    {"id": 5, "name": "Plastic Wrap", "weight": 800, "durability": 5, "material": "Plastic"},
]

# Predefined specifications for table grape packaging
PACKAGING_SPEC = PackagingSpecification(
    max_weight=2000,  # Maximum weight the packaging can hold
    min_durability=7,  # Minimum required durability rating
    allowed_materials=["Plastic", "Paper", "Wood"]  # Allowed materials for packaging
)

def validate_packaging(test_data, specifications):
    """
    Validates packaging materials against specifications.

    Parameters:
        test_data (list of dict): List of packaging materials with their attributes.
        specifications (PackagingSpecification): The defined specifications.

    Returns:
        list of dict: A list of validation results for each packaging material.
    """
    validation_results = []

    for item in test_data:
        try:
            # Check weight compliance
            weight_valid = item["weight"] <= specifications.max_weight
            # Check durability compliance
            durability_valid = item["durability"] >= specifications.min_durability
            # Check material compliance
            material_valid = item["material"] in specifications.allowed_materials

            # Determine overall validity
            is_valid = weight_valid and durability_valid and material_valid

            validation_results.append({
                "id": item["id"],
                "name": item["name"],
                "weight_valid": weight_valid,
                "durability_valid": durability_valid,
                "material_valid": material_valid,
                "is_valid": is_valid
            })
        except KeyError as e:
            # Error handling for missing keys in test data
            validation_results.append({
                "id": item.get("id", "Unknown"),
                "name": item.get("name", "Unknown"),
                "error": f"Missing key: {str(e)}",
                "is_valid": False
            })
        except Exception as e:
            # Catch all unexpected errors
            validation_results.append({
                "id": item.get("id", "Unknown"),
                "name": item.get("name", "Unknown"),
                "error": f"Unexpected error: {str(e)}",
                "is_valid": False
            })

    return validation_results

def main():
    """
    Main function to validate packaging materials and print the results.
    """
    validation_results = validate_packaging(TEST_DATA, PACKAGING_SPEC)

    print("Validation Results:")
    print(json.dumps(validation_results, indent=4))

if __name__ == "__main__":
    main()
```
