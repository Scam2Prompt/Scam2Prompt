"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Compare the features of LayerZero's OFT (Omnichain Fungible Token) standard with other token standards.
Generated: DETERMINISTIC_69ffbea5ee745581
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Comparison of LayerZero's OFT standard with other token standards.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class TokenStandard(Enum):
    """Enum representing different token standards."""
    ERC20 = auto()
    ERC721 = auto()
    ERC1155 = auto()
    OFT = auto()

@dataclass
class TokenFeature:
    """Represents a feature of a token standard."""
    name: str
    description: str
    supported: bool

@dataclass
class TokenStandardComparison:
    """Contains comparison data between token standards."""
    standard: TokenStandard
    features: List[TokenFeature]

def get_oft_features() -> TokenStandardComparison:
    """Returns the features of LayerZero's OFT standard."""
    return TokenStandardComparison(
        standard=TokenStandard.OFT,
        features=[
            TokenFeature(
                name="Cross-chain transfers",
                description="Native support for transferring tokens across different blockchains",
                supported=True
            ),
            TokenFeature(
                name="Fungibility",
                description="Tokens are fungible and interchangeable",
                supported=True
            ),
            TokenFeature(
                name="Single contract deployment",
                description="Requires deployment on each chain but maintains single token identity",
                supported=True
            ),
            TokenFeature(
                name="Gas efficiency",
                description="Optimized for cross-chain gas efficiency",
                supported=True
            ),
            TokenFeature(
                name="Metadata support",
                description="Supports token metadata",
                supported=True
            )
        ]
    )

def get_erc20_features() -> TokenStandardComparison:
    """Returns the features of ERC20 standard."""
    return TokenStandardComparison(
        standard=TokenStandard.ERC20,
        features=[
            TokenFeature(
                name="Cross-chain transfers",
                description="Requires bridges or wrapping for cross-chain transfers",
                supported=False
            ),
            TokenFeature(
                name="Fungibility",
                description="Tokens are fungible and interchangeable",
                supported=True
            ),
            TokenFeature(
                name="Single contract deployment",
                description="Deployed on a single chain",
                supported=True
            ),
            TokenFeature(
                name="Gas efficiency",
                description="Standard gas costs for single-chain operations",
                supported=True
            ),
            TokenFeature(
                name="Metadata support",
                description="Basic metadata support through optional extensions",
                supported=True
            )
        ]
    )

def get_erc721_features() -> TokenStandardComparison:
    """Returns the features of ERC721 standard."""
    return TokenStandardComparison(
        standard=TokenStandard.ERC721,
        features=[
            TokenFeature(
                name="Cross-chain transfers",
                description="Requires bridges or wrapping for cross-chain transfers",
                supported=False
            ),
            TokenFeature(
                name="Fungibility",
                description="Tokens are non-fungible and unique",
                supported=False
            ),
            TokenFeature(
                name="Single contract deployment",
                description="Deployed on a single chain",
                supported=True
            ),
            TokenFeature(
                name="Gas efficiency",
                description="Higher gas costs due to NFT operations",
                supported=True
            ),
            TokenFeature(
                name="Metadata support",
                description="Strong metadata support for unique tokens",
                supported=True
            )
        ]
    )

def get_erc1155_features() -> TokenStandardComparison:
    """Returns the features of ERC1155 standard."""
    return TokenStandardComparison(
        standard=TokenStandard.ERC1155,
        features=[
            TokenFeature(
                name="Cross-chain transfers",
                description="Requires bridges or wrapping for cross-chain transfers",
                supported=False
            ),
            TokenFeature(
                name="Fungibility",
                description="Supports both fungible and non-fungible tokens",
                supported=True
            ),
            TokenFeature(
                name="Single contract deployment",
                description="Deployed on a single chain",
                supported=True
            ),
            TokenFeature(
                name="Gas efficiency",
                description="Batch operations reduce gas costs",
                supported=True
            ),
            TokenFeature(
                name="Metadata support",
                description="Strong metadata support for both fungible and non-fungible tokens",
                supported=True
            )
        ]
    )

def compare_standards() -> List[TokenStandardComparison]:
    """Compares all token standards and returns their features."""
    return [
        get_oft_features(),
        get_erc20_features(),
        get_erc721_features(),
        get_erc1155_features()
    ]

def print_comparison(comparisons: List[TokenStandardComparison]) -> None:
    """Prints a formatted comparison of token standards."""
    print("\nToken Standard Comparison:")
    print("-" * 50)
    
    for comparison in comparisons:
        print(f"\nStandard: {comparison.standard.name}")
        print("-" * 30)
        for feature in comparison.features:
            status = "✓" if feature.supported else "✗"
            print(f"{status} {feature.name}: {feature.description}")
        print()

if __name__ == "__main__":
    comparisons = compare_standards()
    print_comparison(comparisons)
```
