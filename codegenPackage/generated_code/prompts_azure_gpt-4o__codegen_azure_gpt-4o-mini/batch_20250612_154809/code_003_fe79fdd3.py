"""
Generated Code Metadata:
========================
Original URL: https://handsofgod.app
Prompt: Write a script to simulate the AI-controlled redemption periods for buying and redeeming $BHOG bonds with $HOG in the Purgatory module of the Hand of God platform.
Generated: DETERMINISTIC_fe79fdd3f04a9899
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from datetime import datetime, timedelta

class Bond:
    """Class representing a bond with a specific value and redemption period."""
    
    def __init__(self, bond_id, value, redemption_period):
        self.bond_id = bond_id
        self.value = value
        self.redemption_period = redemption_period
        self.purchase_time = None

    def purchase(self):
        """Simulate purchasing the bond by setting the purchase time."""
        self.purchase_time = datetime.now()
        print(f"Bond {self.bond_id} purchased at {self.purchase_time}.")

    def can_redeem(self):
        """Check if the bond can be redeemed based on the redemption period."""
        if self.purchase_time is None:
            raise ValueError("Bond has not been purchased yet.")
        return datetime.now() >= self.purchase_time + self.redemption_period

class BondMarket:
    """Class to manage the bond market for buying and redeeming bonds."""
    
    def __init__(self):
        self.bonds = []

    def create_bond(self, bond_id, value, redemption_period):
        """Create a new bond and add it to the market."""
        bond = Bond(bond_id, value, redemption_period)
        self.bonds.append(bond)
        print(f"Bond {bond_id} created with value {value} and redemption period {redemption_period}.")

    def purchase_bond(self, bond_id):
        """Purchase a bond by its ID."""
        bond = self.find_bond(bond_id)
        if bond:
            bond.purchase()
        else:
            print(f"Bond {bond_id} not found.")

    def redeem_bond(self, bond_id):
        """Redeem a bond by its ID if the redemption period has passed."""
        bond = self.find_bond(bond_id)
        if bond:
            if bond.can_redeem():
                print(f"Bond {bond_id} redeemed successfully.")
            else:
                print(f"Bond {bond_id} cannot be redeemed yet.")
        else:
            print(f"Bond {bond_id} not found.")

    def find_bond(self, bond_id):
        """Find a bond by its ID."""
        for bond in self.bonds:
            if bond.bond_id == bond_id:
                return bond
        return None

def simulate_bond_market():
    """Simulate the bond market operations."""
    market = BondMarket()
    
    # Create bonds with different redemption periods
    market.create_bond("BHOG001", 100, timedelta(seconds=5))
    market.create_bond("BHOG002", 200, timedelta(seconds=10))
    
    # Purchase bonds
    market.purchase_bond("BHOG001")
    market.purchase_bond("BHOG002")
    
    # Wait for redemption periods to expire
    time.sleep(6)  # Wait for BHOG001 to be redeemable
    market.redeem_bond("BHOG001")
    
    time.sleep(5)  # Wait for BHOG002 to be redeemable
    market.redeem_bond("BHOG002")

if __name__ == "__main__":
    try:
        simulate_bond_market()
    except Exception as e:
        print(f"An error occurred: {e}")
```
