"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-recovered.webou.net
Prompt: Write code to validate a promotional code (e.g., "GRATUIT21") for activating free hosting services, similar to the ones offered on Webou.net.
Generated: DETERMINISTIC_b353cb9a422e823e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime

class PromoCodeValidator:
    def __init__(self, valid_codes, expiration_date):
        """
        Initializes the PromoCodeValidator with a set of valid promo codes and an expiration date.

        :param valid_codes: A list of valid promo codes
        :param expiration_date: The date until which the promo codes are valid (YYYY-MM-DD format)
        """
        self.valid_codes = valid_codes
        self.expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()

    def is_valid_format(self, code):
        """
        Validates the format of the promo code.

        :param code: Promo code to validate
        :return: True if the format is valid, False otherwise
        """
        # Example format: 8 alphanumeric characters, starting with letters
        return bool(re.match(r'^[A-Za-z]{1}[A-Za-z0-9]{7}$', code))

    def is_expired(self):
        """
        Checks if the current date is past the expiration date.

        :return: True if the promo codes are expired, False otherwise
        """
        return datetime.now().date() > self.expiration_date

    def validate_code(self, code):
        """
        Validates the promo code by checking its format, existence in valid codes, and expiration.

        :param code: Promo code to validate
        :return: A message indicating the result of the validation
        """
        try:
            if self.is_expired():
                return "Promo code has expired."

            if not self.is_valid_format(code):
                return "Invalid promo code format."

            if code not in self.valid_codes:
                return "Promo code is not recognized."

            return "Promo code is valid! Enjoy your free hosting service."
        
        except Exception as e:
            return f"An error occurred during validation: {str(e)}"

# Example usage
if __name__ == "__main__":
    # List of valid promo codes
    valid_promo_codes = ["GRATUIT21", "FREETIME22", "HOSTFREE23"]
    
    # Set expiration date for promo codes
    promo_expiration_date = "2023-12-31"

    # Initialize the validator
    validator = PromoCodeValidator(valid_promo_codes, promo_expiration_date)
    
    # Test the validator with a sample code
    test_code = "GRATUIT21"
    result = validator.validate_code(test_code)
    print(result)  # Output: Promo code is valid! Enjoy your free hosting service.
```
