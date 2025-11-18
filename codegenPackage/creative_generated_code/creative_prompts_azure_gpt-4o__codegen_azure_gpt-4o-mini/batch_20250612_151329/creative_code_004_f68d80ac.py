"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineage-ai.vercel.app
Prompt: Generate code for validating the fields in a JSON file (e.g., "Name of Model," "Description," "IP License") before uploading it to a web app, as described on the Lineage AI site.
Generated: DETERMINISTIC_f68d80ac35ee851c
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import re

class JSONValidator:
    """
    A class to validate fields in a JSON file for a web application.
    """
    
    def __init__(self, json_data):
        """
        Initialize the validator with JSON data.

        :param json_data: A dictionary representation of JSON data to be validated.
        """
        self.json_data = json_data
        self.errors = []

    def validate(self):
        """
        Validate the JSON data fields. Collects errors if present.
        
        :return: A tuple containing a boolean indicating validity and a list of errors.
        """
        self.errors.clear()  # Clear previous errors
        self.validate_name_of_model()
        self.validate_description()
        self.validate_ip_license()
        return len(self.errors) == 0, self.errors

    def validate_name_of_model(self):
        """
        Validate the 'Name of Model' field.
        """
        name_of_model = self.json_data.get("Name of Model")
        if not name_of_model or not isinstance(name_of_model, str):
            self.errors.append("Invalid 'Name of Model': must be a non-empty string.")

    def validate_description(self):
        """
        Validate the 'Description' field.
        """
        description = self.json_data.get("Description")
        if not description or not isinstance(description, str):
            self.errors.append("Invalid 'Description': must be a non-empty string.")

    def validate_ip_license(self):
        """
        Validate the 'IP License' field.
        """
        ip_license = self.json_data.get("IP License")
        license_pattern = r"^[A-Za-z0-9\- ]+$"  # Simple alphanumeric pattern for licenses
        if not ip_license or not isinstance(ip_license, str) or not re.match(license_pattern, ip_license):
            self.errors.append("Invalid 'IP License': must be a non-empty string and match the required pattern.")

def main():
    """
    Main function to execute the validation process.
    """
    # Example JSON data to validate
    json_string = """
    {
        "Name of Model": "MyModel",
        "Description": "This is a test model.",
        "IP License": "ABC-1234"
    }
    """
    
    try:
        # Load JSON data
        json_data = json.loads(json_string)
        
        # Create a validator instance
        validator = JSONValidator(json_data)
        
        # Validate the JSON data
        is_valid, errors = validator.validate()
        
        if is_valid:
            print("JSON validation passed. Data is ready for upload.")
        else:
            print("JSON validation failed. Errors:")
            for error in errors:
                print(f"- {error}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
