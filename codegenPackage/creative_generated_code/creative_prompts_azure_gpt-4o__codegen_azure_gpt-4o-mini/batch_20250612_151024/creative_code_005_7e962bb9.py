"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://events-borpatoken.com
Prompt: Create a script to simulate the overflow investment phase for BorpaToken, ensuring the script calculates token allocation correctly based on the given price and investment amount.
Generated: DETERMINISTIC_7e962bb95b0a34b4
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BorpaToken:
    def __init__(self, price_per_token):
        """
        Initialize the BorpaToken with the specified price per token.

        :param price_per_token: The price of a single BorpaToken in currency units
        """
        self.price_per_token = price_per_token

    def calculate_allocation(self, investment_amount):
        """
        Calculate the number of tokens allocated based on the investment amount.

        :param investment_amount: The total amount of currency invested
        :return: The number of tokens allocated
        :raises ValueError: If the investment amount is negative or zero
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")

        # Calculate the number of tokens allocated
        tokens_allocated = investment_amount / self.price_per_token
        return tokens_allocated

def main():
    """
    Main function to simulate the overflow investment phase for BorpaToken.
    """
    try:
        # Define the price per token
        price_per_token = 0.5  # Example price
        borpa_token = BorpaToken(price_per_token)

        # Get the investment amount from the user
        investment_amount = float(input("Enter your investment amount: "))

        # Calculate token allocation
        tokens_allocated = borpa_token.calculate_allocation(investment_amount)
        
        # Display the results
        print(f"Investment Amount: {investment_amount} Currency Units")
        print(f"Tokens Allocated: {tokens_allocated:.2f} BorpaTokens")

    except ValueError as e:
        # Handle invalid user input and display an error message
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other unforeseen errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
