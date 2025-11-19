"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evamobi.com
Prompt: How can I leverage laser-focused targeting in my in-app advertising to reach specific demographics effectively?
Generated: DETERMINISTIC_1fab2d7877b5b1b1
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class User:
    """Class representing a user in the application."""
    
    def __init__(self, user_id: int, demographics: Dict[str, str]):
        """
        Initializes a User instance.

        Args:
            user_id (int): Unique identifier for the user.
            demographics (Dict[str, str]): A dictionary containing demographic information.
        """
        self.user_id = user_id
        self.demographics = demographics


class Ad:
    """Class representing an advertisement."""
    
    def __init__(self, ad_id: int, target_demographics: List[str]):
        """
        Initializes an Ad instance.

        Args:
            ad_id (int): Unique identifier for the advertisement.
            target_demographics (List[str]): List of demographics the ad targets.
        """
        self.ad_id = ad_id
        self.target_demographics = target_demographics


class AdManager:
    """Class to manage in-app advertisements and targeting."""

    def __init__(self):
        """
        Initializes the AdManager with an empty list of ads.
        """
        self.ads = []

    def add_ad(self, ad: Ad):
        """
        Adds a new advertisement to the manager.

        Args:
            ad (Ad): The advertisement to be added.
        """
        self.ads.append(ad)

    def get_targeted_ads(self, user: User) -> List[Ad]:
        """
        Retrieves a list of ads targeted to a specific user based on their demographics.

        Args:
            user (User): The user for whom to retrieve targeted ads.

        Returns:
            List[Ad]: A list of ads that match the user's demographics.
        """
        targeted_ads = []
        for ad in self.ads:
            if any(demographic in user.demographics.values() for demographic in ad.target_demographics):
                targeted_ads.append(ad)
        return targeted_ads


def main():
    """
    Main function to demonstrate the functionality of targeted advertising.
    """
    # Create some users with demographics
    users = [
        User(user_id=1, demographics={'age': '25-34', 'gender': 'female'}),
        User(user_id=2, demographics={'age': '18-24', 'gender': 'male'}),
        User(user_id=3, demographics={'age': '35-44', 'gender': 'female'}),
    ]
    
    # Create some advertisements with target demographics
    ads = [
        Ad(ad_id=1, target_demographics=['female']),
        Ad(ad_id=2, target_demographics=['male', '18-24']),
        Ad(ad_id=3, target_demographics=['35-44']),
    ]
    
    # Instantiate the AdManager and add ads to it
    ad_manager = AdManager()
    for ad in ads:
        ad_manager.add_ad(ad)

    # Demonstrate targeted ad retrieval for each user
    for user in users:
        targeted_ads = ad_manager.get_targeted_ads(user)
        print(f"User {user.user_id} targeted ads: {[ad.ad_id for ad in targeted_ads]}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
