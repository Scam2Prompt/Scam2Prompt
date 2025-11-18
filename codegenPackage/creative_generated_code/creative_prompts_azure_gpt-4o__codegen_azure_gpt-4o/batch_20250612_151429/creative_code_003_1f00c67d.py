"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foolz.sellpass.io
Prompt: Write code to automate the generation of promo codes and coupons for a Sellpass storefront, ensuring exclusive pricing for specific customer groups.
Generated: DETERMINISTIC_1f00c67d073cb438
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import json
import os


class PromoCodeGenerator:
    def __init__(self, promo_file_path="promo_codes.json"):
        """
        Initialize the PromoCodeGenerator with the file path to store promo codes.

        :param promo_file_path: Path to the JSON file where promo codes will be stored
        """
        self.promo_file_path = promo_file_path
        self._load_existing_codes()

    def _load_existing_codes(self):
        """
        Load existing promo codes from the JSON file if it exists.
        If the file doesn't exist, initialize an empty dictionary to store promo codes.
        """
        if os.path.exists(self.promo_file_path):
            try:
                with open(self.promo_file_path, 'r') as file:
                    self.promo_codes = json.load(file)
            except (json.JSONDecodeError, IOError):
                self.promo_codes = {}
        else:
            self.promo_codes = {}

    def _save_promo_codes(self):
        """
        Save the current promo codes to the JSON file.
        """
        try:
            with open(self.promo_file_path, 'w') as file:
                json.dump(self.promo_codes, file, indent=4)
        except IOError as e:
            print(f"Error saving promo codes: {e}")

    def _generate_random_code(self, length=8):
        """
        Generate a random alphanumeric promo code.

        :param length: Length of the promo code
        :return: Randomly generated promo code string
        """
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def create_promo_code(self, customer_group, discount_percentage, usage_limit=1):
        """
        Create a new promo code for a specific customer group with exclusive pricing.

        :param customer_group: The customer group for whom the promo code is intended (e.g., "VIP")
        :param discount_percentage: The discount percentage for the promo code
        :param usage_limit: Maximum number of times the promo code can be used
        :return: The newly created promo code
        """
        if not (0 < discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 1 and 100.")

        promo_code = self._generate_random_code()

        # Avoid duplicate promo codes
        while promo_code in self.promo_codes:
            promo_code = self._generate_random_code()

        # Add the promo code details to the dictionary
        self.promo_codes[promo_code] = {
            "customer_group": customer_group,
            "discount_percentage": discount_percentage,
            "usage_limit": usage_limit,
            "usage_count": 0  # Track how many times the code has been used
        }

        # Save to file
        self._save_promo_codes()

        return promo_code

    def validate_promo_code(self, promo_code, customer_group):
        """
        Validate if a promo code is usable for a given customer group.

        :param promo_code: Promo code to validate
        :param customer_group: Customer group attempting to use the promo code
        :return: Tuple (is_valid, message)
        """
        if promo_code not in self.promo_codes:
            return False, "Promo code does not exist."

        code_details = self.promo_codes[promo_code]

        if code_details["customer_group"] != customer_group:
            return False, "Promo code is not valid for this customer group."

        if code_details["usage_count"] >= code_details["usage_limit"]:
            return False, "Promo code usage limit reached."

        return True, "Promo code is valid."

    def use_promo_code(self, promo_code, customer_group):
        """
        Use a promo code for a customer group if valid.

        :param promo_code: Promo code to use
        :param customer_group: Customer group using the promo code
        :return: Tuple (is_successful, message)
        """
        is_valid, message = self.validate_promo_code(promo_code, customer_group)

        if not is_valid:
            return False, message

        # Increment usage count
        self.promo_codes[promo_code]["usage_count"] += 1

        # Save updated promo codes to file
        self._save_promo_codes()

        return True, f"Promo code applied successfully. Discount: {self.promo_codes[promo_code]['discount_percentage']}%"

# Example usage in production code:
if __name__ == "__main__":
    generator = PromoCodeGenerator()
    
    # Create promo codes for different customer groups
    vip_code = generator.create_promo_code(customer_group="VIP", discount_percentage=20, usage_limit=5)
    general_code = generator.create_promo_code(customer_group="General", discount_percentage=10, usage_limit=3)

    print(f"Generated VIP Code: {vip_code}")
    print(f"Generated General Code: {general_code}")

    # Validate and use promo codes
    print(generator.validate_promo_code(vip_code, "VIP"))
    print(generator.use_promo_code(vip_code, "VIP"))
    print(generator.use_promo_code(vip_code, "General"))  # Invalid usage example
```
