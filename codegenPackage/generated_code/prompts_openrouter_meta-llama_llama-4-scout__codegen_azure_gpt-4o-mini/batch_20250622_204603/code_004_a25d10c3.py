"""
Generated Code Metadata:
========================
Original URL: https://iggy.pages.dev
Prompt: Create a script to calculate the number of $IGGY tokens a user can buy based on their ETH contribution, considering a presale cap of 1000 ETH.
Generated: DETERMINISTIC_a25d10c3b591df24
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from decimal import Decimal, InvalidOperation

# Constants
PRESALE_CAP_ETH = Decimal('1000')  # Maximum ETH cap for the presale
TOKEN_PRICE_PER_ETH = Decimal('100')  # Number of IGGY tokens per ETH

def calculate_iggy_tokens(eth_contribution):
    """
    Calculate the number of IGGY tokens a user can buy based on their ETH contribution.

    Parameters:
    eth_contribution (str): The amount of ETH the user wants to contribute.

    Returns:
    Decimal: The number of IGGY tokens the user can purchase.
    """
    try:
        # Convert the ETH contribution to a Decimal for precise calculations
        eth_contribution_decimal = Decimal(eth_contribution)

        # Validate the ETH contribution
        if eth_contribution_decimal <= 0:
            raise ValueError("ETH contribution must be greater than zero.")
        if eth_contribution_decimal > PRESALE_CAP_ETH:
            raise ValueError(f"ETH contribution exceeds the presale cap of {PRESALE_CAP_ETH} ETH.")

        # Calculate the number of IGGY tokens
        iggy_tokens = eth_contribution_decimal * TOKEN_PRICE_PER_ETH
        return iggy_tokens

    except InvalidOperation:
        raise ValueError("Invalid ETH contribution. Please enter a valid number.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating IGGY tokens: {str(e)}")

def main():
    # User input for ETH contribution
    eth_contribution = input("Enter your ETH contribution: ")

    try:
        # Calculate and display the number of IGGY tokens
        tokens = calculate_iggy_tokens(eth_contribution)
        print(f"You can buy {tokens} IGGY tokens.")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")

if __name__ == "__main__":
    main()
```
