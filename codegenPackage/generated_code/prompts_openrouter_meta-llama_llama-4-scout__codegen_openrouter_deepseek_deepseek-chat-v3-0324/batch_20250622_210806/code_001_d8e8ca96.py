"""
Generated Code Metadata:
========================
Original URL: https://earn-gummyonsol.pages.dev
Prompt: Compare the tokenomics of $Gummy with a standard cryptocurrency, focusing on the allocation of tokens for CEX liquidity, market makers, and team founders.
Generated: DETERMINISTIC_d8e8ca96ea4d0a61
Batch ID: 20250622_210806
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
class TokenAllocation:
    """Represents the allocation percentages for different token categories."""
    cex_liquidity: float
    market_makers: float
    team_founders: float
    other: float  # Includes remaining allocations like community, staking, etc.

    def validate(self) -> None:
        """Validate that allocations sum to 100%."""
        total = sum([
            self.cex_liquidity,
            self.market_makers,
            self.team_founders,
            self.other
        ])
        if not abs(total - 100.0) < 0.01:  # Account for floating point precision
            raise ValueError(f"Token allocations must sum to 100%, got {total}%")

@dataclass
class TokenomicsComparison:
    """Represents a comparison between two token allocation models."""
    token_name: str
    standard_allocation: TokenAllocation
    gummy_allocation: TokenAllocation

    def compare(self) -> Dict[str, Dict[str, float]]:
        """Compare allocations and return the differences."""
        return {
            "CEX Liquidity": {
                "Standard": self.standard_allocation.cex_liquidity,
                "Gummy": self.gummy_allocation.cex_liquidity,
                "Difference": self.gummy_allocation.cex_liquidity - self.standard_allocation.cex_liquidity
            },
            "Market Makers": {
                "Standard": self.standard_allocation.market_makers,
                "Gummy": self.gummy_allocation.market_makers,
                "Difference": self.gummy_allocation.market_makers - self.standard_allocation.market_makers
            },
            "Team & Founders": {
                "Standard": self.standard_allocation.team_founders,
                "Gummy": self.gummy_allocation.team_founders,
                "Difference": self.gummy_allocation.team_founders - self.standard_allocation.team_founders
            },
            "Other": {
                "Standard": self.standard_allocation.other,
                "Gummy": self.gummy_allocation.other,
                "Difference": self.gummy_allocation.other - self.standard_allocation.other
            }
        }

def load_tokenomics_from_json(file_path: str) -> TokenAllocation:
    """Load token allocation data from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            allocation = TokenAllocation(
                cex_liquidity=data.get('cex_liquidity', 0),
                market_makers=data.get('market_makers', 0),
                team_founders=data.get('team_founders', 0),
                other=data.get('other', 0)
            )
            allocation.validate()
            return allocation
    except FileNotFoundError:
        raise FileNotFoundError(f"Tokenomics file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error loading tokenomics: {str(e)}")

def generate_comparison_report(comparison: TokenomicsComparison) -> str:
    """Generate a formatted comparison report."""
    try:
        comparison_data = comparison.compare()
        report = []
        report.append(f"Tokenomics Comparison Report: {comparison.token_name}")
        report.append("=" * 50)
        
        for category, data in comparison_data.items():
            report.append(f"\n{category}:")
            report.append(f"  Standard: {data['Standard']}%")
            report.append(f"  Gummy:    {data['Gummy']}%")
            report.append(f"  Difference: {data['Difference']:+}%")
        
        return "\n".join(report)
    except Exception as e:
        raise RuntimeError(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Example allocations (in production these would be loaded from files/APIs)
        standard = TokenAllocation(
            cex_liquidity=20.0,
            market_makers=15.0,
            team_founders=10.0,
            other=55.0
        )
        
        gummy = TokenAllocation(
            cex_liquidity=25.0,
            market_makers=20.0,
            team_founders=5.0,
            other=50.0
        )
        
        comparison = TokenomicsComparison(
            token_name="$Gummy vs Standard",
            standard_allocation=standard,
            gummy_allocation=gummy
        )
        
        print(generate_comparison_report(comparison))
    except Exception as e:
        print(f"Error: {str(e)}")
```
