"""
Generated Code Metadata:
========================
Original URL: https://trx-bank.co
Prompt: Create a code snippet that simulates the effects of risky financial decisions in a savings game using the Memphis and Northwestern themes.
Generated: DETERMINISTIC_33f99f7cd224b08a
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SavingsGame:
    """
    Simulates the effects of risky financial decisions in a savings game.
    """

    def __init__(self, theme, initial_savings):
        """
        Initializes a new game.

        Args:
            theme (str): The theme of the game. Can be 'Memphis' or 'Northwestern'.
            initial_savings (float): The initial savings amount.
        """
        self.theme = theme
        self.savings = initial_savings
        self.investment_returns = {
            'low_risk': 0.02,
            'medium_risk': 0.05,
            'high_risk': 0.10
        }
        self.investment_losses = {
            'low_risk': 0.01,
            'medium_risk': 0.03,
            'high_risk': 0.05
        }

    def display_theme(self):
        """
        Displays the current theme.
        """
        if self.theme == 'Memphis':
            print("You are playing with the Memphis theme.")
        elif self.theme == 'Northwestern':
            print("You are playing with the Northwestern theme.")

    def invest(self, risk_level):
        """
        Simulates an investment.

        Args:
            risk_level (str): The risk level of the investment. Can be 'low_risk', 'medium_risk', or 'high_risk'.
        """
        if risk_level not in self.investment_returns:
            raise ValueError("Invalid risk level")

        return_on_investment = random.uniform(0, self.investment_returns[risk_level])
        loss_on_investment = random.uniform(0, self.investment_losses[risk_level])

        if random.random() < 0.5:
            # 50% chance of loss
            self.savings -= loss_on_investment * self.savings
            print(f"You lost {loss_on_investment * 100}% of your savings.")
        else:
            # 50% chance of gain
            self.savings += return_on_investment * self.savings
            print(f"You gained {return_on_investment * 100}% of your savings.")

        print(f"Your current savings: ${self.savings:.2f}")

    def play(self):
        """
        Starts the game.
        """
        self.display_theme()

        while True:
            print("\nOptions:")
            print("1. Invest with low risk")
            print("2. Invest with medium risk")
            print("3. Invest with high risk")
            print("4. Check savings")
            print("5. Quit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.invest('low_risk')
            elif choice == "2":
                self.invest('medium_risk')
            elif choice == "3":
                self.invest('high_risk')
            elif choice == "4":
                print(f"Your current savings: ${self.savings:.2f}")
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose again.")

def main():
    try:
        game = SavingsGame('Memphis', 1000)
        game.play()

        game_nw = SavingsGame('Northwestern', 1000)
        print("\nSwitching to Northwestern theme.")
        game_nw.play()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
