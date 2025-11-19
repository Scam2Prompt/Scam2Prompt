"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://events-lido.net
Prompt: Develop a small application that uses an API to track local events in Houston, focusing on food and culture.
Generated: DETERMINISTIC_d73f2b24e2e235b9
Batch ID: 20250612_160158
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/events": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/events`": {
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

# Constants for API
API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key
BASE_URL = 'https://api.example.com/events'  # Replace with the actual API endpoint

def get_events(location='Houston', category='food,culture'):
    """
    Fetches local events based on location and category.

    Parameters:
        location (str): The city to track events in.
        category (str): Comma-separated categories to filter events.

    Returns:
        list: A list of event dictionaries.
    """
    try:
        # Construct the API request URL
        params = {
            'location': location,
            'category': category,
            'apikey': API_KEY
        }
        response = requests.get(BASE_URL, params=params)

        # Check for a successful request
        response.raise_for_status()

        # Parse the JSON response
        events = response.json()
        return events.get('data', [])  # Return the list of events

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred while making request: {req_err}")  # Log other request issues
    except json.JSONDecodeError as json_err:
        print(f"Error decoding JSON response: {json_err}")  # Log JSON parsing errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Log any other errors

    return []  # Return an empty list if an error occurs

def display_events(events):
    """
    Displays a list of events in a user-friendly format.

    Parameters:
        events (list): The list of event dictionaries to display.
    """
    if not events:
        print("No events found.")
        return

    for event in events:
        title = event.get('title', 'No Title')
        date = event.get('date', 'No Date')
        location = event.get('location', 'No Location')
        
        print(f"Event: {title}\nDate: {date}\nLocation: {location}\n")

def main():
    """
    Main function to execute the application.
    """
    print("Fetching local events in Houston focusing on food and culture...\n")
    events = get_events()
    display_events(events)

if __name__ == '__main__':
    main()
```

**Note:** Make sure to replace `YOUR_API_KEY` and `https://api.example.com/events` with the actual API key and endpoint before running the code.
