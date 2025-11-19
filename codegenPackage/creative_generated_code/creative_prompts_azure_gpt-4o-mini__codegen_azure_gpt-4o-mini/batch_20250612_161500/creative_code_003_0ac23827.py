"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
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

# Creative Generated Code:
# ========================

```python
import requests
import matplotlib.pyplot as plt
import pandas as pd

class PhiLandVisualizer:
    """
    A class to visualize on-chain activities in Phi Land using various content formats 
    supported by the Phi Protocol.
    """

    def __init__(self, api_url):
        """
        Initializes the visualizer with the API URL.
        
        :param api_url: The URL of the Phi Protocol API.
        """
        self.api_url = api_url

    def fetch_onchain_data(self, content_format='json'):
        """
        Fetches on-chain activity data from the Phi Protocol API.
        
        :param content_format: The format in which to request the data (e.g., 'json', 'csv').
        :return: Parsed data in the requested format.
        """
        try:
            response = requests.get(f"{self.api_url}/onchain_activities", params={'format': content_format})
            response.raise_for_status()  # Raise an error for bad requests

            if content_format == 'json':
                return response.json()
            elif content_format == 'csv':
                return pd.read_csv(response.text)
            else:
                raise ValueError("Unsupported content format requested.")
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
        except ValueError as ve:
            print(ve)
            return None

    def visualize_data(self, data, plot_type='bar'):
        """
        Visualizes the fetched on-chain activity data.

        :param data: The data to visualize, expected to be in a pandas DataFrame.
        :param plot_type: The type of plot to create ('bar' or 'line').
        """
        if data is None or data.empty:
            print("No data to visualize")
            return

        try:
            if plot_type == 'bar':
                data.plot(kind='bar', x='timestamp', y='activity_count', title='On-Chain Activity (Bar Chart)')
            elif plot_type == 'line':
                data.plot(kind='line', x='timestamp', y='activity_count', title='On-Chain Activity (Line Chart)')
            else:
                raise ValueError("Unsupported plot type provided.")

            plt.xlabel('Timestamp')
            plt.ylabel('Activity Count')
            plt.xticks(rotation=45)
            plt.tight_layout()  # Adjust layout to prevent clipping
            plt.show()
        except Exception as e:
            print(f"Error during visualization: {e}")

def main():
    """
    Main function to execute the PhiLand visualizer.
    """
    api_url = "https://api.phi-protocol.com"  # Example API URL
    visualizer = PhiLandVisualizer(api_url)

    # Fetch data in JSON format
    onchain_data = visualizer.fetch_onchain_data(content_format='json')
    if onchain_data is not None:
        df = pd.DataFrame(onchain_data)
        # Visualize the data as a bar chart
        visualizer.visualize_data(df, plot_type='bar')

if __name__ == "__main__":
    main()
```
