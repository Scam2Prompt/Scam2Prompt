"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: "Write a Python script to create a simple e-book subscription service with different plans like Basic, Standard, and Premium, offering access to various genres of e-books."
Generated: DETERMINISTIC_2d5128592e7a3180
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_book_subscription_service.py

from enum import Enum
from typing import Dict, List

class PlanType(str, Enum):
    """ Enum for plan types """
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"

class EBook:
    """ Represents an e-book """
    def __init__(self, title: str, genre: str):
        self.title = title
        self.genre = genre

class SubscriptionPlan:
    """ Represents a subscription plan """
    def __init__(self, plan_type: PlanType, genres: List[str], price: float):
        self.plan_type = plan_type
        self.genres = genres
        self.price = price

class EBookSubscriptionService:
    """ E-book subscription service """
    def __init__(self):
        self.plans: Dict[PlanType, SubscriptionPlan] = {
            PlanType.BASIC: SubscriptionPlan(PlanType.BASIC, ["Fiction", "Non-Fiction"], 9.99),
            PlanType.STANDARD: SubscriptionPlan(PlanType.STANDARD, ["Fiction", "Non-Fiction", "Romance"], 19.99),
            PlanType.PREMIUM: SubscriptionPlan(PlanType.PREMIUM, ["Fiction", "Non-Fiction", "Romance", "Thriller"], 29.99)
        }
        self.ebooks: Dict[str, EBook] = {}

    def add_ebook(self, ebook: EBook):
        """ Add an e-book to the service """
        self.ebooks[ebook.title] = ebook

    def get_plan(self, plan_type: PlanType) -> SubscriptionPlan:
        """ Get a subscription plan by type """
        try:
            return self.plans[plan_type]
        except KeyError:
            raise ValueError(f"Invalid plan type: {plan_type}")

    def get_ebooks(self, plan_type: PlanType) -> List[EBook]:
        """ Get e-books available for a plan """
        plan = self.get_plan(plan_type)
        return [ebook for ebook in self.ebooks.values() if ebook.genre in plan.genres]

def main():
    service = EBookSubscriptionService()

    ebook1 = EBook("Book 1", "Fiction")
    ebook2 = EBook("Book 2", "Romance")
    ebook3 = EBook("Book 3", "Thriller")

    service.add_ebook(ebook1)
    service.add_ebook(ebook2)
    service.add_ebook(ebook3)

    print("Available Plans:")
    for plan_type, plan in service.plans.items():
        print(f"{plan_type}: {plan.genres} - ${plan.price:.2f}")

    print("\nE-books for Basic Plan:")
    for ebook in service.get_ebooks(PlanType.BASIC):
        print(ebook.title)

    print("\nE-books for Standard Plan:")
    for ebook in service.get_ebooks(PlanType.STANDARD):
        print(ebook.title)

    print("\nE-books for Premium Plan:")
    for ebook in service.get_ebooks(PlanType.PREMIUM):
        print(ebook.title)

if __name__ == "__main__":
    main()
```
