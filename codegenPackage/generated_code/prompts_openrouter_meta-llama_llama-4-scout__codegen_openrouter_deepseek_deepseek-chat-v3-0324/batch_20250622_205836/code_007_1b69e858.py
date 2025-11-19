"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoinweb.pages.dev
Prompt: Develop a comprehensive report on the Green Bitcoin project's tokenomics, highlighting the allocation of tokens for presale, staking rewards, marketing, liquidity, and community rewards.
Generated: DETERMINISTIC_1b69e858254b762b
Batch ID: 20250622_205836
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
    """Data class representing a single token allocation category."""
    name: str
    percentage: float
    description: str
    vesting_period: str = None

class TokenomicsReport:
    """Generates a comprehensive report on token allocation for the Green Bitcoin project."""
    
    def __init__(self):
        self.allocations: List[TokenAllocation] = []
        self.total_supply: int = 21_000_000  # Example total supply
    
    def add_allocation(self, allocation: TokenAllocation) -> None:
        """Adds a token allocation category to the report."""
        self.allocations.append(allocation)
    
    def validate_allocations(self) -> bool:
        """Validates that allocations sum to 100%."""
        total = sum(alloc.percentage for alloc in self.allocations)
        return abs(total - 100.0) < 0.01  # Account for floating point precision
    
    def generate_report(self) -> Dict:
        """Generates the tokenomics report with detailed allocations."""
        if not self.validate_allocations():
            raise ValueError("Token allocations do not sum to 100%")
        
        report = {
            "total_supply": self.total_supply,
            "allocations": [],
            "token_distribution": {}
        }
        
        for alloc in self.allocations:
            token_amount = int(self.total_supply * (alloc.percentage / 100))
            allocation_data = {
                "category": alloc.name,
                "percentage": alloc.percentage,
                "tokens": token_amount,
                "description": alloc.description,
                "vesting_period": alloc.vesting_period
            }
            report["allocations"].append(allocation_data)
            report["token_distribution"][alloc.name] = token_amount
        
        return report
    
    def save_report(self, filename: str = "green_bitcoin_tokenomics.json") -> None:
        """Saves the report to a JSON file."""
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)

def main():
    """Main function to generate and display the Green Bitcoin tokenomics report."""
    try:
        report = TokenomicsReport()
        
        # Add token allocations
        report.add_allocation(TokenAllocation(
            name="Presale",
            percentage=40.0,
            description="Tokens allocated for presale investors",
            vesting_period="6-month linear vesting"
        ))
        
        report.add_allocation(TokenAllocation(
            name="Staking Rewards",
            percentage=30.0,
            description="Tokens allocated for staking rewards to incentivize network participation",
            vesting_period="Released over 5 years"
        ))
        
        report.add_allocation(TokenAllocation(
            name="Marketing",
            percentage=10.0,
            description="Tokens allocated for marketing and partnerships",
            vesting_period="12-month linear vesting"
        ))
        
        report.add_allocation(TokenAllocation(
            name="Liquidity",
            percentage=10.0,
            description="Tokens allocated for exchange liquidity pools",
            vesting_period="Locked for 1 year, then released"
        ))
        
        report.add_allocation(TokenAllocation(
            name="Community Rewards",
            percentage=10.0,
            description="Tokens allocated for community incentives and airdrops",
            vesting_period="Released quarterly over 2 years"
        ))
        
        # Generate and display report
        tokenomics = report.generate_report()
        print(json.dumps(tokenomics, indent=4))
        
        # Save report to file
        report.save_report()
        print("\nReport saved to 'green_bitcoin_tokenomics.json'")
        
    except ValueError as e:
        print(f"Error generating report: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
