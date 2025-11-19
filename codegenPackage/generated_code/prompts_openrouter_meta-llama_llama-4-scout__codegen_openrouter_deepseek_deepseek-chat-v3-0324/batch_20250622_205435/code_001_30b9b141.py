"""
Generated Code Metadata:
========================
Original URL: https://andyonblxst.pages.dev
Prompt: Compare the tokenomics of $ANDY with other similar tokens, focusing on total supply and tax structure.
Generated: DETERMINISTIC_30b9b141cdc693c4
Batch ID: 20250622_205435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class Tokenomics:
    name: str
    total_supply: int
    buy_tax: float
    sell_tax: float
    transfer_tax: float

class TokenomicsComparator:
    def __init__(self):
        self.tokens: Dict[str, Tokenomics] = {}
    
    def add_token(self, token: Tokenomics) -> None:
        """Add a token to the comparator."""
        self.tokens[token.name] = token
    
    def get_token(self, name: str) -> Optional[Tokenomics]:
        """Retrieve tokenomics by token name."""
        return self.tokens.get(name)
    
    def compare_total_supply(self) -> List[Tokenomics]:
        """Compare tokens by total supply (ascending order)."""
        return sorted(self.tokens.values(), key=lambda x: x.total_supply)
    
    def compare_tax_structures(self) -> Dict[str, List[Tokenomics]]:
        """Compare tokens by tax structures."""
        return {
            "buy_tax": sorted(self.tokens.values(), key=lambda x: x.buy_tax),
            "sell_tax": sorted(self.tokens.values(), key=lambda x: x.sell_tax),
            "transfer_tax": sorted(self.tokens.values(), key=lambda x: x.transfer_tax)
        }
    
    def fetch_token_data(self, api_url: str) -> None:
        """Fetch token data from an API and add to comparator."""
        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            for token_data in data:
                token = Tokenomics(
                    name=token_data['name'],
                    total_supply=int(token_data['total_supply']),
                    buy_tax=float(token_data['buy_tax']),
                    sell_tax=float(token_data['sell_tax']),
                    transfer_tax=float(token_data['transfer_tax'])
                )
                self.add_token(token)
                
        except requests.exceptions.RequestException as e:
            print(f"Error fetching token data: {e}")
        except (KeyError, ValueError) as e:
            print(f"Error parsing token data: {e}")

# Example usage
if __name__ == "__main__":
    comparator = TokenomicsComparator()
    
    # Add $ANDY token manually
    andy_token = Tokenomics(
        name="$ANDY",
        total_supply=1_000_000_000,
        buy_tax=0.05,
        sell_tax=0.10,
        transfer_tax=0.02
    )
    comparator.add_token(andy_token)
    
    # Add other tokens (could be fetched from API)
    eth_token = Tokenomics(
        name="ETH",
        total_supply=120_000_000,
        buy_tax=0.0,
        sell_tax=0.0,
        transfer_tax=0.0
    )
    comparator.add_token(eth_token)
    
    # Compare tokenomics
    print("Tokens by total supply:")
    for token in comparator.compare_total_supply():
        print(f"{token.name}: {token.total_supply:,}")
    
    print("\nTax structures:")
    tax_comparison = comparator.compare_tax_structures()
    for tax_type, tokens in tax_comparison.items():
        print(f"\n{tax_type}:")
        for token in tokens:
            print(f"{token.name}: {token.__getattribute__(tax_type) * 100}%")
```
