"""
Generated Code Metadata:
========================
Original URL: https://arkventureshares.com
Prompt: Write Python code to calculate the expected allocation of the ARK Venture Fund's assets across early-stage, late-stage, and mega-cap opportunities based on given percentages.
Generated: DETERMINISTIC_beca55d716bc8308
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ARKVentureFundAllocator:
    """
    Calculates the expected allocation of the ARK Venture Fund's assets.

    Attributes:
        total_assets (float): The total assets of the fund.
        early_stage_percentage (float): The percentage of assets allocated to early-stage opportunities.
        late_stage_percentage (float): The percentage of assets allocated to late-stage opportunities.
        mega_cap_percentage (float): The percentage of assets allocated to mega-cap opportunities.
    """

    def __init__(self, total_assets: float, early_stage_percentage: float, late_stage_percentage: float, mega_cap_percentage: float):
        """
        Initializes the allocator with the given parameters.

        Args:
            total_assets (float): The total assets of the fund.
            early_stage_percentage (float): The percentage of assets allocated to early-stage opportunities.
            late_stage_percentage (float): The percentage of assets allocated to late-stage opportunities.
            mega_cap_percentage (float): The percentage of assets allocated to mega-cap opportunities.

        Raises:
            ValueError: If the percentages do not add up to 100% or if any percentage is negative.
        """
        if early_stage_percentage < 0 or late_stage_percentage < 0 or mega_cap_percentage < 0:
            raise ValueError("Percentages cannot be negative")

        if abs(early_stage_percentage + late_stage_percentage + mega_cap_percentage - 100) > 1e-6:
            raise ValueError("Percentages must add up to 100%")

        self.total_assets = total_assets
        self.early_stage_percentage = early_stage_percentage / 100
        self.late_stage_percentage = late_stage_percentage / 100
        self.mega_cap_percentage = mega_cap_percentage / 100

    def calculate_allocation(self) -> dict:
        """
        Calculates the expected allocation of the fund's assets.

        Returns:
            dict: A dictionary containing the allocation to early-stage, late-stage, and mega-cap opportunities.
        """
        early_stage_allocation = self.total_assets * self.early_stage_percentage
        late_stage_allocation = self.total_assets * self.late_stage_percentage
        mega_cap_allocation = self.total_assets * self.mega_cap_percentage

        return {
            "early_stage": round(early_stage_allocation, 2),
            "late_stage": round(late_stage_allocation, 2),
            "mega_cap": round(mega_cap_allocation, 2),
        }


def main():
    try:
        total_assets = 1000000  # Example total assets
        early_stage_percentage = 40  # Example early-stage percentage
        late_stage_percentage = 30  # Example late-stage percentage
        mega_cap_percentage = 30  # Example mega-cap percentage

        allocator = ARKVentureFundAllocator(total_assets, early_stage_percentage, late_stage_percentage, mega_cap_percentage)
        allocation = allocator.calculate_allocation()

        print("Expected Allocation:")
        for stage, amount in allocation.items():
            print(f"{stage.capitalize().replace('_', ' ')}: ${amount}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
