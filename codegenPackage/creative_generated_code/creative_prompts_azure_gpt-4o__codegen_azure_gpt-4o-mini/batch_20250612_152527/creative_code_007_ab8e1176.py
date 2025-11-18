"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-jup.pages.dev
Prompt: Write a function to calculate the diminishing voting power for a wallet unlocking JUP tokens over the 30-day countdown, as described on the Jupiter voting platform.
Generated: DETERMINISTIC_ab8e117683d78002
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class VotingPowerCalculator:
    """
    A class to calculate the diminishing voting power for a wallet unlocking JUP tokens
    over a 30-day countdown period, as described on the Jupiter voting platform.
    """
    
    def __init__(self):
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=30)
    
    def calculate_voting_power(self, unlocked_tokens: float, current_date: datetime) -> float:
        """
        Calculate the diminishing voting power based on the current date.

        Args:
            unlocked_tokens (float): The number of unlocked JUP tokens.
            current_date (datetime): The current date for which to calculate voting power.

        Returns:
            float: The calculated voting power.
        
        Raises:
            ValueError: If unlocked_tokens is negative or if current_date is before start_date or after end_date.
        """
        # Validate parameters
        if unlocked_tokens < 0:
            raise ValueError("Unlocked tokens must be a non-negative value.")
        if current_date < self.start_date or current_date > self.end_date:
            raise ValueError("Current date must be within the 30-day countdown period.")
        
        # Calculate the number of days passed since unlocking
        days_passed = (current_date - self.start_date).days
        
        # Calculate the diminishing factor
        diminishing_factor = max(0, (30 - days_passed) / 30)
        
        # Calculate remaining voting power
        voting_power = unlocked_tokens * diminishing_factor
        
        return voting_power

# Example usage
if __name__ == "__main__":
    calculator = VotingPowerCalculator()
    
    try:
        unlocked_tokens = 1000.0  # Example token amount
        current_date = datetime.now()  # Use current date for demonstration
        power = calculator.calculate_voting_power(unlocked_tokens, current_date)
        print(f"Remaining voting power: {power:.2f} JUP tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
