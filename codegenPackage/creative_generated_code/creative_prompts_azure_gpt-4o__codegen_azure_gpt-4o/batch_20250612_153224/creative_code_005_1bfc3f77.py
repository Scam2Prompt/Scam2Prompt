"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erpify.co
Prompt: Write a function to develop custom forms for Oracle ERP, using the form development services highlighted on ERPIFY.
Generated: DETERMINISTIC_1bfc3f77aa65e82a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module: oracle_form_builder

This module provides functionality to develop custom forms for Oracle ERP using
ERPIFY development services. The function `create_custom_form` allows users to create
forms with specified fields, validation rules, and submission actions.
"""

# Import necessary libraries
import json

# Define custom exception for form creation errors
class FormCreationError(Exception):
    """Exception raised for errors in the custom form creation process."""
    pass

def create_custom_form(form_name, fields, submit_action):
    """
    Creates a custom form for Oracle ERP using ERPIFY.

    Args:
        form_name (str): The name of the form to be created.
        fields (list): A list of dictionaries representing form fields. Each field should have:
            - 'name' (str): The name of the field.
            - 'type' (str): The data type of the field (e.g., 'text', 'number', 'date').
            - 'required' (bool): Whether the field is required.
            - 'validation' (dict): Additional validation rules (optional, e.g., min/max length).
        submit_action (callable): A callback function to handle form submission.

    Returns:
        dict: A JSON-like dictionary representing the created form.

    Raises:
        FormCreationError: If the form name is invalid or required fields are missing.
    """
    try:
        # Validate inputs
        if not isinstance(form_name, str) or not form_name.strip():
            raise FormCreationError("Form name must be a non-empty string.")

        if not isinstance(fields, list) or not all(isinstance(field, dict) for field in fields):
            raise FormCreationError("Fields must be a list of dictionaries.")

        if not callable(submit_action):
            raise FormCreationError("Submit action must be a callable function.")

        # Construct the form
        form = {
            "form_name": form_name,
            "fields": [],
            "submit_action": submit_action.__name__,  # Store submit action name for reference
        }

        for field in fields:
            # Validate each field
            if not all(key in field for key in ['name', 'type', 'required']):
                raise FormCreationError(f"Field {field} is missing required keys.")

            field_entry = {
                "name": field["name"],
                "type": field["type"],
                "required": field["required"],
                "validation": field.get("validation", {}),
            }

            form["fields"].append(field_entry)

        # Convert the form structure to JSON for further processing
        form_json = json.dumps(form, indent=4)
        print("Form created successfully:")
        print(form_json)

        return form

    except FormCreationError as e:
        print(f"Error creating form: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Define fields for the custom form
    fields = [
        {"name": "username", "type": "text", "required": True, "validation": {"min_length": 5, "max_length": 20}},
        {"name": "age", "type": "number", "required": False, "validation": {"min_value": 0, "max_value": 150}},
        {"name": "dob", "type": "date", "required": True},
    ]

    # Define a submission action
    def submit_callback(form_data):
        """Handles form submission."""
        print("Form submitted with data:", form_data)

    # Create the custom form
    try:
        custom_form = create_custom_form("UserDetailsForm", fields, submit_callback)
    except Exception as e:
        print(f"Failed to create the form: {e}")
```
