"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgcasino-app.pages.dev
Prompt: Write code to simulate the buy-back mechanism for $TGC tokens as described in TG.Casino's roadmap.
Generated: DETERMINISTIC_fe0f09b631f2a384
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TGCToken:
    def __init__(self, total_supply, buy_back_fund):
        """
        Initialize the TGC token with total supply and initial buy-back fund.

        :param total_supply: Total number of TGC tokens in circulation.
        :param buy_back_fund: Initial amount of funds available for buy-backs.
        """
        self.total_supply = total_supply
        self.buy_back_fund = buy_back_fund
        self.buy_back_history = []

    def buy_back_tokens(self, amount):
        """
        Simulate the buy-back of TGC tokens.

        :param amount: The amount of tokens to buy back.
        :raises ValueError: If the amount exceeds available buy-back funds.
        :raises RuntimeError: If the total supply is exhausted.
        """
        if amount <= 0:
            logging.error("Amount must be greater than zero.")
            raise ValueError("Amount must be greater than zero.")

        # Calculate the cost for the buy-back
        cost = self.calculate_buy_back_cost(amount)
        
        # Check if the cost can be covered by the buy-back fund
        if cost > self.buy_back_fund:
            logging.error("Insufficient funds for buy-back. Available: %s, Required: %s", self.buy_back_fund, cost)
            raise ValueError("Insufficient funds for buy-back.")

        # Check if there are enough tokens in circulation
        if amount > self.total_supply:
            logging.error("Cannot buy back more tokens than available in supply: %s requested, %s available", amount, self.total_supply)
            raise RuntimeError("Cannot buy back more tokens than available in supply.")

        # Carry out the buy-back
        self.buy_back_fund -= cost
        self.total_supply -= amount
        self.buy_back_history.append((amount, cost))
        
        logging.info("Successfully bought back %s tokens for a cost of %s.", amount, cost)

    def calculate_buy_back_cost(self, amount):
        """
        Calculate the cost of buying back a specified amount of tokens.
        
        Assuming a fixed price per token for simplicity.

        :param amount: The amount of tokens to buy back.
        :return: The total cost for the buy-back.
        """
        price_per_token = 1.0  # Define the price per token
        return amount * price_per_token

    def get_buy_back_history(self):
        """
        Retrieve the history of buy-back transactions.

        :return: A list of tuples containing the amount of tokens bought back and the cost.
        """
        return self.buy_back_history

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the TGC token with a total supply of 10000 and a buy-back fund of 5000.
        tgc_token = TGCToken(total_supply=10000, buy_back_fund=5000)
        
        # Attempt to buy back 200 tokens
        tgc_token.buy_back_tokens(200)

        # Print buy-back history
        print("Buy-back history:", tgc_token.get_buy_back_history())

        # Attempt to buy back 6000 tokens (should raise an error)
        tgc_token.buy_back_tokens(6000)

    except Exception as e:
        logging.error("An error occurred: %s", e)
```
