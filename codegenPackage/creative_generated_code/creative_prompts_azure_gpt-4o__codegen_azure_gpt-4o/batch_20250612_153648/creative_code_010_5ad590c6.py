"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: Generate a Python script using Pyth's off-chain API to fetch and display the latest price data for commodities like XAG/USD.
Generated: DETERMINISTIC_5ad590c6b1334adc
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pyth.network/v1/": {
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

def fetch_pyth_price(product_id, api_url="https://api.pyth.network/v1/"):
    """
    Fetch the latest price data for a commodity using Pyth's off-chain API.

    Parameters:
        product_id (str): The product ID for the commodity (e.g., "XAG/USD").
        api_url (str): The base URL of the Pyth off-chain API.

    Returns:
        dict: A dictionary containing the latest price information.
    """
    try:
        # Construct the endpoint URL to fetch price data for a specific product ID
        endpoint = f"{api_url}/prices/{product_id}"

        # Make a GET request to the Pyth API
        response = requests.get(endpoint)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Parse the JSON response
        price_data = response.json()

        # Return the price data
        return price_data

    except requests.exceptions.RequestException as e:
        # Handle HTTP-related exceptions
        print(f"An error occurred while fetching price data: {e}")
        return None
    except ValueError as e:
        # Handle JSON parsing exceptions
        print(f"An error occurred while parsing the response data: {e}")
        return None


def display_price_data(price_data):
    """
    Display the latest price data for a commodity in a readable format.

    Parameters:
        price_data (dict): The price data dictionary fetched from Pyth's API.
    """
    if not price_data:
        print("No price data available to display.")
        return

    try:
        # Extract relevant details from the price data
        product_id = price_data.get("id", "Unknown Product ID")
        price = price_data.get("price", {}).get("price", "Unknown Price")
        status = price_data.get("price", {}).get("status", "Unknown Status")
        updated_at = price_data.get("price", {}).get("publishTime", "Unknown Time")

        # Display the price information
        print(f"Product ID: {product_id}")
        print(f"Latest Price: {price}")
        print(f"Status: {status}")
        print(f"Last Updated At: {updated_at}")

    except KeyError as e:
        # Handle missing keys in the price data
        print(f"An error occurred while displaying price data: {e}")


def main():
    """
    Main function to fetch and display the latest price data for commodities.
    """
    # Replace "XAG/USD" with the desired commodity product ID
    product_id = "XAG/USD"

    # Fetch the latest price data from Pyth's API
    price_data = fetch_pyth_price(product_id)

    # Display the fetched price data
    display_price_data(price_data)


if __name__ == "__main__":
    # Entry point of the script
    main()
```
