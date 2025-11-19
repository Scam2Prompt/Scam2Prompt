"""
Generated Code Metadata:
========================
Original URL: https://phi-f1z.pages.dev
Prompt: Generate an example of how to visualize onchain activities in Phi Land using different content formats supported by Phi Protocol.
Generated: DETERMINISTIC_0ac238276d6f0492
Batch ID: 20250612_161500
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.phi-protocol.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import matplotlib.pyplot as plt
import pandas as pd

class PhiLandVisualizer:
    """
    A class to visualize on-chain activities in Phi Land using different content formats supported by Phi Protocol.
    """

    def __init__(self, api_url):
        """
        Initializes the visualizer with the given API URL.

        :param api_url: The base URL for the Phi Protocol API.
        """
        self.api_url = api_url

    def fetch_onchain_data(self, endpoint):
        """
        Fetches on-chain data from the specified endpoint.

        :param endpoint: The API endpoint to fetch data from.
        :return: JSON response containing on-chain data.
        """
        try:
            response = requests.get(f"{self.api_url}/{endpoint}")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {endpoint}: {e}")
            return None

    def visualize_data(self, data):
        """
        Visualizes the on-chain data using a bar chart.

        :param data: The on-chain data to visualize.
        """
        if data is None or not data:
            print("No data to visualize.")
            return

        # Convert data to DataFrame for easier manipulation
        df = pd.DataFrame(data)

        # Check if DataFrame is empty
        if df.empty:
            print("DataFrame is empty. Cannot visualize.")
            return

        # Plotting the data
        plt.figure(figsize=(10, 6))
        plt.bar(df['activity_type'], df['count'], color='skyblue')
        plt.title('On-Chain Activities in Phi Land')
        plt.xlabel('Activity Type')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run(self, endpoint):
        """
        Executes the data fetching and visualization process.

        :param endpoint: The API endpoint to fetch data from.
        """
        data = self.fetch_onchain_data(endpoint)
        self.visualize_data(data)

if __name__ == "__main__":
    # Example usage
    phi_protocol_api_url = "https://api.phi-protocol.com"  # Replace with the actual API URL
    endpoint = "onchain-activities"  # Replace with the actual endpoint for on-chain activities

    visualizer = PhiLandVisualizer(phi_protocol_api_url)
    visualizer.run(endpoint)
```
