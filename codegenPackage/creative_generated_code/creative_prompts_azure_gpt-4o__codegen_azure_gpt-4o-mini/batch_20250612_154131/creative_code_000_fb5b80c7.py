"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unstaked-token.world
Prompt: Write a script to calculate the potential profit from buying $UNSD tokens at Stage 17 price ($0.01043) and selling at the launch price ($0.1819). Include user input for the investment amount in USD.
Generated: DETERMINISTIC_fb5b80c7e35d6715
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# profit_calculator.py

def calculate_profit(investment_amount_usd, buy_price, sell_price):
    """
    Calculate the potential profit from buying and selling tokens.

    Parameters:
    investment_amount_usd (float): The amount of USD invested in buying tokens.
    buy_price (float): The price per token at the time of buying.
    sell_price (float): The price per token at the time of selling.

    Returns:
    float: The potential profit from the investment.
    """
    try:
        # Calculate the number of tokens purchased
        tokens_purchased = investment_amount_usd / buy_price
        
        # Calculate the total value when sold at the selling price
        total_value_at_sale = tokens_purchased * sell_price
        
        # Calculate the profit
        profit = total_value_at_sale - investment_amount_usd
        
        return profit

    except ZeroDivisionError:
        print("Error: Buy price cannot be zero.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Main function to execute the profit calculation based on user input.
    """
    # Constants for the buy and sell prices
    STAGE_17_PRICE = 0.01043  # Buy price in USD
    LAUNCH_PRICE = 0.1819      # Sell price in USD

    try:
        # Get user input for the investment amount
        investment_amount_usd = float(input("Enter the investment amount in USD: "))
        
        # Check for non-negative investment
        if investment_amount_usd < 0:
            print("Investment amount cannot be negative.")
            return
        
        # Calculate the potential profit
        potential_profit = calculate_profit(investment_amount_usd, STAGE_17_PRICE, LAUNCH_PRICE)
        
        if potential_profit is not None:
            print(f"Potential profit from the investment: ${potential_profit:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number for the investment amount.")

if __name__ == "__main__":
    main()
```
