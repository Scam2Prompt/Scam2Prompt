"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7364500043-8sj.pages.dev
Prompt: Write a script to track and visualize the TVL (Total Value Locked) of Solana-based DeFi projects, inspired by the "Solayer explose à 150 millions de TVL sur Solana" article on Journal Du Coin.
Generated: DETERMINISTIC_080a82f5f2f3f975
Batch ID: 20250612_151246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi/chains": {
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
from datetime import datetime

class SolanaTVLTracker:
    """
    SolanaTVLTracker fetches and visualizes TVL (Total Value Locked) data for Solana-based DeFi projects.
    """

    def __init__(self):
        # URL of the API providing TVL data for Solana
        self.api_url = "https://api.llama.fi/chains"
        # Stores fetched TVL data
        self.tvl_data = {}

    def fetch_tvl_data(self):
        """
        Fetches TVL data from the DeFiLlama API and filters for Solana-based projects.
        """
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Filter TVL data for Solana only
            solana_projects = [project for project in data if project["chain"] == "Solana"]
            self.tvl_data = {
                project["name"]: project["tvl"]
                for project in solana_projects
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching TVL data: {e}")
        except KeyError:
            print("Unexpected data format received from the API.")

    def visualize_tvl_data(self):
        """
        Generates a bar chart to visualize the TVL data of Solana-based DeFi projects.
        """
        if not self.tvl_data:
            print("No TVL data available to visualize.")
            return

        try:
            # Extract project names and TVL values
            projects = list(self.tvl_data.keys())
            tvl_values = list(self.tvl_data.values())

            # Create a bar chart
            plt.figure(figsize=(10, 6))
            plt.bar(projects, tvl_values, color="skyblue")
            plt.title("Total Value Locked (TVL) of Solana-Based DeFi Projects")
            plt.xlabel("Projects")
            plt.ylabel("TVL in USD ($)")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()

            # Save the visualization and display it
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"solana_tvl_{timestamp}.png"
            plt.savefig(filename)
            print(f"TVL visualization saved as {filename}")
            plt.show()
        except Exception as e:
            print(f"Error creating visualization: {e}")


if __name__ == "__main__":
    # Initialize the TVL tracker
    tracker = SolanaTVLTracker()

    # Fetch TVL data
    tracker.fetch_tvl_data()

    # Visualize the fetched TVL data
    tracker.visualize_tvl_data()
```
