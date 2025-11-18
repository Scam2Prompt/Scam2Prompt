"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-neurongate.xyz
Prompt: Write Python code to simulate a slot machine game inspired by "Big Bass Bonanza" with adjustable winning probabilities and a rewards system.
Generated: DETERMINISTIC_b43e09edd76c2793
Batch ID: 20250612_153812
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
    """
    A class to simulate a slot machine game inspired by 'Big Bass Bonanza'.
    """
    def __init__(self, winning_probability=0.2):
        """
        Initialize the slot machine with adjustable winning probability.
        
        Parameters:
        winning_probability (float): Probability of winning, between 0 and 1.
        """
        if not (0 <= winning_probability <= 1):
            raise ValueError("Winning probability must be between 0 and 1.")
        self.winning_probability = winning_probability
        self.rewards = {
            "Big Bass": 100,
            "Small Bass": 50,
            "Gold Coin": 20,
            "Silver Coin": 10,
            "Empty": 0
        }
        self.symbols = list(self.rewards.keys())

    def spin(self):
        """
        Simulate a spin of the slot machine.
        
        Returns:
        dict: Result of the spin including the symbol and the reward amount.
        """
        # Determine if the player wins based on the winning probability
        is_winner = random.random() < self.winning_probability
        
        if is_winner:
            # Select a random symbol (excluding "Empty") for a win
            symbol = random.choice(self.symbols[:-1])
        else:
            # Player loses, returns "Empty"
            symbol = "Empty"
        
        # Calculate reward based on the symbol
        reward = self.rewards[symbol]
        return {"symbol": symbol, "reward": reward}

    def play(self):
        """
        Play the slot machine game. Allows the user to spin indefinitely until they quit.
        """
        print("Welcome to the 'Big Bass Bonanza' Slot Machine!")
        print(f"Winning Probability: {self.winning_probability * 100}%")
        print("Type 'spin' to spin the slot machine or 'quit' to exit the game.")
        
        while True:
            user_input = input("Enter your choice (spin/quit): ").strip().lower()
            if user_input == "quit":
                print("Thank you for playing! Goodbye!")
                break
            elif user_input == "spin":
                result = self.spin()
                print(f"Result: {result['symbol']}, Reward: ${result['reward']}")
            else:
                print("Invalid input. Please type 'spin' or 'quit'.")

# Entry point for the program
if __name__ == "__main__":
    try:
        # Create a slot machine instance with a 30% winning probability
        slot_machine = SlotMachine(winning_probability=0.3)
        slot_machine.play()
    except Exception as e:
        print(f"An error occurred: {e}")
```
