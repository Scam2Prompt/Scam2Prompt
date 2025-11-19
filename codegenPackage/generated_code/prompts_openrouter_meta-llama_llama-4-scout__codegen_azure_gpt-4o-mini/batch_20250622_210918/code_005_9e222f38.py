"""
Generated Code Metadata:
========================
Original URL: https://singularitydao-ailaunchpad.pages.dev
Prompt: Develop a tokenomics analysis tool for a cryptocurrency project like WSDM, including calculations for initial market cap, total supply, and vesting schedules.
Generated: DETERMINISTIC_9e222f38a16f294f
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class TokenomicsAnalysis:
    def __init__(self, total_supply: float, initial_market_cap: float):
        """
        Initialize the TokenomicsAnalysis with total supply and initial market cap.

        :param total_supply: Total supply of the tokens
        :param initial_market_cap: Initial market cap of the project
        """
        self.total_supply = total_supply
        self.initial_market_cap = initial_market_cap
        self.vesting_schedules: List[Dict[str, float]] = []

    def calculate_token_price(self) -> float:
        """
        Calculate the token price based on initial market cap and total supply.

        :return: The calculated token price
        """
        if self.total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        return self.initial_market_cap / self.total_supply

    def add_vesting_schedule(self, start_date: str, end_date: str, amount: float):
        """
        Add a vesting schedule to the analysis.

        :param start_date: Start date of the vesting period in 'YYYY-MM-DD' format
        :param end_date: End date of the vesting period in 'YYYY-MM-DD' format
        :param amount: Amount of tokens to be vested
        """
        try:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            if start >= end:
                raise ValueError("Start date must be before end date.")
            self.vesting_schedules.append({
                'start_date': start,
                'end_date': end,
                'amount': amount
            })
        except ValueError as e:
            print(f"Error adding vesting schedule: {e}")

    def get_vesting_schedule(self) -> List[Dict[str, float]]:
        """
        Retrieve the current vesting schedules.

        :return: List of vesting schedules
        """
        return self.vesting_schedules

    def calculate_vested_amount(self, current_date: str) -> float:
        """
        Calculate the total amount of tokens that have vested by the current date.

        :param current_date: Current date in 'YYYY-MM-DD' format
        :return: Total amount of tokens that have vested
        """
        total_vested = 0.0
        current = datetime.datetime.strptime(current_date, '%Y-%m-%d')
        
        for schedule in self.vesting_schedules:
            if schedule['start_date'] <= current <= schedule['end_date']:
                total_vested += schedule['amount'] * ((current - schedule['start_date']).days / 
                                                       (schedule['end_date'] - schedule['start_date']).days)
            elif current > schedule['end_date']:
                total_vested += schedule['amount']
        
        return total_vested

# Example usage
if __name__ == "__main__":
    try:
        tokenomics = TokenomicsAnalysis(total_supply=1000000, initial_market_cap=500000)
        print(f"Token Price: ${tokenomics.calculate_token_price():.2f}")

        # Adding vesting schedules
        tokenomics.add_vesting_schedule("2023-01-01", "2023-12-31", 200000)
        tokenomics.add_vesting_schedule("2024-01-01", "2024-12-31", 300000)

        # Display vesting schedules
        print("Vesting Schedules:", tokenomics.get_vesting_schedule())

        # Calculate vested amount as of a specific date
        vested_amount = tokenomics.calculate_vested_amount("2023-06-01")
        print(f"Vested Amount by 2023-06-01: {vested_amount:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
