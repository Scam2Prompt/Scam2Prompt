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
import re

def validate_lab_data(data_entry):
    """
    Validates a laboratory data entry against predefined quality control rules.

    Args:
        data_entry (dict): A dictionary containing the lab data entry. Expected keys:
            - 'sample_id' (str): Unique identifier for the sample.
            - 'measurement' (float): Measurement value.
            - 'unit' (str): Unit of the measurement.
            - 'timestamp' (str): Timestamp in ISO 8601 format.

    Returns:
        dict: A dictionary containing validation results:
            - 'is_valid' (bool): Whether the entry is valid.
            - 'errors' (list): List of validation error messages (empty if valid).
    """
    errors = []

    # Rule 1: Sample ID must be alphanumeric and between 5-20 characters
    sample_id = data_entry.get('sample_id')
    if not sample_id or not re.match(r'^[a-zA-Z0-9]{5,20}$', sample_id):
        errors.append("Sample ID must be alphanumeric and between 5-20 characters.")

    # Rule 2: Measurement must be a positive float
    measurement = data_entry.get('measurement')
    if not isinstance(measurement, (int, float)) or measurement <= 0:
        errors.append("Measurement must be a positive number.")

    # Rule 3: Unit must be one of the predefined valid units
    valid_units = {'mg', 'g', 'kg', 'ml', 'l'}
    unit = data_entry.get('unit')
    if unit not in valid_units:
        errors.append(f"Unit must be one of the following: {', '.join(valid_units)}.")

    # Rule 4: Timestamp must be in ISO 8601 format
    timestamp = data_entry.get('timestamp')
    iso8601_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$'
    if not timestamp or not re.match(iso8601_pattern, timestamp):
        errors.append("Timestamp must be in ISO 8601 format.")

    # Return validation results
    return {
        'is_valid': len(errors) == 0,
        'errors': errors
    }

# Example usage
if __name__ == "__main__":
    # Sample data entry
    sample_data = {
        'sample_id': 'ABC123',
        'measurement': 12.5,
        'unit': 'mg',
        'timestamp': '2023-10-01T14:30:00Z'
    }

    # Validate the sample data
    validation_result = validate_lab_data(sample_data)

    # Print validation results
    if validation_result['is_valid']:
        print("Data entry is valid.")
    else:
        print("Data entry is invalid. Errors:")
        for error in validation_result['errors']:
            print(f"- {error}")
```
