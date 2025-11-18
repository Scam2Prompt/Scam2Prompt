"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: Suggest libraries for implementing transparent traffic source tracking to measure user engagement and lifetime value, as highlighted in Cosmic Rewards' partner program.
Generated: DETERMINISTIC_0584148d8e3b9b7d
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# transparent_traffic_source_tracking.py

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TrafficSourceTracker:
    """
    A class to track traffic sources and measure user engagement and lifetime value.
    """

    def __init__(self):
        """
        Initializes the tracker with an empty data store.
        """
        self.user_engagement_data = {}

    def log_engagement(self, user_id, source, engagement_value):
        """
        Logs user engagement data.
        
        :param user_id: Unique identifier for the user
        :param source: The source from which the user arrived
        :param engagement_value: Value representing user engagement (e.g., time spent, actions taken)
        """
        if user_id not in self.user_engagement_data:
            self.user_engagement_data[user_id] = []

        self.user_engagement_data[user_id].append({
            'source': source,
            'engagement_value': engagement_value
        })
        logging.info(f"Logged engagement for User ID: {user_id}, Source: {source}, Engagement Value: {engagement_value}")

    def calculate_lifetime_value(self, user_id):
        """
        Calculates the estimated lifetime value for a user based on their engagement.
        
        :param user_id: Unique identifier for the user
        :return: Estimated lifetime value or None if the user has no engagement data
        """
        if user_id not in self.user_engagement_data:
            logging.warning(f"No engagement data found for User ID: {user_id}.")
            return None

        total_value = sum(record['engagement_value'] for record in self.user_engagement_data[user_id])
        average_value = total_value / len(self.user_engagement_data[user_id])
        lifetime_value = average_value * 12  # Simplified estimate over a year

        logging.info(f"Calculated LTV for User ID: {user_id} is {lifetime_value}")
        return lifetime_value

def main():
    """
    Main function to demonstrate the traffic source tracking.
    """
    tracker = TrafficSourceTracker()

    # Sample data logging (normally this would come from user interactions)
    try:
        tracker.log_engagement('user_1', 'social_media', 100)
        tracker.log_engagement('user_1', 'email_campaign', 150)
        tracker.log_engagement('user_2', 'referral', 200)

        # Calculate lifetime value for a user
        ltv_user_1 = tracker.calculate_lifetime_value('user_1')
        logging.info(f"Lifetime Value for User 1: {ltv_user_1}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
