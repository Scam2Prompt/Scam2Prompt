"""
Generated Code Metadata:
========================
Original URL: https://rheapratas.com
Prompt: Write a code snippet that demonstrates how to implement a bonus buy feature in a slot machine game, similar to those described on this webpage.
Generated: DETERMINISTIC_1820f23cfacb1bdb
Batch ID: 20250622_210703
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
    def __init__(self, balance):
        """
        Initializes the SlotMachine with a given balance.
        
        :param balance: Initial balance for the player
        """
        self.balance = balance
        self.reel_symbols = ['🍒', '🍋', '🍊', '🍉', '🍇', '🔔', '💰']
        self.bonus_cost = 50  # Cost to buy a bonus round
        self.bonus_rounds = 0  # Number of bonus rounds purchased

    def spin(self):
        """
        Simulates a spin of the slot machine.
        
        :return: Result of the spin as a list of symbols
        """
        return [random.choice(self.reel_symbols) for _ in range(3)]

    def buy_bonus(self):
        """
        Allows the player to buy a bonus round if they have enough balance.
        
        :raises ValueError: If the player does not have enough balance to buy a bonus
        """
        if self.balance < self.bonus_cost:
            raise ValueError("Insufficient balance to buy a bonus round.")
        
        self.balance -= self.bonus_cost
        self.bonus_rounds += 1
        print(f"Bonus round purchased! Total bonus rounds: {self.bonus_rounds}")

    def play(self):
        """
        Main method to play the slot machine.
        The player can spin or buy a bonus round.
        """
        while True:
            action = input("Enter 'spin' to play or 'buy' to purchase a bonus round (or 'exit' to quit): ").strip().lower()
            if action == 'spin':
                result = self.spin()
                print(f"Spin result: {result}")
                # Here you can add logic to determine winnings based on the result
            elif action == 'buy':
                try:
                    self.buy_bonus()
                except ValueError as e:
                    print(e)
            elif action == 'exit':
                print("Thank you for playing!")
                break
            else:
                print("Invalid action. Please enter 'spin', 'buy', or 'exit'.")

if __name__ == "__main__":
    initial_balance = 100  # Starting balance for the player
    slot_machine = SlotMachine(initial_balance)
    slot_machine.play()
```
