"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aspjj.com
Prompt: "Generate code to implement a step-by-step bet adjustment system (e.g., 5-10-20 units) for a slot game, similar to the techniques described on สล็อตเว็บตรง."
Generated: DETERMINISTIC_8b8618c8b98c4d2a
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BetAdjustmentSystem:
    """
    A class to manage a step-by-step bet adjustment system for a slot game.
    The system allows players to increase or decrease their bet based on predefined steps.
    """
    
    def __init__(self, bet_steps):
        """
        Initialize the BetAdjustmentSystem with a list of valid bet steps.

        :param bet_steps: A list of integers representing the possible bet amounts (e.g., [5, 10, 20]).
        """
        if not bet_steps or not all(isinstance(step, int) and step > 0 for step in bet_steps):
            raise ValueError("bet_steps must be a list of positive integers.")
        
        # Sort the steps to ensure ascending order
        self.bet_steps = sorted(bet_steps)
        self.current_index = 0  # Start with the smallest bet

    def increase_bet(self):
        """
        Increase the bet to the next step, if possible.
        """
        if self.current_index < len(self.bet_steps) - 1:
            self.current_index += 1
            return self.bet_steps[self.current_index]
        else:
            # Already at the maximum bet
            return self.bet_steps[self.current_index]

    def decrease_bet(self):
        """
        Decrease the bet to the previous step, if possible.
        """
        if self.current_index > 0:
            self.current_index -= 1
            return self.bet_steps[self.current_index]
        else:
            # Already at the minimum bet
            return self.bet_steps[self.current_index]

    def get_current_bet(self):
        """
        Get the current bet amount.

        :return: The current bet amount.
        """
        return self.bet_steps[self.current_index]


# Example usage:
if __name__ == "__main__":
    try:
        # Define the bet steps
        bet_steps = [5, 10, 20]

        # Initialize the system
        bet_system = BetAdjustmentSystem(bet_steps)

        # Display the initial bet
        print(f"Initial Bet: {bet_system.get_current_bet()}")

        # Increase the bet step-by-step
        print(f"Increased Bet: {bet_system.increase_bet()}")
        print(f"Increased Bet: {bet_system.increase_bet()}")

        # Attempt to go beyond the maximum
        print(f"Increased Bet (Max): {bet_system.increase_bet()}")

        # Decrease the bet step-by-step
        print(f"Decreased Bet: {bet_system.decrease_bet()}")
        print(f"Decreased Bet: {bet_system.decrease_bet()}")

        # Attempt to go below the minimum
        print(f"Decreased Bet (Min): {bet_system.decrease_bet()}")
    except ValueError as e:
        print(f"Error: {e}")
```
