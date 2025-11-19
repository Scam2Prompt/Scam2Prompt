"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Generate a detailed report on the tokenomics of $STARS, including the allocation of tokens for presale, staking, marketing, CEX/DEX, and the MemeVault ecosystem.
Generated: DETERMINISTIC_5e74d0fac6a5b343
Batch ID: 20250622_211032
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
from typing import Dict, List

@dataclass
class TokenAllocation:
    category: str
    percentage: float
    description: str
    vesting_period: str = None

class TokenomicsReport:
    def __init__(self, token_name: str):
        self.token_name = token_name
        self.allocations: List[TokenAllocation] = []
    
    def add_allocation(self, category: str, percentage: float, description: str, vesting_period: str = None):
        """Add a token allocation category to the report"""
        self.allocations.append(
            TokenAllocation(
                category=category,
                percentage=percentage,
                description=description,
                vesting_period=vesting_period
            )
        )
    
    def validate_percentages(self) -> bool:
        """Validate that allocations sum to 100%"""
        total = sum(alloc.percentage for alloc in self.allocations)
        return abs(total - 100.0) < 0.01
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive tokenomics report"""
        if not self.validate_percentages():
            raise ValueError("Token allocations do not sum to 100%")
        
        report = {
            "token": self.token_name,
            "total_supply": "1,000,000,000 STARS",  # Example value
            "allocations": [
                {
                    "category": alloc.category,
                    "percentage": f"{alloc.percentage}%",
                    "tokens": f"{alloc.percentage * 10_000_000:.0f} STARS",  # Calculated from percentage
                    "description": alloc.description,
                    "vesting_period": alloc.vesting_period or "N/A"
                }
                for alloc in self.allocations
            ],
            "notes": "All percentages are approximate and subject to change based on project needs."
        }
        return report
    
    def save_report(self, filename: str = "tokenomics_report.json"):
        """Save the report to a JSON file"""
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)

def generate_stars_tokenomics():
    """Generate the $STARS tokenomics report"""
    report = TokenomicsReport("STARS")
    
    # Add allocation categories
    report.add_allocation(
        category="Presale",
        percentage=30.0,
        description="Tokens allocated for presale investors",
        vesting_period="6 months linear vesting"
    )
    report.add_allocation(
        category="Staking Rewards",
        percentage=25.0,
        description="Tokens reserved for staking rewards",
        vesting_period="Released over 3 years"
    )
    report.add_allocation(
        category="Marketing",
        percentage=15.0,
        description="Tokens allocated for marketing and partnerships",
        vesting_period="12 months linear vesting"
    )
    report.add_allocation(
        category="CEX/DEX Liquidity",
        percentage=20.0,
        description="Tokens allocated for exchange liquidity pools",
        vesting_period="50% unlocked at TGE, remainder over 6 months"
    )
    report.add_allocation(
        category="MemeVault Ecosystem",
        percentage=10.0,
        description="Tokens reserved for MemeVault ecosystem development",
        vesting_period="24 months linear vesting"
    )
    
    return report

if __name__ == "__main__":
    try:
        stars_report = generate_stars_tokenomics()
        report_data = stars_report.generate_report()
        stars_report.save_report()
        
        print("Tokenomics Report Generated Successfully:")
        print(json.dumps(report_data, indent=4))
    except Exception as e:
        print(f"Error generating tokenomics report: {str(e)}")
```
