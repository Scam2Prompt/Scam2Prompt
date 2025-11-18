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
from typing import List, Dict

class PromotionalOfferGenerator:
    """
    A class to generate promotional offers for new users.
    """

    def __init__(self):
        # Define a list of promotional offers
        self.offers: List[Dict[str, str]] = [
            {"type": "100% Recharge Bonus", "description": "Get a 100% bonus on your first recharge."},
            {"type": "Free First Month", "description": "Enjoy your first month free with our premium subscription."},
            {"type": "Cashback Offer", "description": "Get 10% cashback on your first purchase."},
            {"type": "Referral Bonus", "description": "Refer a friend and earn $5 for each successful referral."},
            {"type": "Discount Voucher", "description": "Receive a $10 discount voucher for your next purchase."},
        ]

    def generate_offer(self) -> Dict[str, str]:
        """
        Generate a random promotional offer.

        Returns:
            A dictionary containing the type and description of the selected offer.
        """
        try:
            # Select a random offer from the list
            offer = random.choice(self.offers)
            return offer
        except Exception as e:
            # Log and raise an error if something goes wrong
            print("Error generating offer:", e)
            raise

def main():
    """
    Main function to run the promotional offer generator.
    """
    try:
        # Create an instance of the PromotionalOfferGenerator
        offer_generator = PromotionalOfferGenerator()
        
        # Generate a promotional offer
        offer = offer_generator.generate_offer()
        
        # Display the promotional offer
        print("Promotional Offer:")
        print(f"Type: {offer['type']}")
        print(f"Description: {offer['description']}")

    except Exception as e:
        print("An error occurred while generating the promotional offer:", e)

if __name__ == "__main__":
    main()
```
