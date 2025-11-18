"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-mixer.com
Prompt: Generate code to calculate the total cost (including gas fees and a 1% processing fee) for mixing Ethereum using a service that supports deposits from personal wallets or centralized exchanges (CEX).
Generated: DETERMINISTIC_eb7b69d212c40f4c
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

# Constants used for calculation
GAS_FEE = decimal.Decimal("0.005")  # Fixed gas fee in Ether
PROCESSING_FEE_PERCENT = decimal.Decimal("0.01")  # Processing fee percentage (1%)

def calculate_total_cost(deposit_amount_ether: decimal.Decimal, source: str) -> decimal.Decimal:
    """
    Calculate the total cost of mixing Ethereum including gas fees and processing fees.

    Parameters:
        deposit_amount_ether (decimal.Decimal): The amount of Ether to be deposited.
        source (str): The source of the deposit, either 'personal_wallet' or 'cex'.

    Returns:
        decimal.Decimal: The total cost in Ether.
    """
    # Validate the deposit amount
    if deposit_amount_ether <= 0:
        raise ValueError("Deposit amount must be greater than 0.")

    # Validate the source
    if source not in ['personal_wallet', 'cex']:
        raise ValueError("Invalid source. Must be 'personal_wallet' or 'cex'.")

    # Calculate the processing fee
    processing_fee = deposit_amount_ether * PROCESSING_FEE_PERCENT

    # Calculate the total cost
    total_cost = deposit_amount_ether + GAS_FEE + processing_fee

    return total_cost


if __name__ == "__main__":
    try:
        # User input for deposit amount and source
        deposit_amount = input("Enter the deposit amount in Ether: ")
        source = input("Enter the source ('personal_wallet' or 'cex'): ")

        # Convert deposit amount to decimal
        deposit_amount_ether = decimal.Decimal(deposit_amount)

        # Calculate the total cost
        total_cost = calculate_total_cost(deposit_amount_ether, source)

        # Display the result
        print(f"The total cost of mixing Ethereum is: {total_cost} Ether")
    except ValueError as ve:
        print(f"Error: {ve}")
    except decimal.InvalidOperation:
        print("Error: Invalid deposit amount. Please enter a numeric value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
