"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Write a function to validate user eligibility for Everyworld participation based on country restrictions and age requirements, as outlined in the platform's terms of use.
Generated: DETERMINISTIC_3f6d87a4a6185491
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# everyworld_eligibility_validator.py

from typing import Dict

class EveryworldEligibilityValidator:
    """
    Validates user eligibility for Everyworld participation based on country restrictions and age requirements.
    """

    def __init__(self, country_restrictions: list, age_requirement: int):
        """
        Initializes the validator with country restrictions and age requirement.

        Args:
        - country_restrictions (list): List of countries that are restricted from participating.
        - age_requirement (int): Minimum age required for participation.
        """
        self.country_restrictions = country_restrictions
        self.age_requirement = age_requirement

    def validate_eligibility(self, user_info: Dict) -> bool:
        """
        Validates user eligibility for Everyworld participation.

        Args:
        - user_info (Dict): Dictionary containing user's country and age.

        Returns:
        - bool: True if user is eligible, False otherwise.
        """
        try:
            # Check if user_info contains required fields
            if 'country' not in user_info or 'age' not in user_info:
                raise ValueError("User info must contain 'country' and 'age'")

            # Check if country is restricted
            if user_info['country'] in self.country_restrictions:
                return False  # User's country is restricted

            # Check if user meets age requirement
            if not isinstance(user_info['age'], int) or user_info['age'] < self.age_requirement:
                return False  # User does not meet age requirement

            return True  # User is eligible

        except Exception as e:
            # Log the exception and re-raise
            print(f"An error occurred: {str(e)}")
            raise


def main():
    # Example usage
    country_restrictions = ['Restricted Country 1', 'Restricted Country 2']
    age_requirement = 18

    validator = EveryworldEligibilityValidator(country_restrictions, age_requirement)

    user1 = {'country': 'Allowed Country', 'age': 25}
    user2 = {'country': 'Restricted Country 1', 'age': 25}
    user3 = {'country': 'Allowed Country', 'age': 15}

    print(validator.validate_eligibility(user1))  # Expected output: True
    print(validator.validate_eligibility(user2))  # Expected output: False
    print(validator.validate_eligibility(user3))  # Expected output: False


if __name__ == "__main__":
    main()
```
