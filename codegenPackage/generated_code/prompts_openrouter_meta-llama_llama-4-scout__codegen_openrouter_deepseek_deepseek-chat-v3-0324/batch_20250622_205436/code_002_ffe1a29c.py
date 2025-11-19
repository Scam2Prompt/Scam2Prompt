"""
Generated Code Metadata:
========================
Original URL: https://ethereumprofit.org
Prompt: Explain the concept of stablecoins, utility tokens, and payment cryptocurrencies, and provide examples of each, as discussed on the Auto Profit Hub website.
Generated: DETERMINISTIC_ffe1a29ca6b98cbd
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that demonstrates the concepts of stablecoins, utility tokens, and payment cryptocurrencies with examples, following best practices:

```python
# crypto_types_demo.py
"""
This script demonstrates the concepts of stablecoins, utility tokens, and payment cryptocurrencies
with examples from the cryptocurrency market.
"""

from dataclasses import dataclass
from typing import List, Optional
from enum import Enum, auto

class CryptoCategory(Enum):
    """Enum representing different cryptocurrency categories."""
    STABLECOIN = auto()
    UTILITY_TOKEN = auto()
    PAYMENT = auto()

@dataclass
class Cryptocurrency:
    """Data class representing a cryptocurrency with its properties."""
    name: str
    symbol: str
    category: CryptoCategory
    description: str
    use_case: Optional[str] = None
    pegged_to: Optional[str] = None

def get_crypto_examples() -> List[Cryptocurrency]:
    """
    Returns a list of example cryptocurrencies for each category.
    
    Returns:
        List[Cryptocurrency]: List of cryptocurrency examples
    """
    return [
        Cryptocurrency(
            name="Tether",
            symbol="USDT",
            category=CryptoCategory.STABLECOIN,
            description="A fiat-collateralized stablecoin",
            pegged_to="US Dollar"
        ),
        Cryptocurrency(
            name="USD Coin",
            symbol="USDC",
            category=CryptoCategory.STABLECOIN,
            description="A regulated stablecoin backed by cash reserves",
            pegged_to="US Dollar"
        ),
        Cryptocurrency(
            name="Chainlink",
            symbol="LINK",
            category=CryptoCategory.UTILITY_TOKEN,
            description="Oracle network providing real-world data to smart contracts",
            use_case="Smart contract data feeds"
        ),
        Cryptocurrency(
            name="Filecoin",
            symbol="FIL",
            category=CryptoCategory.UTILITY_TOKEN,
            description="Decentralized storage network",
            use_case="Data storage and retrieval"
        ),
        Cryptocurrency(
            name="Bitcoin",
            symbol="BTC",
            category=CryptoCategory.PAYMENT,
            description="First decentralized digital currency"
        ),
        Cryptocurrency(
            name="Litecoin",
            symbol="LTC",
            category=CryptoCategory.PAYMENT,
            description="Peer-to-peer cryptocurrency with faster transactions than Bitcoin"
        )
    ]

def print_crypto_examples():
    """Prints formatted examples of different cryptocurrency types."""
    examples = get_crypto_examples()
    
    print("Cryptocurrency Examples by Category:\n")
    
    for category in CryptoCategory:
        print(f"=== {category.name} ===")
        for crypto in [c for c in examples if c.category == category]:
            print(f"\nName: {crypto.name} ({crypto.symbol})")
            print(f"Description: {crypto.description}")
            if crypto.pegged_to:
                print(f"Pegged to: {crypto.pegged_to}")
            if crypto.use_case:
                print(f"Primary Use Case: {crypto.use_case}")
        print("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    try:
        print_crypto_examples()
    except Exception as e:
        print(f"An error occurred while displaying cryptocurrency examples: {str(e)}")
```
