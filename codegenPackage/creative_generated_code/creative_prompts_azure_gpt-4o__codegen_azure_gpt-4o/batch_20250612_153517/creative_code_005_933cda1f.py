"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openweb-3ua.pages.dev
Prompt: Develop a script to query and visualize the distribution of submitted artworks for Opepen's Permanent Collection using a blockchain-based API.
Generated: DETERMINISTIC_933cda1ffbd0b30f
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opepen.xyz": {
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
import matplotlib.pyplot as plt


class OpepenAPIClient:
    """
    A client to interact with the Opepen blockchain-based API.
    """

    def __init__(self, base_url):
        """
        Initializes the API client.
        
        :param base_url: The base URL of the API.
        """
        self.base_url = base_url

    def get_artwork_distribution(self):
        """
        Queries the artwork distribution data from the API.

        :return: A dictionary containing artwork distribution data.
        :raises: RuntimeError if the API call fails.
        """
        try:
            response = requests.get(f"{self.base_url}/artwork-distribution")
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch artwork distribution data: {e}")


def visualize_artwork_distribution(data):
    """
    Visualizes the artwork distribution as a bar chart.

    :param data: A dictionary containing artwork distribution data.
                 Example format: {"Artist A": 10, "Artist B": 20, "Artist C": 5}
    """
    try:
        # Extract keys (artists) and values (artwork counts)
        artists = list(data.keys())
        artwork_counts = list(data.values())

        # Generate the bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(artists, artwork_counts, color='skyblue')
        plt.title("Opepen Permanent Collection Artwork Distribution")
        plt.xlabel("Artists")
        plt.ylabel("Number of Submitted Artworks")
        plt.xticks(rotation=45, ha='right')
        
        # Display the chart
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error occurred while visualizing data: {e}")


def main():
    """
    Main function to query and visualize the artwork distribution data.
    """
    # Base URL of the blockchain-based API
    API_BASE_URL = "https://api.opepen.xyz"

    # Initialize the API client
    client = OpepenAPIClient(API_BASE_URL)

    try:
        # Fetch artwork distribution data
        distribution_data = client.get_artwork_distribution()

        # Visualize the data
        visualize_artwork_distribution(distribution_data)
    except RuntimeError as e:
        print(e)


if __name__ == "__main__":
    main()
```
