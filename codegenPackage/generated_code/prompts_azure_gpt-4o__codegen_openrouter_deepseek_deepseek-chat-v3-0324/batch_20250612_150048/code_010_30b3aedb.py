"""
Generated Code Metadata:
========================
Original URL: https://ifundsoption.com
Prompt: Generate code for managing investment plans (e.g., Silver, Gold, Premium accounts) with automated profit calculations, inspired by iFundsOption's account structure.
Generated: DETERMINISTIC_30b3aedbddd762d5
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 6

class InvestmentPlanType(Enum):
    """Enum representing different investment plan types."""
    SILVER = "Silver"
    GOLD = "Gold"
    PREMIUM = "Premium"

class InvestmentPlan:
    """Class representing an investment plan with its properties."""
    
    def __init__(
        self,
        plan_type: InvestmentPlanType,
        min_investment: Decimal,
        max_investment: Decimal,
        daily_profit_percentage: Decimal,
        duration_days: int,
        referral_bonus_percentage: Decimal
    ):
        self.plan_type = plan_type
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_profit_percentage = daily_profit_percentage
        self.duration_days = duration_days
        self.referral_bonus_percentage = referral_bonus_percentage

class InvestmentAccount:
    """Class representing a user's investment account."""
    
    def __init__(
        self,
        user_id: str,
        plan_type: InvestmentPlanType,
        investment_amount: Decimal,
        start_date: datetime.date,
        referral_code: Optional[str] = None
    ):
        self.user_id = user_id
        self.plan_type = plan_type
        self.investment_amount = investment_amount
        self.start_date = start_date
        self.referral_code = referral_code
        self.is_active = True
        self._validate_investment()

    def _validate_investment(self) -> None:
        """Validate investment amount against plan limits."""
        plan = InvestmentPlanManager.get_plan(self.plan_type)
        if not plan:
            raise ValueError(f"Invalid plan type: {self.plan_type}")
        
        if not (plan.min_investment <= self.investment_amount <= plan.max_investment):
            raise ValueError(
                f"Investment amount {self.investment_amount} is outside "
                f"the allowed range for {self.plan_type.value} plan "
                f"({plan.min_investment}-{plan.max_investment})"
            )

    def calculate_profit(self, as_of_date: datetime.date = None) -> Decimal:
        """
        Calculate profit up to the given date or today if not specified.
        
        Args:
            as_of_date: Date to calculate profit up to. Defaults to today.
            
        Returns:
            Decimal: Calculated profit amount
        """
        if not self.is_active:
            return Decimal(0)
            
        as_of_date = as_of_date or datetime.date.today()
        plan = InvestmentPlanManager.get_plan(self.plan_type)
        
        if not plan:
            raise ValueError(f"Plan {self.plan_type.value} not found")
            
        days_invested = (as_of_date - self.start_date).days
        days_invested = min(days_invested, plan.duration_days)
        
        if days_invested <= 0:
            return Decimal(0)
            
        daily_profit = self.investment_amount * (plan.daily_profit_percentage / Decimal(100))
        total_profit = daily_profit * Decimal(days_invested)
        return total_profit.quantize(Decimal('0.01'))

    def calculate_referral_bonus(self) -> Decimal:
        """Calculate referral bonus if referral code was provided."""
        if not self.referral_code:
            return Decimal(0)
            
        plan = InvestmentPlanManager.get_plan(self.plan_type)
        if not plan:
            return Decimal(0)
            
        bonus = self.investment_amount * (plan.referral_bonus_percentage / Decimal(100))
        return bonus.quantize(Decimal('0.01'))

    def close_account(self) -> None:
        """Mark account as inactive."""
        self.is_active = False

