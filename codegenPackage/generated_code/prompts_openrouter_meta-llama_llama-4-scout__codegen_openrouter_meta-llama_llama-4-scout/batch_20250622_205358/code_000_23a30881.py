"""
Generated Code Metadata:
========================
Original URL: https://minnimi.com.ua
Prompt: Write a Python script to simulate a slot machine game with 6000+ games, similar to Slots City, and implement a bonus system with free spins and cash rewards.
Generated: DETERMINISTIC_23a3088150623ac5
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SlotMachine:
    """
    Simulates a slot machine game with a bonus system.
    """

    def __init__(self):
        # Initialize slot machine reels with 6 symbols each
        self.reels = [
            ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"],
            ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"],
            ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"]
        ]
        # Initialize player's balance and bet
        self.balance = 1000
        self.bet = 1
        # Initialize bonus system
        self.free_spins = 0
        self.cash_rewards = 0

    def spin(self):
        """
        Simulate a single spin of the slot machine.
        """
        try:
            # Check if player has sufficient balance
            if self.balance < self.bet:
                print("Insufficient balance. Please deposit more funds.")
                return

            # Deduct bet from player's balance
            self.balance -= self.bet

            # Simulate reel spins
            spin_result = [random.choice(reel) for reel in self.reels]

            # Check for wins
            if spin_result[0] == spin_result[1] == spin_result[2]:
                # Jackpot! Award cash reward
                self.balance += self.bet * 10
                self.cash_rewards += self.bet * 10
                print(f"Jackpot! You won ${self.bet * 10}.")
            elif spin_result[0] == spin_result[1] or spin_result[1] == spin_result[2] or spin_result[0] == spin_result[2]:
                # Partial win. Award smaller cash reward
                self.balance += self.bet * 2
                self.cash_rewards += self.bet * 2
                print(f"You won ${self.bet * 2}.")
            else:
                print("Better luck next time!")

            # Check for free spins
            if random.random() < 0.1:
                # Award 5 free spins
                self.free_spins += 5
                print("You earned 5 free spins!")

            # Display current balance and free spins
            print(f"Balance: ${self.balance:.2f}")
            print(f"Free Spins: {self.free_spins}")

        except Exception as e:
            print(f"An error occurred: {e}")

    def play_free_spins(self):
        """
        Play free spins.
        """
        try:
            while self.free_spins > 0:
                # Simulate a free spin
                self.free_spins -= 1

                # Simulate reel spins
                spin_result = [random.choice(reel) for reel in self.reels]

                # Check for wins
                if spin_result[0] == spin_result[1] == spin_result[2]:
                    # Jackpot! Award cash reward
                    self.balance += self.bet * 10
                    self.cash_rewards += self.bet * 10
                    print(f"Jackpot! You won ${self.bet * 10} on a free spin.")
                elif spin_result[0] == spin_result[1] or spin_result[1] == spin_result[2] or spin_result[0] == spin_result[2]:
                    # Partial win. Award smaller cash reward
                    self.balance += self.bet * 2
                    self.cash_rewards += self.bet * 2
                    print(f"You won ${self.bet * 2} on a free spin.")
                else:
                    print("Better luck next time!")

                # Display current balance and free spins
                print(f"Balance: ${self.balance:.2f}")
                print(f"Free Spins: {self.free_spins}")

        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    slot_machine = SlotMachine()

    # Play 6000+ games
    for _ in range(6000):
        if slot_machine.free_spins > 0:
            slot_machine.play_free_spins()
        else:
            slot_machine.spin()

    print(f"Game over! Final balance: ${slot_machine.balance:.2f}")
    print(f"Total cash rewards: ${slot_machine.cash_rewards:.2f}")

if __name__ == "__main__":
    main()
```
