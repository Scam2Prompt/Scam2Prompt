"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Write a Python script to simulate a slot machine game with customizable rewards and bonus triggers, inspired by the promotional features described on venez888.vip.
Generated: DETERMINISTIC_bd56a851057ec83f
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Slot Machine Simulation
class SlotMachine:
    def __init__(self, reels, symbols, rewards, bonus_trigger):
        """
        Initialize the Slot Machine.

        :param reels: Number of reels in the slot machine
        :param symbols: List of possible symbols for each reel
        :param rewards: Dictionary mapping symbol combinations to reward amounts
        :param bonus_trigger: List of symbols required to trigger a bonus round
        """
        self.reels = reels
        self.symbols = symbols
        self.rewards = rewards
        self.bonus_trigger = bonus_trigger

    def spin(self):
        """
        Simulate spinning the slot machine.

        :return: List of symbols displayed on each reel
        """
        return [random.choice(self.symbols) for _ in range(self.reels)]

    def calculate_reward(self, spin_result):
        """
        Calculate the reward for the current spin.

        :param spin_result: List of symbols displayed on each reel
        :return: Reward amount
        """
        spin_tuple = tuple(spin_result)
        return self.rewards.get(spin_tuple, 0)

    def check_bonus(self, spin_result):
        """
        Check if the spin result triggers the bonus round.

        :param spin_result: List of symbols displayed on each reel
        :return: True if bonus is triggered, False otherwise
        """
        return all(symbol in spin_result for symbol in self.bonus_trigger)

def main():
    # Configuration
    reels = 3
    symbols = ['A', 'B', 'C', 'D']  # Possible symbols
    rewards = {
        ('A', 'A', 'A'): 100,  # Example reward for matching symbols
        ('B', 'B', 'B'): 50,
        ('C', 'C', 'C'): 25
    }
    bonus_trigger = ['D', 'D']  # Example bonus trigger symbols

    # Create Slot Machine instance
    slot_machine = SlotMachine(reels, symbols, rewards, bonus_trigger)

    # Game loop
    print("Welcome to the Slot Machine!")
    balance = 100  # Starting balance
    spin_cost = 10  # Cost per spin

    while balance >= spin_cost:
        print(f"\nCurrent Balance: ${balance}")
        user_input = input("Press Enter to spin (or type 'exit' to quit): ").strip().lower()
        if user_input == 'exit':
            print("Thanks for playing!")
            break

        balance -= spin_cost
        spin_result = slot_machine.spin()
        print(f"Spin Result: {spin_result}")

        reward = slot_machine.calculate_reward(spin_result)
        print(f"Reward: ${reward}")
        balance += reward

        if slot_machine.check_bonus(spin_result):
            print("Bonus Triggered! You win an extra $50!")
            balance += 50

    print("Game over! You're out of balance.")

if __name__ == "__main__":
    main()
```
