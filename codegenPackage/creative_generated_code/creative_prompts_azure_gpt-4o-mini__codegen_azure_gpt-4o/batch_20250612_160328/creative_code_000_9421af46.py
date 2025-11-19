"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.solanary.com
Prompt: Write a Python script to interact with the Solanary API for participating in the SOL lottery with multiple prize pools.
Generated: DETERMINISTIC_9421af46b3a70744
Batch ID: 20250612_160328
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.solanary.com/v1": {
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

# Constants
BASE_URL = "https://api.solanary.com/v1"  # Replace with actual Solanary API URL
API_KEY = "your_api_key_here"  # Replace with your API key
LOTTERY_ENDPOINT = "/lottery"  # Endpoint for lottery interaction
TIMEOUT = 10  # Timeout (in seconds) for API requests

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_lottery_info():
    """
    Fetches the details of available prize pools in the SOL lottery.

    Returns:
        dict: Lottery details or an error message.
    """
    try:
        response = requests.get(f"{BASE_URL}{LOTTERY_ENDPOINT}", headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def participate_in_lottery(pool_id, amount):
    """
    Participates in the SOL lottery in a specific prize pool.

    Args:
        pool_id (str): ID of the prize pool to participate in.
        amount (float): Amount of SOL to participate with.

    Returns:
        dict: Response from the API or an error message.
    """
    payload = {
        "pool_id": pool_id,
        "amount": amount
    }

    try:
        response = requests.post(f"{BASE_URL}{LOTTERY_ENDPOINT}/participate", 
                                 headers=HEADERS, json=payload, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def main():
    """
    Main function to interact with the SOL lottery API.
    """
    print("Fetching lottery information...")
    lottery_info = get_lottery_info()
    
    if "error" in lottery_info:
        print(f"Error fetching lottery info: {lottery_info['error']}")
        return
    
    print("Available prize pools:")
    for pool in lottery_info.get("prize_pools", []):
        print(f"Pool ID: {pool['id']}, Prize: {pool['prize']} SOL, Entry Fee: {pool['entry_fee']} SOL")

    pool_id = input("Enter the Pool ID you want to participate in: ").strip()
    amount = input("Enter the amount of SOL to participate with: ").strip()

    try:
        amount = float(amount)
        print("Submitting participation request...")
        result = participate_in_lottery(pool_id, amount)
        
        if "error" in result:
            print(f"Error participating in lottery: {result['error']}")
        else:
            print("Participation successful! Response:")
            print(json.dumps(result, indent=4))
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")

if __name__ == "__main__":
    main()
```
