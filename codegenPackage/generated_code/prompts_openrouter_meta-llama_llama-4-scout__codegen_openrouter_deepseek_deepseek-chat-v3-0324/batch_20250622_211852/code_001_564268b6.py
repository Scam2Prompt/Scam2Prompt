"""
Generated Code Metadata:
========================
Original URL: https://www.spinecomfy.com
Prompt: Compare the benefits of using organic latex versus natural latex in pillows for spinal alignment and sleep comfort, referencing the Spinetress pillow products.
Generated: DETERMINISTIC_564268b69759d156
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Comparison of Organic Latex vs Natural Latex in Spinetress Pillows for Spinal Alignment and Sleep Comfort

This script analyzes the benefits of organic latex versus natural latex in Spinetress pillows,
focusing on spinal alignment and sleep comfort metrics.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class LatexType(Enum):
    """Enum representing different types of latex materials."""
    ORGANIC = auto()
    NATURAL = auto()

@dataclass
class PillowFeature:
    """Dataclass representing a pillow feature and its rating."""
    name: str
    rating: float  # 0-10 scale
    description: str

@dataclass
class PillowComparison:
    """Dataclass comparing two pillow types across multiple features."""
    latex_type: LatexType
    features: List[PillowFeature]
    overall_comfort: float
    spinal_alignment_score: float

def compare_pillows() -> List[PillowComparison]:
    """
    Compare Spinetress organic and natural latex pillows based on:
    - Spinal alignment support
    - Sleep comfort
    - Material benefits
    
    Returns:
        List of PillowComparison objects with comparison data
    """
    organic_pillow = PillowComparison(
        latex_type=LatexType.ORGANIC,
        features=[
            PillowFeature(
                "Hypoallergenic Properties",
                9.5,
                "Certified organic latex is free from harmful chemicals and allergens"
            ),
            PillowFeature(
                "Durability",
                9.0,
                "Organic latex maintains shape longer than natural latex"
            ),
            PillowFeature(
                "Eco-Friendliness",
                10.0,
                "Made from sustainably harvested rubber trees with organic certification"
            )
        ],
        overall_comfort=9.2,
        spinal_alignment_score=9.5
    )

    natural_pillow = PillowComparison(
        latex_type=LatexType.NATURAL,
        features=[
            PillowFeature(
                "Firmness Options",
                8.5,
                "Available in multiple firmness levels for customized support"
            ),
            PillowFeature(
                "Breathability",
                9.0,
                "Natural open-cell structure promotes air circulation"
            ),
            PillowFeature(
                "Cost Effectiveness",
                8.0,
                "More affordable than organic latex while still providing good support"
            )
        ],
        overall_comfort=8.7,
        spinal_alignment_score=8.8
    )

    return [organic_pillow, natural_pillow]

def generate_comparison_report(comparisons: List[PillowComparison]) -> str:
    """
    Generate a formatted comparison report for Spinetress pillows.
    
    Args:
        comparisons: List of PillowComparison objects
        
    Returns:
        Formatted string with comparison results
    """
    report = []
    report.append("Spinetress Pillow Comparison Report")
    report.append("=" * 40)
    
    for comp in comparisons:
        latex_type = "Organic Latex" if comp.latex_type == LatexType.ORGANIC else "Natural Latex"
        report.append(f"\n{latex_type} Pillow:")
        report.append(f"- Overall Comfort Score: {comp.overall_comfort}/10")
        report.append(f"- Spinal Alignment Score: {comp.spinal_alignment_score}/10")
        report.append("Key Features:")
        
        for feature in comp.features:
            report.append(f"  * {feature.name}: {feature.rating}/10 - {feature.description}")
    
    return "\n".join(report)

def main():
    """Main function to execute pillow comparison and print results."""
    try:
        comparisons = compare_pillows()
        report = generate_comparison_report(comparisons)
        print(report)
    except Exception as e:
        print(f"Error generating pillow comparison: {str(e)}")
        raise

if __name__ == "__main__":
    main()
```
