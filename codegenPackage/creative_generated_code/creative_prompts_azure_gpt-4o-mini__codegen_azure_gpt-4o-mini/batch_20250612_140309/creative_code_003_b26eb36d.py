"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-jup.pages.dev
Prompt: Create a function that calculates the voting power based on the amount of locked JUP tokens and the countdown period.
Generated: DETERMINISTIC_b26eb36dd9410d42
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VotingPowerCalculator:
    def __init__(self, locked_tokens: float, countdown_period: int):
        """
        Initializes the VotingPowerCalculator with locked tokens and countdown period.

        :param locked_tokens: The amount of locked JUP tokens (must be non-negative).
        :param countdown_period: The countdown period in seconds (must be positive).
        """
        self.locked_tokens = locked_tokens
        self.countdown_period = countdown_period

        self.validate_input()

    def validate_input(self):
        """
        Validates the input parameters for locked tokens and countdown period.
        Raises ValueError if the parameters are invalid.
        """
        if self.locked_tokens < 0:
            raise ValueError("Locked tokens must be non-negative.")
        if self.countdown_period <= 0:
            raise ValueError("Countdown period must be positive.")

    def calculate_voting_power(self) -> float:
        """
        Calculates the voting power based on locked tokens and countdown period.

        :return: The calculated voting power as a float.
        """
        # Example formula: voting power is proportional to locked tokens and inversely proportional to the countdown period
        if self.countdown_period == 0:
            raise ZeroDivisionError("Countdown period cannot be zero.")
        
        voting_power = self.locked_tokens / self.countdown_period
        return voting_power

# Example Usage
if __name__ == "__main__":
    try:
        # Create an instance of VotingPowerCalculator
        locked_tokens = 1000.0  # example locked tokens
        countdown_period = 3600  # example countdown period in seconds (1 hour)

        calculator = VotingPowerCalculator(locked_tokens, countdown_period)
        power = calculator.calculate_voting_power()
        print(f"Voting Power: {power:.2f}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
```
