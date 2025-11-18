"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethclaim.pages.dev
Prompt: Develop a script to track and display the remaining program duration for the stETH Rewards Pool and calculate the total rewards distributed so far.
Generated: DETERMINISTIC_b05c7338c9a8de97
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class StETHRewardsPoolTracker:
    def __init__(self, start_date, end_date, total_rewards, rewards_per_second):
        """
        Initialize the tracker with the given parameters.

        :param start_date: Pool start date as a string in 'YYYY-MM-DD' format.
        :param end_date: Pool end date as a string in 'YYYY-MM-DD' format.
        :param total_rewards: Total rewards distributed over the program duration.
        :param rewards_per_second: Rewards distributed per second.
        """
        try:
            self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format. Please use 'YYYY-MM-DD'. Error: {e}")
        
        if self.start_date >= self.end_date:
            raise ValueError("The end date must be later than the start date.")
        
        self.total_rewards = total_rewards
        self.rewards_per_second = rewards_per_second
    
    def get_remaining_duration(self):
        """
        Calculate and return the remaining duration of the program.

        :return: Remaining duration as a string in days, hours, minutes, and seconds.
        """
        now = datetime.datetime.now()
        if now > self.end_date:
            return "The rewards pool program has ended."
        
        remaining_time = self.end_date - now
        return str(remaining_time)
    
    def calculate_distributed_rewards(self):
        """
        Calculate the total rewards distributed so far.

        :return: Total rewards distributed so far.
        """
        now = datetime.datetime.now()
        
        if now <= self.start_date:
            return 0  # No rewards distributed yet.
        elif now >= self.end_date:
            return self.total_rewards  # All rewards distributed.
        else:
            elapsed_seconds = (now - self.start_date).total_seconds()
            distributed_rewards = elapsed_seconds * self.rewards_per_second
            return round(distributed_rewards, 2)  # Rounded to two decimal places.
    
    def display_status(self):
        """
        Display the remaining program duration and total rewards distributed so far.

        :return: None
        """
        remaining_duration = self.get_remaining_duration()
        distributed_rewards = self.calculate_distributed_rewards()
        
        print(f"Remaining Program Duration: {remaining_duration}")
        print(f"Total Rewards Distributed So Far: {distributed_rewards}")


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the tracker with sample data
        start_date = "2023-01-01"
        end_date = "2023-12-31"
        total_rewards = 1000000  # 1,000,000 stETH distributed in total
        rewards_per_second = total_rewards / ((datetime.datetime.strptime(end_date, '%Y-%m-%d') - datetime.datetime.strptime(start_date, '%Y-%m-%d')).total_seconds())

        tracker = StETHRewardsPoolTracker(start_date, end_date, total_rewards, rewards_per_second)
        tracker.display_status()

    except Exception as e:
        print(f"An error occurred: {e}")
```
