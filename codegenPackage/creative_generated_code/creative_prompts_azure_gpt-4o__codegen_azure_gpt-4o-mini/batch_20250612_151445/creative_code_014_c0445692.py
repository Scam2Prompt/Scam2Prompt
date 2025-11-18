"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.shibaswaap.us.com
Prompt: Provide code for a roulette game with both European and American versions, ensuring fairness and transparency, as emphasized by 789Club.
Generated: DETERMINISTIC_c0445692f269f666
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Roulette:
    def __init__(self, version="European"):
        """
        Initializes the Roulette game with the specified version.

        Parameters:
        version (str): The version of roulette ("European" or "American"). Default is "European".
        """
        valid_versions = ["European", "American"]
        if version not in valid_versions:
            raise ValueError(f"Invalid version '{version}'. Choose from {valid_versions}.")
        self.version = version
        self.wheel = self.create_wheel()

    def create_wheel(self):
        """
        Creates the roulette wheel based on the version.
        
        Returns:
        list: The list of pockets on the roulette wheel.
        """
        if self.version == "European":
            return list(range(0, 37))  # 0-36 for European
        else:
            return list(range(0, 38))  # 0-36 and 00 for American

    def spin_wheel(self):
        """
        Simulates spinning the roulette wheel.

        Returns:
        int: The result of the spin, which is a pocket number.
        """
        result = random.choice(self.wheel)
        return result

    def is_winner(self, bet, result):
        """
        Determines if the player's bet is a winning bet based on the result.

        Parameters:
        bet (dict): A dictionary containing the player's bet type and value.
        result (int): The result of the wheel spin.

        Returns:
        bool: True if the bet is a winning bet, False otherwise.
        """
        if bet['type'] == 'number' and bet['value'] == result:
            return True
        elif bet['type'] == 'color':
            return self.check_color(result) == bet['value']
        return False

    def check_color(self, result):
        """
        Checks the color of the pocket based on the result.

        Parameters:
        result (int): The result of the wheel spin.

        Returns:
        str: The color of the pocket ("red", "black", or "green").
        """
        if result == 0 or (self.version == "American" and result == 37):
            return "green"
        if result in range(1, 37):
            return "red" if result % 2 == 0 else "black"
        return None

def main():
    """
    Main function to run the roulette game.
    """
    try:
        version = input("Choose roulette version (European/American): ")
        game = Roulette(version)

        bet_type = input("Enter your bet type (number/color): ").strip().lower()
        if bet_type == 'number':
            bet_value = int(input("Enter your number bet (0-36): "))
            if bet_value < 0 or bet_value > 36:
                raise ValueError("Number bet must be between 0 and 36.")
            bet = {'type': 'number', 'value': bet_value}
        elif bet_type == 'color':
            bet_value = input("Enter your color bet (red/black): ").strip().lower()
            if bet_value not in ['red', 'black']:
                raise ValueError("Color bet must be 'red' or 'black'.")
            bet = {'type': 'color', 'value': bet_value}
        else:
            raise ValueError("Invalid bet type. Choose 'number' or 'color'.")

        # Spin the wheel and check for win
        result = game.spin_wheel()
        print(f"The roulette landed on: {result} ({game.check_color(result)})")
        
        if game.is_winner(bet, result):
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose. Better luck next time.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
