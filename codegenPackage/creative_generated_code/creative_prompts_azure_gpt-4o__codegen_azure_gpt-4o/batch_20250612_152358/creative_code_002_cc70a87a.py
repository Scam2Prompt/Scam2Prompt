"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://startupsadvisory.com
Prompt: Generate Python code to implement a restaurant loyalty program and reward system, incorporating gift cards and feedback forms as detailed on StartUp Advisory.
Generated: DETERMINISTIC_cc70a87a8e266427
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta

# Constants for the loyalty program
POINTS_PER_DOLLAR = 10
REWARD_THRESHOLD = 1000  # Points needed to redeem rewards
GIFT_CARD_EXPIRATION_DAYS = 365  # Validity of gift cards in days

# In-memory storage for user data
users = {}

# Exception Classes for Error Handling
class UserNotFoundError(Exception):
    pass

class InsufficientPointsError(Exception):
    pass

class GiftCardExpiredError(Exception):
    pass

# User Class
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.points = 0
        self.feedback = []
        self.gift_cards = []
    
    def add_points(self, amount_spent):
        """Add points based on amount spent."""
        self.points += amount_spent * POINTS_PER_DOLLAR
    
    def redeem_points(self, points):
        """Redeem points for rewards, with error handling if points are insufficient."""
        if points > self.points:
            raise InsufficientPointsError("Insufficient points to redeem rewards.")
        self.points -= points
        return f"Successfully redeemed {points} points."

    def add_feedback(self, feedback_text):
        """Store feedback in the user's profile."""
        feedback_entry = {
            "feedback_id": str(uuid.uuid4()),
            "text": feedback_text,
            "timestamp": datetime.now()
        }
        self.feedback.append(feedback_entry)
        return f"Feedback added successfully. Feedback ID: {feedback_entry['feedback_id']}"
    
    def issue_gift_card(self, amount):
        """Issue a gift card to the user."""
        gift_card = {
            "card_id": str(uuid.uuid4()),
            "amount": amount,
            "issued_date": datetime.now(),
            "expiration_date": datetime.now() + timedelta(days=GIFT_CARD_EXPIRATION_DAYS)
        }
        self.gift_cards.append(gift_card)
        return f"Gift card issued successfully. Card ID: {gift_card['card_id']}"

    def redeem_gift_card(self, card_id):
        """Redeem a gift card, checking for expiration."""
        for card in self.gift_cards:
            if card["card_id"] == card_id:
                if datetime.now() > card["expiration_date"]:
                    raise GiftCardExpiredError("Gift card has expired.")
                self.gift_cards.remove(card)
                return f"Successfully redeemed gift card worth ${card['amount']}."
        raise UserNotFoundError("Gift card not found.")

# Functions to manage users and program operations
def create_user(name):
    """Create a new user."""
    user_id = str(uuid.uuid4())
    users[user_id] = User(user_id, name)
    return f"User created successfully. User ID: {user_id}"

def get_user(user_id):
    """Retrieve a user by ID."""
    if user_id not in users:
        raise UserNotFoundError("User not found.")
    return users[user_id]

# Example Usage (this would normally be in the UI or API layer)
if __name__ == "__main__":
    try:
        # Create a user
        user_id = create_user("John Doe").split(": ")[1]
        user = get_user(user_id)

        # Add points for spending $50
        user.add_points(50)
        print(f"User points: {user.points}")

        # Redeem 500 points
        print(user.redeem_points(500))

        # Add feedback
        print(user.add_feedback("Great food and service!"))

        # Issue a $25 gift card
        print(user.issue_gift_card(25))

        # Redeem the gift card (assuming we know the card ID)
        card_id = user.gift_cards[0]["card_id"]
        print(user.redeem_gift_card(card_id))

    except (UserNotFoundError, InsufficientPointsError, GiftCardExpiredError) as e:
        print(f"Error: {e}")
```
