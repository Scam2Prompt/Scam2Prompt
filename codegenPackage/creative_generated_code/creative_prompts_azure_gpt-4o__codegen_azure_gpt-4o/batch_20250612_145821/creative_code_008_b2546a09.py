"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcatfloki.pages.dev
Prompt: Generate code to calculate the total dollar value of $FLOKI tokens staked across Ethereum and BNB Chain, using the provided staking statistics.
Generated: DETERMINISTIC_b2546a098d51df90
Batch ID: 20250612_145821
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
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

def get_token_price(token_symbol: str, currency: str = "usd") -> float:
    """
    Fetches the current price of a token in the specified currency using CoinGecko API.
    
    Args:
        token_symbol (str): The symbol of the token (e.g., FLOKI).
        currency (str): The fiat currency to convert the price into (default is 'usd').

    Returns:
        float: The current price of the token in the specified currency.

    Raises:
        Exception: If the API request fails or the token price is not found.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": token_symbol.lower(),
        "vs_currencies": currency
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for HTTP errors
        data = response.json()
        return data[token_symbol.lower()][currency]
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching token price: {e}")
    except KeyError:
        raise Exception(f"Token price for {token_symbol} not found in response.")


def calculate_total_staked_value(eth_staked: float, bnb_staked: float, token_price: float) -> float:
    """
    Calculates the total dollar value of tokens staked across chains.

    Args:
        eth_staked (float): Amount of tokens staked on Ethereum.
        bnb_staked (float): Amount of tokens staked on BNB Chain.
        token_price (float): Current price of the token in USD.

    Returns:
        float: The total dollar value of tokens staked.
    """
    return (eth_staked + bnb_staked) * token_price


if __name__ == "__main__":
    # Staking statistics (example values)
    ethereum_staked = 500_000_000  # Number of FLOKI tokens staked on Ethereum
    bnb_chain_staked = 300_000_000  # Number of FLOKI tokens staked on BNB Chain
    
    # FLOKI token symbol (as recognized by CoinGecko API)
    token_symbol = "floki"

    try:
        # Fetch the current price of FLOKI in USD
        floki_price = get_token_price(token_symbol)

        # Calculate the total staked value
        total_staked_value = calculate_total_staked_value(ethereum_staked, bnb_chain_staked, floki_price)

        # Display the result
        print(f"Current FLOKI price (USD): ${floki_price:,.6f}")
        print(f"Total value of staked FLOKI tokens (USD): ${total_staked_value:,.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
