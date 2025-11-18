"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rrr-9a3.pages.dev
Prompt: Generate code to calculate the total investment in BorpaToken using the given price of 0.0056 USDT and display the corresponding number of tokens claimable.
Generated: DETERMINISTIC_e7964ff4b3d62845
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BorpaTokenInvestmentCalculator:
    """
    A class to calculate the total investment in BorpaToken
    based on a given price in USDT and to determine the 
    corresponding number of tokens claimable.
    """

    def __init__(self, price_per_token: float):
        """
        Initialize the investment calculator with the price per token.
        
        :param price_per_token: The price of one BorpaToken in USDT
        """
        if price_per_token <= 0:
            raise ValueError("Price per token must be a positive number.")
        self.price_per_token = price_per_token

    def calculate_tokens_claimable(self, total_investment: float) -> float:
        """
        Calculate the number of tokens claimable based on total investment.
        
        :param total_investment: The total amount invested in USDT
        :return: The number of claimable tokens
        """
        if total_investment < 0:
            raise ValueError("Total investment cannot be negative.")
        
        tokens_claimable = total_investment / self.price_per_token
        return tokens_claimable

def main():
    # Define the price of BorpaToken
    price_per_token = 0.0056

    try:
        # Create an instance of the investment calculator
        investment_calculator = BorpaTokenInvestmentCalculator(price_per_token)

        # Define the total investment in USDT (example amount)
        total_investment = float(input("Enter your total investment in USDT: "))

        # Calculate the number of tokens claimable
        tokens_claimable = investment_calculator.calculate_tokens_claimable(total_investment)

        # Display the result
        print(f"With an investment of {total_investment} USDT, you can claim {tokens_claimable:.2f} BorpaTokens.")

    except ValueError as e:
        # Handle any value errors that occur during input or calculations
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
