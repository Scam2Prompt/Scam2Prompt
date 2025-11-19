"""
Generated Code Metadata:
========================
Original URL: https://meta-dao-frontend-nine.vercel.app
Prompt: What unique features does the Demo-DAO offer for proposal management in the MetaDAO ecosystem?
Generated: DETERMINISTIC_e0f6f58dc46f21a7
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# demo_dao.py

class Proposal:
    """Represents a proposal in the MetaDAO ecosystem."""
    
    def __init__(self, id, title, description, proposer):
        """
        Initializes a Proposal object.

        Args:
        id (int): Unique identifier for the proposal.
        title (str): Title of the proposal.
        description (str): Description of the proposal.
        proposer (str): Address of the proposer.
        """
        self.id = id
        self.title = title
        self.description = description
        self.proposer = proposer
        self.votes = []

    def add_vote(self, vote):
        """Adds a vote to the proposal."""
        self.votes.append(vote)


class Vote:
    """Represents a vote on a proposal."""
    
    def __init__(self, voter, vote_type):
        """
        Initializes a Vote object.

        Args:
        voter (str): Address of the voter.
        vote_type (str): Type of vote (e.g., 'yes', 'no', 'abstain').
        """
        self.voter = voter
        self.vote_type = vote_type


class DemoDAO:
    """Represents the Demo-DAO for proposal management in the MetaDAO ecosystem."""
    
    def __init__(self):
        """Initializes the Demo-DAO."""
        self.proposals = {}

    def create_proposal(self, title, description, proposer):
        """
        Creates a new proposal.

        Args:
        title (str): Title of the proposal.
        description (str): Description of the proposal.
        proposer (str): Address of the proposer.

        Returns:
        int: Unique identifier for the proposal.
        """
        proposal_id = len(self.proposals) + 1
        proposal = Proposal(proposal_id, title, description, proposer)
        self.proposals[proposal_id] = proposal
        return proposal_id

    def get_proposal(self, proposal_id):
        """
        Retrieves a proposal by its ID.

        Args:
        proposal_id (int): Unique identifier for the proposal.

        Returns:
        Proposal: The proposal object, or None if not found.
        """
        return self.proposals.get(proposal_id)

    def cast_vote(self, proposal_id, voter, vote_type):
        """
        Casts a vote on a proposal.

        Args:
        proposal_id (int): Unique identifier for the proposal.
        voter (str): Address of the voter.
        vote_type (str): Type of vote (e.g., 'yes', 'no', 'abstain').

        Raises:
        ValueError: If the proposal is not found or the vote type is invalid.
        """
        proposal = self.get_proposal(proposal_id)
        if proposal is None:
            raise ValueError("Proposal not found")

        if vote_type not in ['yes', 'no', 'abstain']:
            raise ValueError("Invalid vote type")

        vote = Vote(voter, vote_type)
        proposal.add_vote(vote)

    def get_unique_features(self):
        """
        Retrieves the unique features of the Demo-DAO for proposal management.

        Returns:
        list: A list of unique features.
        """
        return [
            "Decentralized proposal management",
            "On-chain voting",
            "Transparent decision-making",
            "Flexible proposal structuring"
        ]


def main():
    demo_dao = DemoDAO()

    # Create a proposal
    proposal_id = demo_dao.create_proposal("Example Proposal", "This is an example proposal.", "0x1234567890")
    print(f"Proposal created with ID: {proposal_id}")

    # Cast votes
    demo_dao.cast_vote(proposal_id, "0x9876543210", "yes")
    demo_dao.cast_vote(proposal_id, "0x5678901234", "no")

    # Retrieve proposal and votes
    proposal = demo_dao.get_proposal(proposal_id)
    print(f"Proposal title: {proposal.title}")
    print(f"Proposal description: {proposal.description}")
    print("Votes:")
    for vote in proposal.votes:
        print(f"  - {vote.voter}: {vote.vote_type}")

    # Retrieve unique features
    unique_features = demo_dao.get_unique_features()
    print("Unique features:")
    for feature in unique_features:
        print(f"  - {feature}")


if __name__ == "__main__":
    main()
```
