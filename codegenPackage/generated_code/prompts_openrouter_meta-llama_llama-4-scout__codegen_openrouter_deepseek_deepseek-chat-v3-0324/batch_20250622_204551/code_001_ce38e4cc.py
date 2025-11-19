"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-is.pages.dev
Prompt: Compare the tokenomics of WienerAI with a similar meme coin, highlighting the unique features of WienerAI's token distribution.
Generated: DETERMINISTIC_ce38e4cc2e06ee32
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class TokenomicsFeature:
    """Represents a tokenomics feature of a meme coin."""
    name: str
    description: str
    is_unique: bool = False

@dataclass
class MemeCoinTokenomics:
    """Represents the tokenomics of a meme coin."""
    name: str
    total_supply: int
    distribution: Dict[str, float]  # Percentage allocations
    features: List[TokenomicsFeature]
    burn_mechanism: Optional[str] = None
    tax_structure: Optional[str] = None

def compare_tokenomics(coin1: MemeCoinTokenomics, coin2: MemeCoinTokenomics) -> Dict:
    """
    Compare two meme coin tokenomics and highlight unique features.
    
    Args:
        coin1: First meme coin tokenomics
        coin2: Second meme coin tokenomics
    
    Returns:
        Dictionary containing comparison results
    """
    comparison = {
        "coins": [coin1.name, coin2.name],
        "total_supply_comparison": {
            coin1.name: coin1.total_supply,
            coin2.name: coin2.total_supply,
            "difference": abs(coin1.total_supply - coin2.total_supply)
        },
        "distribution_comparison": {
            "common_allocations": [],
            "unique_allocations": {
                coin1.name: [],
                coin2.name: []
            }
        },
        "unique_features": {
            coin1.name: [],
            coin2.name: []
        }
    }

    # Compare distribution allocations
    for allocation in coin1.distribution:
        if allocation in coin2.distribution:
            comparison["distribution_comparison"]["common_allocations"].append({
                "category": allocation,
                coin1.name: coin1.distribution[allocation],
                coin2.name: coin2.distribution[allocation]
            })
        else:
            comparison["distribution_comparison"]["unique_allocations"][coin1.name].append({
                "category": allocation,
                "percentage": coin1.distribution[allocation]
            })

    for allocation in coin2.distribution:
        if allocation not in coin1.distribution:
            comparison["distribution_comparison"]["unique_allocations"][coin2.name].append({
                "category": allocation,
                "percentage": coin2.distribution[allocation]
            })

    # Compare features
    for feature in coin1.features:
        if feature.is_unique:
            comparison["unique_features"][coin1.name].append({
                "name": feature.name,
                "description": feature.description
            })

    for feature in coin2.features:
        if feature.is_unique:
            comparison["unique_features"][coin2.name].append({
                "name": feature.name,
                "description": feature.description
            })

    return comparison

def print_comparison_results(comparison: Dict) -> None:
    """Print formatted comparison results."""
    print(f"\nTokenomics Comparison: {comparison['coins'][0]} vs {comparison['coins'][1]}")
    print("\nTotal Supply:")
    print(f"- {comparison['coins'][0]}: {comparison['total_supply_comparison'][comparison['coins'][0]]:,}")
    print(f"- {comparison['coins'][1]}: {comparison['total_supply_comparison'][comparison['coins'][1]]:,}")
    print(f"- Difference: {comparison['total_supply_comparison']['difference']:,}")

    print("\nDistribution Comparison:")
    print("\nCommon Allocations:")
    for alloc in comparison["distribution_comparison"]["common_allocations"]:
        print(f"- {alloc['category']}:")
        print(f"  - {comparison['coins'][0]}: {alloc[comparison['coins'][0]]}%")
        print(f"  - {comparison['coins'][1]}: {alloc[comparison['coins'][1]]}%")

    print("\nUnique Allocations:")
    for coin in comparison["coins"]:
        if comparison["distribution_comparison"]["unique_allocations"][coin]:
            print(f"- {coin}:")
            for alloc in comparison["distribution_comparison"]["unique_allocations"][coin]:
                print(f"  - {alloc['category']}: {alloc['percentage']}%")

    print("\nUnique Features:")
    for coin in comparison["coins"]:
        if comparison["unique_features"][coin]:
            print(f"- {coin}:")
            for feature in comparison["unique_features"][coin]:
                print(f"  - {feature['name']}: {feature['description']}")

# Example usage
if __name__ == "__main__":
    # WienerAI tokenomics
    wienerai = MemeCoinTokenomics(
        name="WienerAI",
        total_supply=690_000_000_000,
        distribution={
            "Liquidity": 30,
            "Marketing": 15,
            "Development": 20,
            "Community Rewards": 25,
            "Team": 10
        },
        features=[
            TokenomicsFeature(
                name="AI-Powered Trading",
                description="Integrated AI that helps optimize trades for holders",
                is_unique=True
            ),
            TokenomicsFeature(
                name="Dynamic Tax Redistribution",
                description="Taxes automatically redistributed to top holders",
                is_unique=True
            )
        ],
        burn_mechanism="Automatic burn on transactions",
        tax_structure="5% buy/sell tax"
    )

    # Example similar meme coin (DogeCoin-like)
    similar_coin = MemeCoinTokenomics(
        name="SimilarMemeCoin",
        total_supply=1_000_000_000_000,
        distribution={
            "Liquidity": 40,
            "Marketing": 10,
            "Development": 15,
            "Team": 15,
            "Airdrops": 20
        },
        features=[
            TokenomicsFeature(
                name="Community Voting",
                description="Holders can vote on project direction",
                is_unique=False
            )
        ],
        burn_mechanism="Manual burns",
        tax_structure="2% transaction fee"
    )

    # Compare and print results
    results = compare_tokenomics(wienerai, similar_coin)
    print_comparison_results(results)
```
