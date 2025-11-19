"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fi-dapp-git-rk-featadd-new-badge-dumps-sad-etherfi.vercel.app
Prompt: Generate a function that updates user badges based on their participation in eETH promotions.
Generated: DETERMINISTIC_4dbf957416629ff5
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def update_user_badges(user_id, participation_data, promotion_badges):
    """
    Updates user badges based on their participation in eETH promotions.

    Args:
        user_id (int): Unique identifier for the user.
        participation_data (dict): A dictionary containing participation details for each promotion.
                                   Example: {"promo1": True, "promo2": False}
        promotion_badges (dict): A dictionary mapping promotion names to badge names.
                                 Example: {"promo1": "Gold Badge", "promo2": "Silver Badge"}

    Returns:
        dict: Updated list of user badges.
              Example: {"user_id": 123, "badges": ["Gold Badge"]}
    """
    try:
        # Validate input parameters
        if not isinstance(user_id, int):
            raise ValueError("user_id must be an integer.")
        if not isinstance(participation_data, dict):
            raise ValueError("participation_data must be a dictionary.")
        if not isinstance(promotion_badges, dict):
            raise ValueError("promotion_badges must be a dictionary.")

        # Initialize user badges list
        user_badges = {
            "user_id": user_id,
            "badges": []
        }

        # Update badges based on participation
        for promo, participated in participation_data.items():
            if participated and promo in promotion_badges:
                badge = promotion_badges[promo]
                user_badges["badges"].append(badge)

        # Log the successful update
        logging.info(f"Updated badges for user {user_id}: {user_badges['badges']}")

        return user_badges

    except ValueError as ve:
        logging.error(f"ValueError encountered: {ve}")
        raise  # Rethrow exception for upstream handling

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise  # Rethrow exception for upstream handling


# Example Usage:
if __name__ == "__main__":
    try:
        # Input data
        user_id = 123
        participation_data = {"promo1": True, "promo2": False, "promo3": True}
        promotion_badges = {"promo1": "Gold Badge", "promo2": "Silver Badge", "promo3": "Platinum Badge"}

        # Update badges
        updated_badges = update_user_badges(user_id, participation_data, promotion_badges)
        print(updated_badges)  # Expected output: {'user_id': 123, 'badges': ['Gold Badge', 'Platinum Badge']}

    except Exception as e:
        logging.error(f"Failed to update user badges: {e}")
```
