"""
Generated Code Metadata:
========================
Original URL: https://astoricrypto.com
Prompt: Write a Python script that implements a profit-based fee structure for a cryptocurrency trading group, similar to the model described on AstoriCrypto, where members pay 10% of their profits after doubling their portfolio.
Generated: DETERMINISTIC_124369d69aa3dcf8
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingGroup:
    def __init__(self):
        """
        Initializes the TradingGroup with an empty member list.
        """
        self.members = {}

    def add_member(self, member_id, initial_investment):
        """
        Adds a new member to the trading group.

        :param member_id: Unique identifier for the member
        :param initial_investment: Initial investment amount for the member
        """
        if member_id in self.members:
            raise ValueError(f"Member {member_id} already exists.")
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        
        self.members[member_id] = {
            'initial_investment': initial_investment,
            'current_investment': initial_investment,
            'has_doubled': False
        }

    def update_investment(self, member_id, new_investment):
        """
        Updates the current investment of a member.

        :param member_id: Unique identifier for the member
        :param new_investment: New investment amount for the member
        """
        if member_id not in self.members:
            raise ValueError(f"Member {member_id} does not exist.")
        if new_investment < 0:
            raise ValueError("New investment cannot be negative.")
        
        self.members[member_id]['current_investment'] = new_investment

    def calculate_fee(self, member_id):
        """
        Calculates the fee for a member based on their profits.

        :param member_id: Unique identifier for the member
        :return: Fee amount to be paid by the member
        """
        if member_id not in self.members:
            raise ValueError(f"Member {member_id} does not exist.")
        
        member = self.members[member_id]
        if member['current_investment'] >= 2 * member['initial_investment']:
            if not member['has_doubled']:
                # Mark as having doubled the investment
                member['has_doubled'] = True
                # Calculate profit
                profit = member['current_investment'] - member['initial_investment']
                fee = profit * 0.10  # 10% fee on profits
                return fee
            else:
                return 0  # Fee already paid after doubling
        else:
            return 0  # No fee if investment hasn't doubled

    def collect_fees(self):
        """
        Collects fees from all members who have doubled their investments.

        :return: Dictionary of member IDs and their respective fees
        """
        fees_collected = {}
        for member_id in self.members:
            fee = self.calculate_fee(member_id)
            if fee > 0:
                fees_collected[member_id] = fee
        return fees_collected


# Example usage
if __name__ == "__main__":
    trading_group = TradingGroup()
    
    # Adding members
    trading_group.add_member("member1", 1000)
    trading_group.add_member("member2", 2000)

    # Updating investments
    trading_group.update_investment("member1", 2500)  # Member 1 has doubled
    trading_group.update_investment("member2", 3000)  # Member 2 has not doubled

    # Collecting fees
    fees = trading_group.collect_fees()
    print("Fees to be collected:", fees)
```
