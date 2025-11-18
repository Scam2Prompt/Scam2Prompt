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
import random
from datetime import datetime, timedelta

class Voucher:
    """Class representing a promotional voucher."""
    
    def __init__(self, code, discount, expiration_date):
        self.code = code
        self.discount = discount
        self.expiration_date = expiration_date

    def is_valid(self):
        """Check if the voucher is still valid."""
        return datetime.now() < self.expiration_date

class PromotionalSystem:
    """Class to handle promotional activities for slot games."""
    
    def __init__(self):
        self.vouchers = []
        self.exclusive_offers = []

    def generate_voucher(self, discount_percentage, validity_days):
        """Generate a new voucher with a unique code and specified discount."""
        code = self._generate_unique_code()
        expiration_date = datetime.now() + timedelta(days=validity_days)
        voucher = Voucher(code, discount_percentage, expiration_date)
        self.vouchers.append(voucher)
        return voucher

    def _generate_unique_code(self):
        """Generate a unique voucher code."""
        while True:
            code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
            if not any(voucher.code == code for voucher in self.vouchers):
                return code

    def distribute_voucher(self, user_id):
        """Distribute a voucher to a user."""
        if not self.vouchers:
            raise ValueError("No vouchers available for distribution.")
        
        # Randomly select a voucher to distribute
        voucher = random.choice(self.vouchers)
        if not voucher.is_valid():
            raise ValueError("Selected voucher is no longer valid.")
        
        # Here we could implement logic to associate the voucher with the user.
        # For demonstration, we will just print a message.
        print(f"Voucher {voucher.code} with {voucher.discount}% discount distributed to user {user_id}.")

    def add_exclusive_offer(self, offer_description, start_date, end_date):
        """Add an exclusive offer to the promotional system."""
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")
        self.exclusive_offers.append({
            'description': offer_description,
            'start_date': start_date,
            'end_date': end_date
        })

    def get_active_offers(self):
        """Retrieve all active offers."""
        current_date = datetime.now()
        active_offers = [
            offer for offer in self.exclusive_offers
            if offer['start_date'] <= current_date <= offer['end_date']
        ]
        return active_offers

# Example Usage
if __name__ == "__main__":
    promo_system = PromotionalSystem()
    
    # Generate some vouchers
    voucher1 = promo_system.generate_voucher(10, 30)  # 10% off, valid for 30 days
    voucher2 = promo_system.generate_voucher(20, 15)  # 20% off, valid for 15 days

    # Distribute a voucher to user with ID 1
    try:
        promo_system.distribute_voucher(user_id=1)
    except ValueError as e:
        print(f"Error distributing voucher: {e}")

    # Add exclusive offers
    promo_system.add_exclusive_offer("Happy Hour Bonus", datetime.now() - timedelta(days=1), datetime.now() + timedelta(days=7))

    # Retrieve active offers
    active_offers = promo_system.get_active_offers()
    print("Active offers:")
    for offer in active_offers:
        print(f"- {offer['description']} (Valid from {offer['start_date']} to {offer['end_date']})")
```
