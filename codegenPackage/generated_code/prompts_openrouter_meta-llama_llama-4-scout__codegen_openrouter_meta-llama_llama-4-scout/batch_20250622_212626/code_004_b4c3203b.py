"""
Generated Code Metadata:
========================
Original URL: https://labiqc.com
Prompt: Develop a simple script to validate laboratory data entries against predefined quality control rules.
Generated: DETERMINISTIC_b4c3203b011eb3c2
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Laboratory Data Validator

Validates laboratory data entries against predefined quality control rules.

Author: [Your Name]
Date: [Today's Date]
"""

import logging

# Define quality control rules
class QualityControlRule:
    def __init__(self, name, func):
        """
        Initialize a quality control rule.

        Args:
            name (str): Rule name
            func (callable): Rule function
        """
        self.name = name
        self.func = func

def validate_range(min_value, max_value):
    """
    Validate a value within a range.

    Args:
        min_value (float): Minimum allowed value
        max_value (float): Maximum allowed value

    Returns:
        callable: Validation function
    """
    def validate(value):
        if value < min_value or value > max_value:
            raise ValueError(f"Value {value} is outside the allowed range [{min_value}, {max_value}]")
        return True
    return validate

def validate_not_empty(value):
    """
    Validate a value is not empty.

    Args:
        value (str): Value to validate

    Returns:
        bool: Validation result
    """
    if not value:
        raise ValueError("Value is empty")
    return True

class LaboratoryDataValidator:
    def __init__(self):
        """
        Initialize the validator with predefined rules.
        """
        self.rules = [
            QualityControlRule("Glucose level", validate_range(0, 1000)),
            QualityControlRule("Patient name", validate_not_empty),
        ]

    def validate(self, data):
        """
        Validate laboratory data entries.

        Args:
            data (dict): Laboratory data entries

        Raises:
            ValueError: If any validation fails
        """
        for rule in self.rules:
            try:
                value = data.get(rule.name.lower().replace(" ", "_"))
                if value is None:
                    raise ValueError(f"Missing value for rule {rule.name}")
                rule.func(value)
            except Exception as e:
                logging.error(f"Validation failed for rule {rule.name}: {str(e)}")
                raise

def main():
    # Example usage
    data = {
        "glucose_level": 50,
        "patient_name": "John Doe",
    }

    validator = LaboratoryDataValidator()
    try:
        validator.validate(data)
        print("Data is valid")
    except ValueError as e:
        print(f"Data is invalid: {str(e)}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    main()
```
