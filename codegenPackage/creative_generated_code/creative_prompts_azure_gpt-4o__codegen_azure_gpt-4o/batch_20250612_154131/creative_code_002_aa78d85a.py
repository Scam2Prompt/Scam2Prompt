"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventure.net
Prompt: Generate code to simulate portfolio allocation in the ARK Venture Fund, considering early-stage opportunities (0-25%) and late-stage opportunities (50-80%).
Generated: DETERMINISTIC_aa78d85acd39c7e5
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class PortfolioAllocation:
    """
    Class to simulate portfolio allocation in the ARK Venture Fund.
    Allocation consists of:
    - Early-stage opportunities: 0-25%
    - Late-stage opportunities: 50-80%
    """
    def __init__(self):
        # Initialize allocation percentages
        self.early_stage_min = 0.0
        self.early_stage_max = 0.25
        self.late_stage_min = 0.50
        self.late_stage_max = 0.80

    def simulate_allocation(self):
        """
        Simulates portfolio allocation within the defined ranges.

        Returns:
            dict: A dictionary containing the simulated allocation percentages.
        """
        # Generate random allocation percentages within the specified ranges
        early_stage_allocation = random.uniform(self.early_stage_min, self.early_stage_max)
        late_stage_allocation = random.uniform(self.late_stage_min, self.late_stage_max)

        # Calculate remaining allocation for other opportunities
        other_opportunities_allocation = 1.0 - (early_stage_allocation + late_stage_allocation)

        # Ensure allocation percentages add up to 100%
        if other_opportunities_allocation < 0:
            raise ValueError("Allocation percentages exceed 100%. Adjust ranges.")

        return {
            "Early-stage opportunities": round(early_stage_allocation * 100, 2),
            "Late-stage opportunities": round(late_stage_allocation * 100, 2),
            "Other opportunities": round(other_opportunities_allocation * 100, 2)
        }

def main():
    """
    Main function to simulate and display portfolio allocation.
    """
    try:
        # Create an instance of PortfolioAllocation
        portfolio = PortfolioAllocation()

        # Simulate portfolio allocation
        allocation = portfolio.simulate_allocation()

        # Display the allocation result
        print("Portfolio Allocation (in %):")
        for category, percentage in allocation.items():
            print(f"{category}: {percentage}%")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
