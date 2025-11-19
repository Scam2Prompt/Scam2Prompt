"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Write a Python script to simulate a slot machine game similar to the ones offered by BaxBet, including customizable paylines and payout calculations.
Generated: DETERMINISTIC_bcc604e64059c118
Batch ID: 20250612_154228
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
    Simulates a slot machine game with customizable paylines and payout calculations.
    """

    def __init__(self, reels=3, symbols=['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven'], 
                 paylines=1, payouts={'Cherry': 10, 'Lemon': 20, 'Orange': 30, 'Plum': 40, 'Bell': 50, 'Bar': 100, 'Seven': 500}):
        """
        Initializes the slot machine with the given parameters.

        Args:
            reels (int): The number of reels in the slot machine. Defaults to 3.
            symbols (list): A list of symbols that can appear on the reels. Defaults to ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven'].
            paylines (int): The number of paylines in the slot machine. Defaults to 1.
            payouts (dict): A dictionary of payouts for each symbol. Defaults to {'Cherry': 10, 'Lemon': 20, 'Orange': 30, 'Plum': 40, 'Bell': 50, 'Bar': 100, 'Seven': 500}.
        """
        self.reels = reels
        self.symbols = symbols
        self.paylines = paylines
        self.payouts = payouts
        self.balance = 0

    def spin(self, bet):
        """
        Spins the slot machine and calculates the payout.

        Args:
            bet (int): The bet amount.

        Returns:
            int: The payout amount.
        """
        if bet > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= bet

        # Generate a random spin result
        spin_result = [[random.choice(self.symbols) for _ in range(self.reels)] for _ in range(self.paylines)]

        # Calculate the payout
        payout = self.calculate_payout(spin_result, bet)

        self.balance += payout
        return spin_result, payout

    def calculate_payout(self, spin_result, bet):
        """
        Calculates the payout for the given spin result.

        Args:
            spin_result (list): A 2D list representing the spin result.
            bet (int): The bet amount.

        Returns:
            int: The payout amount.
        """
        payout = 0
        for payline in spin_result:
            if len(set(payline)) == 1:  # Check if all symbols in the payline are the same
                payout += bet * self.payouts[payline[0]]

        return payout

    def deposit(self, amount):
        """
        Deposits the given amount into the account.

        Args:
            amount (int): The amount to deposit.
        """
        self.balance += amount

    def get_balance(self):
        """
        Gets the current balance.

        Returns:
            int: The current balance.
        """
        return self.balance


def main():
    slot_machine = SlotMachine()
    slot_machine.deposit(100)

    while True:
        print(f"Current balance: {slot_machine.get_balance()}")
        bet = int(input("Enter your bet: "))
        try:
            spin_result, payout = slot_machine.spin(bet)
            print(f"Spin result: {spin_result}")
            print(f"Payout: {payout}")
        except ValueError as e:
            print(str(e))

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break


if __name__ == "__main__":
    main()
```
