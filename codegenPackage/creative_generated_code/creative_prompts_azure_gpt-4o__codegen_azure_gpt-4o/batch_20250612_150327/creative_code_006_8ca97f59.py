"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy-dashboard.pages.dev
Prompt: Develop a script to monitor and alert users about changes in APY for vaults listed on Beefy Finance's platform.
Generated: DETERMINISTIC_8ca97f59de6848f4
Batch ID: 20250612_150327
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
import logging

# Setup logging for the script
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("apy_monitor.log"),
        logging.StreamHandler()
    ]
)

# Constants
BEEFY_API_URL = "https://api.beefy.finance/vaults"
CHECK_INTERVAL = 300  # Time interval in seconds to recheck for changes (5 minutes)
APY_THRESHOLD_CHANGE = 0.01  # Threshold to alert if APY changes by more than 1%

# Previous vault APY state
previous_apy_data = {}

def fetch_vaults_data():
    """
    Fetch vault data from Beefy Finance API.
    Returns:
        list: A list of vault data dictionaries.
    """
    try:
        response = requests.get(BEEFY_API_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching vault data: {e}")
        return []

def monitor_apy_changes(vault_data):
    """
    Monitor APY changes for vaults and log alerts if APY changes exceed the threshold.

    Args:
        vault_data (list): List of vault dictionaries containing APY information.
    """
    global previous_apy_data
    
    for vault in vault_data:
        try:
            vault_id = vault.get('id')
            current_apy = vault.get('apy')

            if not vault_id or current_apy is None:
                # Skip vaults with missing data
                logging.warning(f"Missing data for vault: {vault}")
                continue

            # Initialize previous APY data if not already set
            if vault_id not in previous_apy_data:
                previous_apy_data[vault_id] = current_apy

            previous_apy = previous_apy_data[vault_id]

            # Calculate change in APY
            apy_change = abs(current_apy - previous_apy)

            if apy_change >= APY_THRESHOLD_CHANGE:
                logging.info(f"Significant APY change detected for vault '{vault_id}': "
                             f"Previous APY = {previous_apy:.2f}, Current APY = {current_apy:.2f}, Change = {apy_change:.2f}")

            # Update the previous APY to the current value
            previous_apy_data[vault_id] = current_apy
        
        except Exception as e:
            logging.error(f"Error processing vault '{vault.get('id')}': {e}")

def main():
    """
    Main script execution loop. Monitors APY changes at regular intervals.
    """
    logging.info("Starting Beefy Finance APY monitor script...")

    while True:
        logging.info("Fetching latest vault data...")
        vault_data = fetch_vaults_data()

        if vault_data:
            logging.info("Checking for APY changes...")
            monitor_apy_changes(vault_data)
        else:
            logging.warning("No vault data received. Skipping this check.")

        logging.info(f"Sleeping for {CHECK_INTERVAL} seconds...")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
```
