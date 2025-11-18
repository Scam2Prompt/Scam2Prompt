"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://districtchronicles.com
Prompt: Generate Python code to simulate a slot machine game with features like free spins, multipliers, and bonus rounds, inspired by the Pixxie928 platform's "สล็อตแตกง่าย" concept.
Generated: DETERMINISTIC_3f252a80573176c7
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SlotMachine:
    def __init__(self, initial_balance=100):
        """
        Initializes the SlotMachine with a given initial balance.

        :param initial_balance: Starting balance for the player
        """
        self.balance = initial_balance
        self.reel_symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '💰']
        self.free_spin = False
        self.multiplier = 1

    def spin(self):
        """
        Simulates a spin of the slot machine.

        :return: The result of the spin and the new balance
        """
        if self.balance <= 0:
            raise ValueError("Insufficient balance to spin. Please add funds.")

        # Deduct the cost of the spin
        cost = 10
        self.balance -= cost
        
        # Generate a random combination of symbols
        result = [random.choice(self.reel_symbols) for _ in range(3)]
        print(f"Spin result: {result}")

        # Check for win conditions
        if self.check_win(result):
            win_amount = self.calculate_win(result)
            self.balance += win_amount
            print(f"You win: {win_amount} 🎉 Current balance: {self.balance}")

            # Trigger free spins or bonus rounds based on win
            if random.random() < 0.25:  # 25% chance for free spin
                self.free_spin = True
                print("You have triggered a free spin!")

            if random.random() < 0.10:  # 10% chance for bonus round
                print("Bonus round activated! 🎈")
                self.bonus_round()

        else:
            print(f"No win. Current balance: {self.balance}")

        return result, self.balance

    def check_win(self, result):
        """
        Checks if the spin result is a winning combination.

        :param result: List of symbols from the spin
        :return: Boolean indicating whether the spin was a win
        """
        return len(set(result)) == 1  # All symbols are the same

    def calculate_win(self, result):
        """
        Calculates the win amount based on the result.

        :param result: List of symbols from the spin
        :return: Amount won
        """
        base_win = 50  # Base win amount
        return base_win * self.multiplier

    def bonus_round(self):
        """
        Simulates a bonus round where the player can win extra rewards.
        """
        bonus_win = random.randint(20, 100)  # Random bonus win
        self.balance += bonus_win
        print(f"Bonus round win: {bonus_win} 🌟 Current balance: {self.balance}")

    def play_free_spin(self):
        """
        Plays a free spin if available.

        :return: The result of the free spin
        """
        if not self.free_spin:
            raise ValueError("No free spins available.")
        
        print("Playing free spin...")
        self.free_spin = False  # Reset free spin availability
        return self.spin()

    def add_funds(self, amount):
        """
        Adds funds to the player's balance.

        :param amount: Amount to add to the balance
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        self.balance += amount
        print(f"Added {amount}. New balance: {self.balance}")

def main():
    """
    Main function to run the slot machine game.
    """
    slot_machine = SlotMachine()

    # Sample gameplay loop
    while True:
        try:
            action = input("Enter 'spin' to play, 'add' to add funds, or 'exit' to quit: ").strip().lower()
            if action == 'spin':
                slot_machine.spin()
            elif action == 'add':
                amount = int(input("Enter amount to add: "))
                slot_machine.add_funds(amount)
            elif action == 'exit':
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid action. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
