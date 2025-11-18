"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tron-presents.blogspot.com
Prompt: Write a script to query the Tron blockchain for the latest block information using TronGrid API.
Generated: DETERMINISTIC_0b7513d4dbd489af
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.trongrid.io/v1/blocks": {
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

# Configurations
TRONGRID_API_URL = "https://api.trongrid.io/v1/blocks"
TIMEOUT_SECONDS = 10  # Timeout for API requests

def fetch_latest_block():
    """
    Fetches the latest block information from the Tron blockchain using the TronGrid API.
    
    Returns:
        dict: A dictionary containing the latest block information.
    
    Raises:
        RuntimeError: If the API request fails or returns an error response.
    """
    try:
        # Send a GET request to the TronGrid API to fetch the latest block
        response = requests.get(f"{TRONGRID_API_URL}?limit=1", timeout=TIMEOUT_SECONDS)
        
        # Check if the response status code indicates success
        if response.status_code == 200:
            # Parse the JSON response from the API
            data = response.json()
            
            # Ensure the response contains block data
            if 'data' in data and len(data['data']) > 0:
                # Return the latest block information
                return data['data'][0]
            else:
                raise RuntimeError("No block data found in the API response.")
        else:
            raise RuntimeError(f"API request failed with status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        # Handle networking or timeout errors
        raise RuntimeError(f"An error occurred while connecting to the API: {str(e)}")
    
def main():
    """
    Main function to fetch and display the latest block information.
    """
    try:
        # Fetch the latest block info
        latest_block = fetch_latest_block()
        
        # Display the block information
        print("Latest Block Information:")
        print(f"Block Number: {latest_block.get('number')}")
        print(f"Block Hash: {latest_block.get('hash')}")
        print(f"Timestamp: {latest_block.get('timestamp')}")
        print(f"Transactions Count: {latest_block.get('transactions_count')}")
    except RuntimeError as error:
        # Handle errors gracefully
        print(f"Error: {error}")

if __name__ == "__main__":
    # Run the main function
    main()
```
