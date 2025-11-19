"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-en.web.app
Prompt: Explain how to implement a rewards calculator for DOGE20 that takes user input for the amount purchased and outputs potential future values based on price changes.
Generated: DETERMINISTIC_7d46cfd2efe160d3
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_calculator.py
# This script calculates potential future values of DOGE20 based on price changes.
# Users input the amount of DOGE20 purchased, and the script outputs projected future values.

def rewards_calculator():
    """
    Main function to calculate potential future values of DOGE20 based on user input.
    """
    try:
        # Prompt user for the amount of DOGE20 purchased
        amount_purchased = float(input("Enter the amount of DOGE20 purchased (in tokens): "))
        if amount_purchased <= 0:
            print("The amount purchased must be greater than zero.")
            return
        
        # Prompt user for the current price of DOGE20
        current_price = float(input("Enter the current price of DOGE20 (per token): "))
        if current_price <= 0:
            print("The current price must be greater than zero.")
            return
        
        # Define potential price change percentages
        price_changes = [-50, -25, 0, 25, 50, 100]  # Price change percentages (-50% to +100%)
        
        print("\nPotential future values based on price changes:")
        print("-------------------------------------------------")
        
        # Calculate and display future values based on price changes
        for change in price_changes:
            future_price = current_price * (1 + (change / 100))
            future_value = future_price * amount_purchased
            print(f"Price Change: {change:+3d}% | Future Price: ${future_price:.2f} | Future Value: ${future_value:.2f}")
    
    except ValueError:
        # Handle invalid numerical input
        print("Invalid input. Please enter numerical values for amount and price.")
    except Exception as e:
        # Handle other unexpected errors
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Execute the rewards calculator
    print("DOGE20 Rewards Calculator")
    print("==========================")
    rewards_calculator()
```
