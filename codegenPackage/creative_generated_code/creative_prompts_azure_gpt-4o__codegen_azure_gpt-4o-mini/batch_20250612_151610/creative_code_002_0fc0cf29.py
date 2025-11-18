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
import json
import logging

# Configure logging for better traceability and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PackagingMaterialValidator:
    def __init__(self, valid_materials):
        """
        Initialize the PackagingMaterialValidator with a list of valid materials.
        
        :param valid_materials: List of valid packaging materials.
        """
        self.valid_materials = valid_materials

    def validate_material(self, material):
        """
        Validate a single packaging material against the list of valid materials.
        
        :param material: Packaging material to validate.
        :return: Boolean indicating whether the material is valid.
        """
        if not isinstance(material, str):
            logging.error("Invalid input type: Expected a string.")
            raise ValueError("Material must be a string.")
        
        is_valid = material in self.valid_materials
        logging.info(f"Material '{material}' validation result: {is_valid}")
        return is_valid

    def validate_materials(self, materials):
        """
        Validate a list of packaging materials.
        
        :param materials: List of packaging materials to validate.
        :return: Dictionary with materials and their validation results.
        """
        if not isinstance(materials, list):
            logging.error("Invalid input type: Expected a list.")
            raise ValueError("Materials must be a list.")
        
        results = {}
        for material in materials:
            try:
                results[material] = self.validate_material(material)
            except ValueError as e:
                results[material] = str(e)

        return results

# Sample test data for packaging material validation
if __name__ == "__main__":
    # List of valid packaging materials
    valid_materials = ["plastic", "cardboard", "biodegradable", "glass"]

    # Create an instance of the PackagingMaterialValidator
    validator = PackagingMaterialValidator(valid_materials)

    # Test data to validate
    test_materials = ["plastic", "cardboard", "metal", "biodegradable", "wood"]

    # Validate the test materials
    validation_results = validator.validate_materials(test_materials)

    # Output the validation results
    print(json.dumps(validation_results, indent=4))
```
