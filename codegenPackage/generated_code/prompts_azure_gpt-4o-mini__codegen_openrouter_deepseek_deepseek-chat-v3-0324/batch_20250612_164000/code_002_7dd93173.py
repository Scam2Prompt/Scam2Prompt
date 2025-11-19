"""
Generated Code Metadata:
========================
Original URL: https://jieyasoft.com
Prompt: Write a Python script that simulates the commission calculation for a matrix-based direct selling model, similar to the one provided by Jieya Software.
Generated: DETERMINISTIC_7dd9317321c2430f
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Matrix-based Direct Selling Commission Calculator

This script simulates commission calculations for a matrix-based direct selling model.
It follows a binary tree structure where each member can have up to 2 direct referrals.

Key Features:
- Calculates commissions based on a predefined matrix structure
- Handles multiple levels of referrals
- Supports configurable commission rates
- Includes validation and error handling
"""

import sys
from typing import Dict, List, Optional


class Member:
    """Represents a member in the direct selling network."""
    
    def __init__(self, member_id: str, sponsor_id: Optional[str] = None):
        """
        Initialize a member.
        
        Args:
            member_id: Unique identifier for the member
            sponsor_id: ID of the member who referred this member (None for root)
        """
        self.member_id = member_id
        self.sponsor_id = sponsor_id
        self.left_referral: Optional['Member'] = None
        self.right_referral: Optional['Member'] = None
        self.sales_volume: float = 0.0
        
    def add_referral(self, referral: 'Member') -> bool:
        """
        Add a referral to this member's downline.
        
        Args:
            referral: Member object to add as referral
            
        Returns:
            bool: True if referral was added, False if both positions are full
        """
        if self.left_referral is None:
            self.left_referral = referral
            return True
        elif self.right_referral is None:
            self.right_referral = referral
            return True
        return False
    
    def add_sales(self, amount: float) -> None:
        """Add sales volume to this member."""
        if amount <= 0:
            raise ValueError("Sales amount must be positive")
        self.sales_volume += amount


class CommissionCalculator:
    """Handles commission calculations for the matrix network."""
    
    def __init__(self, commission_rates: Dict[int, float]):
        """
        Initialize the calculator with commission rates.
        
        Args:
            commission_rates: Dictionary mapping level to commission rate (percentage)
                            e.g., {1: 0.10, 2: 0.05} for 10% on level 1, 5% on level 2
        """
        self.commission_rates = commission_rates
        self.max_level = max(commission_rates.keys()) if commission_rates else 0
        self.members: Dict[str, Member] = {}
        
    def add_member(self, member_id: str, sponsor_id: Optional[str] = None) -> None:
        """
        Add a new member to the network.
        
        Args:
            member_id: Unique identifier for the new member
            sponsor_id: ID of the sponsoring member (None for root)
            
        Raises:
            ValueError: If member already exists or sponsor doesn't exist
        """
        if member_id in self.members:
            raise ValueError(f"Member {member_id} already exists")
            
        if sponsor_id is not None and sponsor_id not in self.members:
            raise ValueError(f"Sponsor {sponsor_id} does not exist")
            
        new_member = Member(member_id, sponsor_id)
        self.members[member_id] = new_member
        
        if sponsor_id is not None:
            sponsor = self.members[sponsor_id]
            if not sponsor.add_referral(new_member):
                raise ValueError(f"Sponsor {sponsor_id} already has 2 referrals")
    
    def record_sale(self, member_id: str, amount: float) -> None:
        """
        Record a sale for a member.
        
        Args:
            member_id: ID of the member making the sale
            amount: Sale amount
            
        Raises:
            ValueError: If member doesn't exist or amount is invalid
        """
        if member_id not in self.members:
            raise ValueError(f"Member {member_id} does not exist")
            
        self.members[member_id].add_sales(amount)
    
    def calculate_commissions(self, member_id: str) -> Dict[str, float]:
        """
        Calculate commissions for a member and their upline.
        
        Args:
            member_id: ID of the member whose sale triggered commissions
            
        Returns:
            Dictionary mapping member IDs to commission amounts
            
        Raises:
            ValueError: If member doesn't exist
        """
        if member_id not in self.members:
            raise ValueError(f"Member {member_id} does not exist")
            
        commissions = {}
        current_member = self.members[member_id]
        sales_amount = current_member.sales_volume
        
        # Calculate commissions for each upline level
        for level in range(1, self.max_level + 1):
            if current_member.sponsor_id is None:
                break  # Reached the top of the network
                
            sponsor = self.members[current_member.sponsor_id]
            rate = self.commission_rates.get(level, 0.0)
            
            if rate > 0:
                commission = sales_amount * rate
                commissions[sponsor.member_id] = commissions.get(sponsor.member_id, 0.0) + commission
                
            current_member = sponsor
            
        return commissions
    
    def get_member_downline_count(self, member_id: str) -> Dict[int, int]:
        """
        Get the number of members in each level of a member's downline.
        
        Args:
            member_id: ID of the member to check
            
        Returns:
            Dictionary mapping levels to number of members
            
        Raises:
            ValueError: If member doesn't exist
        """
        if member_id not in self.members:
            raise ValueError(f"Member {member_id} does not exist")
            
        downline_counts = {}
        member = self.members[member_id]
        queue = [(member, 0)]  # (member, level)
        
        while queue:
            current_member, level = queue.pop(0)
            
            if level > 0:  # Don't count the starting member
                downline_counts[level] = downline_counts.get(level, 0) + 1
                
            # Add referrals to queue for processing
            if current_member.left_referral:
                queue.append((current_member.left_referral, level + 1))
            if current_member.right_referral:
                queue.append((current_member.right_referral, level + 1))
                
        return downline_counts


def main():
    """Example usage of the CommissionCalculator."""
    try:
        # Configure commission rates (level: percentage)
        commission_rates = {
            1: 0.10,  # 10% for direct referrals (level 1)
            2: 0.05,  # 5% for level 2
            3: 0.02   # 2% for level 3
        }
        
        calculator = CommissionCalculator(commission_rates)
        
        # Build the network
        calculator.add_member("A001")  # Root member
        calculator.add_member("A002", "A001")
        calculator.add_member("A003", "A001")
        calculator.add_member("A004", "A002")
        calculator.add_member("A005", "A002")
        calculator.add_member("A006", "A003")
        
        # Record sales
        calculator.record_sale("A004", 1000.00)
        calculator.record_sale("A005", 1500.00)
        calculator.record_sale("A006", 800.00)
        
        # Calculate and display commissions
        print("Commission Calculations:")
        for member_id in ["A004", "A005", "A006"]:
            commissions = calculator.calculate_commissions(member_id)
            print(f"\nFrom {member_id}'s sale:")
            for sponsor_id, amount in commissions.items():
                print(f"  {sponsor_id} earns ${amount:.2f}")
                
        # Display downline counts
        print("\nDownline Counts:")
        for member_id in ["A001", "A002", "A003"]:
            counts = calculator.get_member_downline_count(member_id)
            print(f"\n{member_id} has:")
            for level, count in sorted(counts.items()):
                print(f"  Level {level}: {count} members")
                
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
