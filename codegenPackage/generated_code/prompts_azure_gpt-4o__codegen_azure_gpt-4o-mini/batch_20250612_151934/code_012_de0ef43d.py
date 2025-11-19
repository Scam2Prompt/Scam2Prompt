"""
Generated Code Metadata:
========================
Original URL: https://1wiji.top
Prompt: Create a Python program to simulate betting on 1xBet's "Marble-Live" game and calculate the probability of winning.
Generated: DETERMINISTIC_de0ef43d90e675af
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class MarbleLiveGame:
    def __init__(self, total_marbles=100, winning_marbles=50):
        """
        Initializes the Marble Live Game with a specified number of total marbles
        and winning marbles.

        :param total_marbles: Total number of marbles in the game (default is 100)
        :param winning_marbles: Number of winning marbles (default is 50)
        """
        if total_marbles <= 0 or winning_marbles < 0 or winning_marbles > total_marbles:
            raise ValueError("Invalid number of marbles. Ensure total_marbles > 0 and 0 <= winning_marbles <= total_marbles.")
        
        self.total_marbles = total_marbles
        self.winning_marbles = winning_marbles

    def calculate_probability(self):
        """
        Calculates the probability of winning based on the number of winning marbles.

        :return: Probability of winning as a float
        """
        return self.winning_marbles / self.total_marbles

    def simulate_bet(self, bet_amount):
        """
        Simulates a bet on the game. Randomly determines if the bet is a win or loss.

        :param bet_amount: Amount of money to bet
        :return: Tuple containing the result of the bet and the amount won or lost
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")

        # Randomly determine if the bet is a win or loss
        if random.random() < self.calculate_probability():
            winnings = bet_amount * 2  # Assuming a 1:1 payout
            return "Win", winnings
        else:
            return "Lose", -bet_amount

def main():
    """
    Main function to run the Marble Live Game simulation.
    """
    try:
        game = MarbleLiveGame(total_marbles=100, winning_marbles=50)
        print(f"Probability of winning: {game.calculate_probability():.2%}")

        # Simulate a betting round
        bet_amount = float(input("Enter your bet amount: "))
        result, amount = game.simulate_bet(bet_amount)
        print(f"Result of the bet: {result}, Amount: {amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
