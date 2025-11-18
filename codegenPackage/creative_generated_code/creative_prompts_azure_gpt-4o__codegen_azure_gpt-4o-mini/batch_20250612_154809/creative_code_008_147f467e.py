"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pawscommunity.life
Prompt: Write a script to track the delivery time of Telegram Stars orders on the Buy&Stars platform and calculate the average completion time based on historical data.
Generated: DETERMINISTIC_147f467e5f809b6f
Batch ID: 20250612_154809
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.buyandstars.com/delivery-data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import logging
from datetime import datetime
from statistics import mean

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DeliveryTimeTracker:
    def __init__(self, api_url):
        """
        Initializes the DeliveryTimeTracker with the specified API URL.
        
        :param api_url: The API endpoint to fetch delivery data from.
        """
        self.api_url = api_url
        self.delivery_times = []

    def fetch_delivery_data(self):
        """
        Fetches delivery data from the Buy&Stars API.

        :return: JSON response from the API if successful, otherwise None.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching delivery data: {e}")
            return None

    def calculate_average_delivery_time(self):
        """
        Calculates the average delivery time from the historical data.

        :return: The average delivery time in hours, or None if no data available.
        """
        if not self.delivery_times:
            logging.warning("No delivery times available to calculate average.")
            return None
        average_time = mean(self.delivery_times)
        logging.info(f"Average delivery time calculated: {average_time:.2f} hours.")
        return average_time

    def process_delivery_data(self):
        """
        Processes the fetched delivery data to extract delivery times.

        :return: None
        """
        data = self.fetch_delivery_data()
        if data:
            for order in data.get('orders', []):
                delivery_time = self.calculate_time_difference(order['order_date'], order['completion_date'])
                if delivery_time is not None:
                    self.delivery_times.append(delivery_time)
                    logging.info(f"Delivery time for order {order['id']}: {delivery_time:.2f} hours.")

    @staticmethod
    def calculate_time_difference(order_date_str, completion_date_str):
        """
        Calculates the time difference in hours between order and completion dates.

        :param order_date_str: The order date in string format.
        :param completion_date_str: The completion date in string format.
        :return: Time difference in hours, or None if parsing fails.
        """
        try:
            order_date = datetime.fromisoformat(order_date_str)
            completion_date = datetime.fromisoformat(completion_date_str)
            time_diff = (completion_date - order_date).total_seconds() / 3600  # Convert seconds to hours
            return time_diff
        except ValueError as e:
            logging.error(f"Error parsing date: {e}")
            return None

def main():
    """
    Main function to run the delivery time tracker.
    """
    api_url = "https://api.buyandstars.com/delivery-data"  # Replace with actual API URL
    tracker = DeliveryTimeTracker(api_url)
    tracker.process_delivery_data()
    average_time = tracker.calculate_average_delivery_time()
    if average_time is not None:
        print(f"Average delivery time: {average_time:.2f} hours.")

if __name__ == "__main__":
    main()
```
