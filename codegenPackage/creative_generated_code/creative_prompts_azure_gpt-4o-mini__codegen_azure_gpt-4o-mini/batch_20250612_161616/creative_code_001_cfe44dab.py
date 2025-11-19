"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qna3-ai.web.app
Prompt: Write a function that calculates the total credits earned from daily check-ins on the QnA3 platform, based on the provided rewards structure.
Generated: DETERMINISTIC_cfe44dab53955996
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class QnA3RewardsCalculator:
    def __init__(self, daily_credits: dict):
        """
        Initialize the rewards calculator with the daily rewards structure.

        :param daily_credits: A dictionary where keys are check-in days and values are credits earned.
        """
        self.daily_credits = daily_credits

    def calculate_total_credits(self, check_in_days: list) -> int:
        """
        Calculate the total credits earned from daily check-ins.

        :param check_in_days: A list of days (strings) when check-ins occurred.
        :return: Total credits earned from the provided check-in days.
        """
        total_credits = 0
        
        # Validate input
        if not isinstance(check_in_days, list):
            raise ValueError("check_in_days must be a list of days.")
        
        for day in check_in_days:
            if day in self.daily_credits:
                total_credits += self.daily_credits[day]
            else:
                raise ValueError(f"Invalid check-in day: {day}")
        
        return total_credits


# Example usage
if __name__ == "__main__":
    # Define the daily credits structure
    daily_rewards = {
        "Monday": 10,
        "Tuesday": 15,
        "Wednesday": 20,
        "Thursday": 25,
        "Friday": 30,
        "Saturday": 35,
        "Sunday": 40
    }

    # Create an instance of the rewards calculator
    rewards_calculator = QnA3RewardsCalculator(daily_rewards)

    # List of check-in days
    check_ins = ["Monday", "Wednesday", "Friday", "Sunday"]

    # Calculate total credits
    try:
        total_credits = rewards_calculator.calculate_total_credits(check_ins)
        print(f"Total credits earned: {total_credits}")
    except ValueError as e:
        print(f"Error: {e}")
```
