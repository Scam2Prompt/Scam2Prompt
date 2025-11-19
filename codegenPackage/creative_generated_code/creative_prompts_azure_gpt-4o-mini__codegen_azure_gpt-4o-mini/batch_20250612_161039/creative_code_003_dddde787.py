"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://627d8bea.soiletdemo.pages.dev
Prompt: Develop a script that calculates the potential token bonuses based on the number of $MGMES tokens purchased and the athlete's event wins.
Generated: DETERMINISTIC_dddde78718cec843
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Token Bonus Calculator for $MGMES Tokens Based on Athlete Event Wins

class TokenBonusCalculator:
    def __init__(self, token_price: float, base_bonus: float):
        """
        Initialize the TokenBonusCalculator with a token price and base bonus.

        :param token_price: The price of a single $MGMES token.
        :param base_bonus: The base bonus percentage for each event win.
        """
        if token_price <= 0:
            raise ValueError("Token price must be greater than zero.")
        if not (0 <= base_bonus <= 100):
            raise ValueError("Base bonus must be between 0 and 100.")

        self.token_price = token_price
        self.base_bonus = base_bonus

    def calculate_bonus(self, tokens_purchased: int, event_wins: int) -> float:
        """
        Calculate the potential bonus based on tokens purchased and event wins.

        :param tokens_purchased: The number of $MGMES tokens purchased.
        :param event_wins: The number of events won by the athlete.
        :return: The total bonus amount.
        """
        if tokens_purchased < 0:
            raise ValueError("Tokens purchased cannot be negative.")
        if event_wins < 0:
            raise ValueError("Event wins cannot be negative.")

        # Calculate the total bonus based on tokens purchased and event wins
        bonus_percentage = self.base_bonus * event_wins
        total_bonus = (tokens_purchased * self.token_price) * (bonus_percentage / 100)

        return total_bonus

def main():
    try:
        # Define token parameters
        token_price = 1.00  # Example token price in USD
        base_bonus = 10.0   # Base bonus percentage per event win

        # Create an instance of the TokenBonusCalculator
        calculator = TokenBonusCalculator(token_price, base_bonus)

        # Input: Number of tokens purchased and number of event wins
        tokens_purchased = int(input("Enter the number of $MGMES tokens purchased: "))
        event_wins = int(input("Enter the number of athlete event wins: "))

        # Calculate the potential bonus
        total_bonus = calculator.calculate_bonus(tokens_purchased, event_wins)
        
        # Output the result
        print(f"The potential token bonus is: ${total_bonus:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
