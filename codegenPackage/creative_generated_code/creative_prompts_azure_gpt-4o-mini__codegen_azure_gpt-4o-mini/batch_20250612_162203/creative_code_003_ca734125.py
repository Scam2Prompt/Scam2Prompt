"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Create a function that retrieves and displays event data for a cooperative, inspired by the features of the Nexelit CMS.
Generated: DETERMINISTIC_ca73412529c921ac
Batch ID: 20250612_162203
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/events": {
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

class EventDataRetriever:
    """
    A class to retrieve and display event data for a cooperative,
    inspired by features of the Nexelit CMS.
    """

    def __init__(self, api_url):
        """
        Initializes the EventDataRetriever with the given API URL.

        Args:
            api_url (str): The URL of the API to retrieve event data from.
        """
        self.api_url = api_url

    def fetch_event_data(self):
        """
        Fetches event data from the API.

        Returns:
            list: A list of events retrieved from the API.

        Raises:
            Exception: If there is an issue with the API request.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise  # re-raise the exception for further handling
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            raise  # re-raise the exception for further handling

    def display_event_data(self, event_data):
        """
        Displays the event data in a readable format.

        Args:
            event_data (list): A list of events to display.
        """
        if not event_data:
            print("No event data available.")
            return

        print("Upcoming Events:")
        for event in event_data:
            try:
                title = event.get("title", "No Title Available")
                date = event.get("date", "No Date Available")
                location = event.get("location", "No Location Available")
                description = event.get("description", "No Description Available")

                print(f"Title: {title}")
                print(f"Date: {date}")
                print(f"Location: {location}")
                print(f"Description: {description}")
                print("-" * 40)  # Separator line
            except Exception as e:
                print(f"Error displaying event: {e}")

    def run(self):
        """
        Executes the process of fetching and displaying event data.
        """
        try:
            event_data = self.fetch_event_data()
            self.display_event_data(event_data)
        except Exception as e:
            print(f"An error occurred while processing events: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your actual API URL
    api_url = "https://api.example.com/events"
    event_data_retriever = EventDataRetriever(api_url)
    event_data_retriever.run()
```
