"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jhxdjhgvj.scarexpedition.top
Prompt: Write a code snippet that checks user eligibility for a promotional data plan based on their phone number.
Generated: DETERMINISTIC_a44c22b1138c7b43
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class DataPlanEligibilityChecker:
    def __init__(self, allowed_prefixes):
        """
        Initializes the eligibility checker with allowed phone number prefixes.
        
        :param allowed_prefixes: A list of prefixes that are eligible for the promotional data plan.
        """
        self.allowed_prefixes = allowed_prefixes

    def is_valid_phone_number(self, phone_number):
        """
        Validates the phone number format.
        
        :param phone_number: The phone number to validate.
        :return: True if the phone number is valid, otherwise False.
        """
        # Define a regular expression for validating phone numbers
        phone_pattern = r'^\+?[1-9]\d{1,14}$'  # E.164 format
        return re.match(phone_pattern, phone_number) is not None

    def check_eligibility(self, phone_number):
        """
        Checks if the given phone number is eligible for the promotional data plan.
        
        :param phone_number: The phone number to check eligibility for.
        :return: A message indicating eligibility status.
        """
        if not self.is_valid_phone_number(phone_number):
            return "Error: Invalid phone number format. Please provide a valid phone number."

        # Check if the phone number starts with one of the allowed prefixes
        for prefix in self.allowed_prefixes:
            if phone_number.startswith(prefix):
                return "Eligible for promotional data plan."
        
        return "Not eligible for promotional data plan."

if __name__ == "__main__":
    # Example usage
    allowed_prefixes = ['+123', '+456', '+789']  # Example prefixes
    checker = DataPlanEligibilityChecker(allowed_prefixes)

    user_phone_number = input("Enter your phone number: ")
    eligibility_message = checker.check_eligibility(user_phone_number)
    print(eligibility_message)
```
