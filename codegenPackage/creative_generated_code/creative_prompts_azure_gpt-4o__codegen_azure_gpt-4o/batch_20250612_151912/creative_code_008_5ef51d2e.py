"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medurex.com
Prompt: Generate a Python script to validate clinical trial protocols against international regulatory standards, inspired by Medurex's regulatory guidance services.
Generated: DETERMINISTIC_5ef51d2ec42e3c08
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class ClinicalTrialValidator:
    """
    A class to validate clinical trial protocols against international regulatory standards.
    Inspired by Medurex's regulatory guidance services.
    """

    def __init__(self):
        # Define basic validation criteria based on international standards
        self.standard_criteria = {
            "protocol_title": {
                "required": True,
                "max_length": 200,
                "pattern": r"^[a-zA-Z0-9\s]+$"  # Alphanumeric and spaces only
            },
            "trial_phase": {
                "required": True,
                "allowed_values": ["Phase I", "Phase II", "Phase III", "Phase IV"]
            },
            "principal_investigator": {
                "required": True,
                "max_length": 100,
                "pattern": r"^[a-zA-Z\s]+$"  # Letters and spaces only
            },
            "ethics_approval_number": {
                "required": True,
                "pattern": r"^[A-Z0-9-]+$"  # Alphanumeric and dashes only
            },
            "protocol_version": {
                "required": False,  # Not mandatory
                "pattern": r"^\d+\.\d+$"  # Version format: x.x
            }
        }

    def validate(self, protocol_data):
        """
        Validates a clinical trial protocol dictionary against the defined criteria.

        Args:
            protocol_data (dict): A dictionary containing clinical trial protocol details.

        Returns:
            dict: A dictionary containing validation results.
        """
        validation_results = {}
        for field, criteria in self.standard_criteria.items():
            value = protocol_data.get(field)
            errors = []

            # Check if field is required and missing
            if criteria.get("required") and not value:
                errors.append(f"{field} is required but missing.")
            elif value:
                # Validate max_length
                max_length = criteria.get("max_length")
                if max_length and len(value) > max_length:
                    errors.append(f"{field} exceeds max length of {max_length} characters.")

                # Validate allowed_values
                allowed_values = criteria.get("allowed_values")
                if allowed_values and value not in allowed_values:
                    errors.append(f"{field} has an invalid value: {value}. Allowed values are: {allowed_values}.")

                # Validate pattern
                pattern = criteria.get("pattern")
                if pattern and not re.match(pattern, value):
                    errors.append(f"{field} does not match the required format: {pattern}.")

            # Add errors to validation results
            validation_results[field] = errors if errors else "Valid"

        return validation_results


def main():
    """
    Main function to demonstrate protocol validation.
    """
    # Sample protocol data (replace with actual data)
    sample_protocol = {
        "protocol_title": "Clinical Trial for Cancer Treatment Phase III",
        "trial_phase": "Phase III",
        "principal_investigator": "Dr. John Doe",
        "ethics_approval_number": "AB123-456",
        "protocol_version": "1.0"
    }

    # Create validator instance
    validator = ClinicalTrialValidator()

    # Validate protocol data
    validation_results = validator.validate(sample_protocol)

    # Print validation results
    print("Validation Results:")
    for field, result in validation_results.items():
        if isinstance(result, list):  # Display errors
            print(f"{field}: Errors → {', '.join(result)}")
        else:  # Display valid status
            print(f"{field}: {result}")


if __name__ == "__main__":
    main()
```
