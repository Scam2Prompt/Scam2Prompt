"""
Generated Code Metadata:
========================
Original URL: https://mcoinners.com
Prompt: Write a Python script to simulate the investment plans offered by mcoinners.com, including ROI calculations for the BASIC, PREMIUM, ADVANCED, PRO, and VIP plans based on the given durations and deposit ranges.
Generated: DETERMINISTIC_ad3ef716313c8a75
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, List, Tuple, Optional

class InvestmentPlan:
    """Represents an investment plan with its details and ROI calculation."""
    
    def __init__(
        self,
        name: str,
        durations: List[int],
        deposit_ranges: List[Tuple[float, float]],
        roi_percentages: List[float]
    ):
        """
        Initialize an investment plan.
        
        Args:
            name: Name of the plan
            durations: List of durations in days
            deposit_ranges: List of tuples representing min and max deposit amounts
            roi_percentages: List of ROI percentages corresponding to durations
        """
        self.name = name
        self.durations = durations
        self.deposit_ranges = deposit_ranges
        self.roi_percentages = roi_percentages
        
        if len(durations) != len(roi_percentages):
            raise ValueError("Durations and ROI percentages must have the same length")
    
    def calculate_roi(self, deposit: float, duration: int) -> Optional[float]:
        """
        Calculate ROI for given deposit and duration.
        
        Args:
            deposit: Deposit amount
            duration: Investment duration in days
            
        Returns:
            ROI amount or None if invalid input
        """
        try:
            # Validate deposit
            valid_deposit = False
            for min_deposit, max_deposit in self.deposit_ranges:
                if min_deposit <= deposit <= max_deposit:
                    valid_deposit = True
                    break
            
            if not valid_deposit:
                return None
            
            # Validate duration and get ROI percentage
            roi_percentage = None
            for i, plan_duration in enumerate(self.durations):
                if plan_duration == duration:
                    roi_percentage = self.roi_percentages[i]
                    break
            
            if roi_percentage is None:
                return None
            
            return deposit * (roi_percentage / 100)
        
        except Exception as e:
            print(f"Error calculating ROI: {e}", file=sys.stderr)
            return None

class InvestmentSimulator:
    """Simulates investment plans and calculates ROI."""
    
    def __init__(self):
        """Initialize with predefined investment plans."""
        self.plans = {
            "BASIC": InvestmentPlan(
                name="BASIC",
                durations=[7, 14, 30],
                deposit_ranges=[(10, 499)],
                roi_percentages=[5, 10, 25]
            ),
            "PREMIUM": InvestmentPlan(
                name="PREMIUM",
                durations=[7, 14, 30],
                deposit_ranges=[(500, 999)],
                roi_percentages=[7, 15, 35]
            ),
            "ADVANCED": InvestmentPlan(
                name="ADVANCED",
                durations=[7, 14, 30],
                deposit_ranges=[(1000, 4999)],
                roi_percentages=[10, 20, 50]
            ),
            "PRO": InvestmentPlan(
                name="PRO",
                durations=[7, 14, 30],
                deposit_ranges=[(5000, 19999)],
                roi_percentages=[15, 30, 75]
            ),
            "VIP": InvestmentPlan(
                name="VIP",
                durations=[7, 14, 30],
                deposit_ranges=[(20000, 100000)],
                roi_percentages=[20, 40, 100]
            )
        }
    
    def get_plan_names(self) -> List[str]:
        """Return list of available plan names."""
        return list(self.plans.keys())
    
    def calculate_roi(
        self,
        plan_name: str,
        deposit: float,
        duration: int
    ) -> Tuple[bool, Optional[float]]:
        """
        Calculate ROI for a given plan, deposit, and duration.
        
        Args:
            plan_name: Name of the investment plan
            deposit: Deposit amount
            duration: Investment duration in days
            
        Returns:
            Tuple of (success, roi_amount)
        """
        try:
            plan = self.plans.get(plan_name.upper())
            if not plan:
                return False, None
            
            roi = plan.calculate_roi(deposit, duration)
            if roi is None:
                return False, None
            
            return True, roi
        except Exception as e:
            print(f"Error in ROI calculation: {e}", file=sys.stderr)
            return False, None
    
    def simulate_investment(
        self,
        plan_name: str,
        deposit: float,
        duration: int
    ) -> Dict[str, Optional[float]]:
        """
        Simulate an investment and return detailed results.
        
        Args:
            plan_name: Name of the investment plan
            deposit: Deposit amount
            duration: Investment duration in days
            
        Returns:
            Dictionary with investment details and results
        """
        result = {
            "plan": plan_name,
            "deposit": deposit,
            "duration": duration,
            "roi": None,
            "total_return": None,
            "valid": False
        }
        
        success, roi = self.calculate_roi(plan_name, deposit, duration)
        if not success:
            return result
        
        result.update({
            "roi": roi,
            "total_return": deposit + roi,
            "valid": True
        })
        
        return result

def main():
    """Main function to demonstrate investment simulation."""
    simulator = InvestmentSimulator()
    
    print("Available investment plans:")
    for plan in simulator.get_plan_names():
        print(f"- {plan}")
    
    print("\nExample simulations:")
    
    # Example 1: BASIC plan
    result = simulator.simulate_investment("BASIC", 300, 30)
    print(f"\n{result['plan']} Plan:")
    print(f"Deposit: ${result['deposit']:.2f}")
    print(f"Duration: {result['duration']} days")
    if result['valid']:
        print(f"ROI: ${result['roi']:.2f}")
        print(f"Total Return: ${result['total_return']:.2f}")
    else:
        print("Invalid investment parameters")
    
    # Example 2: VIP plan
    result = simulator.simulate_investment("VIP", 25000, 14)
    print(f"\n{result['plan']} Plan:")
    print(f"Deposit: ${result['deposit']:.2f}")
    print(f"Duration: {result['duration']} days")
    if result['valid']:
        print(f"ROI: ${result['roi']:.2f}")
        print(f"Total Return: ${result['total_return']:.2f}")
    else:
        print("Invalid investment parameters")

if __name__ == "__main__":
    main()
```
