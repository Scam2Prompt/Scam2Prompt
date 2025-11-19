"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-guh1xmcsb-voteagora.vercel.app
Prompt: Provide an example of how to use the Agora governance calendar API to check upcoming voting events for Optimism proposals.
Generated: DETERMINISTIC_40a91fe9b1244e00
Batch ID: 20250612_163854
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.agora.org/v1": {
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

def get_upcoming_voting_events(api_url, api_key):
    """
    Fetches upcoming voting events using the Agora Governance Calendar API.

    Args:
        api_url (str): The base URL of the Agora Governance Calendar API.
        api_key (str): The API key for authentication.

    Returns:
        list: A list of upcoming voting events for Optimism proposals.
    """
    # Endpoint for fetching events
    endpoint = f"{api_url}/events"

    # Headers for authentication
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    try:
        # Make a GET request to the API
        response = requests.get(endpoint, headers=headers)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the response JSON
        events = response.json()

        # Filter events related to Optimism proposals
        optimism_events = [
            event for event in events
            if "Optimism" in event.get("tags", [])
        ]

        return optimism_events

    except requests.exceptions.RequestException as e:
        # Log the error and return an empty list
        print(f"An error occurred while fetching events: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Replace with the actual API URL and your API key
    AGORA_API_URL = "https://api.agora.org/v1"
    API_KEY = "your_api_key_here"

    # Fetch upcoming voting events
    events = get_upcoming_voting_events(AGORA_API_URL, API_KEY)

    # Display the results
    if events:
        print("Upcoming voting events for Optimism proposals:")
        for event in events:
            print(f"- {event.get('title')} (Date: {event.get('date')})")
    else:
        print("No upcoming voting events found for Optimism proposals.")
```
