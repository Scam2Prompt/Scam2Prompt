"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stader.pages.dev
Prompt: Develop a dashboard using Dune Analytics to visualize the decentralization stats of ETHx, including the total node operators and node operator bond.
Generated: DETERMINISTIC_4db6662c1eabd3a2
Batch ID: 20250612_151158
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

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt

class DuneAnalyticsDashboard:
    def __init__(self, api_key: str):
        """Initialize the DuneAnalyticsDashboard with an API key."""
        self.api_key = api_key
        self.base_url = "https://api.dune.com/api/v1"

    def fetch_query_result(self, query_id: int) -> dict:
        """
        Fetch the results of a Dune Analytics query.
        
        Args:
            query_id (int): The ID of the Dune Analytics query.
        
        Returns:
            dict: The JSON response containing the query results.
        """
        url = f"{self.base_url}/query/{query_id}/results"
        headers = {
            "x-dune-api-key": self.api_key
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")  # Log the error for debugging
            return {}
        except Exception as e:
            print(f"An error occurred: {e}")  # Log any other errors
            return {}

    def visualize_stats(self, data: pd.DataFrame):
        """
        Visualize the decentralization stats using a bar chart.
        
        Args:
            data (pd.DataFrame): DataFrame containing the decentralization stats.
        """
        plt.figure(figsize=(10, 5))
        plt.bar(data['node_operator'], data['bond'], color='skyblue')
        plt.xlabel('Node Operators')
        plt.ylabel('Node Operator Bond')
        plt.title('Decentralization Stats of ETHx')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run_dashboard(self, query_id: int):
        """
        Execute the dashboard by fetching data and visualizing it.
        
        Args:
            query_id (int): The ID of the Dune Analytics query.
        """
        result = self.fetch_query_result(query_id)
        
        if result and 'data' in result:
            # Convert the results into a DataFrame
            df = pd.DataFrame(result['data'])
            self.visualize_stats(df)
        else:
            print("Failed to retrieve or parse results.")

if __name__ == "__main__":
    # Example usage
    API_KEY = "YOUR_DUNE_API_KEY"  # Replace with your actual Dune Analytics API key
    QUERY_ID = 123456  # Replace with your actual query ID
    
    dashboard = DuneAnalyticsDashboard(API_KEY)
    dashboard.run_dashboard(QUERY_ID)
```
