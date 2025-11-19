"""
Generated Code Metadata:
========================
Original URL: https://alixa.tech
Prompt: Design a loyalty points system in Python that rewards users for active bonds and matured bonds, inspired by the "Loyalty Points" feature on https://alixa.tech.
Generated: DETERMINISTIC_f1fcebedbcb2377c
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum, auto

class BondStatus(Enum):
    ACTIVE = auto()
    MATURED = auto()
    CANCELLED = auto()

@dataclass
class Bond:
    id: str
    user_id: str
    amount: float
    start_date: datetime.date
    end_date: datetime.date
    status: BondStatus = BondStatus.ACTIVE

@dataclass
class LoyaltyPointsTransaction:
    id: str
    user_id: str
    points: int
    bond_id: str
    transaction_date: datetime.date
    description: str

class LoyaltyPointsSystem:
    def __init__(self):
        self.bonds: List[Bond] = []
        self.transactions: List[LoyaltyPointsTransaction] = []
    
    def add_bond(self, bond: Bond) -> None:
        """Add a new bond to the system."""
        if bond.end_date < bond.start_date:
            raise ValueError("End date cannot be before start date")
        self.bonds.append(bond)
    
    def calculate_points_for_bond(self, bond: Bond) -> int:
        """
        Calculate loyalty points for a bond.
        Active bonds earn 1 point per day, matured bonds earn 5 points per day.
        """
        if bond.status == BondStatus.CANCELLED:
            return 0
        
        days = (bond.end_date - bond.start_date).days
        if bond.status == BondStatus.ACTIVE:
            return days * 1
        elif bond.status == BondStatus.MATURED:
            return days * 5
        return 0
    
    def process_matured_bond(self, bond_id: str) -> None:
        """Process a bond that has matured and award loyalty points."""
        bond = next((b for b in self.bonds if b.id == bond_id), None)
        if not bond:
            raise ValueError("Bond not found")
        
        if bond.status != BondStatus.ACTIVE:
            raise ValueError("Only active bonds can be matured")
        
        bond.status = BondStatus.MATURED
        points = self.calculate_points_for_bond(bond)
        
        transaction = LoyaltyPointsTransaction(
            id=str(len(self.transactions) + 1),
            user_id=bond.user_id,
            points=points,
            bond_id=bond.id,
            transaction_date=datetime.date.today(),
            description=f"Points awarded for matured bond {bond.id}"
        )
        self.transactions.append(transaction)
    
    def get_user_points(self, user_id: str) -> int:
        """Get total loyalty points for a user."""
        return sum(
            t.points for t in self.transactions 
            if t.user_id == user_id
        )
    
    def get_user_transactions(self, user_id: str) -> List[LoyaltyPointsTransaction]:
        """Get all loyalty points transactions for a user."""
        return [t for t in self.transactions if t.user_id == user_id]
    
    def cancel_bond(self, bond_id: str) -> None:
        """Cancel a bond and remove any associated loyalty points."""
        bond = next((b for b in self.bonds if b.id == bond_id), None)
        if not bond:
            raise ValueError("Bond not found")
        
        if bond.status == BondStatus.CANCELLED:
            return
        
        # Remove any transactions associated with this bond
        self.transactions = [
            t for t in self.transactions 
            if t.bond_id != bond_id
        ]
        
        bond.status = BondStatus.CANCELLED
```
