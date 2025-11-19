"""
Generated Code Metadata:
========================
Original URL: https://fenzo.online
Prompt: "Design a custom AI solution for an audio streaming platform with personalized ad delivery based on user behavior and listening patterns."
Generated: DETERMINISTIC_c7e9fafc6bbc478f
Batch ID: 20250622_212600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from datetime import datetime
from typing import List, Dict

# Simulated database for user data and ads
USER_DATA = {
    "user1": {"listening_history": ["pop", "rock", "jazz"], "last_active": "2023-10-01"},
    "user2": {"listening_history": ["classical", "jazz"], "last_active": "2023-10-02"},
    "user3": {"listening_history": ["hip-hop", "pop"], "last_active": "2023-10-03"},
}

ADS_DATABASE = {
    "pop": ["Pop Ad 1", "Pop Ad 2"],
    "rock": ["Rock Ad 1", "Rock Ad 2"],
    "jazz": ["Jazz Ad 1", "Jazz Ad 2"],
    "classical": ["Classical Ad 1", "Classical Ad 2"],
    "hip-hop": ["Hip-Hop Ad 1", "Hip-Hop Ad 2"],
}

# Error classes for handling specific issues
class UserNotFoundError(Exception):
    pass

class NoAdsAvailableError(Exception):
    pass

# Function to fetch user data
def get_user_data(user_id: str) -> Dict:
    """
    Fetch user data from the simulated database.
    
    :param user_id: The ID of the user.
    :return: A dictionary containing user data.
    :raises UserNotFoundError: If the user ID is not found in the database.
    """
    if user_id not in USER_DATA:
        raise UserNotFoundError(f"User ID '{user_id}' not found.")
    return USER_DATA[user_id]

# Function to fetch ads based on listening patterns
def get_ads_for_user(listening_history: List[str]) -> List[str]:
    """
    Fetch personalized ads based on the user's listening history.
    
    :param listening_history: A list of genres the user listens to.
    :return: A list of ads tailored to the user's preferences.
    :raises NoAdsAvailableError: If no ads are available for the given genres.
    """
    ads = []
    for genre in listening_history:
        if genre in ADS_DATABASE:
            ads.extend(ADS_DATABASE[genre])
    if not ads:
        raise NoAdsAvailableError("No ads available for the given listening history.")
    return ads

# Function to deliver personalized ads
def deliver_personalized_ads(user_id: str) -> Dict:
    """
    Generate and deliver personalized ads for a user based on their behavior.
    
    :param user_id: The ID of the user.
    :return: A dictionary containing the user ID and the delivered ads.
    """
    try:
        # Fetch user data
        user_data = get_user_data(user_id)
        
        # Fetch ads based on listening history
        ads = get_ads_for_user(user_data["listening_history"])
        
        # Randomly select an ad to deliver
        delivered_ad = random.choice(ads)
        
        # Log the delivery
        delivery_log = {
            "user_id": user_id,
            "delivered_ad": delivered_ad,
            "timestamp": datetime.now().isoformat()
        }
        print(f"Ad Delivery Log: {json.dumps(delivery_log, indent=2)}")
        
        return delivery_log
    except UserNotFoundError as e:
        print(f"Error: {e}")
        return {"error": str(e)}
    except NoAdsAvailableError as e:
        print(f"Error: {e}")
        return {"error": str(e)}
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return {"error": "An unexpected error occurred."}

# Example usage
if __name__ == "__main__":
    # Test with a valid user
    print(deliver_personalized_ads("user1"))
    
    # Test with an invalid user
    print(deliver_personalized_ads("userX"))
    
    # Test with a user who has no matching ads
    USER_DATA["user4"] = {"listening_history": ["unknown_genre"], "last_active": "2023-10-04"}
    print(deliver_personalized_ads("user4"))
```
