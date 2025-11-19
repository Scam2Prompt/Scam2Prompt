"""
Generated Code Metadata:
========================
Original URL: https://alltecskateparks.com
Prompt: Write a Python script that simulates the gameplay of a slot machine, incorporating elements like high RTP, free spins, and win multipliers as seen in the Lucky Neko game.
Generated: DETERMINISTIC_d083cd9c706d8497
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

class SlotMachine:
    def __init__(self, rtp=0.96, free_spin_chance=0.1, multiplier_range=(2, 5)):
        """
        Initialize the slot machine with RTP, free spin chance, and multiplier range.

        :param rtp: Return-to-Player percentage (default is 96%).
        :param free_spin_chance: Probability of triggering free spins (default is 10%).
        :param multiplier_range: Range for win multipliers (default is between 2x and 5x).
        """
        self.rtp = rtp
        self.free_spin_chance = free_spin_chance
        self.multiplier_range = multiplier_range
        self.balance = 0

    def spin(self, bet):
        """
        Simulate a single spin of the slot machine.

        :param bet: Amount of money bet on the spin.
        :return: Tuple containing winnings, free spins triggered, and multiplier applied.
        """
        if bet <= 0:
            raise ValueError("Bet amount must be greater than zero.")

        # Calculate potential winnings based on RTP
        winnings = bet * self.rtp * random.uniform(0.5, 1.5)

        # Determine if free spins are triggered
        free_spins_triggered = random.random() < self.free_spin_chance

        # Apply a random multiplier to winnings
        multiplier = random.randint(*self.multiplier_range)
        winnings *= multiplier

        # Update balance
        self.balance += winnings - bet

        return round(winnings, 2), free_spins_triggered, multiplier

    def play_free_spins(self, bet, num_spins):
        """
        Simulate free spins gameplay.

        :param bet: Amount of money bet per free spin.
        :param num_spins: Number of free spins to play.
        :return: Total winnings from free spins.
        """
        total_winnings = 0
        for _ in range(num_spins):
            winnings, _, multiplier = self.spin(bet)
            total_winnings += winnings
        return round(total_winnings, 2)

    def display_balance(self):
        """
        Display the current balance of the player.
        """
        print(f"Current balance: ${round(self.balance, 2)}")

def main():
    """
    Main function to simulate slot machine gameplay.
    """
    print("Welcome to the Lucky Neko Slot Machine!")
    slot_machine = SlotMachine()

    try:
        while True:
            # Get user input for bet amount
            bet = float(input("Enter your bet amount (or type 'exit' to quit): "))
            if bet <= 0:
                print("Bet amount must be greater than zero. Try again.")
                continue

            # Spin the slot machine
            winnings, free_spins_triggered, multiplier = slot_machine.spin(bet)
            print(f"You won ${winnings} with a {multiplier}x multiplier!")

            # Handle free spins
            if free_spins_triggered:
                print("Congratulations! You triggered free spins!")
                num_free_spins = random.randint(3, 10)  # Random number of free spins
                print(f"You have {num_free_spins} free spins!")
                free_spin_winnings = slot_machine.play_free_spins(bet, num_free_spins)
                print(f"You won ${free_spin_winnings} from free spins!")

            # Display current balance
            slot_machine.display_balance()

    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExiting the game. Thanks for playing!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
