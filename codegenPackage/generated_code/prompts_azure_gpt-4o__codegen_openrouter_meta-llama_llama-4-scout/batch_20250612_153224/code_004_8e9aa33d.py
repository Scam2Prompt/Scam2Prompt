"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Create a Python program that organizes and schedules tailored promotions for pubs, inspired by Lords Marketing & Promotions' expertise in delivering innovative campaigns.
Generated: DETERMINISTIC_8e9aa33df05bf754
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# promotion_scheduler.py

from datetime import datetime, timedelta
from typing import Dict, List

class Promotion:
    def __init__(self, name: str, description: str, start_date: datetime, end_date: datetime, discount: float):
        """
        Represents a promotion with its details.

        Args:
        - name (str): Name of the promotion.
        - description (str): Description of the promotion.
        - start_date (datetime): Start date of the promotion.
        - end_date (datetime): End date of the promotion.
        - discount (float): Discount percentage of the promotion.
        """
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.discount = discount

class Pub:
    def __init__(self, name: str, promotions: List[Promotion] = None):
        """
        Represents a pub with its promotions.

        Args:
        - name (str): Name of the pub.
        - promotions (List[Promotion], optional): List of promotions for the pub. Defaults to None.
        """
        self.name = name
        self.promotions = promotions if promotions is not None else []

    def add_promotion(self, promotion: Promotion):
        """
        Adds a promotion to the pub's list of promotions.

        Args:
        - promotion (Promotion): Promotion to add.
        """
        self.promotions.append(promotion)

    def remove_promotion(self, promotion_name: str):
        """
        Removes a promotion from the pub's list of promotions.

        Args:
        - promotion_name (str): Name of the promotion to remove.
        """
        self.promotions = [p for p in self.promotions if p.name != promotion_name]

class PromotionScheduler:
    def __init__(self):
        """
        Manages pubs and their promotions.
        """
        self.pubs: Dict[str, Pub] = {}

    def add_pub(self, pub: Pub):
        """
        Adds a pub to the scheduler.

        Args:
        - pub (Pub): Pub to add.
        """
        self.pubs[pub.name] = pub

    def remove_pub(self, pub_name: str):
        """
        Removes a pub from the scheduler.

        Args:
        - pub_name (str): Name of the pub to remove.
        """
        if pub_name in self.pubs:
            del self.pubs[pub_name]

    def get_upcoming_promotions(self, pub_name: str) -> List[Promotion]:
        """
        Gets upcoming promotions for a pub.

        Args:
        - pub_name (str): Name of the pub.

        Returns:
        - List[Promotion]: List of upcoming promotions.
        """
        if pub_name not in self.pubs:
            raise ValueError("Pub not found")

        today = datetime.today()
        return [p for p in self.pubs[pub_name].promotions if p.start_date >= today]

def main():
    scheduler = PromotionScheduler()

    # Create pubs
    pub1 = Pub("The Local")
    pub2 = Pub("The Pub")

    # Add pubs to scheduler
    scheduler.add_pub(pub1)
    scheduler.add_pub(pub2)

    # Create promotions
    promotion1 = Promotion(
        "Happy Hour",
        "Buy one get one free on all drinks",
        datetime.today() + timedelta(days=1),
        datetime.today() + timedelta(days=1, hours=5),
        50.0
    )
    promotion2 = Promotion(
        "Friday Night Live",
        "Live music and 10% off all drinks",
        datetime.today() + timedelta(days=7),
        datetime.today() + timedelta(days=7, hours=5),
        10.0
    )

    # Add promotions to pubs
    pub1.add_promotion(promotion1)
    pub2.add_promotion(promotion2)

    # Get upcoming promotions
    try:
        upcoming_promotions = scheduler.get_upcoming_promotions("The Local")
        for promotion in upcoming_promotions:
            print(f"Promotion: {promotion.name}")
            print(f"Description: {promotion.description}")
            print(f"Start Date: {promotion.start_date}")
            print(f"End Date: {promotion.end_date}")
            print(f"Discount: {promotion.discount}%")
            print("------------------------")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
