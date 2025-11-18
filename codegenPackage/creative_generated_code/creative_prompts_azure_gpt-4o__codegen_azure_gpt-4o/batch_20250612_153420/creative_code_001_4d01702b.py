"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedrip-app.pages.dev
Prompt: Generate a script to look up faucet IDs and display $BDRIP token statistics, including price in $USDC and total supply.
Generated: DETERMINISTIC_4d01702bfbd9d4c7
Batch ID: 20250612_153420
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/tokens/bdrip/statistics": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/faucets/{faucet_id": {
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

def fetch_token_statistics(faucet_id):
    """
    Fetch token statistics for a given faucet ID.

    Args:
        faucet_id (str): The unique ID of the faucet.

    Returns:
        dict: A dictionary containing token statistics such as price in USDC and total supply.
    """
    try:
        # Base API URLs for faucet information and token statistics
        faucet_api = f"https://api.example.com/faucets/{faucet_id}"
        token_stats_api = f"https://api.example.com/tokens/bdrip/statistics"

        # Fetch faucet information
        faucet_response = requests.get(faucet_api)
        faucet_response.raise_for_status()  # Raise an exception for HTTP errors
        faucet_data = faucet_response.json()

        if not faucet_data.get("valid"):
            raise ValueError(f"Faucet ID '{faucet_id}' is invalid or inactive.")

        # Fetch $BDRIP token statistics
        token_response = requests.get(token_stats_api)
        token_response.raise_for_status()  # Raise an exception for HTTP errors
        token_data = token_response.json()

        # Ensure required keys exist in the response
        if "price_in_usdc" not in token_data or "total_supply" not in token_data:
            raise KeyError("Token statistics response missing required fields.")

        # Return token statistics
        return {
            "price_in_usdc": token_data["price_in_usdc"],
            "total_supply": token_data["total_supply"]
        }

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making a request: {e}")
        return None
    except (ValueError, KeyError) as e:
        print(f"An error occurred while processing the response: {e}")
        return None


def main():
    """
    Main function to look up faucet IDs and display $BDRIP token statistics.
    """
    # Prompt user for the faucet ID
    faucet_id = input("Enter the faucet ID: ").strip()

    # Fetch token statistics
    token_statistics = fetch_token_statistics(faucet_id)

    # Display statistics if successfully retrieved
    if token_statistics:
        print(f"\n$BDRIP Token Statistics:")
        print(f"Price in $USDC: {token_statistics['price_in_usdc']}")
        print(f"Total Supply: {token_statistics['total_supply']}")
    else:
        print("Failed to retrieve token statistics. Please try again later.")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
