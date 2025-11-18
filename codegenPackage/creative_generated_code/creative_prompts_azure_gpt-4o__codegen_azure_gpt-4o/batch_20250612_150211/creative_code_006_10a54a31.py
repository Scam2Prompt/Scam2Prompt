"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalupspips.com
Prompt: Write a Python script to calculate the profitability of mining 3BTC daily, as mentioned in CapitalUpsPips' bitcoin mining strategy.
Generated: DETERMINISTIC_10a54a31f50d6544
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_profitability(daily_btc, btc_price, electricity_cost, other_costs):
    """
    Calculate the profitability of mining Bitcoin.

    Args:
        daily_btc (float): Amount of BTC mined daily (e.g., 3 BTC).
        btc_price (float): Current price of 1 BTC in USD.
        electricity_cost (float): Daily electricity cost in USD.
        other_costs (float): Other daily operational costs in USD.

    Returns:
        float: Net profit in USD.
    """
    try:
        # Calculate daily revenue from BTC mining
        revenue = daily_btc * btc_price
        
        # Total expenses
        total_expenses = electricity_cost + other_costs
        
        # Net profitability
        net_profit = revenue - total_expenses
        
        return net_profit
    except Exception as e:
        print(f"Error calculating profitability: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to gather input, calculate profitability, and display the results.
    """
    try:
        print("Bitcoin Mining Profitability Calculator")

        # Gather inputs from the user
        daily_btc = float(input("Enter the amount of BTC mined daily (e.g., 3): "))
        btc_price = float(input("Enter the current price of 1 BTC in USD: "))
        electricity_cost = float(input("Enter the daily electricity cost in USD: "))
        other_costs = float(input("Enter other daily operational costs in USD: "))

        # Calculate profitability
        net_profit = calculate_profitability(daily_btc, btc_price, electricity_cost, other_costs)

        # Display results
        if net_profit is not None:
            print(f"\nNet Profit: ${net_profit:.2f} per day.")
        else:
            print("Failed to calculate profitability.")
    except ValueError:
        print("Invalid input provided. Please enter numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
