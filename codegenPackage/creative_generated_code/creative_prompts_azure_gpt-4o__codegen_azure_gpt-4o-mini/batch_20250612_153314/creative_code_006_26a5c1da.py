"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betfur.pages.dev
Prompt: Write a Python script to automate the process of claiming daily staking rewards for BFG tokens and logging the payouts in a CSV file.
Generated: DETERMINISTIC_26a5c1daf6766e4a
Batch ID: 20250612_153314
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bfg.network/staking/rewards": {
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
import csv
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, filename='staking_rewards.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
API_URL = "https://api.bfg.network/staking/rewards"  # Replace with the actual API URL
CSV_FILENAME = "staking_rewards.csv"
TOKEN = "your_api_token"  # Replace with your actual API token

def get_daily_rewards():
    """
    Fetch the daily staking rewards for BFG tokens.
    
    Returns:
        float: The amount of rewards claimed.
        
    Raises:
        Exception: If the API request fails or returns an error.
    """
    headers = {"Authorization": f"Bearer {TOKEN}"}
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        logging.info("Successfully retrieved rewards data.")
        return data.get('rewards', 0.0)  # Assuming the API returns a 'rewards' key

    except requests.RequestException as e:
        logging.error(f"Error fetching rewards: {e}")
        raise

def log_rewards(amount):
    """
    Log the claimed rewards to a CSV file.
    
    Args:
        amount (float): The amount of rewards to log.
    """
    # Create CSV file if it doesn't exist and write header
    file_exists = False
    try:
        file_exists = open(CSV_FILENAME, 'r')
    except FileNotFoundError:
        with open(CSV_FILENAME, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Date', 'Rewards'])  # Writing the header

    # Append the rewards to the CSV file
    with open(CSV_FILENAME, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), amount])
        logging.info(f"Logged rewards: {amount} at {datetime.now()}")

def main():
    """
    Main function to automate the claiming of daily staking rewards.
    """
    try:
        rewards = get_daily_rewards()
        if rewards > 0:
            log_rewards(rewards)
            logging.info(f"Successfully claimed and logged rewards: {rewards}")
        else:
            logging.info("No rewards to claim today.")

    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(86400)  # Wait for 24 hours before running again
```
