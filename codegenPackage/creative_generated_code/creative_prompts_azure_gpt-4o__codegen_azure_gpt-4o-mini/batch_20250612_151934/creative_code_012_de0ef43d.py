"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1wiji.top
Prompt: Create a Python program to simulate betting on 1xBet's "Marble-Live" game and calculate the probability of winning.
Generated: DETERMINISTIC_de0ef43d90e675af
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class MarbleLiveGame:
    """
    A class to simulate the Marble-Live betting game.
    """

    def __init__(self, total_balls=100, winning_balls=50):
        """
        Initializes the game with a specific number of total balls
        and a number of winning balls.

        :param total_balls: Total number of balls in the game (default is 100)
        :param winning_balls: Number of winning balls (default is 50)
        """
        if total_balls <= 0 or winning_balls < 0 or winning_balls > total_balls:
            raise ValueError("Invalid total or winning balls configuration.")
        
        self.total_balls = total_balls
        self.winning_balls = winning_balls

    def calculate_probability(self):
        """
        Calculates the probability of winning based on the number of winning balls
        and the total number of balls.

        :return: Probability of winning as a float
        """
        probability = self.winning_balls / self.total_balls
        return probability

    def place_bet(self, bet_amount):
        """
        Simulates placing a bet on the game and determines if the bet is a win or loss.

        :param bet_amount: The amount of money being bet (must be positive)
        :return: A tuple with the result (win/loss) and the payout amount
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be positive.")

        # Simulate the draw
        drawn_ball = random.randint(1, self.total_balls)

        # Determine if the drawn ball is a winning ball
        if drawn_ball <= self.winning_balls:
            winnings = bet_amount * 2  # Assume a winning payout of 2x the bet
            return "win", winnings
        else:
            return "loss", 0

def main():
    """
    Main function to run the Marble Live game simulation.
    """
    try:
        # Initialize the game
        game = MarbleLiveGame(total_balls=100, winning_balls=50)
        
        # Display the probability of winning
        probability = game.calculate_probability()
        print(f"Probability of winning: {probability:.2%}")

        # Simulate placing a bet
        bet_amount = float(input("Enter your bet amount: "))
        result, payout = game.place_bet(bet_amount)
        
        if result == "win":
            print(f"Congratulations! You won: ${payout:.2f}")
        else:
            print("Sorry, you lost your bet.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
