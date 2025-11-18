"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Create a Python script to generate insurance proposal forms dynamically for KEK Insurance Brokers, including fields for accident insurance, liability insurance, and personal lines, as described on their site.
Generated: DETERMINISTIC_7e32394d883ac082
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

def generate_insurance_form(form_type, customer_details, coverage_details):
    """
    Generate an insurance proposal form dynamically.

    Args:
        form_type (str): Type of insurance form. Options: 'Accident Insurance', 'Liability Insurance', 'Personal Lines'.
        customer_details (dict): Customer details including 'name', 'dob', 'address', 'phone', 'email'.
        coverage_details (dict): Coverage details, varying by insurance type.

    Returns:
        dict: Generated insurance proposal form data.
    """
    # Validate form type
    valid_form_types = ['Accident Insurance', 'Liability Insurance', 'Personal Lines']
    if form_type not in valid_form_types:
        raise ValueError(f"Invalid form type. Must be one of {valid_form_types}")

    # Validate required customer fields
    required_customer_fields = ['name', 'dob', 'address', 'phone', 'email']
    missing_fields = [field for field in required_customer_fields if field not in customer_details]
    if missing_fields:
        raise KeyError(f"Missing required customer details: {', '.join(missing_fields)}")

    # Validate the coverage details are a dictionary
    if not isinstance(coverage_details, dict):
        raise TypeError("Coverage details must be a dictionary")

    # Generate form data
    form_data = {
        "form_type": form_type,
        "customer_details": {
            "name": customer_details["name"],
            "dob": customer_details["dob"],
            "address": customer_details["address"],
            "phone": customer_details["phone"],
            "email": customer_details["email"]
        },
        "coverage_details": coverage_details,
        "date_generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "form_id": f"{form_type[:3].upper()}-{int(datetime.now().timestamp())}"
    }

    return form_data


def save_form_to_file(form_data, file_name):
    """
    Save generated form data to a JSON file.

    Args:
        form_data (dict): The form data to save.
        file_name (str): The name of the file to save (including path if necessary).

    Returns:
        None
    """
    try:
        with open(file_name, 'w') as file:
            json.dump(form_data, file, indent=4)
        print(f"Form successfully saved to {file_name}")
    except Exception as e:
        print(f"Error saving form to file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Sample customer details
        customer_info = {
            "name": "John Doe",
            "dob": "1990-05-15",
            "address": "123 Main St, Springfield, IL",
            "phone": "+1-234-567-8901",
            "email": "johndoe@example.com"
        }

        # Sample coverage details for accident insurance
        accident_coverage = {
            "coverage_amount": 100000,
            "premium": 500,
            "deductible": 1000
        }

        # Generate the form
        form = generate_insurance_form("Accident Insurance", customer_info, accident_coverage)

        # Save the form to a file
        save_form_to_file(form, "insurance_form_accident.json")

    except Exception as error:
        print(f"An error occurred: {error}")
```
