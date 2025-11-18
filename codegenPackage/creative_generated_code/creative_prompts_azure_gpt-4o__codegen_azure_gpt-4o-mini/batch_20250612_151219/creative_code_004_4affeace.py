"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbbag.com
Prompt: Develop a program to simulate the allocation of presale funds according to MoonBag's strategic roadmap (e.g., 20% liquidity boost, 75% marketing blitz, 5% operational warp drive).
Generated: DETERMINISTIC_4affeacea5bfbe64
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PresaleFundAllocator:
    def __init__(self, total_funds):
        """
        Initialize the PresaleFundAllocator with total funds.
        
        :param total_funds: The total amount of funds to be allocated.
        """
        if total_funds <= 0:
            raise ValueError("Total funds must be greater than zero.")
        self.total_funds = total_funds
        self.allocated_funds = {
            "liquidity_boost": 0,
            "marketing_blitz": 0,
            "operational_warp_drive": 0
        }

    def allocate_funds(self):
        """
        Allocate funds according to the strategic roadmap.
        
        Allocations:
        - 20% to liquidity boost
        - 75% to marketing blitz
        - 5% to operational warp drive
        """
        # Calculate allocations based on percentages
        try:
            self.allocated_funds["liquidity_boost"] = self._allocate(0.20)
            self.allocated_funds["marketing_blitz"] = self._allocate(0.75)
            self.allocated_funds["operational_warp_drive"] = self._allocate(0.05)
        except ValueError as e:
            print(f"Error during allocation: {e}")

    def _allocate(self, percentage):
        """
        Helper method to calculate the allocated amount based on a percentage.
        
        :param percentage: The percentage of total funds to allocate.
        :return: The allocated amount.
        """
        if percentage < 0 or percentage > 1:
            raise ValueError("Percentage must be between 0 and 1.")
        return self.total_funds * percentage

    def get_allocated_funds(self):
        """
        Retrieve the allocated funds.
        
        :return: A dictionary of allocated funds.
        """
        return self.allocated_funds

if __name__ == "__main__":
    try:
        # Example usage
        total_funds = 100000  # Total funds for presale
        allocator = PresaleFundAllocator(total_funds)
        allocator.allocate_funds()
        print("Allocated Funds:", allocator.get_allocated_funds())
    except ValueError as e:
        print(f"Initialization error: {e}")
```
