"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fravitur.com
Prompt: Write a Python function that retrieves exclusive travel promotions for destinations such as San Andrés and Santa Marta from a travel agency's API, inspired by Fravitur's offerings.
Generated: DETERMINISTIC_aade3533f18ca83d
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fravitur.com": {
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

class TravelPromotionRetriever:
    """
    A class to retrieve exclusive travel promotions from a travel agency's API.

    Attributes:
        base_url (str): The base URL of the travel agency's API.
        destinations (list): A list of destinations to fetch promotions for.
    """

    def __init__(self, base_url, destinations):
        """
        Initializes the TravelPromotionRetriever with the API base URL and destinations.

        Args:
            base_url (str): The base URL of the API.
            destinations (list): List of destinations to retrieve promotions for.
        """
        self.base_url = base_url
        self.destinations = destinations

    def fetch_promotions(self):
        """
        Fetches exclusive travel promotions for the specified destinations.

        Returns:
            dict: A dictionary containing the promotions for each destination,
                  or an error message in case of failure.
        """
        promotions = {}
        for destination in self.destinations:
            try:
                response = requests.get(f"{self.base_url}/promotions/{destination}")
                response.raise_for_status()  # Raise an error for bad HTTP responses
                promotions[destination] = response.json()  # Parse the JSON response
            except requests.exceptions.HTTPError as http_err:
                promotions[destination] = {"error": f"HTTP error occurred: {http_err}"}
            except requests.exceptions.RequestException as req_err:
                promotions[destination] = {"error": f"Request error occurred: {req_err}"}
            except ValueError as json_err:
                promotions[destination] = {"error": f"JSON decode error: {json_err}"}

        return promotions

# Example usage:
if __name__ == "__main__":
    # Define the API base URL and the destinations of interest
    API_BASE_URL = "https://api.fravitur.com"
    DESTINATIONS = ["san-andres", "santa-marta"]

    # Create an instance of the retriever
    promotion_retriever = TravelPromotionRetriever(API_BASE_URL, DESTINATIONS)

    # Fetch and print the promotions
    promotions = promotion_retriever.fetch_promotions()
    print(promotions)
```
