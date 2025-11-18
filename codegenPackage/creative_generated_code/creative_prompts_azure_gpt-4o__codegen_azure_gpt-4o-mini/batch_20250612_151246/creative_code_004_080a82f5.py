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
  "https://api.coingecko.com/api/v3/simple/price": {
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
from datetime import datetime
import time

# Constants
API_URL = "https://api.coingecko.com/api/v3/simple/price"
SOLANA_PROJECTS = {
    "project_1": "project_1_coin_id",  # Replace with actual coin ID
    "project_2": "project_2_coin_id",  # Replace with actual coin ID
    "project_3": "project_3_coin_id",  # Replace with actual coin ID
}

# Function to fetch TVL for a given project
def fetch_tvl(project_id):
    try:
        response = requests.get(f"{API_URL}?ids={project_id}&vs_currencies=usd")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data[project_id]["usd"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching TVL for {project_id}: {e}")
        return None

# Main tracking function
def track_tvl(projects, interval=300):
    tvl_data = {project: [] for project in projects}
    timestamps = []

    try:
        while True:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            timestamps.append(current_time)

            for project, project_id in projects.items():
                tvl = fetch_tvl(project_id)
                if tvl is not None:
                    tvl_data[project].append(tvl)
                else:
                    tvl_data[project].append(None)  # Append None if TVL fetch fails

            # Sleep for the specified interval
            time.sleep(interval)

    except KeyboardInterrupt:
        print("Tracking stopped by user.")
        return pd.DataFrame(tvl_data, index=timestamps)

# Function to visualize the TVL data
def visualize_tvl(tvl_df):
    plt.figure(figsize=(12, 6))
    for project in tvl_df.columns:
        plt.plot(tvl_df.index, tvl_df[project], label=project)

    plt.title("Total Value Locked (TVL) of Solana DeFi Projects")
    plt.xlabel("Time")
    plt.ylabel("TVL (USD)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Execute the tracking and visualization process
if __name__ == "__main__":
    tvl_df = track_tvl(SOLANA_PROJECTS)
    visualize_tvl(tvl_df)
```

Make sure to replace the placeholder coin IDs in the `SOLANA_PROJECTS` dictionary with the actual CoinGecko IDs of the projects you want to track. The code fetches the TVL data every 5 minutes (300 seconds) and visualizes it in a line graph when tracking is stopped by the user.
