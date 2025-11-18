"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pawthereum.pages.dev
Prompt: Develop a Python application using the Pawthereum contract address to track donations made to charities and display the total amount donated in real-time.
Generated: DETERMINISTIC_fd5d97afdfa2e5b0
Batch ID: 20250612_152235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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

# Constants
PAWTHEREUM_CONTRACT_ADDRESS = '0xYourPawthereumContractAddress'  # Replace with actual contract address
ETHERSCAN_API_KEY = 'YourEtherscanAPIKey'  # Replace with your Etherscan API Key
ETHERSCAN_API_URL = 'https://api.etherscan.io/api'

# Function to get the total donations from the Pawthereum contract
def get_total_donations():
    """
    Fetch the total donations made to the Pawthereum contract from the Etherscan API.
    
    Returns:
        float: Total amount of donations in Ether or None if an error occurs.
    """
    try:
        # Etherscan API parameters
        params = {
            'module': 'account',
            'action': 'balance',
            'address': PAWTHEREUM_CONTRACT_ADDRESS,
            'tag': 'latest',
            'apikey': ETHERSCAN_API_KEY
        }

        # Make a GET request to Etherscan API
        response = requests.get(ETHERSCAN_API_URL, params=params)
        response_data = response.json()

        # Check if the response is successful
        if response_data['status'] == '1':
            balance_wei = int(response_data['result'])  # Balance in Wei
            balance_eth = balance_wei / 10**18  # Convert Wei to Ether
            return balance_eth
        else:
            print(f"Error fetching data: {response_data['message']}")
            return None

    except requests.RequestException as e:
        print(f"Network error occurred: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_donations():
    """
    Periodically fetch and display the total donations made to the Pawthereum contract.
    """
    try:
        while True:
            total_donations = get_total_donations()
            if total_donations is not None:
                print(f"Total Donations to Pawthereum: {total_donations:.4f} ETH")
            else:
                print("Could not retrieve total donations.")

            time.sleep(60)  # Wait for 1 minute before the next update

    except KeyboardInterrupt:
        print("\nStopped tracking donations.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    display_donations()
```

**Note:** Replace `'0xYourPawthereumContractAddress'` and `'YourEtherscanAPIKey'` with the actual Pawthereum contract address and your Etherscan API key. This application will fetch and display the total donations made to the specified contract every minute.
