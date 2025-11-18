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
    def __init__(self):
        """Initializes the bet adjustment system with predefined bet steps."""
        self.bet_steps = [5, 10, 20]  # Bet adjustment steps
        self.current_bet_index = 0     # Index to track the current bet step

    def get_current_bet(self):
        """Returns the current bet amount based on the bet steps."""
        return self.bet_steps[self.current_bet_index]

    def adjust_bet(self, win: bool):
        """
        Adjusts the bet amount based on the outcome of the previous bet.
        
        Parameters:
        win (bool): True if the previous bet was a win, False otherwise.
        """
        if win:
            # If the bet was won, move to the next higher bet step
            if self.current_bet_index < len(self.bet_steps) - 1:
                self.current_bet_index += 1
        else:
            # If the bet was lost, reset to the lowest bet step
            self.current_bet_index = 0

    def reset_bet(self):
        """Resets the bet to the initial step."""
        self.current_bet_index = 0

    def play_round(self):
        """Simulates a round of betting, randomly determining the outcome."""
        import random

        # Simulate a win or loss (50% chance)
        outcome = random.choice([True, False])
        current_bet = self.get_current_bet()

        # Log the bet and outcome
        print(f"Current Bet: {current_bet}, Outcome: {'Win' if outcome else 'Lose'}")
        
        # Adjust the bet based on the outcome
        self.adjust_bet(outcome)

def main():
    """Main function to run the betting system."""
    bet_system = BetAdjustmentSystem()
    
    try:
        rounds = 10  # Number of rounds to play
        for _ in range(rounds):
            bet_system.play_round()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
