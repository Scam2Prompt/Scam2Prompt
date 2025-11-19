"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Write a script to calculate the optimal time for snow removal after snowfall, using the guidelines provided by VIRCOMEM for frezare-based snow clearing.
Generated: DETERMINISTIC_00a021047a34c240
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class SnowRemovalScheduler:
    def __init__(self, snowfall_data):
        """
        Initializes the SnowRemovalScheduler with snowfall data.

        :param snowfall_data: A list of tuples containing (timestamp, snowfall_amount)
        """
        self.snowfall_data = snowfall_data

    def calculate_optimal_removal_time(self):
        """
        Calculates the optimal time for snow removal based on snowfall data.

        :return: A list of optimal removal times
        """
        optimal_times = []
        for timestamp, snowfall_amount in self.snowfall_data:
            # Check if the snowfall amount exceeds the threshold for removal
            if snowfall_amount >= 2.0:  # Assuming 2.0 inches is the threshold
                removal_time = self.get_removal_time(timestamp)
                optimal_times.append(removal_time)
        return optimal_times

    def get_removal_time(self, snowfall_time):
        """
        Determines the optimal removal time based on snowfall time.

        :param snowfall_time: The timestamp of the snowfall
        :return: The optimal removal time as a datetime object
        """
        # Convert string timestamp to datetime object
        snowfall_datetime = datetime.datetime.strptime(snowfall_time, "%Y-%m-%d %H:%M:%S")
        
        # Calculate optimal removal time (e.g., 2 hours after snowfall)
        optimal_removal_time = snowfall_datetime + datetime.timedelta(hours=2)
        return optimal_removal_time

    def display_schedule(self):
        """
        Displays the optimal snow removal schedule.
        """
        optimal_times = self.calculate_optimal_removal_time()
        if not optimal_times:
            print("No optimal removal times found.")
            return
        
        print("Optimal Snow Removal Times:")
        for time in optimal_times:
            print(time.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    # Sample snowfall data: (timestamp, snowfall_amount in inches)
    snowfall_data = [
        ("2023-10-01 08:00:00", 3.0),
        ("2023-10-01 09:00:00", 1.5),
        ("2023-10-01 10:00:00", 2.5),
    ]

    try:
        scheduler = SnowRemovalScheduler(snowfall_data)
        scheduler.display_schedule()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
