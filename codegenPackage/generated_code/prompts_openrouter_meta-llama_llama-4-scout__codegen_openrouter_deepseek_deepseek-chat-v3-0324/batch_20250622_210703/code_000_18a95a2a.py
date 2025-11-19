"""
Generated Code Metadata:
========================
Original URL: https://breakthroughstudio.in
Prompt: Write a Python script to create a membership subscription system for a suspension training studio like Breakthrough Studio, offering discounts for new subscribers.
Generated: DETERMINISTIC_18a95a2a6fb2a8df
Batch ID: 20250622_210703
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
from typing import Optional, List, Dict

class SubscriptionTier(Enum):
    """Enum representing different subscription tiers."""
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"

class SubscriptionStatus(Enum):
    """Enum representing subscription statuses."""
    ACTIVE = "Active"
    EXPIRED = "Expired"
    CANCELLED = "Cancelled"

class DiscountType(Enum):
    """Enum representing discount types."""
    PERCENTAGE = "Percentage"
    FIXED_AMOUNT = "Fixed Amount"

class Discount:
    """Class representing a discount offer."""
    def __init__(self, code: str, discount_type: DiscountType, value: float, 
                 valid_until: datetime.date, applicable_tiers: List[SubscriptionTier]):
        self.code = code
        self.discount_type = discount_type
        self.value = value
        self.valid_until = valid_until
        self.applicable_tiers = applicable_tiers

    def is_valid(self) -> bool:
        """Check if discount is still valid."""
        return datetime.date.today() <= self.valid_until

class Member:
    """Class representing a member."""
    def __init__(self, member_id: str, name: str, email: str, phone: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.subscriptions: List['Subscription'] = []

    def add_subscription(self, subscription: 'Subscription') -> None:
        """Add a subscription to the member."""
        self.subscriptions.append(subscription)

    def get_active_subscription(self) -> Optional['Subscription']:
        """Get the member's active subscription if any."""
        for sub in self.subscriptions:
            if sub.status == SubscriptionStatus.ACTIVE:
                return sub
        return None

class Subscription:
    """Class representing a subscription."""
    def __init__(self, subscription_id: str, member: Member, tier: SubscriptionTier, 
                 start_date: datetime.date, duration_months: int, 
                 monthly_price: float, discount: Optional[Discount] = None):
        self.subscription_id = subscription_id
        self.member = member
        self.tier = tier
        self.start_date = start_date
        self.duration_months = duration_months
        self.monthly_price = monthly_price
        self.discount = discount
        self.status = SubscriptionStatus.ACTIVE
        self.end_date = self._calculate_end_date()

    def _calculate_end_date(self) -> datetime.date:
        """Calculate the end date based on start date and duration."""
        year = self.start_date.year + (self.start_date.month + self.duration_months - 1) // 12
        month = (self.start_date.month + self.duration_months - 1) % 12 + 1
        day = min(self.start_date.day, [31, 29 if year % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
        return datetime.date(year, month, day)

    def calculate_total_price(self) -> float:
        """Calculate the total price with discount applied if applicable."""
        total = self.monthly_price * self.duration_months
        
        if self.discount and self.discount.is_valid() and self.tier in self.discount.applicable_tiers:
            if self.discount.discount_type == DiscountType.PERCENTAGE:
                total *= (1 - self.discount.value / 100)
            else:
                total -= self.discount.value
        
        return max(0, total)  # Ensure price doesn't go negative

    def cancel(self) -> None:
        """Cancel the subscription."""
        if self.status == SubscriptionStatus.ACTIVE:
            self.status = SubscriptionStatus.CANCELLED

    def check_status(self) -> None:
        """Check and update subscription status based on end date."""
        if self.status == SubscriptionStatus.ACTIVE and datetime.date.today() > self.end_date:
            self.status = SubscriptionStatus.EXPIRED

class SubscriptionSystem:
    """Class representing the subscription system."""
    def __init__(self):
        self.members: Dict[str, Member] = {}
        self.subscriptions: Dict[str, Subscription] = {}
        self.discounts: Dict[str, Discount] = {}
        self.tier_pricing = {
            SubscriptionTier.BASIC: 50.0,
            SubscriptionTier.STANDARD: 75.0,
            SubscriptionTier.PREMIUM: 100.0
        }

    def add_member(self, member: Member) -> None:
        """Add a member to the system."""
        if member.member_id in self.members:
            raise ValueError(f"Member with ID {member.member_id} already exists.")
        self.members[member.member_id] = member

    def create_subscription(self, member_id: str, tier: SubscriptionTier, 
                           duration_months: int, discount_code: Optional[str] = None) -> Subscription:
        """Create a new subscription for a member."""
        if member_id not in self.members:
            raise ValueError(f"Member with ID {member_id} not found.")
        
        member = self.members[member_id]
        
        # Check if member already has an active subscription
        if member.get_active_subscription():
            raise ValueError("Member already has an active subscription.")
        
        # Apply discount if valid
        discount = None
        if discount_code:
            if discount_code not in self.discounts:
                raise ValueError("Invalid discount code.")
            discount = self.discounts[discount_code]
            if not discount.is_valid():
                raise ValueError("Discount has expired.")
            if tier not in discount.applicable_tiers:
                raise ValueError("Discount not applicable to selected tier.")
        
        subscription_id = f"SUB-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
        subscription = Subscription(
            subscription_id=subscription_id,
            member=member,
            tier=tier,
            start_date=datetime.date.today(),
            duration_months=duration_months,
            monthly_price=self.tier_pricing[tier],
            discount=discount
        )
        
        member.add_subscription(subscription)
        self.subscriptions[subscription_id] = subscription
        return subscription

    def add_discount(self, discount: Discount) -> None:
        """Add a discount to the system."""
        if discount.code in self.discounts:
            raise ValueError(f"Discount with code {discount.code} already exists.")
        self.discounts[discount.code] = discount

    def get_member_subscriptions(self, member_id: str) -> List[Subscription]:
        """Get all subscriptions for a member."""
        if member_id not in self.members:
            raise ValueError(f"Member with ID {member_id} not found.")
        return self.members[member_id].subscriptions

    def update_subscription_statuses(self) -> None:
        """Update statuses of all subscriptions."""
        for subscription in self.subscriptions.values():
            subscription.check_status()

# Example usage
if __name__ == "__main__":
    system = SubscriptionSystem()
    
    # Add some discounts
    new_year_discount = Discount(
        code="NEWYEAR25",
        discount_type=DiscountType.PERCENTAGE,
        value=25.0,
        valid_until=datetime.date(2024, 2, 1),
        applicable_tiers=[SubscriptionTier.STANDARD, SubscriptionTier.PREMIUM]
    )
    system.add_discount(new_year_discount)
    
    # Create a member
    member1 = Member(
        member_id="M001",
        name="John Doe",
        email="john@example.com",
        phone="555-1234"
    )
    system.add_member(member1)
    
    # Create a subscription with discount
    try:
        subscription = system.create_subscription(
            member_id="M001",
            tier=SubscriptionTier.PREMIUM,
            duration_months=6,
            discount_code="NEWYEAR25"
        )
        print(f"Created subscription with total price: ${subscription.calculate_total_price():.2f}")
    except ValueError as e:
        print(f"Error creating subscription: {e}")
```
