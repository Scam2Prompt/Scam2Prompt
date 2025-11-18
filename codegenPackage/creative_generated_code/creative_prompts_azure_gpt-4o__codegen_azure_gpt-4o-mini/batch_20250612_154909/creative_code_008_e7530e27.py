"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigmgroup.co.ug
Prompt: Write code to simulate a "Happy Hour Activation" campaign, similar to the Shell activations described on Paradigm Group's website, including customer engagement tracking.
Generated: DETERMINISTIC_e7530e27144f8bd1
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta

class HappyHourActivation:
    """Class to simulate a Happy Hour Activation campaign."""

    def __init__(self, start_time, duration_minutes, engagement_limit):
        """
        Initializes the Happy Hour Activation campaign.

        Args:
            start_time (datetime): The start time of the happy hour.
            duration_minutes (int): The duration of the happy hour in minutes.
            engagement_limit (int): The maximum number of customer engagements.
        """
        self.start_time = start_time
        self.end_time = start_time + timedelta(minutes=duration_minutes)
        self.engagement_limit = engagement_limit
        self.engagements = []

    def is_active(self):
        """Checks if the happy hour is currently active."""
        now = datetime.now()
        return self.start_time <= now <= self.end_time

    def engage_customer(self, customer_id):
        """
        Simulates customer engagement during the happy hour.

        Args:
            customer_id (str): Unique identifier for the customer.

        Raises:
            Exception: If the happy hour is not active or engagement limit is reached.
        """
        if not self.is_active():
            raise Exception("Happy hour is not active.")
        if len(self.engagements) >= self.engagement_limit:
            raise Exception("Engagement limit reached.")

        # Simulate engagement process
        engagement_data = {
            'customer_id': customer_id,
            'timestamp': datetime.now(),
            'offer': self._generate_offer()
        }
        self.engagements.append(engagement_data)
        print(f"Engaged customer {customer_id}: {engagement_data}")

    def _generate_offer(self):
        """Generates a random offer for the happy hour."""
        offers = [
            "10% off drinks",
            "Buy one get one free",
            "Free appetizer with any purchase",
            "20% off total bill",
            "Happy Hour special cocktails"
        ]
        return random.choice(offers)

    def get_engagement_summary(self):
        """Returns a summary of all engagements during the happy hour."""
        return self.engagements


if __name__ == "__main__":
    # Example usage
    try:
        happy_hour_start = datetime.now() + timedelta(seconds=10)  # Start in 10 seconds
        happy_hour = HappyHourActivation(start_time=happy_hour_start, duration_minutes=30, engagement_limit=5)

        # Simulating customers engaging after happy hour starts
        for i in range(1, 7):  # Attempt to engage 6 customers
            try:
                # Wait for the happy hour to start
                while not happy_hour.is_active():
                    pass
                happy_hour.engage_customer(f'customer_{i}')
            except Exception as e:
                print(e)

        # Print engagement summary
        print("Engagement summary:", happy_hour.get_engagement_summary())
    except Exception as e:
        print(f"An error occurred: {e}")
```

This code simulates a Happy Hour Activation campaign with customer engagement tracking.
