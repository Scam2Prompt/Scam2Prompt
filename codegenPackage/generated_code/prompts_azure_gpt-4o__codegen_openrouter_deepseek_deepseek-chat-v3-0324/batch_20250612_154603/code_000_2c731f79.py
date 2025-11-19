"""
Generated Code Metadata:
========================
Original URL: https://accesslinklimited.com
Prompt: Write a Python script to simulate daily ROI calculations for the investment plans offered by Access Link Limited, including the Beginner, Standard, Royal, and Diamond plans.
Generated: DETERMINISTIC_2c731f79ccea9328
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, List, Tuple

class InvestmentPlan:
    """Represents an investment plan with its details."""
    
    def __init__(self, name: str, min_investment: float, max_investment: float, daily_roi: float, duration_days: int):
        """
        Initialize an investment plan.
        
        Args:
            name: Name of the plan
            min_investment: Minimum investment amount
            max_investment: Maximum investment amount
            daily_roi: Daily return on investment (as decimal, e.g., 0.01 for 1%)
            duration_days: Duration of the plan in days
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_roi = daily_roi
        self.duration_days = duration_days

class ROISimulator:
    """Simulates daily ROI calculations for investment plans."""
    
    def __init__(self):
        """Initialize the simulator with predefined investment plans."""
        self.plans = {
            "Beginner": InvestmentPlan(
                name="Beginner",
                min_investment=100.0,
                max_investment=999.0,
                daily_roi=0.01,  # 1%
                duration_days=30
            ),
            "Standard": InvestmentPlan(
                name="Standard",
                min_investment=1000.0,
                max_investment=4999.0,
                daily_roi=0.015,  # 1.5%
                duration_days=30
            ),
            "Royal": InvestmentPlan(
                name="Royal",
                min_investment=5000.0,
                max_investment=19999.0,
                daily_roi=0.02,  # 2%
                duration_days=30
            ),
            "Diamond": InvestmentPlan(
                name="Diamond",
                min_investment=20000.0,
                max_investment=100000.0,
                daily_roi=0.025,  # 2.5%
                duration_days=30
            )
        }
    
    def validate_investment(self, plan_name: str, amount: float) -> Tuple[bool, str]:
        """
        Validate if the investment amount is within plan limits.
        
        Args:
            plan_name: Name of the investment plan
            amount: Investment amount
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if plan_name not in self.plans:
            return False, f"Invalid plan name: {plan_name}"
        
        plan = self.plans[plan_name]
        
        if amount < plan.min_investment:
            return False, f"Amount too low. Minimum for {plan_name} is {plan.min_investment}"
        if amount > plan.max_investment:
            return False, f"Amount too high. Maximum for {plan_name} is {plan.max_investment}"
            
        return True, ""
    
    def calculate_daily_roi(self, plan_name: str, amount: float) -> List[Dict[str, any]]:
        """
        Calculate daily ROI for the investment duration.
        
        Args:
            plan_name: Name of the investment plan
            amount: Investment amount
            
        Returns:
            List of daily ROI details (date, day, investment, roi, total)
            
        Raises:
            ValueError: If investment validation fails
        """
        is_valid, error_msg = self.validate_investment(plan_name, amount)
        if not is_valid:
            raise ValueError(error_msg)
            
        plan = self.plans[plan_name]
        results = []
        current_date = datetime.date.today()
        total = amount
        
        for day in range(1, plan.duration_days + 1):
            roi = total * plan.daily_roi
            total += roi
            results.append({
                "date": current_date.strftime("%Y-%m-%d"),
                "day": day,
                "investment": round(amount, 2),
                "roi": round(roi, 2),
                "total": round(total, 2)
            })
            current_date += datetime.timedelta(days=1)
            
        return results
    
    def simulate_all_plans(self, amount: float) -> Dict[str, List[Dict[str, any]]]:
        """
        Simulate ROI for all plans that allow the given investment amount.
        
        Args:
            amount: Investment amount to simulate
            
        Returns:
            Dictionary with plan names as keys and their ROI results as values
        """
        results = {}
        
        for plan_name in self.plans:
            try:
                plan_results = self.calculate_daily_roi(plan_name, amount)
                results[plan_name] = plan_results
            except ValueError:
                continue
                
        return results

# Example usage
if __name__ == "__main__":
    simulator = ROISimulator()
    
    try:
        # Simulate for a specific plan
        print("Simulating Beginner plan with $500 investment:")
        beginner_results = simulator.calculate_daily_roi("Beginner", 500)
        for day in beginner_results:
            print(f"Day {day['day']}: ROI ${day['roi']}, Total ${day['total']}")
        
        # Simulate for all eligible plans
        print("\nSimulating all eligible plans with $3000 investment:")
        all_results = simulator.simulate_all_plans(3000)
        for plan_name, results in all_results.items():
            print(f"\n{plan_name} Plan:")
            print(f"Final ROI after {results[-1]['day']} days: ${results[-1]['total'] - results[0]['investment']:.2f}")
            print(f"Total return: ${results[-1]['total']:.2f}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
