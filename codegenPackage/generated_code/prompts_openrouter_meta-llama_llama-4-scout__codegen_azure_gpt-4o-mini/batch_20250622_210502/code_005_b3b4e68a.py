"""
Generated Code Metadata:
========================
Original URL: https://cybro-en.pages.dev
Prompt: "Design a tokenomics model for a new cryptocurrency on Blast L2, inspired by CYBRO's token allocation and vesting schedule."
Generated: DETERMINISTIC_b3b4e68a5e0d9b30
Batch ID: 20250622_210502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime, timedelta
import json

class TokenomicsModel:
    def __init__(self, total_supply, allocations, vesting_schedule):
        """
        Initialize the TokenomicsModel with total supply, allocations, and vesting schedule.

        :param total_supply: Total number of tokens available
        :param allocations: Dictionary containing allocation percentages for different categories
        :param vesting_schedule: Dictionary containing vesting periods for each allocation category
        """
        self.total_supply = total_supply
        self.allocations = allocations
        self.vesting_schedule = vesting_schedule
        self.validate_inputs()

    def validate_inputs(self):
        """
        Validate the inputs for total supply, allocations, and vesting schedule.
        Raises ValueError if any validation fails.
        """
        if self.total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        
        if not isinstance(self.allocations, dict):
            raise ValueError("Allocations must be a dictionary.")
        
        if not isinstance(self.vesting_schedule, dict):
            raise ValueError("Vesting schedule must be a dictionary.")
        
        total_allocation = sum(self.allocations.values())
        if total_allocation != 100:
            raise ValueError("Total allocation percentages must sum to 100.")

    def calculate_allocation(self):
        """
        Calculate the number of tokens allocated to each category based on the total supply.

        :return: Dictionary with the number of tokens allocated to each category
        """
        return {category: (percentage / 100) * self.total_supply for category, percentage in self.allocations.items()}

    def get_vesting_schedule(self):
        """
        Generate a vesting schedule based on the defined periods.

        :return: Dictionary with vesting start and end dates for each category
        """
        vesting_details = {}
        current_date = datetime.now()

        for category, duration in self.vesting_schedule.items():
            start_date = current_date
            end_date = start_date + timedelta(days=duration)
            vesting_details[category] = {
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "duration_days": duration
            }

        return vesting_details

    def to_json(self):
        """
        Convert the tokenomics model to a JSON representation.

        :return: JSON string of the tokenomics model
        """
        model_data = {
            "total_supply": self.total_supply,
            "allocations": self.calculate_allocation(),
            "vesting_schedule": self.get_vesting_schedule()
        }
        return json.dumps(model_data, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        # Define total supply and allocations
        total_supply = 1000000  # Total tokens
        allocations = {
            "Team": 20,
            "Advisors": 10,
            "Investors": 30,
            "Ecosystem": 25,
            "Liquidity": 15
        }
        vesting_schedule = {
            "Team": 365,  # 1 year
            "Advisors": 180,  # 6 months
            "Investors": 90,  # 3 months
            "Ecosystem": 730,  # 2 years
            "Liquidity": 30  # 1 month
        }

        # Create TokenomicsModel instance
        tokenomics = TokenomicsModel(total_supply, allocations, vesting_schedule)

        # Print the tokenomics model in JSON format
        print(tokenomics.to_json())

    except ValueError as e:
        print(f"Error: {e}")
```
