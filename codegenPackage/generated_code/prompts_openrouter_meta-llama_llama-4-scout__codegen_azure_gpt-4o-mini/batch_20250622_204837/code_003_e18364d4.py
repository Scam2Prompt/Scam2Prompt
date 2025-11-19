"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-io.web.app
Prompt: "Design a system to enable gas stations to customize their loyalty offerings for customers using CRUDO tokens for payments, including discounts, freebies, or exclusive deals."
Generated: DETERMINISTIC_e18364d4849b6742
Batch ID: 20250622_204837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_system.py

from typing import List, Dict, Optional

class LoyaltyProgram:
    """
    A class to represent a loyalty program for gas stations.
    It allows customization of loyalty offerings using CRUDO tokens.
    """

    def __init__(self):
        self.offers: Dict[str, Dict[str, float]] = {}  # Store offers with their details

    def add_offer(self, offer_name: str, discount: float, tokens_required: float) -> None:
        """
        Add a new loyalty offer to the program.

        :param offer_name: Name of the offer
        :param discount: Discount amount for the offer
        :param tokens_required: Number of CRUDO tokens required to redeem the offer
        :raises ValueError: If the offer already exists or if discount/tokens are negative
        """
        if offer_name in self.offers:
            raise ValueError("Offer already exists.")
        if discount < 0 or tokens_required < 0:
            raise ValueError("Discount and tokens required must be non-negative.")

        self.offers[offer_name] = {
            'discount': discount,
            'tokens_required': tokens_required
        }

    def remove_offer(self, offer_name: str) -> None:
        """
        Remove an existing loyalty offer from the program.

        :param offer_name: Name of the offer to remove
        :raises KeyError: If the offer does not exist
        """
        if offer_name not in self.offers:
            raise KeyError("Offer does not exist.")
        del self.offers[offer_name]

    def get_offers(self) -> List[Dict[str, float]]:
        """
        Retrieve all available loyalty offers.

        :return: A list of offers with their details
        """
        return [{'offer_name': name, **details} for name, details in self.offers.items()]

    def redeem_offer(self, offer_name: str, customer_tokens: float) -> Optional[str]:
        """
        Redeem a loyalty offer for a customer.

        :param offer_name: Name of the offer to redeem
        :param customer_tokens: Number of CRUDO tokens the customer has
        :return: A message indicating the result of the redemption
        :raises KeyError: If the offer does not exist
        """
        if offer_name not in self.offers:
            raise KeyError("Offer does not exist.")

        offer = self.offers[offer_name]
        if customer_tokens < offer['tokens_required']:
            return "Insufficient tokens to redeem this offer."

        # Deduct tokens and apply discount
        customer_tokens -= offer['tokens_required']
        return f"Offer '{offer_name}' redeemed! You have {customer_tokens} tokens left."

# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()

    # Adding offers
    try:
        loyalty_program.add_offer("10% Off Fuel", 10.0, 100)
        loyalty_program.add_offer("Free Car Wash", 0.0, 50)
    except ValueError as e:
        print(f"Error adding offer: {e}")

    # Displaying offers
    print("Available Offers:")
    for offer in loyalty_program.get_offers():
        print(offer)

    # Redeeming an offer
    try:
        result = loyalty_program.redeem_offer("10% Off Fuel", 150)
        print(result)
    except KeyError as e:
        print(f"Error redeeming offer: {e}")

    # Removing an offer
    try:
        loyalty_program.remove_offer("Free Car Wash")
    except KeyError as e:
        print(f"Error removing offer: {e}")
```
