"""
Generated Code Metadata:
========================
Original URL: https://inceptiontrades.net
Prompt: Create a program to manage investment plans, including starter, enterprise, apex, partnership, and share plans, as outlined on the Inception Trades website.
Generated: DETERMINISTIC_5ff99e1e30376784
Batch ID: 20250612_142620
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


class InvestmentPlanType(Enum):
    """Enum representing different investment plan types."""
    STARTER = "starter"
    ENTERPRISE = "enterprise"
    APEX = "apex"
    PARTNERSHIP = "partnership"
    SHARE = "share"


class InvestmentPlan:
    """Class representing an investment plan with its details."""

    def __init__(
        self,
        name: str,
        plan_type: InvestmentPlanType,
        min_amount: float,
        max_amount: float,
        duration_days: int,
        daily_interest: float,
        referral_bonus: float,
        features: List[str]
    ):
        """Initialize an investment plan.

        Args:
            name: Name of the plan
            plan_type: Type of the plan (from InvestmentPlanType)
            min_amount: Minimum investment amount
            max_amount: Maximum investment amount
            duration_days: Duration of the plan in days
            daily_interest: Daily interest rate (percentage)
            referral_bonus: Referral bonus percentage
            features: List of features included in the plan
        """
        self.name = name
        self.plan_type = plan_type
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.duration_days = duration_days
        self.daily_interest = daily_interest
        self.referral_bonus = referral_bonus
        self.features = features

    def to_dict(self) -> Dict:
        """Convert the plan to a dictionary for serialization."""
        return {
            "name": self.name,
            "plan_type": self.plan_type.value,
            "min_amount": self.min_amount,
            "max_amount": self.max_amount,
            "duration_days": self.duration_days,
            "daily_interest": self.daily_interest,
            "referral_bonus": self.referral_bonus,
            "features": self.features
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InvestmentPlan':
        """Create an InvestmentPlan from a dictionary."""
        return cls(
            name=data["name"],
            plan_type=InvestmentPlanType(data["plan_type"]),
            min_amount=data["min_amount"],
            max_amount=data["max_amount"],
            duration_days=data["duration_days"],
            daily_interest=data["daily_interest"],
            referral_bonus=data["referral_bonus"],
            features=data["features"]
        )


class InvestmentPlanManager:
    """Class to manage investment plans including CRUD operations."""

    def __init__(self, storage_file: str = "investment_plans.json"):
        """Initialize the plan manager with a storage file.

        Args:
            storage_file: Path to JSON file for storing plans
        """
        self.storage_file = storage_file
        self.plans: Dict[str, InvestmentPlan] = {}
        self.load_plans()

    def add_plan(self, plan: InvestmentPlan) -> None:
        """Add a new investment plan.

        Args:
            plan: InvestmentPlan object to add

        Raises:
            ValueError: If a plan with the same name already exists
        """
        if plan.name in self.plans:
            raise ValueError(f"Plan with name '{plan.name}' already exists")
        self.plans[plan.name] = plan
        self.save_plans()

    def get_plan(self, name: str) -> Optional[InvestmentPlan]:
        """Get a plan by its name.

        Args:
            name: Name of the plan to retrieve

        Returns:
            InvestmentPlan if found, None otherwise
        """
        return self.plans.get(name)

    def update_plan(self, name: str, updated_plan: InvestmentPlan) -> None:
        """Update an existing plan.

        Args:
            name: Name of the plan to update
            updated_plan: Updated InvestmentPlan object

        Raises:
            ValueError: If the plan doesn't exist or name is being changed to an existing one
        """
        if name not in self.plans:
            raise ValueError(f"Plan with name '{name}' does not exist")
        if name != updated_plan.name and updated_plan.name in self.plans:
            raise ValueError(f"Cannot rename to '{updated_plan.name}' - plan already exists")
        
        del self.plans[name]
        self.plans[updated_plan.name] = updated_plan
        self.save_plans()

    def delete_plan(self, name: str) -> None:
        """Delete a plan by its name.

        Args:
            name: Name of the plan to delete

        Raises:
            ValueError: If the plan doesn't exist
        """
        if name not in self.plans:
            raise ValueError(f"Plan with name '{name}' does not exist")
        del self.plans[name]
        self.save_plans()

    def list_plans(self) -> List[InvestmentPlan]:
        """Get a list of all investment plans.

        Returns:
            List of all InvestmentPlan objects
        """
        return list(self.plans.values())

    def save_plans(self) -> None:
        """Save all plans to the storage file."""
        with open(self.storage_file, "w") as f:
            json.dump(
                {name: plan.to_dict() for name, plan in self.plans.items()},
                f,
                indent=2
            )

    def load_plans(self) -> None:
        """Load plans from the storage file."""
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                self.plans = {
                    name: InvestmentPlan.from_dict(plan_data)
                    for name, plan_data in data.items()
                }
        except FileNotFoundError:
            self.plans = {}
        except json.JSONDecodeError:
            raise ValueError("Invalid data in storage file")

    def calculate_profit(
        self,
        plan_name: str,
        investment_amount: float,
        days: Optional[int] = None
    ) -> float:
        """Calculate the profit for an investment.

        Args:
            plan_name: Name of the investment plan
            investment_amount: Amount being invested
            days: Optional number of days (defaults to plan duration)

        Returns:
            Calculated profit amount

        Raises:
            ValueError: If plan doesn't exist or investment amount is out of range
        """
        plan = self.get_plan(plan_name)
        if not plan:
            raise ValueError(f"Plan '{plan_name}' not found")
        
        if not (plan.min_amount <= investment_amount <= plan.max_amount):
            raise ValueError(
                f"Investment amount must be between {plan.min_amount} and {plan.max_amount}"
            )
        
        duration = days if days is not None else plan.duration_days
        return investment_amount * (plan.daily_interest / 100) * duration


def initialize_default_plans(manager: InvestmentPlanManager) -> None:
    """Initialize the system with default investment plans."""
    default_plans = [
        InvestmentPlan(
            name="Starter Plan",
            plan_type=InvestmentPlanType.STARTER,
            min_amount=100.0,
            max_amount=999.0,
            duration_days=7,
            daily_interest=1.5,
            referral_bonus=5.0,
            features=["24/7 Support", "Basic Analytics"]
        ),
        InvestmentPlan(
            name="Enterprise Plan",
            plan_type=InvestmentPlanType.ENTERPRISE,
            min_amount=1000.0,
            max_amount=4999.0,
            duration_days=14,
            daily_interest=2.0,
            referral_bonus=7.0,
            features=["Priority Support", "Advanced Analytics", "Dedicated Account Manager"]
        ),
        InvestmentPlan(
            name="Apex Plan",
            plan_type=InvestmentPlanType.APEX,
            min_amount=5000.0,
            max_amount=19999.0,
            duration_days=30,
            daily_interest=2.5,
            referral_bonus=10.0,
            features=["VIP Support", "Premium Analytics", "Personal Consultant"]
        ),
        InvestmentPlan(
            name="Partnership Plan",
            plan_type=InvestmentPlanType.PARTNERSHIP,
            min_amount=20000.0,
            max_amount=100000.0,
            duration_days=60,
            daily_interest=3.0,
            referral_bonus=15.0,
            features=["Executive Support", "Custom Solutions", "Weekly Consultations"]
        ),
        InvestmentPlan(
            name="Share Plan",
            plan_type=InvestmentPlanType.SHARE,
            min_amount=1000.0,
            max_amount=50000.0,
            duration_days=90,
            daily_interest=3.5,
            referral_bonus=20.0,
            features=["Profit Sharing", "Quarterly Dividends", "Company Shares"]
        )
    ]

    for plan in default_plans:
        try:
            manager.add_plan(plan)
        except ValueError:
            continue  # Plan already exists


# Example usage
if __name__ == "__main__":
    manager = InvestmentPlanManager()
    initialize_default_plans(manager)

    # List
