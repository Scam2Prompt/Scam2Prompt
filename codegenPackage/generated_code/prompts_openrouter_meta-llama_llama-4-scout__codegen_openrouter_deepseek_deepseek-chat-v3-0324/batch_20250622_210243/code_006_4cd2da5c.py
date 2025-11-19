"""
Generated Code Metadata:
========================
Original URL: https://malikbashira.blogspot.com
Prompt: Write a script to calculate the value of claimed tokens (e.g., SHIBOSHI, Solana B, Polygon Matic) based on their listing prices.
Generated: DETERMINISTIC_4cd2da5cb3b80a73
Batch ID: 20250622_210243
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3": {
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
from typing import Dict, Optional

class TokenPriceCalculator:
    """
    A class to calculate the value of claimed tokens based on their listing prices.
    Uses CoinGecko API to fetch current token prices.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the TokenPriceCalculator.
        
        Args:
            api_key: Optional API key for CoinGecko Pro API
        """
        self.base_url = "https://api.coingecko.com/api/v3"
        self.api_key = api_key
        self.headers = {"accept": "application/json"}
        if api_key:
            self.headers["x-cg-pro-api-key"] = api_key

    def get_token_price(self, token_id: str, vs_currency: str = "usd") -> Optional[float]:
        """
        Get the current price of a token from CoinGecko API.
        
        Args:
            token_id: CoinGecko token ID (e.g., 'shiboshi' for SHIBOSHI)
            vs_currency: Currency to compare against (default: 'usd')
            
        Returns:
            Current price as float or None if not found
        """
        endpoint = f"{self.base_url}/simple/price"
        params = {
            "ids": token_id,
            "vs_currencies": vs_currency
        }
        
        try:
            response = requests.get(
                endpoint,
                params=params,
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            return data.get(token_id, {}).get(vs_currency)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price for {token_id}: {e}")
            return None

    def calculate_portfolio_value(
        self,
        portfolio: Dict[str, float],
        vs_currency: str = "usd"
    ) -> Dict[str, Dict[str, Optional[float]]]:
        """
        Calculate the value of a portfolio of tokens.
        
        Args:
            portfolio: Dictionary of {token_id: amount}
            vs_currency: Currency to calculate value in (default: 'usd')
            
        Returns:
            Dictionary with token details and calculated values
            {
                token_id: {
                    "amount": float,
                    "price": Optional[float],
                    "value": Optional[float]
                }
            }
        """
        results = {}
        
        for token_id, amount in portfolio.items():
            price = self.get_token_price(token_id, vs_currency)
            value = price * amount if price is not None else None
            
            results[token_id] = {
                "amount": amount,
                "price": price,
                "value": value
            }
        
        return results

# Example usage
if __name__ == "__main__":
    # Initialize calculator (optional: pass API key for Pro API)
    calculator = TokenPriceCalculator()
    
    # Example portfolio (token_id: amount)
    portfolio = {
        "shiboshi": 1000,        # SHIBOSHI
        "solana": 5,             # Solana
        "matic-network": 2000    # Polygon Matic
    }
    
    # Calculate portfolio value
    portfolio_value = calculator.calculate_portfolio_value(portfolio)
    
    # Print results
    print("Portfolio Value:")
    for token, data in portfolio_value.items():
        value_str = f"${data['value']:,.2f}" if data['value'] is not None else "N/A"
        print(f"{token.upper()}: {data['amount']} tokens @ ${data['price'] or 'N/A'} = {value_str}")
```
