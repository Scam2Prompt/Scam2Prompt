"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-etuktuk-io.pages.dev
Prompt: Develop a script to track the reward unlocking schedule for $TUK tokens on the eTukTuk staking platform, displaying rewards by month from Sep-23 to Jan-26.
Generated: DETERMINISTIC_e29b2c96a18ced0c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class RewardSchedule:
    def __init__(self, start_date: str, end_date: str, monthly_reward: float):
        """
        Initialize the RewardSchedule with start and end dates and a monthly reward amount.

        :param start_date: The start date in 'YYYY-MM-DD' format.
        :param end_date: The end date in 'YYYY-MM-DD' format.
        :param monthly_reward: Reward amount unlocked each month.
        """
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        self.monthly_reward = monthly_reward

        # Validate the dates
        if self.start_date >= self.end_date:
            raise ValueError("Start date must be earlier than end date.")

    def generate_schedule(self) -> List[Dict[str, float]]:
        """
        Generate the reward unlocking schedule by month.

        :return: A list of dictionaries containing month and corresponding unlocked rewards.
        """
        schedule = []
        current_date = self.start_date

        while current_date <= self.end_date:
            month_year = current_date.strftime("%b-%y")
            schedule.append({
                "month_year": month_year,
                "reward": self.monthly_reward
            })
            # Move to the next month
            current_date += datetime.timedelta(days=30)  # Approximation for month increment
            current_date = current_date.replace(day=1)  # Reset day to the first of the month
        
        return schedule

    def display_schedule(self) -> None:
        """
        Display the reward schedule in a readable format.
        """
        schedule = self.generate_schedule()
        print(f"Reward Schedule from {self.start_date.strftime('%b %Y')} to {self.end_date.strftime('%b %Y')}:")
        print("Month-Year | Reward")
        print("---------------------")
        for entry in schedule:
            print(f"{entry['month_year']} | ${entry['reward']:.2f}")

if __name__ == "__main__":
    try:
        # Define the parameters for the reward unlocking schedule
        start_date = "2023-09-01"
        end_date = "2026-01-31"
        monthly_reward = 100.0  # Example monthly reward

        # Create an instance of RewardSchedule
        reward_schedule = RewardSchedule(start_date, end_date, monthly_reward)

        # Display the generated reward schedule
        reward_schedule.display_schedule()
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
