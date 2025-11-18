"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finprofm.com
Prompt: Create a script to fetch and display an economic calendar with real-time updates, similar to the feature available on FinProfm.
Generated: DETERMINISTIC_ced2e25c9e2dfe11
Batch ID: 20250612_145114
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example-economic-calendar-api.com/events": {
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
import time
from datetime import datetime

# Constants
API_URL = "https://example-economic-calendar-api.com/events"  # Replace with actual API endpoint
REFRESH_INTERVAL = 60  # Refresh interval in seconds

def fetch_economic_calendar():
    """
    Fetch the latest economic calendar data from the API.

    :return: A list of economic events or None if an error occurs.
    """
    try:
        response = requests.get(API_URL, timeout=10)  # Timeout set to 10 seconds
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching economic calendar: {e}")
        return None

def display_calendar(events):
    """
    Display economic events in a readable format.

    :param events: List of economic events fetched from the API.
    """
    if not events or not isinstance(events, list):
        print("No events available to display.")
        return

    print("\nEconomic Calendar (Real-Time Updates):")
    print("-" * 50)

    for event in events:
        try:
            # Extract event details safely
            time = event.get('time', 'N/A')
            title = event.get('title', 'N/A')
            country = event.get('country', 'N/A')
            importance = event.get('importance', 'N/A')
            forecast = event.get('forecast', 'N/A')

            # Print event details
            print(f"Time: {time}")
            print(f"Title: {title}")
            print(f"Country: {country}")
            print(f"Importance: {importance}")
            print(f"Forecast: {forecast}")
            print("-" * 50)
        except Exception as e:
            # Handle any unexpected issues while processing events
            print(f"Error displaying event: {e}")

def main():
    """
    Main function to fetch and display the economic calendar with real-time updates.
    """
    print("Starting Economic Calendar Listener...")
    
    while True:
        try:
            # Fetch the latest economic calendar data
            events = fetch_economic_calendar()

            # Clear console output for a better real-time experience (cross-platform)
            print("\033[H\033[J", end="")  # ANSI escape sequence to clear the console

            # Display the fetched data
            display_calendar(events)

            # Wait for the next refresh interval
            print(f"Next update in {REFRESH_INTERVAL} seconds...")
            time.sleep(REFRESH_INTERVAL)

        except KeyboardInterrupt:
            # Allow graceful shutdown on Ctrl+C
            print("\nTerminating Economic Calendar Listener. Goodbye!")
            break
        except Exception as e:
            # Catch any unexpected exceptions
            print(f"Unexpected error: {e}")
            time.sleep(REFRESH_INTERVAL)

# Entry point for the script
if __name__ == "__main__":
    main()
```

Make sure to replace `API_URL` with the actual API endpoint that provides the economic calendar data. Adding API keys or authentication headers might be necessary depending on the API's requirements.
