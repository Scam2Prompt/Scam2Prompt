"""
Generated Code Metadata:
========================
Original URL: https://goldenapp.online
Prompt: Create a code example that demonstrates how to validate results in an AI application, similar to the process outlined on goldenapp.online.
Generated: DETERMINISTIC_eb4b30eecf1eb016
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Any, Dict, List, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO)

class AIResultValidator:
    """
    A class to validate results from an AI application.
    """

    def __init__(self, expected_schema: Dict[str, Any]):
        """
        Initializes the validator with the expected schema.

        :param expected_schema: A dictionary defining the expected structure of the AI results.
        """
        self.expected_schema = expected_schema

    def validate(self, results: List[Dict[str, Any]]) -> List[Tuple[int, str]]:
        """
        Validates a list of AI results against the expected schema.

        :param results: A list of dictionaries representing AI results.
        :return: A list of tuples containing the index of the invalid result and the error message.
        """
        errors = []
        for index, result in enumerate(results):
            try:
                self._validate_result(result)
            except ValueError as e:
                errors.append((index, str(e)))
        return errors

    def _validate_result(self, result: Dict[str, Any]) -> None:
        """
        Validates a single AI result against the expected schema.

        :param result: A dictionary representing a single AI result.
        :raises ValueError: If the result does not conform to the expected schema.
        """
        for key, expected_type in self.expected_schema.items():
            if key not in result:
                raise ValueError(f"Missing key: {key}")
            if not isinstance(result[key], expected_type):
                raise ValueError(f"Invalid type for key '{key}': expected {expected_type.__name__}, got {type(result[key]).__name__}")

def main():
    # Define the expected schema for the AI results
    expected_schema = {
        "id": int,
        "name": str,
        "score": float,
        "is_valid": bool
    }

    # Sample AI results to validate
    ai_results = [
        {"id": 1, "name": "Result A", "score": 0.95, "is_valid": True},
        {"id": 2, "name": "Result B", "score": "high", "is_valid": False},  # Invalid score type
        {"id": 3, "name": "Result C", "is_valid": True},  # Missing score
        {"id": 4, "name": "Result D", "score": 0.85, "is_valid": "yes"},  # Invalid is_valid type
    ]

    # Create an instance of the validator
    validator = AIResultValidator(expected_schema)

    # Validate the AI results
    validation_errors = validator.validate(ai_results)

    # Log the validation results
    if validation_errors:
        logging.error("Validation errors found:")
        for index, error in validation_errors:
            logging.error(f"Result at index {index}: {error}")
    else:
        logging.info("All results are valid.")

if __name__ == "__main__":
    main()
```
