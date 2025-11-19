"""
Generated Code Metadata:
========================
Original URL: https://aspjj.com
Prompt: "Write a Python script to simulate a slot machine game with features like auto-play and adjustable bet amounts, inspired by the mechanics of สล็อตเว็บตรง."
Generated: DETERMINISTIC_ec77bf1af7d1ba3f
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class SlotMachine:
    """
    Simulates a slot machine game with features like auto-play and adjustable bet amounts.
    """

    def __init__(self):
        self.symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']
        self.balance = 0
        self.bet_amount = 0

    def spin(self):
        """
        Simulates a single spin of the slot machine.
        Returns:
            list: A list of three random symbols.
        """
        return random.sample(self.symbols, 3)

    def check_win(self, spin_result):
        """
        Checks if the spin result is a win.
        Args:
            spin_result (list): A list of three symbols.
        Returns:
            int: The win amount if it's a win, otherwise 0.
        """
        if spin_result[0] == spin_result[1] == spin_result[2]:
            return self.bet_amount * 10
        elif spin_result[0] == spin_result[1] or spin_result[0] == spin_result[2] or spin_result[1] == spin_result[2]:
            return self.bet_amount * 2
        else:
            return 0

    def play(self):
        """
        Starts the slot machine game.
        """
        print("Welcome to the Slot Machine Game!")
        self.balance = float(input("Enter your initial balance: "))
        while True:
            print(f"\nCurrent Balance: {self.balance}")
            try:
                self.bet_amount = float(input("Enter your bet amount: "))
                if self.bet_amount > self.balance:
                    print("Insufficient balance. Please enter a lower bet amount.")
                    continue
                if self.bet_amount <= 0:
                    print("Bet amount must be greater than 0.")
                    continue
            except ValueError:
                print("Invalid bet amount. Please enter a number.")
                continue

            auto_play = input("Do you want to play auto-play? (yes/no): ")
            if auto_play.lower() == "yes":
                num_spins = int(input("Enter the number of spins: "))
                for _ in range(num_spins):
                    spin_result = self.spin()
                    print(f"\nSpin Result: {spin_result}")
                    win_amount = self.check_win(spin_result)
                    if win_amount > 0:
                        print(f"Congratulations, you won {win_amount}!")
                        self.balance += win_amount
                    else:
                        print("Better luck next time!")
                        self.balance -= self.bet_amount
                    time.sleep(1)  # simulate spin delay
            else:
                spin_result = self.spin()
                print(f"\nSpin Result: {spin_result}")
                win_amount = self.check_win(spin_result)
                if win_amount > 0:
                    print(f"Congratulations, you won {win_amount}!")
                    self.balance += win_amount
                else:
                    print("Better luck next time!")
                    self.balance -= self.bet_amount

            play_again = input("\nDo you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break

        print(f"\nGame Over. Your final balance is: {self.balance}")


if __name__ == "__main__":
    game = SlotMachine()
    game.play()
```
