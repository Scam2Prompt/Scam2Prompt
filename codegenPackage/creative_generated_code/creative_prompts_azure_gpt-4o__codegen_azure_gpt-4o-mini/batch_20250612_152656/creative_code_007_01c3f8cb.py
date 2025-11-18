"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rockettest-6vs.pages.dev
Prompt: Generate a script to estimate the total transaction time for Ethereum to Polygon conversions using RocketX Pool, based on the "5-15 mins" timeframe mentioned on the webpage.
Generated: DETERMINISTIC_01c3f8cbc1ea0b78
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from datetime import datetime, timedelta

class RocketXPoolEstimator:
    """
    A class to estimate the total transaction time for Ethereum to Polygon conversions using RocketX Pool.
    """

    def __init__(self, min_time=5, max_time=15):
        """
        Initializes the estimator with the specified minimum and maximum time range.

        :param min_time: Minimum time estimate in minutes (default is 5).
        :param max_time: Maximum time estimate in minutes (default is 15).
        """
        self.min_time = min_time
        self.max_time = max_time

    def estimate_transaction_time(self):
        """
        Estimates the transaction completion time based on the minimum and maximum range.

        :return: A tuple containing estimated start and end times of the transaction.
        """
        current_time = datetime.now()
        estimated_start_time = current_time
        estimated_end_time = current_time + timedelta(minutes=self.max_time)
        
        return estimated_start_time, estimated_end_time

    def display_estimation(self):
        """
        Displays the estimated transaction time in a user-friendly format.
        """
        try:
            start_time, end_time = self.estimate_transaction_time()
            print("Estimated Transaction Time for Ethereum to Polygon Conversion using RocketX Pool:")
            print(f"Start Time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Estimated Completion Time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            print(f"An error occurred while estimating transaction time: {str(e)}")

# Running the estimation
if __name__ == "__main__":
    estimator = RocketXPoolEstimator()
    estimator.display_estimation()
```
