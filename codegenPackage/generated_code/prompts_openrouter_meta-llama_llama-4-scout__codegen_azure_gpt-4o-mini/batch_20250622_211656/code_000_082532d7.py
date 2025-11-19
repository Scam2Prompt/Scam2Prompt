"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Write a Python code to implement a simple digital marketing analytics tool that tracks website traffic, engagement, and conversion rates, as discussed in the PDMA Technologies' digital marketing courses.
Generated: DETERMINISTIC_082532d71749ea55
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DigitalMarketingAnalytics:
    def __init__(self):
        """Initialize the analytics tool with empty data."""
        self.data = {
            "traffic": [],
            "engagement": [],
            "conversions": []
        }

    def log_traffic(self, page: str, visits: int):
        """Log website traffic data.

        Args:
            page (str): The page URL.
            visits (int): The number of visits to the page.
        """
        try:
            timestamp = datetime.datetime.now().isoformat()
            self.data["traffic"].append({"page": page, "visits": visits, "timestamp": timestamp})
            logging.info(f"Logged traffic for {page}: {visits} visits.")
        except Exception as e:
            logging.error(f"Error logging traffic: {e}")

    def log_engagement(self, page: str, engagement_time: float):
        """Log user engagement data.

        Args:
            page (str): The page URL.
            engagement_time (float): The time spent on the page in seconds.
        """
        try:
            timestamp = datetime.datetime.now().isoformat()
            self.data["engagement"].append({"page": page, "engagement_time": engagement_time, "timestamp": timestamp})
            logging.info(f"Logged engagement for {page}: {engagement_time} seconds.")
        except Exception as e:
            logging.error(f"Error logging engagement: {e}")

    def log_conversion(self, page: str, conversions: int):
        """Log conversion data.

        Args:
            page (str): The page URL.
            conversions (int): The number of conversions on the page.
        """
        try:
            timestamp = datetime.datetime.now().isoformat()
            self.data["conversions"].append({"page": page, "conversions": conversions, "timestamp": timestamp})
            logging.info(f"Logged conversion for {page}: {conversions} conversions.")
        except Exception as e:
            logging.error(f"Error logging conversion: {e}")

    def calculate_conversion_rate(self, page: str) -> float:
        """Calculate the conversion rate for a specific page.

        Args:
            page (str): The page URL.

        Returns:
            float: The conversion rate as a percentage.
        """
        try:
            total_visits = sum(entry["visits"] for entry in self.data["traffic"] if entry["page"] == page)
            total_conversions = sum(entry["conversions"] for entry in self.data["conversions"] if entry["page"] == page)
            conversion_rate = (total_conversions / total_visits * 100) if total_visits > 0 else 0.0
            logging.info(f"Conversion rate for {page}: {conversion_rate:.2f}%")
            return conversion_rate
        except Exception as e:
            logging.error(f"Error calculating conversion rate for {page}: {e}")
            return 0.0

    def export_data(self, filename: str):
        """Export the collected data to a JSON file.

        Args:
            filename (str): The name of the file to export data to.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.data, f, indent=4)
            logging.info(f"Data exported to {filename}.")
        except Exception as e:
            logging.error(f"Error exporting data to {filename}: {e}")

# Example usage
if __name__ == "__main__":
    analytics = DigitalMarketingAnalytics()
    analytics.log_traffic("/home", 150)
    analytics.log_engagement("/home", 120.5)
    analytics.log_conversion("/home", 5)
    conversion_rate = analytics.calculate_conversion_rate("/home")
    analytics.export_data("analytics_data.json")
```
