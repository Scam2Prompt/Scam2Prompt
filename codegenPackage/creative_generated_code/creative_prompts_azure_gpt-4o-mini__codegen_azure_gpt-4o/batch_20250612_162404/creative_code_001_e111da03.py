"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bookofeth-xyz.pages.dev
Prompt: Write a code snippet to validate the $BOOE tokenomics details, including supply and tax information.
Generated: DETERMINISTIC_e111da03ab8ccffd
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class TokenomicsValidator:
    """
    A class to validate $BOOE tokenomics details including maximum supply 
    and tax rate information.
    """
    def __init__(self, max_supply_limit, max_tax_rate):
        """
        Initialize the validator with constraints.

        :param max_supply_limit: Maximum allowable token supply.
        :param max_tax_rate: Maximum allowable tax rate as a percentage.
        """
        self.max_supply_limit = max_supply_limit
        self.max_tax_rate = max_tax_rate

    def validate_supply(self, supply):
        """
        Validate the token supply.

        :param supply: The token supply to validate.
        :return: Tuple (bool, str), where bool indicates validity, and str explains the result.
        """
        try:
            if not isinstance(supply, int):
                return False, "Supply must be an integer."
            if supply <= 0:
                return False, "Supply must be greater than zero."
            if supply > self.max_supply_limit:
                return False, f"Supply exceeds maximum limit of {self.max_supply_limit}."
            return True, "Supply is valid."
        except Exception as e:
            return False, f"Error validating supply: {str(e)}"

    def validate_tax_rate(self, tax_rate):
        """
        Validate the tax rate.

        :param tax_rate: The tax rate to validate (as a percentage).
        :return: Tuple (bool, str), where bool indicates validity, and str explains the result.
        """
        try:
            if not isinstance(tax_rate, (int, float)):
                return False, "Tax rate must be a number."
            if tax_rate < 0 or tax_rate > self.max_tax_rate:
                return False, f"Tax rate must be between 0 and {self.max_tax_rate}."
            return True, "Tax rate is valid."
        except Exception as e:
            return False, f"Error validating tax rate: {str(e)}"

    def validate_token_name(self, token_name):
        """
        Validate the token name format.

        :param token_name: The token name to validate.
        :return: Tuple (bool, str), where bool indicates validity, and str explains the result.
        """
        try:
            if not isinstance(token_name, str):
                return False, "Token name must be a string."
            if not re.match(r"^\$[A-Z]{3,5}$", token_name):
                return False, "Token name must start with '$' followed by 3 to 5 uppercase letters."
            return True, "Token name is valid."
        except Exception as e:
            return False, f"Error validating token name: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Instantiate the validator with max supply and tax rate limits
    validator = TokenomicsValidator(max_supply_limit=1_000_000_000, max_tax_rate=10)

    # Tokenomics details to validate
    token_name = "$BOOE"
    token_supply = 500_000_000
    token_tax_rate = 5

    # Validate token name
    name_valid, name_message = validator.validate_token_name(token_name)
    print(f"Token Name Validation: {name_message}")

    # Validate token supply
    supply_valid, supply_message = validator.validate_supply(token_supply)
    print(f"Token Supply Validation: {supply_message}")

    # Validate token tax rate
    tax_valid, tax_message = validator.validate_tax_rate(token_tax_rate)
    print(f"Token Tax Rate Validation: {tax_message}")
```
