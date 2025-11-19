"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismsio.vercel.app
Prompt: How do I set up a governance model using the two-house system described in the Optimism documentation?
Generated: DETERMINISTIC_08a2caa0e39ae367
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GovernanceModel:
    """
    A simple implementation of a governance model using a two-house system
    inspired by the Optimism documentation.
    """

    def __init__(self):
        """
        Initializes the GovernanceModel with two houses: the Council and the Assembly.
        Each house has its own set of members and voting rules.
        """
        self.council_members = set()
        self.assembly_members = set()
        self.council_votes = {}
        self.assembly_votes = {}

    def add_council_member(self, member_id):
        """
        Adds a member to the Council.

        :param member_id: Unique identifier for the council member
        """
        if member_id in self.council_members:
            raise ValueError("Member already in the council.")
        self.council_members.add(member_id)

    def add_assembly_member(self, member_id):
        """
        Adds a member to the Assembly.

        :param member_id: Unique identifier for the assembly member
        """
        if member_id in self.assembly_members:
            raise ValueError("Member already in the assembly.")
        self.assembly_members.add(member_id)

    def cast_council_vote(self, member_id, vote):
        """
        Casts a vote from a council member.

        :param member_id: Unique identifier for the council member
        :param vote: The vote cast (can be 'yes' or 'no')
        """
        if member_id not in self.council_members:
            raise ValueError("Member is not part of the council.")
        if vote not in ['yes', 'no']:
            raise ValueError("Invalid vote. Must be 'yes' or 'no'.")
        self.council_votes[member_id] = vote

    def cast_assembly_vote(self, member_id, vote):
        """
        Casts a vote from an assembly member.

        :param member_id: Unique identifier for the assembly member
        :param vote: The vote cast (can be 'yes' or 'no')
        """
        if member_id not in self.assembly_members:
            raise ValueError("Member is not part of the assembly.")
        if vote not in ['yes', 'no']:
            raise ValueError("Invalid vote. Must be 'yes' or 'no'.")
        self.assembly_votes[member_id] = vote

    def get_council_result(self):
        """
        Computes the result of the council votes.

        :return: The outcome of the council votes as a string
        """
        if not self.council_votes:
            return "No votes cast in the council."

        yes_votes = sum(1 for vote in self.council_votes.values() if vote == 'yes')
        no_votes = sum(1 for vote in self.council_votes.values() if vote == 'no')
        
        if yes_votes > no_votes:
            return "Council Vote: Passed"
        elif no_votes > yes_votes:
            return "Council Vote: Failed"
        else:
            return "Council Vote: Tie"

    def get_assembly_result(self):
        """
        Computes the result of the assembly votes.

        :return: The outcome of the assembly votes as a string
        """
        if not self.assembly_votes:
            return "No votes cast in the assembly."

        yes_votes = sum(1 for vote in self.assembly_votes.values() if vote == 'yes')
        no_votes = sum(1 for vote in self.assembly_votes.values() if vote == 'no')

        if yes_votes > no_votes:
            return "Assembly Vote: Passed"
        elif no_votes > yes_votes:
            return "Assembly Vote: Failed"
        else:
            return "Assembly Vote: Tie"

# Example usage:
if __name__ == "__main__":
    governance = GovernanceModel()
    
    # Adding members
    governance.add_council_member("councilor1")
    governance.add_council_member("councilor2")
    governance.add_assembly_member("assembly_member1")
    governance.add_assembly_member("assembly_member2")

    # Casting votes
    governance.cast_council_vote("councilor1", "yes")
    governance.cast_council_vote("councilor2", "no")
    governance.cast_assembly_vote("assembly_member1", "yes")
    governance.cast_assembly_vote("assembly_member2", "yes")

    # Getting results
    print(governance.get_council_result())  # Output: Council Vote: Tie
    print(governance.get_assembly_result())  # Output: Assembly Vote: Passed
```
