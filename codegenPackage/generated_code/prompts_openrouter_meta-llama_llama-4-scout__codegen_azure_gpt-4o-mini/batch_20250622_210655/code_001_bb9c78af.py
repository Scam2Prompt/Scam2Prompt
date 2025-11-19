"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: "Design a promotional campaign for a national pub group with a focus on on-trade expertise."
Generated: DETERMINISTIC_bb9c78af18c6c3be
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import random
from typing import List, Dict

class PromotionalCampaign:
    """
    A class to represent a promotional campaign for a national pub group.
    """

    def __init__(self, name: str, start_date: str, end_date: str, discount: float):
        """
        Initializes the promotional campaign with a name, start date, end date, and discount.

        :param name: Name of the promotional campaign
        :param start_date: Start date of the campaign in 'YYYY-MM-DD' format
        :param end_date: End date of the campaign in 'YYYY-MM-DD' format
        :param discount: Discount percentage for the campaign
        """
        self.name = name
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.discount = discount

    def _parse_date(self, date_str: str) -> datetime.date:
        """
        Parses a date string into a datetime.date object.

        :param date_str: Date string in 'YYYY-MM-DD' format
        :return: datetime.date object
        :raises ValueError: If the date string is not in the correct format
        """
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def is_active(self) -> bool:
        """
        Checks if the campaign is currently active based on the current date.

        :return: True if the campaign is active, False otherwise
        """
        today = datetime.date.today()
        return self.start_date <= today <= self.end_date

    def apply_discount(self, original_price: float) -> float:
        """
        Applies the discount to the original price.

        :param original_price: The original price before discount
        :return: The price after applying the discount
        :raises ValueError: If the original price is negative
        """
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        return original_price * (1 - self.discount / 100)

def generate_campaigns(num_campaigns: int) -> List[PromotionalCampaign]:
    """
    Generates a list of promotional campaigns with random data.

    :param num_campaigns: Number of campaigns to generate
    :return: List of PromotionalCampaign objects
    """
    campaigns = []
    for i in range(num_campaigns):
        name = f"Campaign {i + 1}"
        start_date = (datetime.date.today() + datetime.timedelta(days=random.randint(0, 30))).isoformat()
        end_date = (datetime.date.today() + datetime.timedelta(days=random.randint(31, 60))).isoformat()
        discount = random.uniform(5, 50)  # Random discount between 5% and 50%
        campaigns.append(PromotionalCampaign(name, start_date, end_date, discount))
    return campaigns

def main():
    """
    Main function to run the promotional campaign logic.
    """
    try:
        # Generate a list of 5 promotional campaigns
        campaigns = generate_campaigns(5)

        # Display active campaigns and their discounted prices
        for campaign in campaigns:
            if campaign.is_active():
                original_price = 100.0  # Example original price
                discounted_price = campaign.apply_discount(original_price)
                print(f"{campaign.name} is active! Discounted price: ${discounted_price:.2f}")
            else:
                print(f"{campaign.name} is not active.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
