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

class SlotGameStrategy:
    """
    A class to implement a slot game strategy with win/loss limits and free spins.
    """

    def __init__(self, balance, win_limit, loss_limit, free_spins):
        """
        Initialize the slot game strategy.

        :param balance: Initial balance of the player.
        :param win_limit: Maximum profit before stopping.
        :param loss_limit: Maximum loss before stopping.
        :param free_spins: Number of free spins available.
        """
        self.balance = balance
        self.win_limit = win_limit
        self.loss_limit = loss_limit
        self.free_spins = free_spins
        self.initial_balance = balance

    def spin(self, bet_amount):
        """
        Simulate a single spin of the slot machine.

        :param bet_amount: Amount to bet on the spin.
        :return: Result of the spin (win or loss amount).
        """
        if bet_amount > self.balance:
            raise ValueError("Bet amount exceeds current balance.")
        
        # Simulate the outcome of the spin (50% chance to win or lose)
        outcome = random.choice(["win", "loss"])
        if outcome == "win":
            # Random win amount between 1x and 5x the bet
            return bet_amount * random.randint(1, 5)
        else:
            # Loss equals the bet amount
            return -bet_amount

    def play(self, bet_amount):
        """
        Play the slot game until win/loss limits are reached or balance is depleted.

        :param bet_amount: Amount to bet on each spin.
        """
        spin_count = 0

        while self.balance > 0:
            # Check if win/loss limits are reached
            profit = self.balance - self.initial_balance
            if profit >= self.win_limit:
                print(f"Win limit reached! Profit: {profit}")
                break
            elif profit <= -self.loss_limit:
                print(f"Loss limit reached! Loss: {abs(profit)}")
                break

            # Use free spins if available
            if self.free_spins > 0:
                print("Using a free spin!")
                self.free_spins -= 1
                result = self.spin(0)  # Free spin, no bet amount
            else:
                result = self.spin(bet_amount)

            # Update balance based on spin result
            self.balance += result
            spin_count += 1

            # Log the result of the spin
            print(f"Spin {spin_count}: {'Win' if result > 0 else 'Loss'} | Result: {result} | Balance: {self.balance}")

        if self.balance <= 0:
            print("Game over! Balance depleted.")

    def reset(self):
        """
        Reset the game strategy to its initial state.
        """
        self.balance = self.initial_balance
        print("Game reset. Balance restored to initial value.")

# Example usage
if __name__ == "__main__":
    # Initialize the strategy with a balance of 100, win limit of 50, loss limit of 30, and 3 free spins
    strategy = SlotGameStrategy(balance=100, win_limit=50, loss_limit=30, free_spins=3)

    try:
        # Play the game with a bet amount of 10 per spin
        strategy.play(bet_amount=10)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        # Reset the game after playing
        strategy.reset()
```
