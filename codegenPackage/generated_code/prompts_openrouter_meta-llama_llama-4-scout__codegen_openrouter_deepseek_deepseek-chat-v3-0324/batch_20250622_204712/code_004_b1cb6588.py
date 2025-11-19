"""
Generated Code Metadata:
========================
Original URL: https://x1blockdag.pages.dev
Prompt: Create a detailed report on the tokenomics of BlockDAG, including the allocation of BDAG coins for the community, presale, and team, and the implications for the project's ecosystem.
Generated: DETERMINISTIC_b1cb6588a1154ec9
Batch ID: 20250622_204712
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
from enum import Enum

class AllocationCategory(Enum):
    COMMUNITY = "Community"
    PRESALE = "Presale"
    TEAM = "Team"
    ECOSYSTEM = "Ecosystem Development"
    ADVISORS = "Advisors"
    RESERVES = "Reserves"

@dataclass
class TokenAllocation:
    category: AllocationCategory
    percentage: float
    vesting_period: str
    purpose: str

class BlockDAGTokenomicsReport:
    def __init__(self):
        self.total_supply = 100_000_000  # Example total supply
        self.allocations: List[TokenAllocation] = [
            TokenAllocation(
                category=AllocationCategory.COMMUNITY,
                percentage=40.0,
                vesting_period="Immediate",
                purpose="Community incentives, airdrops, and rewards"
            ),
            TokenAllocation(
                category=AllocationCategory.PRESALE,
                percentage=25.0,
                vesting_period="6-12 months",
                purpose="Early investors and presale participants"
            ),
            TokenAllocation(
                category=AllocationCategory.TEAM,
                percentage=15.0,
                vesting_period="24 months with 6-month cliff",
                purpose="Core team development and retention"
            ),
            TokenAllocation(
                category=AllocationCategory.ECOSYSTEM,
                percentage=10.0,
                vesting_period="12-24 months",
                purpose="Partnerships, grants, and ecosystem growth"
            ),
            TokenAllocation(
                category=AllocationCategory.ADVISORS,
                percentage=5.0,
                vesting_period="12 months with 3-month cliff",
                purpose="Strategic advisors and consultants"
            ),
            TokenAllocation(
                category=AllocationCategory.RESERVES,
                percentage=5.0,
                vesting_period="TBD",
                purpose="Future development and contingencies"
            )
        ]

    def calculate_allocation_amounts(self) -> Dict[str, float]:
        """Calculate the exact token amounts for each allocation category."""
        return {
            allocation.category.value: round(self.total_supply * (allocation.percentage / 100))
            for allocation in self.allocations
        }

    def generate_report(self) -> Dict:
        """Generate a comprehensive tokenomics report."""
        allocation_amounts = self.calculate_allocation_amounts()
        
        report = {
            "total_supply": self.total_supply,
            "allocations": [
                {
                    "category": alloc.category.value,
                    "percentage": alloc.percentage,
                    "amount": allocation_amounts[alloc.category.value],
                    "vesting_period": alloc.vesting_period,
                    "purpose": alloc.purpose,
                    "implications": self._get_implications(alloc.category)
                }
                for alloc in self.allocations
            ],
            "summary": self._generate_summary()
        }
        
        return report

    def _get_implications(self, category: AllocationCategory) -> str:
        """Return the ecosystem implications for each allocation category."""
        implications = {
            AllocationCategory.COMMUNITY: "Ensures wide distribution and active participation in the network.",
            AllocationCategory.PRESALE: "Provides early funding while preventing immediate dumping through vesting.",
            AllocationCategory.TEAM: "Aligns team incentives with long-term project success.",
            AllocationCategory.ECOSYSTEM: "Fuels growth through strategic partnerships and developer incentives.",
            AllocationCategory.ADVISORS: "Brings expertise while maintaining alignment with project goals.",
            AllocationCategory.RESERVES: "Provides flexibility for future needs and unexpected opportunities."
        }
        return implications.get(category, "No specific implications documented.")

    def _generate_summary(self) -> str:
        """Generate a summary of the tokenomics model."""
        return (
            "The BlockDAG tokenomics model is designed to balance immediate community incentives "
            "with long-term project sustainability. The majority of tokens are allocated to the "
            "community and presale participants to ensure decentralization, while team and advisor "
            "allocations are vested to align interests with the project's success. Ecosystem and "
            "reserve funds provide flexibility for future growth and development."
        )

    def save_report(self, filename: str = "blockdag_tokenomics_report.json"):
        """Save the report to a JSON file."""
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        report_generator = BlockDAGTokenomicsReport()
        report = report_generator.generate_report()
        print(json.dumps(report, indent=4))
        report_generator.save_report()
    except Exception as e:
        print(f"Error generating tokenomics report: {str(e)}")
```
