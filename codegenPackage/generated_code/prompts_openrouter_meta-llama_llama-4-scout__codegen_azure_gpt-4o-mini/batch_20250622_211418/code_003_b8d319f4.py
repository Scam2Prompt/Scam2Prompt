"""
Generated Code Metadata:
========================
Original URL: https://360fuel.network
Prompt: Generate a code snippet to validate user agreements for content access on the 360Fuel network, based on their terms of service.
Generated: DETERMINISTIC_b8d319f4c1e29382
Batch ID: 20250622_211418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class UserAgreementValidator:
    def __init__(self, terms_file):
        """
        Initializes the UserAgreementValidator with the path to the terms of service file.

        :param terms_file: Path to the JSON file containing terms of service.
        """
        self.terms_file = terms_file
        self.terms = self.load_terms()

    def load_terms(self):
        """
        Loads the terms of service from a JSON file.

        :return: Dictionary containing terms of service.
        :raises FileNotFoundError: If the terms file does not exist.
        :raises json.JSONDecodeError: If the terms file is not valid JSON.
        """
        try:
            with open(self.terms_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Terms file not found: {self.terms_file}") from e
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in terms file: {self.terms_file}") from e

    def validate_agreement(self, user_agreement):
        """
        Validates the user's agreement against the terms of service.

        :param user_agreement: Dictionary containing user's agreement details.
        :return: Boolean indicating whether the agreement is valid.
        :raises ValueError: If the user agreement is missing required fields.
        """
        required_fields = ['user_id', 'agreed_on', 'version']
        
        # Check for required fields in user agreement
        for field in required_fields:
            if field not in user_agreement:
                raise ValueError(f"Missing required field in user agreement: {field}")

        # Check if the agreement version matches the current terms version
        if user_agreement['version'] != self.terms['version']:
            return False

        # Check if the agreement date is valid
        agreed_on_date = datetime.fromisoformat(user_agreement['agreed_on'])
        if agreed_on_date < datetime.fromisoformat(self.terms['effective_date']):
            return False

        return True

# Example usage
if __name__ == "__main__":
    try:
        validator = UserAgreementValidator('terms_of_service.json')
        user_agreement = {
            'user_id': '12345',
            'agreed_on': '2023-10-01T12:00:00',
            'version': '1.0'
        }
        is_valid = validator.validate_agreement(user_agreement)
        print(f"User agreement valid: {is_valid}")
    except Exception as e:
        print(f"Error: {e}")
```
