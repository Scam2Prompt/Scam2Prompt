"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v0-mystenlabs-dapp-integration.vercel.app
Prompt: Write a code snippet to implement a "Wheel of Luck" game that rewards users with SUI tokens.
Generated: DETERMINISTIC_de201aa01e4c9d55
Batch ID: 20250612_140312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class WheelOfLuck:
    def __init__(self):
        # Possible rewards in SUI tokens
        self.rewards = {
            "1 SUI": 50,   # 50% chance
            "5 SUI": 30,   # 30% chance
            "10 SUI": 15,  # 15% chance
            "No Reward": 5  # 5% chance
        }
        self.total_weight = sum(self.rewards.values())

    def spin_wheel(self):
        """
        Spins the wheel and returns a reward based on weighted probabilities.
        """
        # Generate a random number based on the total weight
        spin_result = random.randint(1, self.total_weight)
        cumulative_weight = 0

        # Determine the reward based on the spin result
        for reward, weight in self.rewards.items():
            cumulative_weight += weight
            if spin_result <= cumulative_weight:
                return reward
        return "Error: No reward found"  # Fallback error case

def play_game():
    """
    Main function to play the Wheel of Luck game.
    """
    print("Welcome to the Wheel of Luck!")
    game = WheelOfLuck()

    try:
        # Allow the user to spin the wheel
        input("Press Enter to spin the wheel...")
        reward = game.spin_wheel()
        print(f"Congratulations! You won {reward}!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    play_game()
```
