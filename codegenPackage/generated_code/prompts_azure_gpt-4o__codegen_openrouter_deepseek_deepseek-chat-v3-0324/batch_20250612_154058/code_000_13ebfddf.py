"""
Generated Code Metadata:
========================
Original URL: https://bonanzavc.com
Prompt: Write code to implement a membership system with multiple earning levels (e.g., Junior Member, Intermediate Member, Premium Member, Professional Member) using Python. Include functionality for calculating earnings based on percentages (e.g., 0.7%, 0.8%, 1%, 1.2%).
Generated: DETERMINISTIC_13ebfddffb2fc62e
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import enum
from dataclasses import dataclass
from typing import Optional

class MembershipLevel(enum.Enum):
    """Enum representing different membership levels and their earning percentages."""
    JUNIOR = 0.007  # 0.7%
    INTERMEDIATE = 0.008  # 0.8%
    PREMIUM = 0.01  # 1%
    PROFESSIONAL = 0.012  # 1.2%

@dataclass
class Member:
    """Class representing a member in the membership system."""
    name: str
    level: MembershipLevel
    balance: float = 0.0

    def calculate_earnings(self, amount: float) -> float:
        """Calculate earnings based on membership level percentage.
        
        Args:
            amount: The base amount to calculate earnings from.
            
        Returns:
            The calculated earnings amount.
            
        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return amount * self.level.value

    def add_earnings(self, amount: float) -> None:
        """Add earnings to member's balance.
        
        Args:
            amount: The amount to add to balance.
            
        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

class MembershipSystem:
    """Class representing the membership system."""
    def __init__(self):
        self.members = {}

    def add_member(self, name: str, level: MembershipLevel) -> Member:
        """Add a new member to the system.
        
        Args:
            name: Name of the member.
            level: Membership level.
            
        Returns:
            The created Member object.
            
        Raises:
            ValueError: If member with same name already exists.
        """
        if name in self.members:
            raise ValueError(f"Member '{name}' already exists")
        member = Member(name, level)
        self.members[name] = member
        return member

    def get_member(self, name: str) -> Optional[Member]:
        """Retrieve a member by name.
        
        Args:
            name: Name of the member to retrieve.
            
        Returns:
            Member object if found, None otherwise.
        """
        return self.members.get(name)

    def process_earnings(self, member_name: str, amount: float) -> float:
        """Process earnings for a member and update their balance.
        
        Args:
            member_name: Name of the member.
            amount: Base amount to calculate earnings from.
            
        Returns:
            The calculated earnings amount.
            
        Raises:
            ValueError: If member doesn't exist or amount is invalid.
        """
        member = self.get_member(member_name)
        if not member:
            raise ValueError(f"Member '{member_name}' not found")
        
        earnings = member.calculate_earnings(amount)
        member.add_earnings(earnings)
        return earnings

    def get_member_balance(self, member_name: str) -> float:
        """Get current balance for a member.
        
        Args:
            member_name: Name of the member.
            
        Returns:
            The member's current balance.
            
        Raises:
            ValueError: If member doesn't exist.
        """
        member = self.get_member(member_name)
        if not member:
            raise ValueError(f"Member '{member_name}' not found")
        return member.balance
```
