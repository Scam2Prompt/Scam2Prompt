"""
Generated Code Metadata:
========================
Original URL: https://raydiumgold.com
Prompt: Generate a Python script that utilizes the Raydium DEX API to fetch the latest trading volume data for the $RAY token.
Generated: DETERMINISTIC_df41e7c86c198805
Batch ID: 20250612_163826
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.raydium.io/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

class RaydiumAPI:
    """
    A class to interact with the Raydium DEX API to fetch trading volume data.
    """

    BASE_URL = "https://api.raydium.io/v2"

    def __init__(self):
        """
        Initializes the RaydiumAPI class.
        """
        pass

    def get_trading_volume(self, token_symbol: str) -> dict:
        """
        Fetches the latest trading volume data for the specified token.

        Args:
            token_symbol (str): The symbol of the token to fetch volume data for.

        Returns:
            dict: A dictionary containing the trading volume data.

        Raises:
            ValueError: If the token symbol is invalid or not found.
            Exception: For any other errors during the API request.
        """
        if token_symbol != "RAY":
            raise ValueError("Invalid token symbol. Only $RAY is supported.")

        endpoint = f"{self.BASE_URL}/market"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Find the trading volume for the specified token
            for market in data.get("markets", []):
                if market.get("baseMint") == "RAY_MINT_ADDRESS":  # Replace with actual RAY mint address
                    return {
                        "symbol": token_symbol,
                        "trading_volume": market.get("volume24h"),
                        "liquidity": market.get("liquidity"),
                    }

            raise ValueError("Trading volume data for $RAY not found.")
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")

if __name__ == "__main__":
    raydium_api = RaydiumAPI()
    try:
        trading_volume_data = raydium_api.get_trading_volume("RAY")
        print(f"Trading Volume Data for $RAY: {trading_volume_data}")
    except Exception as e:
        print(f"Error: {e}")
```

**Note:** Replace `"RAY_MINT_ADDRESS"` with the actual mint address for the $RAY token.
