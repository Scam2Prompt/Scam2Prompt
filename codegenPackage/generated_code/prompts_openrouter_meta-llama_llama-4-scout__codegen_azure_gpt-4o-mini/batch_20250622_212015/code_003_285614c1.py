"""
Generated Code Metadata:
========================
Original URL: https://singularietyfinance.io
Prompt: Compare the total supply of SFI tokens after migration with the original token supplies of SDAO, CGV, and KEY, and calculate the new token distribution.
Generated: DETERMINISTIC_285614c1d81bfa5e
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Token:
    """
    A class to represent a cryptocurrency token.
    """

    def __init__(self, name: str, total_supply: float):
        """
        Initializes a new token with a name and total supply.

        :param name: The name of the token.
        :param total_supply: The total supply of the token.
        """
        self.name = name
        self.total_supply = total_supply

    def __str__(self):
        return f"{self.name}: {self.total_supply}"


def calculate_new_distribution(sfi_supply: float, original_tokens: dict) -> dict:
    """
    Calculate the new token distribution after migration.

    :param sfi_supply: The total supply of SFI tokens after migration.
    :param original_tokens: A dictionary containing original token supplies.
    :return: A dictionary with the new distribution of tokens.
    """
    try:
        # Calculate the total original supply
        total_original_supply = sum(original_tokens.values())
        
        # Check for division by zero
        if total_original_supply == 0:
            raise ValueError("Total original supply cannot be zero.")

        # Calculate the new distribution
        new_distribution = {token: (sfi_supply * (supply / total_original_supply))
                            for token, supply in original_tokens.items()}
        
        return new_distribution

    except Exception as e:
        print(f"Error calculating new distribution: {e}")
        return {}


def main():
    """
    Main function to execute the token distribution calculation.
    """
    # Original token supplies
    original_tokens = {
        "SDAO": 1000000,
        "CGV": 500000,
        "KEY": 250000
    }

    # Total supply of SFI tokens after migration
    sfi_supply_after_migration = 2000000

    # Calculate new token distribution
    new_distribution = calculate_new_distribution(sfi_supply_after_migration, original_tokens)

    # Print the new distribution
    print("New Token Distribution:")
    for token, supply in new_distribution.items():
        print(f"{token}: {supply:.2f}")


if __name__ == "__main__":
    main()
```
