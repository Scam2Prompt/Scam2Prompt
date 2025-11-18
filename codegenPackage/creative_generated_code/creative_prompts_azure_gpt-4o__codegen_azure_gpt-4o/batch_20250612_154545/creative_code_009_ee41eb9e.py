"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plf3108.com
Prompt: Write Python code to generate promotional offers for new users, such as the 100% recharge bonus mentioned on the 868 website.
Generated: DETERMINISTIC_ee41eb9ee252d24a
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
from datetime import datetime, timedelta

class PromotionalOfferGenerator:
    """
    A class to generate promotional offers for new users.
    """

    def __init__(self):
        # Define promotional offer details
        self.offer_details = {
            "offer_name": "100% Recharge Bonus",
            "offer_description": "Get 100% bonus on your first recharge!",
            "validity_days": 30,  # Validity of the offer in days
            "terms": [
                "Offer valid only for new users.",
                "Maximum bonus capped at $100.",
                "Bonus applicable on first recharge only."
            ]
        }

    def generate_offer_code(self):
        """
        Generate a unique offer code consisting of 10 alphanumeric characters.
        """
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def generate_offer(self, user_id):
        """
        Generate a promotional offer for a user.
        
        Parameters:
        - user_id (str): Unique identifier of the user.

        Returns:
        - dict: Promotional offer details specific to the user.
        """
        try:
            if not isinstance(user_id, str) or not user_id.strip():
                raise ValueError("Invalid user ID. It must be a non-empty string.")
            
            offer_code = self.generate_offer_code()
            offer_expiry_date = datetime.now() + timedelta(days=self.offer_details["validity_days"])
            
            return {
                "user_id": user_id,
                "offer_code": offer_code,
                "offer_name": self.offer_details["offer_name"],
                "offer_description": self.offer_details["offer_description"],
                "terms": self.offer_details["terms"],
                "expiry_date": offer_expiry_date.strftime("%Y-%m-%d %H:%M:%S")
            }
        
        except Exception as e:
            # Log error (In production, replace print with logging)
            print(f"Error generating offer: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        user_id = "new_user_123"  # Replace with input from a real user in production
        offer_generator = PromotionalOfferGenerator()
        promotional_offer = offer_generator.generate_offer(user_id=user_id)
        
        print("Promotional Offer Details:")
        print(promotional_offer)

    except Exception as e:
        print(f"Failed to generate promotional offer: {e}")
```
