"""
Generated Code Metadata:
========================
Original URL: https://alltecskateparks.com
Prompt: Create a tutorial on how to implement a slot game strategy that includes setting win/loss limits and utilizing free spins, based on the tips provided for Lucky Neko at INDOXSLOT.
Generated: DETERMINISTIC_9adf66649f5c4d19
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SlotGame:
    def __init__(self, win_limit, loss_limit):
        """
        Initializes the SlotGame with win and loss limits.

        :param win_limit: The maximum amount of winnings before stopping.
        :param loss_limit: The maximum amount of losses before stopping.
        """
        self.win_limit = win_limit
        self.loss_limit = loss_limit
        self.current_balance = 0
        self.total_wins = 0
        self.total_losses = 0
        self.free_spins_available = 0

    def spin(self):
        """
        Simulates a spin of the slot machine. Randomly determines if the spin is a win or loss.
        """
        # Simulate a random outcome: 70% chance of losing, 30% chance of winning
        outcome = random.choices(['win', 'loss'], weights=[0.3, 0.7], k=1)[0]
        if outcome == 'win':
            win_amount = random.randint(10, 100)  # Random win amount between 10 and 100
            self.current_balance += win_amount
            self.total_wins += win_amount
            print(f"Spin Result: Win! You won {win_amount}. Current Balance: {self.current_balance}")
        else:
            loss_amount = random.randint(5, 50)  # Random loss amount between 5 and 50
            self.current_balance -= loss_amount
            self.total_losses += loss_amount
            print(f"Spin Result: Loss! You lost {loss_amount}. Current Balance: {self.current_balance}")

    def check_limits(self):
        """
        Checks if the current balance has reached the win or loss limits.
        """
        if self.current_balance >= self.win_limit:
            print(f"Congratulations! You've reached your win limit of {self.win_limit}.")
            return True
        elif self.current_balance <= -self.loss_limit:
            print(f"Sorry! You've reached your loss limit of {self.loss_limit}.")
            return True
        return False

    def utilize_free_spins(self):
        """
        Utilizes free spins if available. Each free spin is treated as a guaranteed win.
        """
        if self.free_spins_available > 0:
            self.free_spins_available -= 1
            win_amount = random.randint(20, 150)  # Random win amount for free spins
            self.current_balance += win_amount
            self.total_wins += win_amount
            print(f"Free Spin Result: Win! You won {win_amount}. Current Balance: {self.current_balance}")
        else:
            print("No free spins available.")

    def play(self):
        """
        Main method to play the slot game until win/loss limits are reached.
        """
        while True:
            self.spin()
            if self.check_limits():
                break
            if random.random() < 0.1:  # 10% chance to earn a free spin after each spin
                self.free_spins_available += 1
                print(f"You earned a free spin! Total Free Spins: {self.free_spins_available}")
            self.utilize_free_spins()

# Example usage
if __name__ == "__main__":
    try:
        # Set win and loss limits
        win_limit = 500
        loss_limit = 300

        # Create a SlotGame instance
        game = SlotGame(win_limit, loss_limit)

        # Start playing the game
        game.play()
    except Exception as e:
        print(f"An error occurred: {e}")
```
