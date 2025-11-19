"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Create a function that retrieves and displays event data for a cooperative, inspired by the features of the Nexelit CMS.
Generated: DETERMINISTIC_ca73412529c921ac
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from datetime import datetime

def fetch_events(api_url, access_token):
    """
    Fetches and displays event data for a cooperative.

    Parameters:
    api_url (str): The URL of the API endpoint to fetch events.
    access_token (str): The access token for API authentication.

    Returns:
    None: Prints the fetched events to the console.
    """
    try:
        # Define headers for the API request
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        # Make the HTTP GET request to fetch event data
        response = requests.get(api_url, headers=headers)

        # Raise an exception if the status code indicates an error
        response.raise_for_status()

        # Parse the JSON response
        events = response.json()

        # Check if events data exists in the response
        if not events or 'data' not in events:
            print("No events found.")
            return

        # Iterate through the events and display them
        print("Upcoming Events:")
        for event in events['data']:
            event_name = event.get('name', 'Unnamed Event')
            event_description = event.get('description', 'No Description Available')
            event_date = event.get('date', 'Unknown Date')

            # Format the date if it's provided
            if event_date != 'Unknown Date':
                try:
                    formatted_date = datetime.strptime(event_date, '%Y-%m-%d').strftime('%B %d, %Y')
                except ValueError:
                    formatted_date = "Invalid Date Format"
            else:
                formatted_date = event_date

            print(f"- {event_name} ({formatted_date})\n  {event_description}")

    except requests.exceptions.RequestException as e:
        # Handle potential HTTP request errors
        print(f"An error occurred while fetching events: {e}")

    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")

# Example usage:
# Replace 'your_api_url_here' and 'your_access_token_here' with actual values.
fetch_events("your_api_url_here", "your_access_token_here")
```
