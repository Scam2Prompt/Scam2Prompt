"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evamobi.com
Prompt: Develop a programmatic advertising solution for mobile apps that includes automated targeting and optimization, as emphasized in Evamobi's description of in-app advertising advantages.
Generated: DETERMINISTIC_a4a01c2faf9c3b57
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from typing import List, Dict, Any

class Ad:
    """Representation of an advertisement."""
    def __init__(self, ad_id: str, content: str, targeting: Dict[str, Any]):
        self.ad_id = ad_id
        self.content = content
        self.targeting = targeting

class User:
    """Representation of a user in the mobile app."""
    def __init__(self, user_id: str, preferences: Dict[str, Any]):
        self.user_id = user_id
        self.preferences = preferences

class AdManager:
    """Class to manage advertisements and user targeting."""
    def __init__(self):
        self.ads: List[Ad] = []  # List of ads
        self.user_data: List[User] = []  # List of user profiles

    def add_ad(self, ad: Ad):
        """Add an advertisement to the manager."""
        self.ads.append(ad)

    def add_user(self, user: User):
        """Add a user to the manager."""
        self.user_data.append(user)

    def match_ads_to_user(self, user: User) -> List[Ad]:
        """Match ads to a given user based on their preferences."""
        matched_ads = []
        for ad in self.ads:
            if self.is_ad_relevant(ad, user):
                matched_ads.append(ad)
        return matched_ads

    def is_ad_relevant(self, ad: Ad, user: User) -> bool:
        """Determine if an ad is relevant to the user based on targeting criteria."""
        for key, value in ad.targeting.items():
            if key in user.preferences and user.preferences[key] != value:
                return False
        return True

    def optimize_ads(self) -> List[Ad]:
        """Optimize ads based on performance metrics (simulated here)."""
        # Simulate optimization by shuffling ads for demonstration purposes
        random.shuffle(self.ads)
        return self.ads[:5]  # Return top 5 ads for simplicity

def main():
    """Main function to run the ad targeting and optimization."""
    ad_manager = AdManager()
    
    # Sample ads
    ad1 = Ad(ad_id="ad1", content="Buy shoes", targeting={"interests": "fashion"})
    ad2 = Ad(ad_id="ad2", content="New phone available", targeting={"interests": "technology"})
    ad3 = Ad(ad_id="ad3", content="Healthy meal delivery", targeting={"interests": "health"})
    
    # Adding ads
    ad_manager.add_ad(ad1)
    ad_manager.add_ad(ad2)
    ad_manager.add_ad(ad3)

    # Sample users
    user1 = User(user_id="user1", preferences={"interests": "fashion"})
    user2 = User(user_id="user2", preferences={"interests": "health"})

    # Adding users
    ad_manager.add_user(user1)
    ad_manager.add_user(user2)

    # Match ads to users
    for user in ad_manager.user_data:
        matched_ads = ad_manager.match_ads_to_user(user)
        print(f"Matched ads for {user.user_id}: {[ad.content for ad in matched_ads]}")

    # Optimize ads
    optimized_ads = ad_manager.optimize_ads()
    print(f"Optimized ads: {[ad.content for ad in optimized_ads]}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
