"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trx-bank.co
Prompt: Create a code snippet that simulates the effects of risky financial decisions in a savings game using the Memphis and Northwestern themes.
Generated: DETERMINISTIC_33f99f7cd224b08a
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SavingsGame:
    """
    A simulation game to showcase the effects of risky financial decisions 
    on savings in the Memphis and Northwestern themes.
    """
    def __init__(self, initial_balance, theme='Memphis'):
        """
        Initialize the game with an initial balance and theme.

        :param initial_balance: Starting amount in savings (float or int).
        :param theme: Theme of the game, either 'Memphis' or 'Northwestern'. (str)
        """
        if theme not in ['Memphis', 'Northwestern']:
            raise ValueError("Invalid theme. Choose 'Memphis' or 'Northwestern'.")
        
        self.balance = initial_balance
        self.theme = theme
        self.risky_choices = ['Gamble', 'Market Speculation', 'Luxury Spending']

    def risky_decision(self):
        """
        Simulates a risky financial decision, randomly affecting the balance.
        The Memphis theme is more forgiving than the Northwestern theme.
        """
        choice = random.choice(self.risky_choices)
        print(f"The risky choice made: {choice}")
        
        # Define risk impact based on theme
        if self.theme == 'Memphis':
            # Memphis theme: Higher chance of reward, lower chance of loss
            impact = random.uniform(-0.2, 0.5)  # -20% to +50% of current balance
        elif self.theme == 'Northwestern':
            # Northwestern theme: Higher chance of loss, lower chance of reward
            impact = random.uniform(-0.5, 0.2)  # -50% to +20% of current balance
        
        # Calculate the impact on balance
        change = self.balance * impact
        self.balance += change
        print(f"Balance change due to {choice}: {'+' if change > 0 else ''}{change:.2f}")
        print(f"New balance: {self.balance:.2f}")

    def play_game(self, rounds=5):
        """
        Plays the savings game for a specified number of rounds.

        :param rounds: Number of risky decisions to simulate. (int)
        """
        print(f"Starting Savings Game with theme '{self.theme}' and initial balance ${self.balance:.2f}")
        
        for round_num in range(1, rounds + 1):
            print(f"\n--- Round {round_num} ---")
            try:
                self.risky_decision()
            except Exception as e:
                print(f"An error occurred: {e}")
        
        print(f"\nGame Over! Final balance: ${self.balance:.2f}")

if __name__ == "__main__":
    # Example of running the game
    try:
        initial_balance = float(input("Enter your initial savings balance: "))
        theme = input("Choose a theme ('Memphis' or 'Northwestern'): ")
        
        game = SavingsGame(initial_balance, theme)
        game.play_game(rounds=5)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
