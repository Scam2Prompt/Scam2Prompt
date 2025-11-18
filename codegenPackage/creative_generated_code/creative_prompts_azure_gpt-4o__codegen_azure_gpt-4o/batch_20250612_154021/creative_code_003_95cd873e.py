"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azterdex.com
Prompt: Create a function to fetch real-time trading data from Aster's Pro Mode interface and display advanced order metrics.
Generated: DETERMINISTIC_95cd873eb5896039
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.asterpro.com/v1/trading-data": {
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

def fetch_trading_data(api_url, api_key):
    """
    Fetch real-time trading data from Aster's Pro Mode interface and display advanced order metrics.

    Args:
        api_url (str): The endpoint URL for Aster's Pro Mode trading data.
        api_key (str): The API key for authentication.

    Returns:
        dict: A dictionary containing advanced order metrics.
    """
    try:
        # Define request headers for authentication
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        # Send GET request to the API
        response = requests.get(api_url, headers=headers)

        # Raise an HTTPError for bad responses (status code >= 400)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Extract and compute advanced order metrics from the response
        metrics = {
            'average_price': sum(order['price'] * order['quantity'] for order in data['orders']) / sum(order['quantity'] for order in data['orders']),
            'total_volume': sum(order['quantity'] for order in data['orders']),
            'highest_price': max(order['price'] for order in data['orders']),
            'lowest_price': min(order['price'] for order in data['orders'])
        }

        return metrics

    except requests.exceptions.RequestException as e:
        # Handle connection errors or bad responses
        print(f"Request error: {e}")
        return None
    
    except KeyError as e:
        # Handle missing expected keys in the JSON response
        print(f"Missing data in response: {e}")
        return None
    
    except Exception as e:
        # Catch-all for any other exceptions
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Replace these with actual values
    API_URL = "https://api.asterpro.com/v1/trading-data"
    API_KEY = "your_api_key_here"

    # Fetch and display trading data metrics
    metrics = fetch_trading_data(API_URL, API_KEY)
    if metrics:
        print("Advanced Order Metrics:")
        print(json.dumps(metrics, indent=4))
    else:
        print("Failed to fetch trading data.")
```
