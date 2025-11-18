"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedshibainu-com.pages.dev
Prompt: Write a function in Python to fetch and display the current price chart of Based Shiba Inu tokens using data from the BASE blockchain.
Generated: DETERMINISTIC_565c30d6ea572a58
Batch ID: 20250612_153401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.base-blockchain.com": {
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
import matplotlib.pyplot as plt
import datetime


def fetch_based_shiba_inu_price_chart(api_url: str, token_id: str):
    """
    Fetch and display the current price chart for Based Shiba Inu tokens using data from the BASE blockchain.

    Args:
        api_url (str): The URL of the blockchain price data API.
        token_id (str): The unique identifier for the Based Shiba Inu token.

    Raises:
        Exception: If the API request fails or the response data is invalid.
    """
    try:
        # Fetch price history data from the API
        response = requests.get(f"{api_url}/price-history/{token_id}")
        response.raise_for_status()  # Raise an HTTPError for bad responses (e.g., 4xx and 5xx)

        # Parse the JSON response
        data = response.json()

        if "prices" not in data or not data["prices"]:
            raise ValueError("Price data not found in the response.")

        # Extract timestamp and price data
        timestamps = [datetime.datetime.fromtimestamp(price_point["timestamp"]) for price_point in data["prices"]]
        prices = [price_point["price"] for price_point in data["prices"]]

        # Plot the price chart
        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, prices, label="Based Shiba Inu Price", color="blue")
        plt.title("Based Shiba Inu Token Price Chart")
        plt.xlabel("Time")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Display the chart
        plt.show()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching price data: {e}")
    except ValueError as e:
        print(f"Data error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Replace with the actual API URL and token ID for Based Shiba Inu
    API_URL = "https://api.base-blockchain.com"
    TOKEN_ID = "based-shiba-inu"

    fetch_based_shiba_inu_price_chart(API_URL, TOKEN_ID)
```
