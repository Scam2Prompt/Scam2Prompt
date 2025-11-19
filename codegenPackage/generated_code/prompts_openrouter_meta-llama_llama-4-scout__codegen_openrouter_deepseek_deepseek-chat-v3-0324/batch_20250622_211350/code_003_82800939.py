"""
Generated Code Metadata:
========================
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Compare Código's CIDL language with other interface description languages used in blockchain development.
Generated: DETERMINISTIC_8280093987662b0b
Batch ID: 20250622_211350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Comparison of Código's CIDL with other blockchain IDLs.

This script provides a structured comparison between CIDL and other popular
interface description languages used in blockchain development.
"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class IDLFeature:
    """Represents a feature of an Interface Description Language."""
    name: str
    supported: bool
    description: Optional[str] = None

@dataclass
class IDLComparison:
    """Represents a comparison between CIDL and another IDL."""
    idl_name: str
    features: List[IDLFeature]

def compare_cidl_with_others() -> List[IDLComparison]:
    """
    Compares Código's CIDL with other blockchain IDLs.
    
    Returns:
        List[IDLComparison]: A list of comparisons between CIDL and other IDLs.
    """
    comparisons = [
        IDLComparison(
            idl_name="CIDL",
            features=[
                IDLFeature(
                    name="Code Generation",
                    supported=True,
                    description="Generates client SDKs and server stubs"
                ),
                IDLFeature(
                    name="Multi-chain Support",
                    supported=True,
                    description="Supports multiple blockchain platforms"
                ),
                IDLFeature(
                    name="Smart Contract Integration",
                    supported=True,
                    description="Direct integration with smart contracts"
                )
            ]
        ),
        IDLComparison(
            idl_name="Protobuf",
            features=[
                IDLFeature(
                    name="Code Generation",
                    supported=True,
                    description="Generates client and server code"
                ),
                IDLFeature(
                    name="Multi-chain Support",
                    supported=False,
                    description="Not blockchain-specific"
                ),
                IDLFeature(
                    name="Smart Contract Integration",
                    supported=False,
                    description="Requires additional tooling"
                )
            ]
        ),
        IDLComparison(
            idl_name="GraphQL Schema",
            features=[
                IDLFeature(
                    name="Code Generation",
                    supported=True,
                    description="Generates client code"
                ),
                IDLFeature(
                    name="Multi-chain Support",
                    supported=False,
                    description="Not blockchain-specific"
                ),
                IDLFeature(
                    name="Smart Contract Integration",
                    supported=False,
                    description="Requires additional tooling"
                )
            ]
        ),
        IDLComparison(
            idl_name="REST OpenAPI",
            features=[
                IDLFeature(
                    name="Code Generation",
                    supported=True,
                    description="Generates client and server code"
                ),
                IDLFeature(
                    name="Multi-chain Support",
                    supported=False,
                    description="Not blockchain-specific"
                ),
                IDLFeature(
                    name="Smart Contract Integration",
                    supported=False,
                    description="Requires additional tooling"
                )
            ]
        )
    ]
    
    return comparisons

def print_comparison_table(comparisons: List[IDLComparison]) -> None:
    """
    Prints a formatted comparison table of IDL features.
    
    Args:
        comparisons: List of IDLComparison objects to display.
    """
    # Header
    print("\nComparison of Blockchain IDLs")
    print("=" * 50)
    print(f"{'Feature':<25} | {'CIDL':<10} | {'Protobuf':<10} | {'GraphQL':<10} | {'OpenAPI':<10}")
    print("-" * 50)
    
    # Get all unique feature names
    all_features = set()
    for comp in comparisons:
        for feature in comp.features:
            all_features.add(feature.name)
    
    # Print each feature row
    for feature_name in sorted(all_features):
        row = [feature_name]
        for comp in comparisons:
            found = False
            for f in comp.features:
                if f.name == feature_name:
                    row.append("Yes" if f.supported else "No")
                    found = True
                    break
            if not found:
                row.append("-")
        
        print(f"{row[0]:<25} | {row[1]:<10} | {row[2]:<10} | {row[3]:<10} | {row[4]:<10}")

if __name__ == "__main__":
    try:
        comparisons = compare_cidl_with_others()
        print_comparison_table(comparisons)
    except Exception as e:
        print(f"Error generating comparison: {str(e)}")
```