class InvestmentPlanManager:
    """Singleton class managing all investment plans."""
    
    _instance = None
    _plans: Dict[InvestmentPlanType, InvestmentPlan] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._initialize_plans()
        return cls._instance
    
    @classmethod
    def _initialize_plans(cls) -> None:
        """Initialize the available investment plans."""
        cls._plans = {
            InvestmentPlanType.SILVER: InvestmentPlan(
                plan_type=InvestmentPlanType.SILVER,
                min_investment=Decimal('100.00'),
                max_investment=Decimal('999.99'),
                daily_profit_percentage=Decimal('1.5'),
                duration_days=30,
                referral_bonus_percentage=Decimal('5.0')
            ),
            InvestmentPlanType.GOLD: InvestmentPlan(
                plan_type=InvestmentPlanType.GOLD,
                min_investment=Decimal('1000.00'),
                max_investment=Decimal('4999.99'),
                daily_profit_percentage=Decimal('2.0'),
                duration_days=45,
                referral_bonus_percentage=Decimal('7.5')
            ),
            InvestmentPlanType.PREMIUM: InvestmentPlan(
                plan_type=InvestmentPlanType.PREMIUM,
                min_investment=Decimal('5000.00'),
                max_investment=Decimal('50000.00'),
                daily_profit_percentage=Decimal('2.5'),
                duration_days=60,
                referral_bonus_percentage=Decimal('10.0')
            )
        }
    
    @classmethod
    def get_plan(cls, plan_type: InvestmentPlanType) -> Optional[InvestmentPlan]:
        """Get investment plan by type."""
        return cls._plans.get(plan_type)
    
    @classmethod
    def get_all_plans(cls) -> List[InvestmentPlan]:
        """Get all available investment plans."""
        return list(cls._plans.values())
    
    @classmethod
    def get_plan_details(cls, plan_type: InvestmentPlanType) -> Dict:
        """Get plan details as a dictionary."""
        plan = cls.get_plan(plan_type)
        if not plan:
            return {}
            
        return {
            "plan_type": plan.plan_type.value,
            "min_investment": float(plan.min_investment),
            "max_investment": float(plan.max_investment),
            "daily_profit_percentage": float(plan.daily_profit_percentage),
            "duration_days": plan.duration_days,
            "referral_bonus_percentage": float(plan.referral_bonus_percentage)
        }

class InvestmentTracker:
    """Class to track and manage multiple investment accounts."""
    
    def __init__(self):
        self.accounts: Dict[str, InvestmentAccount] = {}
    
    def add_account(self, account: InvestmentAccount) -> None:
        """Add a new investment account."""
        if account.user_id in self.accounts:
            raise ValueError(f"Account already exists for user {account.user_id}")
        self.accounts[account.user_id] = account
    
    def get_account(self, user_id: str) -> Optional[InvestmentAccount]:
        """Get investment account by user ID."""
        return self.accounts.get(user_id)
    
    def calculate_total_profit(self, user_id: str, as_of_date: datetime.date = None) -> Decimal:
        """Calculate total profit for a user's account."""
        account = self.get_account(user_id)
        if not account:
            raise ValueError(f"No account found for user {user_id}")
        return account.calculate_profit(as_of_date)
    
    def close_account(self, user_id: str) -> None:
        """Close a user's investment account."""
        account = self.get_account(user_id)
        if not account:
            raise ValueError(f"No account found for user {user_id}")
        account.close_account()
    
    def get_active_accounts(self) -> List[InvestmentAccount]:
        """Get all active investment accounts."""
        return [account for account in self.accounts.values() if account.is_active]
    
    def get_accounts_by_plan(self, plan_type: InvestmentPlanType) -> List[InvestmentAccount]:
        """Get all accounts of a specific plan type."""
        return [account for account in self.accounts.values() if account.plan_type == plan_type]

# Example usage
if __name__ == "__main__":
    # Initialize plan manager
    plan_manager = InvestmentPlanManager()
    
    # Create a tracker
    tracker = InvestmentTracker()
    
    # Example accounts
    try:
        account1 = InvestmentAccount(
            user_id="user123",
            plan_type=InvestmentPlanType.SILVER,
            investment_amount=Decimal('500.00'),
            start_date=datetime.date.today() - datetime.timedelta(days=10),
            referral_code="REF123"
        )
        tracker.add_account(account1)
        
        account2 = InvestmentAccount(
            user_id="user456",
            plan_type=InvestmentPlanType.GOLD,
            investment_amount=Decimal('2000.00'),
            start_date=datetime.date.today() - datetime.timedelta(days=20)
        )
        tracker.add_account(account2
