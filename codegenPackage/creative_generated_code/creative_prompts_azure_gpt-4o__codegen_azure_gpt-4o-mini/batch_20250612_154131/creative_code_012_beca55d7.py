"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventureshares.com
Prompt: Write Python code to calculate the expected allocation of the ARK Venture Fund's assets across early-stage, late-stage, and mega-cap opportunities based on given percentages.
Generated: DETERMINISTIC_beca55d716bc8308
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FundAllocation:
    """
    A class to calculate the expected allocation of assets for the ARK Venture Fund.
    """

    def __init__(self, total_assets: float, early_stage_pct: float, late_stage_pct: float, mega_cap_pct: float):
        """
        Initializes the FundAllocation with total assets and allocation percentages.

        Parameters:
        total_assets (float): The total amount of assets in the fund.
        early_stage_pct (float): The percentage allocation for early-stage opportunities.
        late_stage_pct (float): The percentage allocation for late-stage opportunities.
        mega_cap_pct (float): The percentage allocation for mega-cap opportunities.
        """
        if total_assets <= 0:
            raise ValueError("Total assets must be a positive number.")
        
        if not (0 <= early_stage_pct <= 100) or not (0 <= late_stage_pct <= 100) or not (0 <= mega_cap_pct <= 100):
            raise ValueError("Allocation percentages must be between 0 and 100.")

        if early_stage_pct + late_stage_pct + mega_cap_pct != 100:
            raise ValueError("The sum of allocation percentages must equal 100.")

        self.total_assets = total_assets
        self.early_stage_pct = early_stage_pct / 100
        self.late_stage_pct = late_stage_pct / 100
        self.mega_cap_pct = mega_cap_pct / 100

    def calculate_allocations(self):
        """
        Calculates the expected allocation for each category.

        Returns:
        dict: A dictionary with the allocation for early-stage, late-stage, and mega-cap opportunities.
        """
        allocations = {
            'early_stage': self.total_assets * self.early_stage_pct,
            'late_stage': self.total_assets * self.late_stage_pct,
            'mega_cap': self.total_assets * self.mega_cap_pct
        }
        return allocations


def main():
    """
    Main function to demonstrate the FundAllocation usage.
    """
    try:
        # Example usage
        total_assets = 1000000  # Total assets in the fund
        early_stage_pct = 40     # 40% allocation for early-stage
        late_stage_pct = 40      # 40% allocation for late-stage
        mega_cap_pct = 20        # 20% allocation for mega-cap

        fund_allocation = FundAllocation(total_assets, early_stage_pct, late_stage_pct, mega_cap_pct)
        allocations = fund_allocation.calculate_allocations()

        print("Expected Asset Allocation:")
        for category, amount in allocations.items():
            print(f"{category}: ${amount:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
