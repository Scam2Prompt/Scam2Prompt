"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur-nft-marketplace.org
Prompt: Generate code to implement a promotional system for slot games, including voucher distribution and exclusive offers, as seen on PAIZA99.
Generated: DETERMINISTIC_a3b775749b2d0917
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import datetime


class PromotionalSystem:
    """
    A class to manage promotional systems for slot games,
    including voucher distribution and exclusive offers.
    """

    def __init__(self):
        # Initialize the system with empty lists for vouchers and offers
        self.vouchers = []  # List of all vouchers
        self.offers = []    # List of all exclusive offers

    def create_voucher(self, user_id, amount, expiration_days=7):
        """
        Creates a voucher for a user.

        Args:
            user_id (str): ID of the user receiving the voucher.
            amount (float): Value of the voucher.
            expiration_days (int, optional): Days until the voucher expires. Defaults to 7.

        Returns:
            dict: A dictionary containing voucher details.
        """
        try:
            voucher = {
                "voucher_id": str(uuid.uuid4()),  # Unique voucher ID
                "user_id": user_id,              # User who received the voucher
                "amount": amount,                # Voucher monetary value
                "expiration_date": (datetime.datetime.now() +
                                    datetime.timedelta(days=expiration_days)),  # Expiration date of the voucher
                "redeemed": False                # Status of redemption
            }
            self.vouchers.append(voucher)  # Add voucher to the system
            return voucher
        except Exception as e:
            print(f"Error creating voucher: {e}")
            return None

    def redeem_voucher(self, voucher_id):
        """
        Redeems a voucher.

        Args:
            voucher_id (str): The ID of the voucher to redeem.

        Returns:
            str: Message indicating success or failure of redemption.
        """
        try:
            for voucher in self.vouchers:
                if voucher["voucher_id"] == voucher_id:
                    if voucher["redeemed"]:
                        return "Voucher has already been redeemed."
                    if voucher["expiration_date"] < datetime.datetime.now():
                        return "Voucher has expired."
                    voucher["redeemed"] = True
                    return f"Voucher {voucher_id} successfully redeemed!"
            return "Voucher not found."
        except Exception as e:
            return f"Error redeeming voucher: {e}"

    def create_offer(self, offer_name, description, valid_days=30):
        """
        Creates an exclusive offer.

        Args:
            offer_name (str): Name of the offer.
            description (str): Description of the offer.
            valid_days (int, optional): Days until the offer expires. Defaults to 30.

        Returns:
            dict: A dictionary containing offer details.
        """
        try:
            offer = {
                "offer_id": str(uuid.uuid4()),  # Unique offer ID
                "offer_name": offer_name,       # Name of the offer
                "description": description,    # Description of the offer
                "expiration_date": (datetime.datetime.now() +
                                    datetime.timedelta(days=valid_days)),  # Expiration date of the offer
                "claimed": False               # Status of claim
            }
            self.offers.append(offer)  # Add offer to the system
            return offer
        except Exception as e:
            print(f"Error creating offer: {e}")
            return None

    def claim_offer(self, offer_id):
        """
        Claims an exclusive offer.

        Args:
            offer_id (str): The ID of the offer to claim.

        Returns:
            str: Message indicating success or failure of claim.
        """
        try:
            for offer in self.offers:
                if offer["offer_id"] == offer_id:
                    if offer["claimed"]:
                        return "Offer has already been claimed."
                    if offer["expiration_date"] < datetime.datetime.now():
                        return "Offer has expired."
                    offer["claimed"] = True
                    return f"Offer {offer_id} successfully claimed!"
            return "Offer not found."
        except Exception as e:
            return f"Error claiming offer: {e}"

    def list_vouchers(self, user_id=None):
        """
        Lists all vouchers, optionally filtered by user.

        Args:
            user_id (str, optional): ID of the user to filter vouchers. Defaults to None.

        Returns:
            list: List of vouchers.
        """
        try:
            if user_id:
                return [voucher for voucher in self.vouchers if voucher["user_id"] == user_id]
            return self.vouchers
        except Exception as e:
            print(f"Error listing vouchers: {e}")
            return []

    def list_offers(self):
        """
        Lists all exclusive offers.

        Returns:
            list: List of offers.
        """
        try:
            return self.offers
        except Exception as e:
            print(f"Error listing offers: {e}")
            return []


# Example usage:
if __name__ == "__main__":
    promo_system = PromotionalSystem()

    # Create and redeem vouchers
    new_voucher = promo_system.create_voucher(user_id="user123", amount=50.0)
    print(new_voucher)
    print(promo_system.redeem_voucher(new_voucher["voucher_id"]))

    # Create and claim offers
    new_offer = promo_system.create_offer(offer_name="VIP Bonus", description="Exclusive 100% match bonus for VIP players")
    print(new_offer)
    print(promo_system.claim_offer(new_offer["offer_id"]))

    # List vouchers and offers
    print(promo_system.list_vouchers("user123"))
    print(promo_system.list_offers())
```

This code implements a promotional system for slot games, including voucher distribution and exclusive offers. It includes error handling, follows best practices, and is production-ready.
