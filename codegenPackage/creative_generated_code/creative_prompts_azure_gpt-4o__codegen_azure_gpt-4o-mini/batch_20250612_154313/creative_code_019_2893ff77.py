"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofi.us.com
Prompt: Write a Python script to simulate the Xóc Đĩa game based on WW88's rules and strategies for winning.
Generated: DETERMINISTIC_2893ff774dd3b83f
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class XocDiaGame:
    def __init__(self):
        self.bets = {
            "Red": 0,
            "Black": 0,
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0
        }
        self.results = []

    def place_bet(self, bet_type, amount):
        """
        Place a bet on the specified bet type.
        
        :param bet_type: Type of bet ('Red', 'Black', '1', '2', '3', '4')
        :param amount: Amount to bet
        """
        if bet_type not in self.bets:
            raise ValueError(f"Invalid bet type: {bet_type}. Valid types are {list(self.bets.keys())}.")
        if amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")

        self.bets[bet_type] += amount

    def spin(self):
        """
        Simulate the spinning of the Xóc Đĩa game and determine the outcome.
        """
        # Simulate the game outcome with random results from 1 to 4 and colors
        colors = ['Red', 'Black']
        color_result = random.choice(colors)
        number_result = str(random.randint(1, 4))

        self.results = [color_result, number_result]
        print(f"Spin results: Color - {color_result}, Number - {number_result}")

    def calculate_winnings(self):
        """
        Calculate the winnings based on the bets placed and the results of the spin.
        
        :return: Total winnings
        """
        winnings = 0
        color_result, number_result = self.results

        # Check winnings for color bets
        if color_result == 'Red':
            winnings += self.bets["Red"] * 2
        elif color_result == 'Black':
            winnings += self.bets["Black"] * 2

        # Check winnings for number bets
        if number_result in self.bets:
            winnings += self.bets[number_result] * 2

        return winnings

    def reset_bets(self):
        """
        Reset all bets to zero after the game round.
        """
        self.bets = {key: 0 for key in self.bets}

    def play_round(self):
        """
        Play a single round of the Xóc Đĩa game.
        """
        try:
            self.spin()
            winnings = self.calculate_winnings()
            print(f"Total winnings for this round: {winnings}")
        except Exception as e:
            print(f"Error during game round: {e}")
        finally:
            self.reset_bets()


if __name__ == "__main__":
    game = XocDiaGame()

    # Example of placing bets
    try:
        game.place_bet("Red", 10)
        game.place_bet("1", 5)
        game.play_round()
    except ValueError as ve:
        print(f"Betting error: {ve}")
```
