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
import math

class OverflowInvestmentSimulator:
    """
    A simulator for the overflow investment phase of BorpaToken.
    Calculates token allocation based on token price and investment amounts.
    """

    def __init__(self, token_price: float, total_tokens: int):
        """
        Initializes the simulator with token price and total tokens available.
        :param token_price: The price of one BorpaToken in investment currency.
        :param total_tokens: The total supply of BorpaTokens available for allocation.
        """
        if token_price <= 0 or total_tokens <= 0:
            raise ValueError("Token price and total tokens must be positive values.")
        self.token_price = token_price
        self.total_tokens = total_tokens
        self.investments = {}

    def add_investment(self, investor_id: str, amount: float):
        """
        Adds an investment for a specific investor.
        :param investor_id: A unique identifier for the investor.
        :param amount: The amount invested by the investor in the investment currency.
        """
        if amount <= 0:
            raise ValueError("Investment amount must be a positive value.")
        self.investments[investor_id] = self.investments.get(investor_id, 0) + amount

    def calculate_allocations(self):
        """
        Calculates token allocations for investors based on the overflow model.
        :return: A dictionary where keys are investor IDs and values are token allocations.
        """
        total_invested = sum(self.investments.values())
        allocations = {}

        if total_invested == 0:
            # No investments, no allocations
            for investor_id in self.investments:
                allocations[investor_id] = 0
            return allocations

        # Calculate allocations
        for investor_id, amount in self.investments.items():
            # Each investor receives tokens proportional to their investment
            investor_share = amount / total_invested
            allocated_tokens = math.floor(investor_share * self.total_tokens)
            allocations[investor_id] = allocated_tokens

        return allocations

    def display_results(self):
        """
        Displays the investment results in a readable format.
        """
        print("Investment Results:\n")
        print(f"Total Tokens Available: {self.total_tokens}")
        print(f"Token Price: {self.token_price}")
        print("\nInvestor Allocations:")
        for investor_id, allocated_tokens in self.calculate_allocations().items():
            print(f"  Investor ID: {investor_id}, Allocated Tokens: {allocated_tokens}")


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the simulator with token price and total supply
        simulator = OverflowInvestmentSimulator(token_price=1.5, total_tokens=1000)

        # Add investments (Investor ID, Amount Invested)
        simulator.add_investment("investor_1", 500)
        simulator.add_investment("investor_2", 300)
        simulator.add_investment("investor_3", 200)

        # Display the results
        simulator.display_results()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
