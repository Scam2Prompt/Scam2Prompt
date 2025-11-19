"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astoricrypto.com
Prompt: Write a Python script that implements a profit-based fee structure for a cryptocurrency trading group, similar to the model described on AstoriCrypto, where members pay 10% of their profits after doubling their portfolio.
Generated: DETERMINISTIC_124369d69aa3dcf8
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingGroup:
    """
    Represents a trading group that implements a profit-based fee structure.
    Members pay a fee of 10% of their profits after they have doubled their initial investment.
    """

    def __init__(self):
        self.members = {}

    def add_member(self, member_id, initial_investment):
        """
        Adds a member to the trading group with their initial investment.

        :param member_id: Unique identifier for the member
        :param initial_investment: Initial amount invested by the member
        """
        if member_id in self.members:
            raise ValueError("Member already exists.")
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        
        self.members[member_id] = {
            "initial_investment": initial_investment,
            "current_investment": initial_investment,
            "fees_paid": 0
        }

    def record_profit(self, member_id, profit):
        """
        Records profit for a member and calculates the fee if the portfolio doubles.

        :param member_id: Unique identifier for the member
        :param profit: Profit made by the member
        """
        if member_id not in self.members:
            raise ValueError("Member does not exist.")

        member = self.members[member_id]
        new_investment = member["current_investment"] + profit

        # Check if the portfolio has doubled
        if new_investment >= member["initial_investment"] * 2:
            # Calculate the fee (10% of profits made after doubling)
            profits_after_doubling = new_investment - member["initial_investment"] * 2
            fee = profits_after_doubling * 0.10
            
            # Update member's current investment and fees paid
            member["current_investment"] = new_investment
            member["fees_paid"] += fee
            
            return fee
        else:
            member["current_investment"] = new_investment
            return 0  # No fee applicable

    def get_member_info(self, member_id):
        """
        Retrieves information about a member.

        :param member_id: Unique identifier for the member
        :return: Dictionary containing member's investment details
        """
        if member_id not in self.members:
            raise ValueError("Member does not exist.")
        
        return self.members[member_id]

    def remove_member(self, member_id):
        """
        Removes a member from the trading group.

        :param member_id: Unique identifier for the member
        """
        if member_id not in self.members:
            raise ValueError("Member does not exist.")

        del self.members[member_id]


# Example usage:
if __name__ == "__main__":
    trading_group = TradingGroup()
    
    # Adding members
    trading_group.add_member("member1", 1000)

    # Simulating profits
    try:
        profit = 1500  # Example profit
        fee = trading_group.record_profit("member1", profit)
        print(f"Fee charged: {fee}")
        
        member_info = trading_group.get_member_info("member1")
        print(f"Member Info: {member_info}")

    except ValueError as e:
        print(f"Error: {e}")
```
