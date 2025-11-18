"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deifllama.github.io
Prompt: Write a script to extract and summarize DeFi Llama's data on token prices and trading activity for a specific protocol.
Generated: DETERMINISTIC_9f21bd974ec92dca
Batch ID: 20250612_153424
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi": {
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

# DefiLlama API base URL
BASE_URL = "https://api.llama.fi"

def get_protocol_data(protocol_name):
    """
    Fetch data for a specific protocol from DefiLlama API.

    Args:
        protocol_name (str): The name of the protocol to fetch data for.

    Returns:
        dict: Parsed JSON data for the specified protocol.
    """
    try:
        response = requests.get(f"{BASE_URL}/protocol/{protocol_name}")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching protocol data: {e}")
        return None

def summarize_token_data(protocol_data):
    """
    Summarize token price and trading activity data from a protocol's data.

    Args:
        protocol_data (dict): The data fetched for a protocol.

    Returns:
        list: A list of summarized token data (name, price, volume).
    """
    try:
        if "tokens" not in protocol_data:
            print("No token data available in the protocol.")
            return []

        token_summary = []
        tokens = protocol_data["tokens"]

        for token in tokens:
            token_name = token.get("symbol", "Unknown")
            token_price = token.get("price", "N/A")
            token_volume = token.get("volume", "N/A")

            token_summary.append({
                "name": token_name,
                "price": token_price,
                "volume": token_volume
            })

        return token_summary

    except KeyError as e:
        print(f"Error summarizing token data: {e}")
        return []

def main():
    """
    Main function to extract and summarize DeFi Llama's data for a specific protocol.
    """
    # Prompt user for the protocol name
    protocol_name = input("Enter the name of the protocol: ").strip()

    print(f"Fetching data for protocol: {protocol_name}")
    protocol_data = get_protocol_data(protocol_name)

    if not protocol_data:
        print("Failed to retrieve protocol data. Exiting.")
        return

    print("Summarizing token data...")
    summarized_data = summarize_token_data(protocol_data)

    if not summarized_data:
        print("No token data found for the protocol.")
        return

    print("\nToken Summary:")
    for token in summarized_data:
        print(f"Name: {token['name']}, Price: {token['price']}, Volume: {token['volume']}")

if __name__ == "__main__":
    main()
```
