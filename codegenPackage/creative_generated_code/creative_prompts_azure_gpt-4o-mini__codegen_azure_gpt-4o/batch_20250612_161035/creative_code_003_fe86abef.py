"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-daddy.pages.dev
Prompt: Develop a script that simulates the buying process of $DADDY tokens and tracks the investment's performance over time.
Generated: DETERMINISTIC_fe86abef1da40e96
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class DaddyTokenInvestment:
    """
    A class to simulate the buying process of $DADDY tokens and 
    track the investment's performance over time.
    """
    def __init__(self, initial_price: float):
        """
        Initialize the investment tracking system.
        
        :param initial_price: Starting price of $DADDY token in USD.
        """
        self.token_price = initial_price  # Current price of $DADDY token
        self.tokens_owned = 0            # Tokens owned by the user
        self.investment_value = 0        # Total investment value in USD

    def buy_tokens(self, usd_amount: float):
        """
        Buy $DADDY tokens with a specified amount of USD.
        
        :param usd_amount: Amount of USD to invest in $DADDY tokens.
        :return: Number of tokens purchased.
        """
        if usd_amount <= 0:
            raise ValueError("Investment amount must be greater than 0.")
        
        tokens_purchased = usd_amount / self.token_price
        self.tokens_owned += tokens_purchased
        self.investment_value += usd_amount
        
        print(f"Purchased {tokens_purchased:.2f} $DADDY tokens at ${self.token_price:.2f} each.")
        return tokens_purchased

    def simulate_price_change(self):
        """
        Simulate a random price change for the $DADDY token.
        """
        # Generate a random percentage change (-10% to +10%)
        percentage_change = random.uniform(-0.1, 0.1)
        self.token_price *= (1 + percentage_change)
        self.token_price = round(self.token_price, 2)  # Round to two decimal places

    def track_performance(self):
        """
        Track the current performance of the investment.
        
        :return: Performance summary as a dictionary.
        """
        current_value = self.tokens_owned * self.token_price
        profit_loss = current_value - self.investment_value
        
        return {
            "Current Token Price": self.token_price,
            "Tokens Owned": self.tokens_owned,
            "Investment Value (USD)": self.investment_value,
            "Current Value (USD)": current_value,
            "Profit/Loss (USD)": profit_loss
        }

def main():
    """
    Main function to simulate $DADDY tokens investment.
    """
    try:
        # Initialize investment with an initial token price of $1.00
        investment = DaddyTokenInvestment(initial_price=1.00)
        
        print("\nWelcome to the $DADDY Token Investment Simulation!")

        # Simulate multiple rounds of investment and price tracking
        for i in range(5):  # Simulate 5 rounds
            print("\nRound", i + 1)

            # Prompt user for investment amount
            usd_amount = float(input("Enter amount (in USD) to invest in $DADDY tokens: "))
            
            # Buy tokens
            investment.buy_tokens(usd_amount)

            # Simulate price change
            print("\nSimulating price change...")
            time.sleep(2)  # Wait for 2 seconds to simulate real-world delay
            investment.simulate_price_change()
            
            # Track performance
            performance = investment.track_performance()
            print("\nInvestment Performance:")
            for key, value in performance.items():
                print(f"{key}: ${value:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
