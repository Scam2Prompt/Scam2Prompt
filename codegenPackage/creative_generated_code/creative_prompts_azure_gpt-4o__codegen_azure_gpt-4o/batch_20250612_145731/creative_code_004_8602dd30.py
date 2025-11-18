"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pass-vee.com
Prompt: Create a script to fetch and display data from an economic calendar API, similar to the one described on the Changexcapital webpage for Forex trading.
Generated: DETERMINISTIC_8602dd30dc2a8386
Batch ID: 20250612_145731
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
from datetime import datetime

# Set up the API URL and your API key (replace 'YOUR_API_KEY' with your actual API key)
API_URL = "https://api.economiccalendar.com/v1/events"
API_KEY = "YOUR_API_KEY"

def fetch_economic_calendar_data():
    """
    Fetches data from the economic calendar API.

    Returns:
        list: A list of economic events or None if an error occurred.
    """
    try:
        # Define headers and parameters for the API request
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(API_URL, headers=headers)

        # Check HTTP response status
        if response.status_code == 200:
            return response.json()  # Parse JSON response
        else:
            print(f"Error: Failed to fetch data (HTTP {response.status_code})")
            return None
    except requests.exceptions.RequestException as e:
        # Handle connection errors or other request exceptions
        print(f"Error: An exception occurred while fetching data - {e}")
        return None

def display_economic_calendar_data(events):
    """
    Displays economic calendar events in a readable format.

    Args:
        events (list): A list of economic events.
    """
    if not events:
        print("No events found.")
        return

    print(f"{'Date':<20}{'Event':<50}{'Impact':<10}")
    print("=" * 80)

    for event in events:
        # Parse fields from the event object
        date = event.get("date", "Unknown")
        name = event.get("name", "Unknown Event")
        impact = event.get("impact", "Unknown")

        # Format and display each event
        try:
            # Convert date to a more readable format
            readable_date = datetime.fromisoformat(date).strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            readable_date = date  # Use raw date if parsing fails

        print(f"{readable_date:<20}{name:<50}{impact:<10}")

def main():
    """
    Main function to orchestrate fetching and displaying data from the economic calendar API.
    """
    print("Fetching data from the economic calendar API...")
    events = fetch_economic_calendar_data()

    # If data is retrieved successfully, display it
    if events:
        print("\nEconomic Calendar Events:\n")
        display_economic_calendar_data(events)

if __name__ == "__main__":
    main()
```
