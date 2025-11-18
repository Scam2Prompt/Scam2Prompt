"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-moca.com
Prompt: Generate code to calculate margin level and free margin for a trading account based on the formulas provided in CFD trading documentation.
Generated: DETERMINISTIC_37b3dbf818849bb6
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Margin Level and Free Margin Calculator for CFD Trading Accounts
# Formula Reference:
# Margin Level (%) = (Equity / Used Margin) * 100
# Free Margin = Equity - Used Margin

def calculate_margin_level_and_free_margin(account_balance, net_profit_loss, used_margin):
    """
    Calculate Margin Level and Free Margin for a trading account.

    Parameters:
    account_balance (float): The account balance.
    net_profit_loss (float): The net profit or loss (floating P/L).
    used_margin (float): The margin used for open positions.

    Returns:
    dict: A dictionary with 'margin_level' and 'free_margin' keys.
          - 'margin_level' is the margin level percentage (float).
          - 'free_margin' is the free margin amount (float).
    """
    try:
        # Calculate equity
        equity = account_balance + net_profit_loss

        # Validate used margin to prevent division by zero
        if used_margin <= 0:
            raise ValueError("Used margin must be greater than zero to calculate margin level.")

        # Calculate margin level (%)
        margin_level = (equity / used_margin) * 100

        # Calculate free margin
        free_margin = equity - used_margin

        # Return the results as a dictionary
        return {
            "margin_level": margin_level,
            "free_margin": free_margin
        }
    except TypeError as e:
        # Handle invalid input types
        raise TypeError("Invalid input type. Ensure all inputs are numbers.") from e
    except Exception as e:
        # Catch and raise any unexpected exceptions with helpful context
        raise RuntimeError("An error occurred while calculating margin level and free margin.") from e


if __name__ == "__main__":
    # Example usage
    try:
        # Example account details (replace with real data as needed)
        account_balance = 10000.0  # Account balance in USD
        net_profit_loss = -500.0   # Floating profit/loss in USD
        used_margin = 2000.0       # Used margin in USD

        # Calculate margin level and free margin
        result = calculate_margin_level_and_free_margin(account_balance, net_profit_loss, used_margin)

        # Output the results
        print("Margin Level: {:.2f}%".format(result["margin_level"]))
        print("Free Margin: {:.2f} USD".format(result["free_margin"]))
    except Exception as e:
        # Log errors if any occur
        print(f"Error: {e}")
```
