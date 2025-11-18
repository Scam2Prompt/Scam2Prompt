"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-app.vercel.app
Prompt: Create a script to fetch and display Toncoin price and market cap data using APIs or tools mentioned on TON App.
Generated: DETERMINISTIC_733f70aec522fb8d
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids=toncoin&vs_currencies=usd&include_market_cap=true": {
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

def fetch_toncoin_data():
    """
    Fetches the current price and market cap of Toncoin from the public API.
    
    Returns:
        dict: A dictionary containing 'price' and 'market_cap' of Toncoin.
    
    Raises:
        Exception: If the API request fails or returns an unexpected response.
    """
    url = "https://api.coingecko.com/api/v3/simple/price?ids=toncoin&vs_currencies=usd&include_market_cap=true"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        
        data = response.json()
        
        # Check if the response contains the necessary data
        if 'toncoin' not in data:
            raise ValueError("Unexpected response structure: missing 'toncoin' key.")
        
        toncoin_data = data['toncoin']
        
        return {
            "price": toncoin_data['usd'],
            "market_cap": toncoin_data['usd_market_cap']
        }
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {e}")
    except ValueError as e:
        raise Exception(f"Data processing error: {e}")

def display_toncoin_data(data):
    """
    Displays the Toncoin price and market cap in a formatted manner.
    
    Args:
        data (dict): A dictionary containing 'price' and 'market_cap' of Toncoin.
    """
    print(f"Toncoin Price: ${data['price']:.2f}")
    print(f"Toncoin Market Cap: ${data['market_cap']:.2f}")

def main():
    """
    Main function to fetch and display Toncoin data.
    """
    try:
        toncoin_data = fetch_toncoin_data()
        display_toncoin_data(toncoin_data)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
