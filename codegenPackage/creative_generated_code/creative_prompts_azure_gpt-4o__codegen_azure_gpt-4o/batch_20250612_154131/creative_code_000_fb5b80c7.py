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
# Script to calculate potential profit from investment in $UNSD tokens
# Stage 17 price: $0.01043
# Launch price: $0.1819

def calculate_profit(investment_amount):
    """
    Calculates the potential profit from investing in $UNSD tokens.

    Args:
        investment_amount (float): The amount invested in USD.

    Returns:
        tuple: A tuple containing the number of tokens purchased, total sell value, and profit.
    """
    # Define constants for token prices
    STAGE_17_PRICE = 0.01043  # USD per token
    LAUNCH_PRICE = 0.1819    # USD per token

    # Calculate the number of tokens purchased
    try:
        tokens_purchased = investment_amount / STAGE_17_PRICE
    except ZeroDivisionError:
        raise ValueError("Stage 17 price cannot be zero.")

    # Calculate total sell value at launch price
    sell_value = tokens_purchased * LAUNCH_PRICE

    # Calculate profit
    profit = sell_value - investment_amount

    return tokens_purchased, sell_value, profit


def main():
    """
    Main function to execute the script.
    """
    print("Welcome to the $UNSD Token Profit Calculator!")
    try:
        # Get user input for investment amount
        investment_amount = float(input("Enter your investment amount in USD: "))

        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")

        # Perform profit calculation
        tokens_purchased, sell_value, profit = calculate_profit(investment_amount)

        # Display results
        print("\nResults:")
        print(f"Tokens purchased: {tokens_purchased:.2f}")
        print(f"Total sell value at launch price: ${sell_value:.2f}")
        print(f"Potential profit: ${profit:.2f}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
