"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy-v2.vercel.app
Prompt: Generate a Python script to track the performance of multiple Beefy Finance vaults over time using their API data.
Generated: DETERMINISTIC_e6a6848a8cb6b4bf
Batch ID: 20250612_145933
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.beefy.finance/vaults": {
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
import time
import json
from datetime import datetime
import os

# Constants for the Beefy API and configuration
BEEFY_API_URL = "https://api.beefy.finance/vaults"  # URL to fetch vault data
TRACKED_VAULTS = ["vault1", "vault2", "vault3"]  # Replace with actual vault IDs
DATA_SAVE_PATH = "beefy_vault_tracking.json"  # File to save performance data
REFRESH_INTERVAL_SECONDS = 300  # Interval to fetch data (e.g., every 5 min)

def fetch_beefy_vaults():
    """
    Fetch the latest data from Beefy's API.
    
    Returns:
        list: List of vault data dictionaries if successful, else None.
    """
    try:
        response = requests.get(BEEFY_API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching Beefy API data: {e}")
        return None

def track_vault_performance(vault_data, tracked_vaults):
    """
    Extract performance metrics for tracked vaults from API data.
    
    Args:
        vault_data (list): List of all vault data from API.
        tracked_vaults (list): List of vault IDs to track.

    Returns:
        dict: Dictionary of tracked vault performance metrics.
    """
    performance_data = {}
    for vault in vault_data:
        if vault.get("id") in tracked_vaults:
            performance_data[vault["id"]] = {
                "name": vault.get("name", "Unknown"),
                "apy": vault.get("apy", "N/A"),
                "tvl": vault.get("tvl", "N/A"),
                "timestamp": datetime.utcnow().isoformat(),
            }
    return performance_data

def save_performance_data(data, file_path):
    """
    Save performance data to a JSON file.
    
    Args:
        data (dict): Data to save.
        file_path (str): Path to the file.
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                existing_data = json.load(file)
        else:
            existing_data = {}

        # Append new data to existing data
        for vault_id, metrics in data.items():
            if vault_id not in existing_data:
                existing_data[vault_id] = []
            existing_data[vault_id].append(metrics)
        
        with open(file_path, "w") as file:
            json.dump(existing_data, file, indent=4)
    except Exception as e:
        print(f"Error saving performance data: {e}")

def main():
    """
    Main function to run the vault performance tracking script.
    """
    print("Starting Beefy Finance vault performance tracking...")
    while True:
        # Fetch data from Beefy API
        vault_data = fetch_beefy_vaults()
        if vault_data is None:
            print("Failed to fetch vault data. Retrying in next interval.")
            time.sleep(REFRESH_INTERVAL_SECONDS)
            continue

        # Track performance of specific vaults
        performance_data = track_vault_performance(vault_data, TRACKED_VAULTS)
        if performance_data:
            print(f"Fetched data for tracked vaults at {datetime.utcnow().isoformat()}")
            save_performance_data(performance_data, DATA_SAVE_PATH)
        else:
            print("No tracked vaults found in the fetched data.")

        print(f"Sleeping for {REFRESH_INTERVAL_SECONDS} seconds...")
        time.sleep(REFRESH_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
```
