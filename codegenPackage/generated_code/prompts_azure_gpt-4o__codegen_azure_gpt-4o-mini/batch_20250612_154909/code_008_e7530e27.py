"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Write code to simulate a "Happy Hour Activation" campaign, similar to the Shell activations described on Paradigm Group's website, including customer engagement tracking.
Generated: DETERMINISTIC_e7530e27144f8bd1
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta
import logging

# Configure logging for tracking events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HappyHourCampaign:
    def __init__(self, start_time: datetime, duration: timedelta, discount: float):
        """
        Initialize the Happy Hour Campaign.

        :param start_time: The start time of the happy hour.
        :param duration: The duration of the happy hour.
        :param discount: The discount percentage offered during happy hour.
        """
        self.start_time = start_time
        self.end_time = start_time + duration
        self.discount = discount
        self.engagement_data = []

    def is_active(self) -> bool:
        """
        Check if the happy hour campaign is currently active.

        :return: True if the campaign is active, False otherwise.
        """
        current_time = datetime.now()
        return self.start_time <= current_time <= self.end_time

    def engage_customer(self, customer_id: str):
        """
        Simulate customer engagement during the happy hour.

        :param customer_id: Unique identifier for the customer.
        """
        if not self.is_active():
            logging.warning(f"Engagement attempt by customer {customer_id} outside of happy hour.")
            return

        engagement_event = {
            'customer_id': customer_id,
            'timestamp': datetime.now(),
            'discount_applied': self.discount
        }
        self.engagement_data.append(engagement_event)
        logging.info(f"Customer {customer_id} engaged during happy hour with {self.discount}% discount.")

    def get_engagement_report(self):
        """
        Generate a report of customer engagements during the happy hour.

        :return: List of engagement events.
        """
        return self.engagement_data

def main():
    # Define the happy hour parameters
    happy_hour_start = datetime.now() + timedelta(seconds=10)  # Starts in 10 seconds
    happy_hour_duration = timedelta(minutes=30)  # Lasts for 30 minutes
    discount_percentage = 20.0  # 20% discount

    # Create a Happy Hour Campaign instance
    happy_hour_campaign = HappyHourCampaign(happy_hour_start, happy_hour_duration, discount_percentage)

    # Simulate customer engagement
    try:
        # Wait for the happy hour to start
        while not happy_hour_campaign.is_active():
            pass  # Busy wait (for demonstration purposes only)

        # Simulate multiple customers engaging
        for customer_id in range(1, 6):
            happy_hour_campaign.engage_customer(f"customer_{customer_id}")
            # Random sleep to simulate time between engagements
            sleep_time = random.uniform(1, 3)
            time.sleep(sleep_time)

        # Generate and print the engagement report
        report = happy_hour_campaign.get_engagement_report()
        print("Engagement Report:", report)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note:** This code simulates a happy hour campaign with customer engagement tracking. It includes logging for tracking events and error handling for robustness. The `sleep` function is used to simulate time between customer engagements, and the busy wait is for demonstration purposes only. In a production environment, consider using asynchronous programming or scheduling libraries for better efficiency.
