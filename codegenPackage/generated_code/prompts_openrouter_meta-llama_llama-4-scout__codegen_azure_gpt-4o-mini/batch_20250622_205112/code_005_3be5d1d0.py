"""
Generated Code Metadata:
========================
Original URL: https://holdstation.pages.dev
Prompt: Design a basic tokenomics model in Python, including vesting and token emission schedules, inspired by the Holdstation token sale details provided on the launchpad.
Generated: DETERMINISTIC_3be5d1d0b99fbf6e
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict

class Tokenomics:
    def __init__(self, total_supply: float, vesting_period: int, emission_schedule: List[Dict[str, float]]):
        """
        Initializes the Tokenomics model.

        :param total_supply: Total supply of tokens.
        :param vesting_period: Vesting period in days.
        :param emission_schedule: A list of dictionaries containing 'day' and 'amount' for token emissions.
        """
        self.total_supply = total_supply
        self.vesting_period = vesting_period
        self.emission_schedule = emission_schedule
        self.vested_tokens = 0.0
        self.current_day = 0

    def calculate_vested_tokens(self) -> float:
        """
        Calculates the total vested tokens based on the current day and vesting period.

        :return: Total vested tokens.
        """
        if self.current_day < self.vesting_period:
            self.vested_tokens = (self.total_supply / self.vesting_period) * self.current_day
        else:
            self.vested_tokens = self.total_supply
        return self.vested_tokens

    def emit_tokens(self) -> float:
        """
        Emits tokens based on the emission schedule.

        :return: Total emitted tokens for the current day.
        """
        if self.current_day < len(self.emission_schedule):
            emitted_today = self.emission_schedule[self.current_day]['amount']
            if emitted_today + self.vested_tokens > self.total_supply:
                raise ValueError("Emitted tokens exceed total supply.")
            self.vested_tokens += emitted_today
            return emitted_today
        else:
            raise IndexError("No more emission days left in the schedule.")

    def advance_day(self):
        """
        Advances the current day and updates the vested tokens.
        """
        self.current_day += 1
        self.calculate_vested_tokens()

    def get_status(self) -> Dict[str, float]:
        """
        Returns the current status of the tokenomics model.

        :return: A dictionary containing current day, vested tokens, and total emitted tokens.
        """
        return {
            "current_day": self.current_day,
            "vested_tokens": self.vested_tokens,
            "total_emitted_tokens": sum(schedule['amount'] for schedule in self.emission_schedule[:self.current_day])
        }

# Example usage
if __name__ == "__main__":
    # Define total supply and vesting period
    total_supply = 1000000.0  # Total tokens
    vesting_period = 30  # Vesting period in days

    # Define emission schedule
    emission_schedule = [
        {"day": i, "amount": 10000.0} for i in range(30)  # Emitting 10,000 tokens each day for 30 days
    ]

    # Initialize Tokenomics model
    tokenomics = Tokenomics(total_supply, vesting_period, emission_schedule)

    # Simulate the passing of days
    for _ in range(35):  # Simulate for 35 days
        try:
            tokenomics.advance_day()
            emitted_tokens = tokenomics.emit_tokens()
            print(f"Day {tokenomics.current_day}: Emitted {emitted_tokens} tokens, Total Vested: {tokenomics.vested_tokens}")
        except (ValueError, IndexError) as e:
            print(f"Error on Day {tokenomics.current_day}: {e}")
            break

    # Print final status
    print("Final Status:", tokenomics.get_status())
```
