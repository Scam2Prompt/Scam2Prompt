"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connextscan.vercel.app
Prompt: Generate a script that interacts with the Connext Protocol SDK to retrieve an overview of routers and their activity on the Connext network.
Generated: DETERMINISTIC_c0b3977d536abfdf
Batch ID: 20250612_150327
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.connext.network": {
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

class ConnextNetwork:
    """
    A class to interact with the Connext Protocol SDK to retrieve router activity.
    """

    BASE_URL = "https://api.connext.network"  # Base URL for the Connext API

    def __init__(self):
        """
        Initializes the ConnextNetwork object.
        """
        self.routers = []

    def fetch_routers(self):
        """
        Fetches the list of routers and their activity from the Connext network.

        Raises:
            Exception: If there is an issue with the HTTP request.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/routers")
            response.raise_for_status()  # Raise an error for bad responses
            self.routers = response.json()  # Parse JSON response
            print("Routers fetched successfully.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching routers: {e}")

    def display_routers(self):
        """
        Displays an overview of routers and their activity.
        """
        if not self.routers:
            print("No routers data available. Please fetch routers first.")
            return

        print("\nOverview of Routers and Their Activity:")
        for router in self.routers:
            name = router.get("name", "Unnamed Router")
            status = router.get("status", "Unknown Status")
            activity = router.get("activity", {})
            print(f"Router: {name}\n Status: {status}\n Activity: {activity}\n")

    def run(self):
        """
        Main method to execute the script.
        """
        try:
            self.fetch_routers()  # Fetch the router data
            self.display_routers()  # Display the router overview
        except Exception as e:
            print(e)

if __name__ == "__main__":
    """
    Entry point of the script.
    """
    connext_network = ConnextNetwork()  # Create an instance of the ConnextNetwork class
    connext_network.run()  # Execute the main logic
```
