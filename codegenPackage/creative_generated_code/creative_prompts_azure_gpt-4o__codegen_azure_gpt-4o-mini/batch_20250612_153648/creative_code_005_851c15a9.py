"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobukineko.pages.dev
Prompt: Develop a roadmap tracker for $BOBUKI using the phases outlined on the website. Include features for monitoring presale events, token listings, and NFT launches.
Generated: DETERMINISTIC_851c15a9487351e9
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bobuki.com": {
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
from datetime import datetime
from typing import List, Dict, Optional

class RoadmapTracker:
    """
    A class to track the roadmap of the $BOBUKI project, including presale events, token listings, and NFT launches.
    """

    def __init__(self, api_base_url: str):
        """
        Initialize the RoadmapTracker with the base URL of the API.

        :param api_base_url: Base URL of the API to fetch roadmap data.
        """
        self.api_base_url = api_base_url

    def fetch_roadmap_data(self) -> List[Dict[str, Optional[str]]]:
        """
        Fetch the roadmap data from the API.

        :return: A list of roadmap phases.
        """
        try:
            response = requests.get(f"{self.api_base_url}/roadmap")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming the response is in JSON format
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
        return []

    def filter_events(self, events: List[Dict[str, Optional[str]]], event_type: str) -> List[Dict[str, Optional[str]]]:
        """
        Filter events by their type (e.g., presale, listing, NFT launch).

        :param events: List of events to filter.
        :param event_type: Type of the event to filter on.
        :return: Filtered list of events.
        """
        return [event for event in events if event.get('type') == event_type]

    def display_events(self, events: List[Dict[str, Optional[str]]]):
        """
        Display a list of events in a user-friendly format.

        :param events: List of events to display.
        """
        if not events:
            print("No events to display.")
            return
        for event in events:
            event_date = datetime.fromisoformat(event['date']).strftime('%Y-%m-%d %H:%M') if event.get('date') else 'N/A'
            print(f"Event: {event.get('name', 'N/A')} | Type: {event.get('type', 'N/A')} | Date: {event_date}")

    def run(self):
        """
        Run the roadmap tracker to fetch and display events.
        """
        roadmap_data = self.fetch_roadmap_data()
        
        # Display presale events
        presale_events = self.filter_events(roadmap_data, event_type='presale')
        print("\n--- Presale Events ---")
        self.display_events(presale_events)

        # Display token listings
        listing_events = self.filter_events(roadmap_data, event_type='listing')
        print("\n--- Token Listings ---")
        self.display_events(listing_events)

        # Display NFT launches
        nft_launches = self.filter_events(roadmap_data, event_type='nft_launch')
        print("\n--- NFT Launches ---")
        self.display_events(nft_launches)

if __name__ == "__main__":
    tracker = RoadmapTracker(api_base_url="https://api.bobuki.com")
    tracker.run()
```
