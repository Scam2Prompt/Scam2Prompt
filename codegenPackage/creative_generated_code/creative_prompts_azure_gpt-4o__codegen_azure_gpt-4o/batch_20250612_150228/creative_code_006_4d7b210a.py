"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifcwow526nmb3jgtqwbbbwh47es7somd24fymtwlttwxedvnbnhku.ipfs.dweb.link
Prompt: Create a script that retrieves the number of users who have migrated their tokens and calculates the total rewards distributed on the sky.money platform.
Generated: DETERMINISTIC_4d7b210a9e386a51
Batch ID: 20250612_150228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sky.money": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
API_BASE_URL = "https://api.sky.money"
MIGRATED_USERS_ENDPOINT = "/users/migrated"
REWARDS_ENDPOINT = "/rewards/total"

def get_migrated_users_count():
    """
    Fetch the number of users who have migrated their tokens.
    
    Returns:
        int: The number of migrated users.
    """
    try:
        response = requests.get(f"{API_BASE_URL}{MIGRATED_USERS_ENDPOINT}")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return data.get("count", 0)  # Default to 0 if count is not present
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching migrated users count: {e}")
        return 0

def get_total_rewards_distributed():
    """
    Fetch the total rewards distributed on the platform.
    
    Returns:
        float: The total rewards distributed.
    """
    try:
        response = requests.get(f"{API_BASE_URL}{REWARDS_ENDPOINT}")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return data.get("total_rewards", 0.0)  # Default to 0.0 if total_rewards is not present
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching total rewards distributed: {e}")
        return 0.0

def main():
    """
    Main function to retrieve and calculate data from the sky.money platform.
    """
    logging.info("Retrieving migrated users count...")
    migrated_users_count = get_migrated_users_count()
    logging.info(f"Number of migrated users: {migrated_users_count}")
    
    logging.info("Retrieving total rewards distributed...")
    total_rewards = get_total_rewards_distributed()
    logging.info(f"Total rewards distributed: {total_rewards}")

if __name__ == "__main__":
    main()
```
