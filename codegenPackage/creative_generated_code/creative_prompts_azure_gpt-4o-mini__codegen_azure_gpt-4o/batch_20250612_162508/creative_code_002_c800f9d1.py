"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jup-dca-ui.vercel.app
Prompt: Provide an example of using the Jupiter DCA API to implement a time-locked DCA strategy.
Generated: DETERMINISTIC_c800f9d1130badde
Batch ID: 20250612_162508
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.jup.ag/v4": {
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
import time
import requests
import json
from datetime import datetime, timedelta

# Constants
API_BASE_URL = "https://api.jup.ag/v4"
DCA_INTERVAL_MIN = 60  # Time interval between purchases in minutes
DCA_TOTAL_DURATION_HOURS = 24  # Total duration for DCA in hours
SOURCE_TOKEN = "USDC"  # Token the user is selling
DESTINATION_TOKEN = "SOL"  # Token the user is buying
AMOUNT_PER_SWAP = 10.0  # Amount of SOURCE_TOKEN to swap per interval
USER_PUBLIC_KEY = "YOUR_PUBLIC_KEY_HERE"  # User's wallet public key

# Error handling class
class DCAError(Exception):
    pass

# Function to perform the swap using the Jupiter DCA API
def perform_swap(source_token, destination_token, amount, user_public_key):
    try:
        # Build the swap request payload
        payload = {
            "inputMint": source_token,
            "outputMint": destination_token,
            "amount": amount,
            "userPublicKey": user_public_key
        }
        # Send the request to Jupiter API
        response = requests.post(f"{API_BASE_URL}/quote", json=payload)

        # Check for errors in response
        if response.status_code != 200:
            raise DCAError(f"Error fetching quote: {response.json().get('error', 'Unknown error')}")

        # Extract the quote information
        quote = response.json()
        swap_transaction = quote["swapTransaction"]

        # Submit the swap transaction
        tx_response = requests.post(f"{API_BASE_URL}/swap", json={"swapTransaction": swap_transaction})
        
        # Check for errors in transaction submission
        if tx_response.status_code != 200:
            raise DCAError(f"Error submitting swap: {tx_response.json().get('error', 'Unknown error')}")

        print(f"Swap successful at {datetime.now()}: {amount} {source_token} -> {destination_token}")
    except Exception as e:
        print(f"An error occurred during the swap: {e}")

# Function to execute the DCA strategy
def execute_dca_strategy():
    try:
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=DCA_TOTAL_DURATION_HOURS)

        print(f"DCA Strategy started at {start_time}. Will end at {end_time}.")
        
        while datetime.now() < end_time:
            perform_swap(SOURCE_TOKEN, DESTINATION_TOKEN, AMOUNT_PER_SWAP, USER_PUBLIC_KEY)
            
            print(f"Waiting {DCA_INTERVAL_MIN} minutes for the next swap...")
            time.sleep(DCA_INTERVAL_MIN * 60)  # Wait for the next interval

        print("DCA Strategy completed.")
    except Exception as e:
        print(f"An error occurred while executing DCA strategy: {e}")

# Entry point for the script
if __name__ == "__main__":
    execute_dca_strategy()
```
