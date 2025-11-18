"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blogdotrabalhadordigital.com
Prompt: Write code to implement a promotional system where users can claim discounts or bonuses, as seen on Pelangi189, based on their gameplay activity.
Generated: DETERMINISTIC_172311bfd156b68f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class PromotionSystem:
    """
    A system to handle promotional discounts or bonuses based on user gameplay activity.
    """

    def __init__(self):
        """
        Initialize the PromotionSystem with user data and promotion rules.
        """
        self.users = {}  # Dictionary to store user data (e.g., {user_id: {"play_time": int, "claimed_promotions": list}})
        self.promotions = {}  # Dictionary to store promotion details (e.g., {promotion_id: {"condition": func, "reward": str}})
    
    def register_user(self, user_id):
        """
        Register a new user in the system.

        :param user_id: Unique identifier for the user.
        """
        if user_id in self.users:
            raise ValueError("User is already registered.")
        self.users[user_id] = {"play_time": 0, "claimed_promotions": []}

    def add_promotion(self, promotion_id, condition, reward):
        """
        Add a new promotion to the system.

        :param promotion_id: Unique identifier for the promotion.
        :param condition: A function that takes user data and returns True if the user qualifies for the promotion.
        :param reward: The reward for the promotion (e.g., discount code, bonus points).
        """
        if promotion_id in self.promotions:
            raise ValueError("Promotion already exists.")
        self.promotions[promotion_id] = {"condition": condition, "reward": reward}

    def log_play_time(self, user_id, minutes):
        """
        Log gameplay time for a user.

        :param user_id: Unique identifier for the user.
        :param minutes: Number of minutes played.
        """
        if user_id not in self.users:
            raise ValueError("User is not registered.")
        if minutes < 0:
            raise ValueError("Play time cannot be negative.")
        self.users[user_id]["play_time"] += minutes

    def claim_promotion(self, user_id, promotion_id):
        """
        Allow a user to claim a promotion if they meet the requirements.

        :param user_id: Unique identifier for the user.
        :param promotion_id: Unique identifier for the promotion.
        :return: Reward if claimed successfully, None otherwise.
        """
        if user_id not in self.users:
            raise ValueError("User is not registered.")
        if promotion_id not in self.promotions:
            raise ValueError("Promotion does not exist.")
        if promotion_id in self.users[user_id]["claimed_promotions"]:
            raise ValueError("Promotion has already been claimed.")
        
        promotion = self.promotions[promotion_id]
        user_data = self.users[user_id]

        # Check if the user meets the condition to claim the promotion
        if promotion["condition"](user_data):
            user_data["claimed_promotions"].append(promotion_id)
            return promotion["reward"]
        return None

    def get_user_promotions(self, user_id):
        """
        Get the list of promotions claimed by a user.

        :param user_id: Unique identifier for the user.
        :return: List of claimed promotions.
        """
        if user_id not in self.users:
            raise ValueError("User is not registered.")
        return self.users[user_id]["claimed_promotions"]

# Example usage:

# Initialize the promotion system
promotion_system = PromotionSystem()

# Register users
promotion_system.register_user("user1")
promotion_system.register_user("user2")

# Define promotions
promotion_system.add_promotion(
    "promo1",
    condition=lambda user_data: user_data["play_time"] >= 60,  # Users who play for 60 minutes or more qualify
    reward="10% discount"
)

promotion_system.add_promotion(
    "promo2",
    condition=lambda user_data: user_data["play_time"] >= 120,  # Users who play for 120 minutes or more qualify
    reward="20 bonus points"
)

# Log play time
promotion_system.log_play_time("user1", 30)
promotion_system.log_play_time("user1", 40)  # Total play time for user1 = 70 minutes
promotion_system.log_play_time("user2", 130)  # Total play time for user2 = 130 minutes

# Claim promotions
try:
    reward = promotion_system.claim_promotion("user1", "promo1")
    print(f"user1 claimed: {reward}")  # Output: user1 claimed: 10% discount
except ValueError as e:
    print(e)

try:
    reward = promotion_system.claim_promotion("user2", "promo2")
    print(f"user2 claimed: {reward}")  # Output: user2 claimed: 20 bonus points
except ValueError as e:
    print(e)

# Check claimed promotions
print("user1 claimed promotions:", promotion_system.get_user_promotions("user1"))  # Output: user1 claimed promotions: ['promo1']
print("user2 claimed promotions:", promotion_system.get_user_promotions("user2"))  # Output: user2 claimed promotions: ['promo2']
```
