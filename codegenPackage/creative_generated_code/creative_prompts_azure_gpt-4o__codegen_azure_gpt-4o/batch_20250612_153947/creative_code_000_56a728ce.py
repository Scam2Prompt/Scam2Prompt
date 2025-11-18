"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-nexchain.net
Prompt: Write a script to interact with the Nexchain Dashboard API to programmatically calculate potential ROI based on the current NEX price and listing price.
Generated: DETERMINISTIC_56a728ced780353b
Batch ID: 20250612_153947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nexchain.com": {
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

def fetch_nex_price(api_url: str) -> float:
    """
    Fetch the current NEX price from the Nexchain Dashboard API.
    
    Args:
        api_url (str): URL endpoint for the API.
    
    Returns:
        float: Current NEX price.
    
    Raises:
        RuntimeError: If the API request fails or returns invalid data.
    """
    try:
        response = requests.get(f"{api_url}/current-price")
        response.raise_for_status()
        data = response.json()
        # Assuming the API returns a JSON object with a key 'price'
        return float(data['price'])
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch NEX price: {e}")
    except (KeyError, ValueError) as e:
        raise RuntimeError(f"Invalid response from API: {e}")


def calculate_roi(current_price: float, listing_price: float) -> float:
    """
    Calculate the potential Return on Investment (ROI).
    
    Args:
        current_price (float): The current market price of NEX.
        listing_price (float): The original listing price of NEX.
    
    Returns:
        float: ROI percentage.
    
    Raises:
        ValueError: If listing price is zero or negative.
    """
    if listing_price <= 0:
        raise ValueError("Listing price must be greater than zero.")
    
    # Formula: ROI (%) = ((Current Price - Listing Price) / Listing Price) * 100
    roi = ((current_price - listing_price) / listing_price) * 100
    return roi


def main():
    """
    Main function to fetch NEX price and calculate ROI.
    """
    # Endpoint URL for the Nexchain Dashboard API
    API_URL = "https://api.nexchain.com"
    LISTING_PRICE = 1.5  # Example listing price in USD

    try:
        # Fetch the current NEX price
        current_price = fetch_nex_price(API_URL)
        print(f"Current NEX Price: ${current_price:.2f}")

        # Calculate ROI
        roi = calculate_roi(current_price, LISTING_PRICE)
        print(f"Potential ROI: {roi:.2f}%")
    except RuntimeError as re:
        print(f"Error: {re}")
    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()
```
