"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepecoin.news
Prompt: Create a function that checks the status of the Xeggex exchange and reports if it is down or if any coins have been moved.
Generated: DETERMINISTIC_695a9b11e1b1f2b2
Batch ID: 20250612_160002
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.xeggex.com/v1/": {
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
from datetime import datetime

def check_xeggex_exchange_status():
    """
    Function to check the status of the Xeggex exchange.
    Reports if the exchange is down or if any coins have been moved.
    """
    # Xeggex API base URL
    base_url = "https://api.xeggex.com/v1/"
    
    try:
        # Check the exchange status endpoint
        response = requests.get(f"{base_url}status", timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        
        # Parse the response JSON
        status_data = response.json()
        
        # Convert the timestamp into a human-readable format if present
        last_updated = status_data.get("last_updated")
        if last_updated:
            last_updated = datetime.fromtimestamp(last_updated).strftime('%Y-%m-%d %H:%M:%S')
        
        # Check if the exchange is operational
        if status_data.get("operational", False):
            print(f"The Xeggex exchange is operational. (Last Updated: {last_updated})")
        else:
            print(f"The Xeggex exchange appears to be down or unavailable. (Last Updated: {last_updated})")
        
        # Check for coin movement (assuming an endpoint exists for coin movement tracking)
        coin_movement_response = requests.get(f"{base_url}coin-movements", timeout=10)
        coin_movement_response.raise_for_status()
        
        coin_movement_data = coin_movement_response.json()
        movements = coin_movement_data.get("movements", [])
        
        if movements:
            print("Coins have been moved on the Xeggex exchange:")
            for movement in movements:
                print(f"  - {movement.get('coin')} | Amount: {movement.get('amount')} | Time: {movement.get('timestamp')}")
        else:
            print("No coin movements detected on the Xeggex exchange.")
    
    except requests.exceptions.RequestException as e:
        # Handle network errors and HTTP-related errors
        print(f"Error while trying to access the Xeggex exchange: {str(e)}")
    except ValueError as ve:
        # Handle JSON decoding errors
        print(f"Error decoding response: {str(ve)}")
    except Exception as ex:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {str(ex)}")

# Example call to the function
if __name__ == "__main__":
    check_xeggex_exchange_status()
```
