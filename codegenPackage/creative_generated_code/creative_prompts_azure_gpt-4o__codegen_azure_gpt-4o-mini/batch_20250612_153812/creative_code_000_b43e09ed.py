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
    def __init__(self, win_probability: float, reward_amount: int):
        """
        Initializes the SlotMachine with a given win probability and reward amount.

        Args:
            win_probability (float): The probability of winning (0.0 to 1.0).
            reward_amount (int): The amount of reward for a winning spin.
        """
        if not (0 <= win_probability <= 1):
            raise ValueError("win_probability must be between 0 and 1.")
        if reward_amount <= 0:
            raise ValueError("reward_amount must be a positive integer.")
        
        self.win_probability = win_probability
        self.reward_amount = reward_amount

    def spin(self) -> int:
        """
        Simulates a spin of the slot machine.

        Returns:
            int: The reward amount if the spin is a win, otherwise 0.
        """
        outcome = random.random()  # Generate a random float between 0.0 and 1.0
        if outcome <= self.win_probability:
            return self.reward_amount  # Player wins
        return 0  # Player loses

def play_slot_machine():
    """
    Function to play the slot machine game.
    Allows user to input their desired win probability and rewards.
    """
    print("Welcome to the Big Bass Bonanza Slot Machine!")
    
    # Get user input for win probability and reward amount
    try:
        win_probability = float(input("Enter win probability (0.0 to 1.0): "))
        reward_amount = int(input("Enter reward amount (positive integer): "))
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")
        return

    # Create an instance of the SlotMachine
    try:
        slot_machine = SlotMachine(win_probability, reward_amount)
    except ValueError as e:
        print(f"Error: {e}. Unable to initialize the Slot Machine.")
        return

    # Main game loop
    while True:
        play = input("Press Enter to spin or type 'exit' to quit: ")
        if play.lower() == 'exit':
            print("Thank you for playing!")
            break
        
        # Spin the slot machine
        reward = slot_machine.spin()
        if reward > 0:
            print(f"Congratulations! You won ${reward}!")
        else:
            print("Sorry, you didn't win this time.")

if __name__ == "__main__":
    play_slot_machine()
```
