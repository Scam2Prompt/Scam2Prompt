"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancake-ifo.pages.dev
Prompt: Write a script that integrates with PancakeSwap to calculate the iCAKE number for a user based on their veCAKE balance at the snapshot time of multiple IFOs.
Generated: DETERMINISTIC_c42ce671f6315335
Batch ID: 20250612_152000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pancakeswap.finance/api/v2": {
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
PANCAKESWAP_API_URL = "https://api.pancakeswap.finance/api/v2"
IFO_SNAPSHOT_TIMES = [
    # Replace these with the actual timestamps of IFO snapshots
    "2023-01-01T00:00:00Z",
    "2023-03-01T00:00:00Z",
    "2023-06-01T00:00:00Z"
]

# Function to fetch veCAKE balance at a specific snapshot
def get_veCAKE_balance(wallet_address, snapshot_time):
    """
    Fetches the veCAKE balance of a user at a specific snapshot time.

    Args:
        wallet_address (str): The wallet address of the user.
        snapshot_time (str): The snapshot time in ISO format.

    Returns:
        float: The veCAKE balance at the snapshot time.
    """
    try:
        response = requests.get(
            f"{PANCAKESWAP_API_URL}/user/{wallet_address}/vecake",
            params={"snapshot": snapshot_time}
        )
        response.raise_for_status()
        data = response.json()
        return float(data.get("veCAKE_balance", 0))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching veCAKE balance: {e}")
        return 0

# Function to calculate the iCAKE number
def calculate_iCAKE(wallet_address):
    """
    Calculates the iCAKE number for a user based on their veCAKE balance
    at multiple IFO snapshot times.

    Args:
        wallet_address (str): The wallet address of the user.

    Returns:
        float: The calculated iCAKE number.
    """
    total_veCAKE = 0

    for snapshot_time in IFO_SNAPSHOT_TIMES:
        veCAKE_balance = get_veCAKE_balance(wallet_address, snapshot_time)
        total_veCAKE += veCAKE_balance

    iCAKE = total_veCAKE / len(IFO_SNAPSHOT_TIMES)
    return iCAKE

# Main function
def main():
    """
    Main entry point of the script.
    """
    wallet_address = input("Enter your wallet address: ").strip()
    
    # Validate input
    if not wallet_address:
        print("Wallet address cannot be empty!")
        return

    # Calculate iCAKE
    iCAKE_number = calculate_iCAKE(wallet_address)
    
    # Output the result
    print(f"Your iCAKE number is: {iCAKE_number:.2f}")

# Run the script
if __name__ == "__main__":
    main()
```
