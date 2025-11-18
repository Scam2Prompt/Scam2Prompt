"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emarlado.com
Prompt: Write a program that integrates an economic calendar API to track global financial events, inspired by the tools available on Emarlado's platform.
Generated: DETERMINISTIC_968d581157187f66
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.economiccalendar.com/v1/events": {
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
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EconomicCalendar:
    """
    A class to interact with an economic calendar API to fetch global financial events.
    """

    BASE_URL = "https://api.economiccalendar.com/v1/events"  # Replace with actual API endpoint
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    def __init__(self):
        """
        Initializes the EconomicCalendar instance.
        """
        self.headers = {
            'Authorization': f'Bearer {self.API_KEY}',
            'Content-Type': 'application/json'
        }

    def fetch_events(self, start_date, end_date):
        """
        Fetches economic events from the API within the specified date range.

        :param start_date: The start date for fetching events (datetime).
        :param end_date: The end date for fetching events (datetime).
        :return: List of events or an error message.
        """
        try:
            # Prepare the URL with query parameters
            params = {
                'start': start_date.isoformat(),
                'end': end_date.isoformat()
            }

            response = requests.get(self.BASE_URL, headers=self.headers, params=params)

            # Check if the request was successful
            response.raise_for_status()
            events = response.json()
            logging.info("Successfully fetched events.")
            return events

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            return {"error": "Failed to fetch events from the API."}
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            return {"error": "An unexpected error occurred."}

def main():
    """
    Main function to execute the program logic.
    """
    # Create an instance of the EconomicCalendar
    calendar = EconomicCalendar()

    # Define the date range for fetching events
    today = datetime.now()
    start_date = today
    end_date = today + timedelta(days=30)  # Fetch events for the next 30 days

    # Fetch economic events
    events = calendar.fetch_events(start_date, end_date)

    # Print the fetched events
    if "error" not in events:
        for event in events:
            print(f"Date: {event.get('date')}, Event: {event.get('title')}, Impact: {event.get('impact')}")
    else:
        print(events['error'])

if __name__ == "__main__":
    main()
```

Make sure to replace `your_api_key_here` with your actual API key and adjust the `BASE_URL` to the actual endpoint of the economic calendar API you intend to use.
