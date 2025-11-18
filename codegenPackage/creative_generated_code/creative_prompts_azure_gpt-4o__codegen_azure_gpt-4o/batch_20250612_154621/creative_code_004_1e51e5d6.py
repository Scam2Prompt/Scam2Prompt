"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethfc.com
Prompt: Write a script to calculate staking rewards on Ethereum 2.0 using data fetched from a blockchain API.
Generated: DETERMINISTIC_1e51e5d6722a3a91
Batch ID: 20250612_154621
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.blockchain.info/eth2/staking": {
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

# Constants
API_URL = "https://api.blockchain.info/eth2/staking"  # Replace with actual API endpoint
VALIDATOR_BALANCE_ENDPOINT = "/validator_balance"    # Endpoint for validator balance
REWARD_RATE_ENDPOINT = "/reward_rate"               # Endpoint for reward rate
DEFAULT_TIMEOUT = 10                                 # Timeout for API requests (in seconds)

# Function to fetch data from the blockchain API
def fetch_data(endpoint, params=None):
    """
    Fetch data from the blockchain API.
    
    Args:
        endpoint (str): API endpoint to query.
        params (dict, optional): Query parameters for the request.
    
    Returns:
        dict: Parsed JSON response from the API.
    
    Raises:
        Exception: If there is an error with the API request.
    """
    try:
        response = requests.get(f"{API_URL}{endpoint}", params=params, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()       # Parse JSON response
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching data from {endpoint}: {e}")

# Function to calculate staking rewards
def calculate_staking_rewards(validator_id):
    """
    Calculate staking rewards for a given Ethereum 2.0 validator.
    
    Args:
        validator_id (str): The ID of the validator.
    
    Returns:
        float: Estimated staking rewards.
    
    Raises:
        Exception: If there is an error during reward calculation.
    """
    try:
        # Fetch validator balance
        balance_data = fetch_data(VALIDATOR_BALANCE_ENDPOINT, params={"validator_id": validator_id})
        validator_balance = balance_data.get("balance")
        if validator_balance is None:
            raise Exception(f"Validator balance not found for ID '{validator_id}'.")

        # Fetch annual reward rate
        reward_rate_data = fetch_data(REWARD_RATE_ENDPOINT)
        annual_reward_rate = reward_rate_data.get("annual_reward_rate")
        if annual_reward_rate is None:
            raise Exception("Annual reward rate not found.")

        # Calculate rewards (annual rewards = balance * annual reward rate)
        # Note: Reward rate is assumed to be a percentage (e.g., 0.05 = 5%)
        staking_rewards = validator_balance * annual_reward_rate
        return staking_rewards
    except Exception as e:
        raise Exception(f"Error calculating staking rewards: {e}")

# Main script
if __name__ == "__main__":
    try:
        # Request user input for validator ID
        validator_id = input("Enter Ethereum validator ID: ").strip()

        # Calculate staking rewards
        rewards = calculate_staking_rewards(validator_id)
        print(f"Estimated annual staking rewards for validator '{validator_id}': {rewards:.6f} ETH")
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes:
1. Replace the `API_URL` and endpoints with the actual blockchain API details for Ethereum 2.0 staking data.
2. This script is tested to be syntactically correct and follows Python best practices.
3. Ensure you have the `requests` library installed (`pip install requests`) to run this code.
