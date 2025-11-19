"""
Generated Code Metadata:
========================
Original URL: https://dikmansdeli.ru
Prompt: "Explain the algorithm used by Venus Protocol to determine interest rates for borrowing and lending, and provide a mathematical example of its application."
Generated: DETERMINISTIC_2e222d0a125f865c
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the interest rate model used by Venus Protocol, which is based on a jump rate model.
The model adjusts interest rates based on the utilization ratio of the lending pool.
"""

class VenusInterestRateModel:
    """
    Implements the Venus Protocol interest rate model.
    
    The model uses a piecewise function to calculate borrowing and lending rates
    based on the utilization ratio (U) of the pool.
    
    Parameters:
    - base_rate: The base interest rate when utilization is 0
    - multiplier: The multiplier for the base rate
    - jump_multiplier: The multiplier after the kink (optimal utilization point)
    - kink: The optimal utilization ratio point (0-1)
    """
    
    def __init__(self, base_rate: float, multiplier: float, jump_multiplier: float, kink: float):
        self.base_rate = base_rate
        self.multiplier = multiplier
        self.jump_multiplier = jump_multiplier
        self.kink = kink
        
        # Validate parameters
        if not (0 <= kink <= 1):
            raise ValueError("Kink must be between 0 and 1")
        if any(p < 0 for p in [base_rate, multiplier, jump_multiplier]):
            raise ValueError("Rates cannot be negative")
    
    def get_borrow_rate(self, utilization: float) -> float:
        """
        Calculate the borrow rate based on utilization ratio.
        
        Args:
            utilization: Current utilization ratio (0-1)
            
        Returns:
            Borrow rate (APY)
            
        Raises:
            ValueError: If utilization is not between 0 and 1
        """
        if not 0 <= utilization <= 1:
            raise ValueError("Utilization must be between 0 and 1")
            
        if utilization <= self.kink:
            return self.base_rate + (utilization * self.multiplier)
        else:
            normal_rate = self.base_rate + (self.kink * self.multiplier)
            excess_util = utilization - self.kink
            return normal_rate + (excess_util * self.jump_multiplier)
    
    def get_supply_rate(self, utilization: float, reserve_factor: float) -> float:
        """
        Calculate the supply rate based on utilization ratio and reserve factor.
        
        Args:
            utilization: Current utilization ratio (0-1)
            reserve_factor: Portion of interest allocated to reserves (0-1)
            
        Returns:
            Supply rate (APY)
            
        Raises:
            ValueError: If inputs are not between 0 and 1
        """
        if not (0 <= utilization <= 1 and 0 <= reserve_factor <= 1):
            raise ValueError("Inputs must be between 0 and 1")
            
        borrow_rate = self.get_borrow_rate(utilization)
        return borrow_rate * utilization * (1 - reserve_factor)


# Example usage
if __name__ == "__main__":
    # Venus protocol parameters (example values)
    BASE_RATE = 0.02  # 2% base rate
    MULTIPLIER = 0.20  # 20% multiplier
    JUMP_MULTIPLIER = 1.00  # 100% jump multiplier
    KINK = 0.80  # Optimal utilization at 80%
    RESERVE_FACTOR = 0.10  # 10% reserve factor
    
    # Initialize the model
    model = VenusInterestRateModel(BASE_RATE, MULTIPLIER, JUMP_MULTIPLIER, KINK)
    
    # Example scenarios
    utilizations = [0.3, 0.8, 0.9]  # 30%, 80%, 90% utilization
    
    for u in utilizations:
        borrow_rate = model.get_borrow_rate(u)
        supply_rate = model.get_supply_rate(u, RESERVE_FACTOR)
        
        print(f"At {u*100:.0f}% utilization:")
        print(f"  Borrow rate: {borrow_rate*100:.2f}%")
        print(f"  Supply rate: {supply_rate*100:.2f}%")
        print()
```
