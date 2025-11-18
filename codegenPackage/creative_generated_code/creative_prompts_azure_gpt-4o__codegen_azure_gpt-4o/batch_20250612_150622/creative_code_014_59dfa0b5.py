"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://to-ousd.pages.dev
Prompt: Create a script to fetch and display the current OGV price, market cap, and circulating supply using the Origin Protocol APIs.
Generated: DETERMINISTIC_59dfa0b5cf845e01
Batch ID: 20250612_150622
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/origin-dollar-governance": {
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

def fetch_ogv_data():
    """
    Fetches the current OGV price, market cap, and circulating supply
    using the Origin Protocol APIs.

    Returns:
        dict: A dictionary containing OGV price, market cap, and circulating supply.
    """
    # Endpoint for the Origin Protocol OGV data
    url = "https://api.coingecko.com/api/v3/coins/origin-dollar-governance"

    try:
        # Make an HTTP GET request to fetch OGV data
        response = requests.get(url, timeout=10)
        
        # Raise an error if the response status code is not 200
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()

        # Extract relevant information
        ogv_price = data["market_data"]["current_price"]["usd"]
        market_cap = data["market_data"]["market_cap"]["usd"]
        circulating_supply = data["market_data"]["circulating_supply"]

        # Return the extracted data as a dictionary
        return {
            "price": ogv_price,
            "market_cap": market_cap,
            "circulating_supply": circulating_supply,
        }
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"Error: An issue occurred while making the request: {e}")
    except KeyError:
        print("Error: Unexpected response structure. Unable to extract data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Return None in case of failure
    return None

def display_ogv_data(data):
    """
    Displays OGV price, market cap, and circulating supply in a user-friendly format.

    Args:
        data (dict): A dictionary containing OGV price, market cap, and circulating supply.
    """
    if data:
        print("Origin Dollar Governance (OGV) Data:")
        print(f"Price (USD): ${data['price']:.2f}")
        print(f"Market Cap (USD): ${data['market_cap']:,}")
        print(f"Circulating Supply: {data['circulating_supply']:,} OGV")
    else:
        print("Failed to retrieve OGV data.")

if __name__ == "__main__":
    # Fetch OGV data
    ogv_data = fetch_ogv_data()

    # Display the data
    display_ogv_data(ogv_data)
```
