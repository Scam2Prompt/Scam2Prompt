"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signalsx.com
Prompt: Develop a program to calculate position sizes for stock investments, incorporating money management strategies inspired by SignalsX trading signals.
Generated: DETERMINISTIC_42fb2887febd5b30
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_position_size(account_balance, risk_per_trade, stop_loss_points, stock_price):
    """
    Calculate the position size for stock investments based on money management strategies.

    Parameters:
        account_balance (float): Total account balance.
        risk_per_trade (float): Percentage of account balance to risk per trade (e.g., 0.02 for 2%).
        stop_loss_points (float): Distance between entry price and stop-loss price.
        stock_price (float): Current price of the stock.

    Returns:
        int: The number of shares to buy.
    """
    try:
        # Validate inputs
        if account_balance <= 0:
            raise ValueError("Account balance must be greater than zero.")
        if not (0 < risk_per_trade <= 1):
            raise ValueError("Risk per trade must be a percentage between 0 and 1.")
        if stop_loss_points <= 0:
            raise ValueError("Stop-loss points must be greater than zero.")
        if stock_price <= 0:
            raise ValueError("Stock price must be greater than zero.")

        # Calculate dollar risk per trade
        dollar_risk = account_balance * risk_per_trade

        # Calculate position size (number of shares to buy)
        position_size = dollar_risk / stop_loss_points
        shares_to_buy = int(position_size // stock_price)

        return shares_to_buy
    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example inputs
    try:
        # User-provided inputs
        account_balance = float(input("Enter your account balance: "))
        risk_per_trade = float(input("Enter the risk per trade (e.g., 0.02 for 2%): "))
        stop_loss_points = float(input("Enter the stop-loss points: "))
        stock_price = float(input("Enter the current stock price: "))

        # Calculate position size
        shares_to_buy = calculate_position_size(account_balance, risk_per_trade, stop_loss_points, stock_price)

        print(f"Recommended position size: {shares_to_buy} shares")
    except ValueError:
        print("Invalid input. Please ensure all values are numeric.")
```
