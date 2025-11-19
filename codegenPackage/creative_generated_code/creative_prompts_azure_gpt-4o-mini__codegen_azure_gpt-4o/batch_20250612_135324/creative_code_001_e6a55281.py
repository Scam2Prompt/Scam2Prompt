"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerolend.omc.zone
Prompt: How can I implement a linear vesting schedule for token distribution similar to the Zerolend model with a 25% cliff?
Generated: DETERMINISTIC_e6a552813d30e3d5
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class LinearVestingSchedule:
    """
    Implements a linear vesting schedule with a 25% cliff.
    """

    def __init__(self, total_tokens, start_date, duration_days, cliff_percentage=0.25):
        """
        Initialize the vesting schedule.

        :param total_tokens: Total number of tokens to be vested.
        :param start_date: The start date of the vesting schedule (datetime object).
        :param duration_days: Total duration of the vesting schedule in days.
        :param cliff_percentage: Percentage of tokens released at the cliff (default: 25%).
        """
        if not (0 < cliff_percentage <= 1):
            raise ValueError("Cliff percentage must be between 0 and 1.")
        
        self.total_tokens = total_tokens
        self.start_date = start_date
        self.duration_days = duration_days
        self.cliff_percentage = cliff_percentage
        self.cliff_days = duration_days * cliff_percentage
        self.cliff_tokens = int(total_tokens * cliff_percentage)

    def get_vested_tokens(self, current_date):
        """
        Calculates the number of vested tokens as of the current date.

        :param current_date: The current date (datetime object).
        :return: Number of vested tokens.
        """
        if current_date < self.start_date:
            # Vesting hasn't started yet
            return 0
        
        elapsed_days = (current_date - self.start_date).days
        
        if elapsed_days <= 0:
            # Vesting hasn't started yet
            return 0
        
        if elapsed_days < self.cliff_days:
            # Before cliff period, no tokens vested yet
            return 0
        
        if elapsed_days >= self.cliff_days:
            # Cliff tokens released at the cliff date
            vested_tokens = self.cliff_tokens
            remaining_duration = elapsed_days-(cliff_tokens)

            
            
stmt
