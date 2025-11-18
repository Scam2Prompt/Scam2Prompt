"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprofit-rex-ervaring.com
Prompt: Create a function that calculates trade setups and risk assessments for cryptocurrency investments, inspired by the features of the Profit Rex Ervaring app.
Generated: DETERMINISTIC_4d5f71e3819ab97e
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_trade_setup(entry_price, stop_loss_price, take_profit_price, account_balance, risk_percentage):
    """
    Calculate trade setup and risk assessment for cryptocurrency investments.

    Parameters:
        entry_price (float): The price at which the trade is entered.
        stop_loss_price (float): The price at which the trade will be stopped to minimize losses.
        take_profit_price (float): The price at which the trade will be exited to secure profits.
        account_balance (float): The total account balance available for trading.
        risk_percentage (float): The percentage of the account balance to risk on this trade.

    Returns:
        dict: A dictionary containing details of the trade setup and risk assessment.
    """
    
    # Validate inputs
    if entry_price <= 0 or stop_loss_price <= 0 or take_profit_price <= 0 or account_balance <= 0 or risk_percentage <= 0:
        raise ValueError("All input values must be positive numbers.")
    
    if stop_loss_price >= entry_price:
        raise ValueError("Stop loss price must be below the entry price.")
    
    if take_profit_price <= entry_price:
        raise ValueError("Take profit price must be above the entry price.")
    
    # Calculate risk per trade in dollars
    risk_amount = (risk_percentage / 100) * account_balance
    
    # Calculate trade size (position size)
    risk_per_unit = entry_price - stop_loss_price
    if risk_per_unit <= 0:
        raise ValueError("Risk per unit must be positive.")
    
    trade_size = math.floor(risk_amount / risk_per_unit)
    
    # Calculate potential profit and loss
    potential_loss = trade_size * risk_per_unit
    potential_profit = trade_size * (take_profit_price - entry_price)
    
    # Risk-to-reward ratio
    risk_reward_ratio = potential_profit / potential_loss if potential_loss != 0 else float('inf')
    
    # Return trade setup details
    return {
        "trade_size": trade_size,
        "risk_amount": round(risk_amount, 2),
        "potential_loss": round(potential_loss, 2),
        "potential_profit": round(potential_profit, 2),
        "risk_reward_ratio": round(risk_reward_ratio, 2)
    }


# Example usage
if __name__ == "__main__":
    try:
        # Parameters for the trade setup
        entry_price = 100.0
        stop_loss_price = 90.0
        take_profit_price = 120.0
        account_balance = 10000.0
        risk_percentage = 2.0

        # Calculate and display the trade setup
        trade_setup = calculate_trade_setup(entry_price, stop_loss_price, take_profit_price, account_balance, risk_percentage)
        print("Trade Setup and Risk Assessment:")
        for key, value in trade_setup.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error: {e}")
```
