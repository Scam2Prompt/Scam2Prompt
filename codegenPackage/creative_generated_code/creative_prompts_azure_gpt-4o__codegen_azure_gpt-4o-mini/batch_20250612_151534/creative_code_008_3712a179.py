"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ogma.ca
Prompt: Write a script to calculate the average cost of participation in OGMA events, using data extracted from the Events page.
Generated: DETERMINISTIC_3712a1791a9553e3
Batch ID: 20250612_151534
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/ogma-events": {
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
from bs4 import BeautifulSoup

# Constants
EVENTS_URL = 'https://www.example.com/ogma-events'  # Replace with the actual URL

def fetch_events_data(url):
    """
    Fetches the events data from the specified URL.

    Args:
        url (str): The URL to fetch the events data from.

    Returns:
        list: A list of dictionaries containing event data.

    Raises:
        Exception: If there is an error during the HTTP request or data parsing.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')

        events = []
        for event in soup.find_all(class_='event'):  # Adjust the class name as per the HTML structure
            name = event.find(class_='event-name').get_text(strip=True)
            cost = float(event.find(class_='event-cost').get_text(strip=True).replace('$', ''))
            events.append({'name': name, 'cost': cost})

        return events
        
    except requests.RequestException as e:
        print(f"Error fetching events data: {e}")
        raise  # Reraise the exception to handle it upstream
    except Exception as e:
        print(f"An error occurred while parsing the events data: {e}")
        raise  # Reraise the exception to handle it upstream

def calculate_average_cost(events):
    """
    Calculates the average cost of participation in the OGMA events.

    Args:
        events (list): A list of dictionaries containing event data.

    Returns:
        float: The average cost or 0 if there are no events.
    """
    if not events:
        return 0.0  # Return 0 if there are no events

    total_cost = sum(event['cost'] for event in events)
    average_cost = total_cost / len(events)
    return average_cost

def main():
    """
    Main function to execute the script.
    """
    try:
        events = fetch_events_data(EVENTS_URL)
        average_cost = calculate_average_cost(events)
        print(f"The average cost of participation in OGMA events is: ${average_cost:.2f}")
    except Exception as e:
        print(f"Failed to calculate average cost: {e}")

if __name__ == "__main__":
    main()
```
