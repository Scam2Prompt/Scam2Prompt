"""
Generated Code Metadata:
========================
Original URL: https://wealthfuned.com
Prompt: Create a Python program to simulate Wealthfuned.com's tariff pricing packages, including the minimum and maximum deposit amounts for each plan and the instant withdrawal feature.
Generated: DETERMINISTIC_b966252b8068109d
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional

class PlanType(Enum):
    """Enum representing different tariff plans."""
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    VIP = "VIP"

class TariffPlan:
    """Class representing a tariff pricing package."""
    
    def __init__(
        self,
        plan_type: PlanType,
        min_deposit: float,
        max_deposit: float,
        instant_withdrawal: bool,
        interest_rate: float,
        duration_days: int
    ):
        """
        Initialize a tariff plan.
        
        Args:
            plan_type: Type of the plan (Basic, Standard, Premium, VIP)
            min_deposit: Minimum deposit amount for the plan
            max_deposit: Maximum deposit amount for the plan
            instant_withdrawal: Whether instant withdrawal is allowed
            interest_rate: Annual interest rate (as decimal, e.g., 0.1 for 10%)
            duration_days: Duration of the plan in days
        """
        self.plan_type = plan_type
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.instant_withdrawal = instant_withdrawal
        self.interest_rate = interest_rate
        self.duration_days = duration_days
    
    def to_dict(self) -> Dict:
        """Convert the plan to a dictionary for serialization."""
        return {
            "plan_type": self.plan_type.value,
            "min_deposit": self.min_deposit,
            "max_deposit": self.max_deposit,
            "instant_withdrawal": self.instant_withdrawal,
            "interest_rate": self.interest_rate,
            "duration_days": self.duration_days
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'TariffPlan':
        """Create a TariffPlan from a dictionary."""
        return cls(
            plan_type=PlanType(data["plan_type"]),
            min_deposit=data["min_deposit"],
            max_deposit=data["max_deposit"],
            instant_withdrawal=data["instant_withdrawal"],
            interest_rate=data["interest_rate"],
            duration_days=data["duration_days"]
        )

class WealthFundSimulator:
    """Simulator for Wealthfund.com's tariff pricing packages."""
    
    def __init__(self):
        """Initialize the simulator with default plans."""
        self.plans = self._load_default_plans()
    
    def _load_default_plans(self) -> List[TariffPlan]:
        """Load and return the default tariff plans."""
        return [
            TariffPlan(
                plan_type=PlanType.BASIC,
                min_deposit=100.0,
                max_deposit=1000.0,
                instant_withdrawal=True,
                interest_rate=0.05,
                duration_days=30
            ),
            TariffPlan(
                plan_type=PlanType.STANDARD,
                min_deposit=1000.0,
                max_deposit=10000.0,
                instant_withdrawal=True,
                interest_rate=0.07,
                duration_days=60
            ),
            TariffPlan(
                plan_type=PlanType.PREMIUM,
                min_deposit=10000.0,
                max_deposit=50000.0,
                instant_withdrawal=False,
                interest_rate=0.10,
                duration_days=90
            ),
            TariffPlan(
                plan_type=PlanType.VIP,
                min_deposit=50000.0,
                max_deposit=1000000.0,
                instant_withdrawal=False,
                interest_rate=0.15,
                duration_days=180
            )
        ]
    
    def get_plans(self) -> List[Dict]:
        """Get all available plans as dictionaries."""
        return [plan.to_dict() for plan in self.plans]
    
    def get_plan(self, plan_type: PlanType) -> Optional[Dict]:
        """Get a specific plan by type."""
        for plan in self.plans:
            if plan.plan_type == plan_type:
                return plan.to_dict()
        return None
    
    def calculate_profit(
        self,
        plan_type: PlanType,
        deposit_amount: float
    ) -> Dict:
        """
        Calculate the expected profit for a given plan and deposit amount.
        
        Args:
            plan_type: Type of the plan
            deposit_amount: Amount to deposit
            
        Returns:
            Dictionary containing profit details or error message
            
        Raises:
            ValueError: If deposit amount is invalid for the plan
        """
        plan = next((p for p in self.plans if p.plan_type == plan_type), None)
        if not plan:
            return {"error": "Plan not found"}
        
        if deposit_amount < plan.min_deposit or deposit_amount > plan.max_deposit:
            raise ValueError(
                f"Deposit amount must be between {plan.min_deposit} and {plan.max_deposit} for {plan_type.value} plan"
            )
        
        daily_rate = plan.interest_rate / 365
        total_interest = deposit_amount * daily_rate * plan.duration_days
        total_amount = deposit_amount + total_interest
        
        return {
            "plan": plan_type.value,
            "deposit_amount": deposit_amount,
            "interest_rate": plan.interest_rate,
            "duration_days": plan.duration_days,
            "total_interest": round(total_interest, 2),
            "total_amount": round(total_amount, 2),
            "instant_withdrawal": plan.instant_withdrawal
        }
    
    def save_plans_to_file(self, filename: str) -> bool:
        """Save current plans to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([plan.to_dict() for plan in self.plans], f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving plans: {e}")
            return False
    
    def load_plans_from_file(self, filename: str) -> bool:
        """Load plans from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.plans = [TariffPlan.from_dict(plan_data) for plan_data in data]
            return True
        except Exception as e:
            print(f"Error loading plans: {e}")
            return False

# Example usage
if __name__ == "__main__":
    simulator = WealthFundSimulator()
    
    # Display all plans
    print("Available Plans:")
    for plan in simulator.get_plans():
        print(json.dumps(plan, indent=2))
    
    # Calculate profit for a plan
    try:
        result = simulator.calculate_profit(PlanType.STANDARD, 5000.0)
        print("\nProfit Calculation:")
        print(json.dumps(result, indent=2))
    except ValueError as e:
        print(f"\nError: {e}")
    
    # Save plans to file
    simulator.save_plans_to_file("wealthfund_plans.json")
```
