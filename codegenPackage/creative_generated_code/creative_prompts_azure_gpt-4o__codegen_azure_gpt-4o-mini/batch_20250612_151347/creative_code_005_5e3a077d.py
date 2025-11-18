"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pocketuniverseshield.com
Prompt: Create a script to implement real-time threat detection for Web3 assets using Pocket Universe Shield's security solutions.
Generated: DETERMINISTIC_5e3a077d0ed6a49b
Batch ID: 20250612_151347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pocketuniverse.com/shield": {
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
import time

class PocketUniverseShield:
    """Class to interact with Pocket Universe Shield's API for threat detection."""
    
    def __init__(self, api_key):
        """
        Initializes the PocketUniverseShield class with the API key.

        Args:
            api_key (str): Your Pocket Universe Shield API key.
        """
        self.api_key = api_key
        self.base_url = "https://api.pocketuniverse.com/shield"

    def check_asset_threat(self, asset_id):
        """
        Checks for threats associated with a given Web3 asset.

        Args:
            asset_id (str): The unique identifier of the Web3 asset to check.

        Returns:
            dict: The response from the Pocket Universe Shield API, containing threat data.

        Raises:
            Exception: Raises an error if the request fails.
        """
        url = f"{self.base_url}/threats/{asset_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def monitor_assets(self, asset_ids, check_interval=60):
        """
        Monitors a list of Web3 assets for threats in real time.

        Args:
            asset_ids (list): A list of asset IDs to monitor.
            check_interval (int): The interval (in seconds) to check for threats. Defaults to 60 seconds.
        """
        while True:
            for asset_id in asset_ids:
                try:
                    threat_data = self.check_asset_threat(asset_id)
                    self.handle_threat_data(asset_id, threat_data)
                except Exception as e:
                    print(f"Failed to check asset {asset_id}: {e}")
            time.sleep(check_interval)  # Wait for the specified interval

    def handle_threat_data(self, asset_id, threat_data):
        """
        Processes and logs the threat data for a specific asset.

        Args:
            asset_id (str): The ID of the asset being checked.
            threat_data (dict): The threat data returned from the API.
        """
        if threat_data.get("threats"):
            print(f"Threats detected for asset {asset_id}: {threat_data['threats']}")
            # Additional processing logic can be added here
        else:
            print(f"No threats detected for asset {asset_id}.")

if __name__ == "__main__":
    # Example usage
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    asset_ids_to_monitor = ["asset_id_1", "asset_id_2", "asset_id_3"]  # Replace with actual asset IDs

    shield = PocketUniverseShield(API_KEY)
    shield.monitor_assets(asset_ids_to_monitor, check_interval=120)  # Check every 120 seconds
```
