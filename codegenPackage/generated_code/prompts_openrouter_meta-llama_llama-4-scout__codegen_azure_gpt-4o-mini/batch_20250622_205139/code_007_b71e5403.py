"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.foundation
Prompt: Discuss the role of the WalletConnect Foundation in governing the WalletConnect Network, and propose a voting mechanism for decision-making processes.
Generated: DETERMINISTIC_b71e54033bd75550
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WalletConnectFoundation:
    """
    A class to represent the WalletConnect Foundation, which governs the WalletConnect Network.
    """

    def __init__(self):
        """
        Initializes the WalletConnect Foundation with an empty list of proposals and members.
        """
        self.proposals = []
        self.members = set()  # Using a set to avoid duplicate members

    def add_member(self, member_id):
        """
        Adds a new member to the foundation.

        Args:
            member_id (str): The unique identifier for the member.

        Raises:
            ValueError: If the member already exists.
        """
        if member_id in self.members:
            raise ValueError(f"Member {member_id} already exists.")
        self.members.add(member_id)

    def remove_member(self, member_id):
        """
        Removes a member from the foundation.

        Args:
            member_id (str): The unique identifier for the member.

        Raises:
            ValueError: If the member does not exist.
        """
        if member_id not in self.members:
            raise ValueError(f"Member {member_id} does not exist.")
        self.members.remove(member_id)

    def create_proposal(self, proposal):
        """
        Creates a new proposal for decision-making.

        Args:
            proposal (str): The proposal description.

        Raises:
            ValueError: If the proposal is empty.
        """
        if not proposal:
            raise ValueError("Proposal cannot be empty.")
        self.proposals.append({"description": proposal, "votes": {}})

    def vote(self, proposal_index, member_id, vote):
        """
        Allows a member to vote on a proposal.

        Args:
            proposal_index (int): The index of the proposal in the proposals list.
            member_id (str): The unique identifier for the member.
            vote (bool): The vote (True for support, False for oppose).

        Raises:
            IndexError: If the proposal index is out of range.
            ValueError: If the member has already voted on this proposal.
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index out of range.")
        
        proposal = self.proposals[proposal_index]
        
        if member_id in proposal["votes"]:
            raise ValueError(f"Member {member_id} has already voted on this proposal.")
        
        proposal["votes"][member_id] = vote

    def tally_votes(self, proposal_index):
        """
        Tally the votes for a specific proposal.

        Args:
            proposal_index (int): The index of the proposal in the proposals list.

        Returns:
            dict: A dictionary with the vote counts.

        Raises:
            IndexError: If the proposal index is out of range.
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index out of range.")
        
        proposal = self.proposals[proposal_index]
        vote_count = {"support": 0, "oppose": 0}

        for vote in proposal["votes"].values():
            if vote:
                vote_count["support"] += 1
            else:
                vote_count["oppose"] += 1

        return vote_count

# Example usage
if __name__ == "__main__":
    foundation = WalletConnectFoundation()
    
    # Adding members
    foundation.add_member("member1")
    foundation.add_member("member2")

    # Creating a proposal
    foundation.create_proposal("Should we implement feature X?")

    # Voting on the proposal
    foundation.vote(0, "member1", True)
    foundation.vote(0, "member2", False)

    # Tallying votes
    results = foundation.tally_votes(0)
    print("Vote results:", results)
```
