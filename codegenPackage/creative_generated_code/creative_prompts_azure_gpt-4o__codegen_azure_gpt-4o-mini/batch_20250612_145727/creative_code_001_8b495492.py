"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oceanreward.net
Prompt: How can I use Hootsuite's social listening features to track brand mentions and generate reports? Provide code examples if applicable.
Generated: DETERMINISTIC_8b4954922570e955
Batch ID: 20250612_145727
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://platform.hootsuite.com/v1": {
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
import json
import datetime

class HootsuiteSocialListening:
    """
    A class to interact with Hootsuite's social listening features
    for tracking brand mentions and generating reports.
    """
    
    BASE_URL = "https://platform.hootsuite.com/v1"  # Hootsuite API base URL
    HEADERS = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN',  # Replace with your Hootsuite access token
        'Content-Type': 'application/json'
    }

    def __init__(self, brand_name):
        """
        Initializes the HootsuiteSocialListening class.

        :param brand_name: The name of the brand to track
        """
        self.brand_name = brand_name

    def fetch_brand_mentions(self, start_date, end_date):
        """
        Fetches brand mentions within the specified date range.

        :param start_date: The start date for tracking mentions (format: YYYY-MM-DD)
        :param end_date: The end date for tracking mentions (format: YYYY-MM-DD)
        :return: List of mentions
        """
        # Constructing the API endpoint
        url = f"{self.BASE_URL}/social-listening/mentions"
        
        params = {
            'query': self.brand_name,
            'startDate': start_date,
            'endDate': end_date
        }
        
        try:
            # Making a GET request to the API
            response = requests.get(url, headers=self.HEADERS, params=params)
            response.raise_for_status()  # Raise an error for bad responses

            mentions = response.json()
            return mentions.get('data', [])  # Return the list of mentions

        except requests.exceptions.RequestException as e:
            print(f"Error fetching brand mentions: {e}")
            return []

    def generate_report(self, mentions):
        """
        Generates a report from the fetched mentions.

        :param mentions: List of mentions to include in the report
        :return: A report string
        """
        if not mentions:
            return "No mentions found."

        report_lines = [f"Report for brand: {self.brand_name}\n"]
        report_lines.append(f"Generated on: {datetime.datetime.now()}\n")
        report_lines.append("Mentions:\n")

        for mention in mentions:
            report_lines.append(f"- Date: {mention['date']}, Content: {mention['content']}, Source: {mention['source']}\n")

        return "".join(report_lines)

# Usage example
if __name__ == "__main__":
    # Initialize the social listening class with brand name
    brand_tracker = HootsuiteSocialListening("YourBrandName")

    # Define date range for tracking mentions
    start_date = "2023-01-01"
    end_date = "2023-01-31"

    # Fetch mentions and generate report
    mentions = brand_tracker.fetch_brand_mentions(start_date, end_date)
    report = brand_tracker.generate_report(mentions)

    # Output the report
    print(report)
```
