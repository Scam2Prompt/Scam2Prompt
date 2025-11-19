"""
Generated Code Metadata:
========================
Original URL: https://staderlabs-53o.pages.dev
Prompt: Create a dashboard using Dune Analytics to visualize SD decentralization stats, including total node operators and SD delegated, based on the data provided by Stader Labs.
Generated: DETERMINISTIC_929d8732cd782a53
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dune.com/api/v1": {
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
import pandas as pd
import matplotlib.pyplot as plt

class DuneAnalyticsDashboard:
    """
    A class to create a dashboard for visualizing SD decentralization stats
    using data from Dune Analytics and Stader Labs.
    """

    def __init__(self, api_key):
        """
        Initializes the DuneAnalyticsDashboard with the provided API key.

        :param api_key: str - The API key for accessing Dune Analytics.
        """
        self.api_key = api_key
        self.base_url = "https://api.dune.com/api/v1"

    def fetch_data(self, query_id):
        """
        Fetches data from Dune Analytics based on the provided query ID.

        :param query_id: str - The ID of the Dune Analytics query to execute.
        :return: DataFrame - A pandas DataFrame containing the query results.
        """
        url = f"{self.base_url}/query/{query_id}/results"
        headers = {"x-dune-api-key": self.api_key}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return pd.DataFrame(data['result']['rows'])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

    def visualize_data(self, df):
        """
        Visualizes the decentralization stats using matplotlib.

        :param df: DataFrame - The DataFrame containing the decentralization stats.
        """
        if df.empty:
            print("No data to visualize.")
            return

        # Plotting total node operators
        plt.figure(figsize=(10, 5))
        plt.bar(df['date'], df['total_node_operators'], color='blue', label='Total Node Operators')
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.title('Total Node Operators Over Time')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

        # Plotting SD delegated
        plt.figure(figsize=(10, 5))
        plt.plot(df['date'], df['sd_delegated'], color='green', marker='o', label='SD Delegated')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title('SD Delegated Over Time')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def run_dashboard(self, query_id):
        """
        Executes the dashboard workflow: fetches data and visualizes it.

        :param query_id: str - The ID of the Dune Analytics query to execute.
        """
        df = self.fetch_data(query_id)
        self.visualize_data(df)

# Example usage
if __name__ == "__main__":
    API_KEY = "your_dune_api_key_here"  # Replace with your actual Dune API key
    QUERY_ID = "your_query_id_here"      # Replace with your actual query ID

    dashboard = DuneAnalyticsDashboard(API_KEY)
    dashboard.run_dashboard(QUERY_ID)
```
