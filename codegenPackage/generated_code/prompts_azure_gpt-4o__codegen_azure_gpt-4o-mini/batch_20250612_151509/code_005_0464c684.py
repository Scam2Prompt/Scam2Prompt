"""
Generated Code Metadata:
========================
Original URL: https://fiberproximus.be
Prompt: Develop a function to compare fiber internet deals based on user preferences, including packs with TV, mobile, and internet, as highlighted by Fiberdeals.
Generated: DETERMINISTIC_0464c684e9b67d47
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Any

class InternetDeal:
    def __init__(self, name: str, price: float, internet_speed: int, has_tv: bool, has_mobile: bool):
        """
        Initialize an InternetDeal instance.

        :param name: Name of the internet deal
        :param price: Monthly price of the deal
        :param internet_speed: Internet speed in Mbps
        :param has_tv: Boolean indicating if the deal includes TV
        :param has_mobile: Boolean indicating if the deal includes mobile
        """
        self.name = name
        self.price = price
        self.internet_speed = internet_speed
        self.has_tv = has_tv
        self.has_mobile = has_mobile

    def __repr__(self):
        return f"{self.name}: ${self.price}/mo, {self.internet_speed} Mbps, TV: {self.has_tv}, Mobile: {self.has_mobile}"

def compare_internet_deals(deals: List[InternetDeal], preferences: Dict[str, Any]) -> List[InternetDeal]:
    """
    Compare internet deals based on user preferences.

    :param deals: List of InternetDeal instances to compare
    :param preferences: Dictionary containing user preferences
    :return: List of InternetDeal instances that match user preferences
    """
    try:
        filtered_deals = []

        for deal in deals:
            # Check if the deal matches user preferences
            if (deal.price <= preferences.get('max_price', float('inf')) and
                deal.internet_speed >= preferences.get('min_speed', 0) and
                (preferences.get('needs_tv', False) == deal.has_tv) and
                (preferences.get('needs_mobile', False) == deal.has_mobile)):
                filtered_deals.append(deal)

        # Sort the filtered deals by price (ascending)
        filtered_deals.sort(key=lambda x: x.price)

        return filtered_deals

    except Exception as e:
        print(f"An error occurred while comparing deals: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Sample internet deals
    deals = [
        InternetDeal("Deal A", 49.99, 100, True, False),
        InternetDeal("Deal B", 39.99, 50, False, True),
        InternetDeal("Deal C", 59.99, 200, True, True),
        InternetDeal("Deal D", 29.99, 30, False, False),
    ]

    # User preferences
    user_preferences = {
        'max_price': 50,
        'min_speed': 50,
        'needs_tv': True,
        'needs_mobile': False
    }

    # Compare deals based on user preferences
    matching_deals = compare_internet_deals(deals, user_preferences)

    # Output the matching deals
    print("Matching Internet Deals:")
    for deal in matching_deals:
        print(deal)
```
