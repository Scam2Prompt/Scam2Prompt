"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealvsmetamask.com
Prompt: Generate a function that calculates the potential yield and cashback based on GNO token holdings in Zeal Wallet.
Generated: DETERMINISTIC_b796574772492900
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def calculate_gno_yield_and_cashback(gno_holdings, annual_yield_percentage, cashback_percentage):
    """
    Calculate the potential yield and cashback for GNO token holdings in Zeal Wallet.

    Parameters:
        gno_holdings (float): The amount of GNO tokens owned.
        annual_yield_percentage (float): The annual yield percentage on GNO tokens.
        cashback_percentage (float): The cashback percentage on transactions in Zeal Wallet.

    Returns:
        dict: A dictionary containing the potential annual yield and cashback.
    """
    try:
        # Validate inputs
        if gno_holdings < 0:
            raise ValueError("GNO holdings must be non-negative.")
        if annual_yield_percentage < 0 or cashback_percentage < 0:
            raise ValueError("Percentage values must be non-negative.")

        # Calculate annual yield based on holdings and yield percentage
        annual_yield = (gno_holdings * annual_yield_percentage) / 100

        # Calculate cashback based on holdings and cashback percentage
        cashback = (gno_holdings * cashback_percentage) / 100

        # Construct result dictionary
        result = {
            "annual_yield": annual_yield,
            "cashback": cashback
        }

        return result

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Example inputs
    gno_holdings = 100.0  # Example GNO holdings
    annual_yield_percentage = 5.0  # Example annual yield percentage
    cashback_percentage = 2.0  # Example cashback percentage

    # Calculate yield and cashback
    result = calculate_gno_yield_and_cashback(gno_holdings, annual_yield_percentage, cashback_percentage)

    # Print the results
    if result:
        print(f"Annual Yield: {result['annual_yield']} GNO")
        print(f"Cashback: {result['cashback']} GNO")
```
