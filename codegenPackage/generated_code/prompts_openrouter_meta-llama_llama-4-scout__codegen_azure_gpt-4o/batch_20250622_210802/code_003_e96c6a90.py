"""
Generated Code Metadata:
========================
Original URL: https://jesse-presale-8r8.pages.dev
Prompt: What is the total supply of $JESSE tokens and how does it relate to the presale cap of 1000 BASE?
Generated: DETERMINISTIC_e96c6a9045fcf9fe
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from decimal import Decimal

class TokenSupplyError(Exception):
    """Custom exception for token supply errors."""
    pass

class JesseToken:
    """
    A class to represent the JESSE token and its relationship to the presale cap.
    """
    def __init__(self, total_supply: Decimal, presale_cap: Decimal):
        """
        Initialize the JesseToken instance.

        :param total_supply: Total supply of JESSE tokens.
        :param presale_cap: Presale cap in BASE tokens.
        """
        if total_supply <= 0 or presale_cap <= 0:
            raise TokenSupplyError("Total supply and presale cap must be positive values.")
        
        self.total_supply = total_supply
        self.presale_cap = presale_cap

    def get_total_supply(self) -> Decimal:
        """
        Get the total supply of JESSE tokens.

        :return: Total supply of JESSE tokens.
        """
        return self.total_supply

    def get_presale_cap(self) -> Decimal:
        """
        Get the presale cap in BASE tokens.

        :return: Presale cap in BASE tokens.
        """
        return self.presale_cap

    def calculate_supply_ratio(self) -> Decimal:
        """
        Calculate the ratio of presale cap to total supply.

        :return: Ratio of presale cap to total supply.
        """
        try:
            ratio = self.presale_cap / self.total_supply
            return ratio
        except ZeroDivisionError:
            raise TokenSupplyError("Total supply cannot be zero.")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize JESSE token with a total supply of 5000 and presale cap of 1000 BASE
        total_supply = Decimal("5000")
        presale_cap = Decimal("1000")
        jesse_token = JesseToken(total_supply, presale_cap)

        # Print total supply and presale cap
        print(f"Total Supply of JESSE Tokens: {jesse_token.get_total_supply()}")
        print(f"Presale Cap in BASE Tokens: {jesse_token.get_presale_cap()}")

        # Calculate and print the ratio of presale cap to total supply
        ratio = jesse_token.calculate_supply_ratio()
        print(f"Presale Cap to Total Supply Ratio: {ratio:.2%}")
    except TokenSupplyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
