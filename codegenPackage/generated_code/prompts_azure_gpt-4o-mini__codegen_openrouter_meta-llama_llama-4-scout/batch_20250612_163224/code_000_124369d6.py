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
# profit_based_fee_structure.py

class TradingGroup:
    def __init__(self, fee_rate=0.1, portfolio_doubling_threshold=2):
        """
        Initialize a TradingGroup instance.

        Args:
        - fee_rate (float): The rate at which members pay fees (default: 0.1 or 10%).
        - portfolio_doubling_threshold (float): The threshold at which a member's portfolio is considered doubled (default: 2).
        """
        self.fee_rate = fee_rate
        self.portfolio_doubling_threshold = portfolio_doubling_threshold
        self.members = {}

    def add_member(self, member_id, initial_portfolio):
        """
        Add a member to the trading group.

        Args:
        - member_id (str): The unique ID of the member.
        - initial_portfolio (float): The initial portfolio value of the member.

        Raises:
        - ValueError: If the initial portfolio is not a positive number.
        """
        if initial_portfolio <= 0:
            raise ValueError("Initial portfolio must be a positive number")

        self.members[member_id] = {
            "initial_portfolio": initial_portfolio,
            "current_portfolio": initial_portfolio,
            "profits": 0
        }

    def update_member_portfolio(self, member_id, new_portfolio):
        """
        Update a member's portfolio and calculate profits.

        Args:
        - member_id (str): The unique ID of the member.
        - new_portfolio (float): The new portfolio value of the member.

        Raises:
        - ValueError: If the new portfolio is not a positive number.
        - KeyError: If the member is not found in the group.
        """
        if new_portfolio <= 0:
            raise ValueError("New portfolio must be a positive number")

        if member_id not in self.members:
            raise KeyError("Member not found in the group")

        member = self.members[member_id]
        initial_portfolio = member["initial_portfolio"]
        current_portfolio = member["current_portfolio"]

        # Check if the portfolio has doubled
        if current_portfolio < self.portfolio_doubling_threshold * initial_portfolio and new_portfolio >= self.portfolio_doubling_threshold * initial_portfolio:
            print(f"Member {member_id}'s portfolio has doubled")

        # Calculate profits
        profits = new_portfolio - current_portfolio
        member["profits"] += profits

        # Update member's portfolio
        member["current_portfolio"] = new_portfolio

        # Calculate fee
        if member["current_portfolio"] >= self.portfolio_doubling_threshold * initial_portfolio and member["profits"] > 0:
            fee = member["profits"] * self.fee_rate
            member["profits"] -= fee
            print(f"Member {member_id} paid a fee of {fee}")

    def get_member_info(self, member_id):
        """
        Get a member's information.

        Args:
        - member_id (str): The unique ID of the member.

        Returns:
        - dict: The member's information.

        Raises:
        - KeyError: If the member is not found in the group.
        """
        if member_id not in self.members:
            raise KeyError("Member not found in the group")

        return self.members[member_id]


def main():
    group = TradingGroup()

    # Add members
    group.add_member("member1", 1000)
    group.add_member("member2", 500)

    # Update member portfolios
    group.update_member_portfolio("member1", 2000)
    group.update_member_portfolio("member2", 1500)

    # Get member information
    print(group.get_member_info("member1"))
    print(group.get_member_info("member2"))


if __name__ == "__main__":
    main()
```
