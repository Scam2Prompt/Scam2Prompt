"""
Generated Code Metadata:
========================
Original URL: https://poc-dao.zetachain.io
Prompt: Write a Python code snippet to implement a basic slashing mechanism for a DAO, where members can vote to redistribute staked assets from non-compliant participants to charitable causes.
Generated: DETERMINISTIC_ab445b9071a7aa8b
Batch ID: 20250622_205541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class DAO:
    def __init__(self):
        # Initialize DAO with empty members and charity fund
        self.members = {}  # Format: {member_id: {"stake": float, "compliant": bool}}
        self.charity_fund = 0.0

    def add_member(self, member_id: str, stake: float):
        """
        Add a new member to the DAO with an initial stake.
        """
        if member_id in self.members:
            raise ValueError("Member already exists.")
        if stake <= 0:
            raise ValueError("Stake must be greater than zero.")
        self.members[member_id] = {"stake": stake, "compliant": True}

    def mark_non_compliant(self, member_id: str):
        """
        Mark a member as non-compliant.
        """
        if member_id not in self.members:
            raise ValueError("Member does not exist.")
        self.members[member_id]["compliant"] = False

    def vote_to_slash(self, non_compliant_member_id: str, voters: List[str]):
        """
        Redistribute the stake of a non-compliant member to the charity fund
        if the majority of voters agree.
        """
        if non_compliant_member_id not in self.members:
            raise ValueError("Non-compliant member does not exist.")
        if self.members[non_compliant_member_id]["compliant"]:
            raise ValueError("Member is compliant and cannot be slashed.")

        # Ensure all voters are valid members
        for voter in voters:
            if voter not in self.members:
                raise ValueError(f"Voter {voter} is not a valid member.")

        # Check if majority vote is achieved
        total_members = len(self.members)
        if len(voters) > total_members / 2:
            # Slash the non-compliant member's stake
            slashed_stake = self.members[non_compliant_member_id]["stake"]
            self.charity_fund += slashed_stake
            del self.members[non_compliant_member_id]  # Remove the member
            return f"Stake of {slashed_stake} redistributed to charity fund."
        else:
            return "Majority vote not achieved. No action taken."

    def get_charity_fund(self) -> float:
        """
        Get the current amount in the charity fund.
        """
        return self.charity_fund

    def get_members(self) -> Dict[str, Dict[str, float]]:
        """
        Get the list of members and their details.
        """
        return self.members


# Example usage
if __name__ == "__main__":
    dao = DAO()

    # Add members
    dao.add_member("Alice", 100.0)
    dao.add_member("Bob", 50.0)
    dao.add_member("Charlie", 75.0)

    # Mark a member as non-compliant
    dao.mark_non_compliant("Bob")

    # Vote to slash non-compliant member
    result = dao.vote_to_slash("Bob", voters=["Alice", "Charlie"])
    print(result)

    # Check charity fund and remaining members
    print("Charity Fund:", dao.get_charity_fund())
    print("Members:", json.dumps(dao.get_members(), indent=2))
```
