"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: Generate code for validating the fields in a JSON file (e.g., "Name of Model," "Description," "IP License") before uploading it to a web app, as described on the Lineage AI site.
Generated: DETERMINISTIC_f68d80ac35ee851c
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def validate_json_fields(json_file_path):
    """
    Validate the fields in a JSON file.

    Args:
        json_file_path (str): The path to the JSON file.

    Returns:
        bool: True if the JSON file is valid, False otherwise.
    """
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{json_file_path}' was not found.")
        return False
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON - {e}")
        return False

    required_fields = ["Name of Model", "Description", "IP License"]

    # Check if all required fields exist
    if not all(field in data for field in required_fields):
        print("Error: The JSON file is missing one or more required fields.")
        return False

    # Check if all fields have values
    for field, value in data.items():
        if not value:
            print(f"Error: The field '{field}' is empty.")
            return False

    print("The JSON file is valid.")
    return True


def validate_json_schema(json_file_path, schema):
    """
    Validate the JSON file against a schema.

    Args:
        json_file_path (str): The path to the JSON file.
        schema (dict): The schema to validate against.

    Returns:
        bool: True if the JSON file is valid, False otherwise.
    """
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{json_file_path}' was not found.")
        return False
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON - {e}")
        return False

    # Check if the JSON data matches the schema
    if not validate_schema(data, schema):
        print("Error: The JSON file does not match the schema.")
        return False

    print("The JSON file is valid.")
    return True


def validate_schema(data, schema):
    """
    Recursively validate the schema.

    Args:
        data (dict): The data to validate.
        schema (dict): The schema to validate against.

    Returns:
        bool: True if the data is valid, False otherwise.
    """
    for key, value in schema.items():
        if key not in data:
            return False
        if isinstance(value, dict):
            if not isinstance(data[key], dict):
                return False
            if not validate_schema(data[key], value):
                return False
        elif value == "string":
            if not isinstance(data[key], str):
                return False
        elif value == "boolean":
            if not isinstance(data[key], bool):
                return False
        elif value == "integer":
            if not isinstance(data[key], int):
                return False

    return True


if __name__ == "__main__":
    json_file_path = "example.json"

    # Define the schema
    schema = {
        "Name of Model": "string",
        "Description": "string",
        "IP License": "string"
    }

    # Validate the JSON fields
    validate_json_fields(json_file_path)

    # Validate the JSON schema
    validate_json_schema(json_file_path, schema)
```
