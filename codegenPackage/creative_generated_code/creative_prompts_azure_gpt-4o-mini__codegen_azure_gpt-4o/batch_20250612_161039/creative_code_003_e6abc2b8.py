"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-bits.com
Prompt: Generate a code snippet that tracks earnings from ad clicks on Claim-Bits and calculates the total payout based on their payment structure.
Generated: DETERMINISTIC_e6abc2b8a26af71f
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AdEarningsTracker:
    """
    A class to track ad-click earnings and calculate the total payout based on Claim-Bits' payment structure.
    """

    def __init__(self, click_rate_usd):
        """
        Initializes the tracker with a given click rate in USD.
        :param click_rate_usd: (float) The earning per ad-click in USD.
        """
        self.click_rate_usd = click_rate_usd
        self.total_clicks = 0
        self.click_records = []
        self.total_earnings = 0.0

    def record_click(self):
        """
        Records a single ad click with the current timestamp.
        Updates total earnings and click count.
        """
        timestamp = datetime.datetime.now()
        self.click_records.append(timestamp)
        self.total_clicks += 1
        self.total_earnings += self.click_rate_usd

    def calculate_total_payout(self):
        """
        Calculates the total payout based on the recorded clicks.
        :return: (float) Total earnings in USD.
        """
        return round(self.total_earnings, 2)

    def get_click_details(self):
        """
        Retrieves details about all recorded clicks.
        :return: (list) Timestamps of all recorded clicks.
        """
        return self.click_records

def main():
    """
    Main function to demonstrate the functionality of AdEarningsTracker.
    """
    # Set the click rate (e.g., 0.02 USD per click)
    click_rate = 0.02

    # Instantiate the tracker
    tracker = AdEarningsTracker(click_rate)

    try:
        # Simulate ad clicks
        tracker.record_click()
        tracker.record_click()
        tracker.record_click()

        # Display total payout
        print(f"Total Payout: ${tracker.calculate_total_payout()}")

        # Display click details
        print("Click Details:")
        for index, timestamp in enumerate(tracker.get_click_details(), start=1):
            print(f"{index}. {timestamp}")

    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
