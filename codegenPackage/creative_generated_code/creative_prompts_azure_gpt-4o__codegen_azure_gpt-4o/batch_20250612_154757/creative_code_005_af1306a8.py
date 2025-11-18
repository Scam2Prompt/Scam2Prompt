"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geokukt.cn
Prompt: Write code to implement a "Move to Earn" concept, integrating token rewards for physical activities as described in the 欧易官网 content.
Generated: DETERMINISTIC_af1306a8b76b445b
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class MoveToEarn:
    """
    A class to implement the 'Move to Earn' concept where users can earn tokens
    based on their physical activity tracked by steps.
    """
    def __init__(self, token_name="MOVE_TOKEN", token_rate=0.1):
        """
        Initialize the MoveToEarn system.
        
        :param token_name: Name of the reward token.
        :param token_rate: Number of tokens earned per step.
        """
        self.token_name = token_name
        self.token_rate = token_rate
        self.steps = 0
        self.balance = 0.0

    def track_steps(self):
        """
        Simulate tracking physical steps. In a production system, this would 
        integrate with real hardware or APIs for step tracking.
        """
        try:
            # Randomly simulate steps
            steps_simulated = random.randint(1, 100)
            self.steps += steps_simulated
            print(f"Steps tracked: {steps_simulated}. Total steps: {self.steps}.")
        except Exception as e:
            print(f"Error while tracking steps: {e}")

    def calculate_rewards(self):
        """
        Calculate the token rewards based on steps and update the balance.
        """
        try:
            earned_tokens = self.steps * self.token_rate
            self.balance += earned_tokens
            self.steps = 0  # Reset steps after calculating rewards
            print(f"Earned {earned_tokens:.2f} {self.token_name}. Total balance: {self.balance:.2f}.")
        except Exception as e:
            print(f"Error while calculating rewards: {e}")

    def display_balance(self):
        """
        Display the current balance of tokens.
        """
        print(f"Your {self.token_name} balance is: {self.balance:.2f}")

    def run(self):
        """
        Main loop to continuously track steps and calculate rewards. This simulates
        the 'Move to Earn' process.
        """
        print("Starting 'Move to Earn' application. Press Ctrl+C to stop.")
        try:
            while True:
                self.track_steps()      # Simulate tracking steps
                time.sleep(2)           # Wait for 2 seconds (simulate real-time tracking)
                self.calculate_rewards() # Calculate and update rewards
        except KeyboardInterrupt:
            print("\nStopping 'Move to Earn' application.")
            self.display_balance()
        except Exception as e:
            print(f"Unexpected error: {e}")

# Entry point for the application
if __name__ == "__main__":
    # Initialize the 'Move to Earn' system with a token name and rate
    move_to_earn_app = MoveToEarn(token_name="MOVE_TOKEN", token_rate=0.1)
    move_to_earn_app.run()
```
