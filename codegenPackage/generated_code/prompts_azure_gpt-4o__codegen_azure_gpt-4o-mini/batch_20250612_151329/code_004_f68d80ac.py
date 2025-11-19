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
import re

class JSONValidator:
    """
    A class to validate the fields in a JSON file before uploading to a web app.
    """

    def __init__(self, json_data):
        """
        Initializes the JSONValidator with the provided JSON data.

        :param json_data: A dictionary representing the JSON data to validate.
        """
        self.json_data = json_data

    def validate(self):
        """
        Validates the required fields in the JSON data.

        :return: A tuple containing a boolean indicating validity and a list of error messages.
        """
        errors = []
        is_valid = True

        # Validate "Name of Model"
        if not self.validate_name_of_model(self.json_data.get("Name of Model", "")):
            errors.append("Invalid 'Name of Model': Must be a non-empty string.")
            is_valid = False

        # Validate "Description"
        if not self.validate_description(self.json_data.get("Description", "")):
            errors.append("Invalid 'Description': Must be a non-empty string.")
            is_valid = False

        # Validate "IP License"
        if not self.validate_ip_license(self.json_data.get("IP License", "")):
            errors.append("Invalid 'IP License': Must be a valid IP address.")
            is_valid = False

        return is_valid, errors

    @staticmethod
    def validate_name_of_model(name):
        """
        Validates the 'Name of Model' field.

        :param name: The name of the model to validate.
        :return: True if valid, False otherwise.
        """
        return isinstance(name, str) and bool(name.strip())

    @staticmethod
    def validate_description(description):
        """
        Validates the 'Description' field.

        :param description: The description to validate.
        :return: True if valid, False otherwise.
        """
        return isinstance(description, str) and bool(description.strip())

    @staticmethod
    def validate_ip_license(ip_license):
        """
        Validates the 'IP License' field to ensure it is a valid IP address.

        :param ip_license: The IP License to validate.
        :return: True if valid, False otherwise.
        """
        ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        return bool(ip_pattern.match(ip_license))

def load_json_file(file_path):
    """
    Loads a JSON file and returns its content as a dictionary.

    :param file_path: The path to the JSON file.
    :return: A dictionary representing the JSON data.
    :raises FileNotFoundError: If the file does not exist.
    :raises json.JSONDecodeError: If the file is not a valid JSON.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def main(file_path):
    """
    Main function to validate JSON data from a file.

    :param file_path: The path to the JSON file to validate.
    """
    try:
        json_data = load_json_file(file_path)
        validator = JSONValidator(json_data)
        is_valid, errors = validator.validate()

        if is_valid:
            print("JSON data is valid.")
        else:
            print("JSON data is invalid. Errors:")
            for error in errors:
                print(f"- {error}")

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON file: {e}")

if __name__ == "__main__":
    # Replace 'path/to/your/file.json' with the actual path to your JSON file
    main('path/to/your/file.json')
```
