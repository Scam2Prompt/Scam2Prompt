"""
Generated Code Metadata:
========================
Original URL: https://agora-next-jlesgw0mi-voteagora.vercel.app
Prompt: "How does Optimism Agora facilitate on-chain governance for RetroPGF projects, and what are the key features of its voting system?"
Generated: DETERMINISTIC_edd88f5555e65439
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Optimism Agora Voting System for RetroPGF Projects

This module simulates a voting system for on-chain governance in RetroPGF projects using Optimism Agora.
It includes features such as proposal creation, voting, and result tallying.
"""

class Proposal:
    """
    Class representing a proposal in the voting system.
    """

    def __init__(self, title: str, description: str):
        """
        Initializes a new proposal.

        :param title: Title of the proposal
        :param description: Description of the proposal
        """
        self.title = title
        self.description = description
        self.votes = 0
        self.voters = set()  # To track unique voters

    def vote(self, voter_id: str):
        """
        Cast a vote for the proposal.

        :param voter_id: Unique identifier for the voter
        :raises ValueError: If the voter has already voted
        """
        if voter_id in self.voters:
            raise ValueError("Voter has already voted.")
        self.votes += 1
        self.voters.add(voter_id)

    def get_results(self):
        """
        Returns the current vote count.

        :return: Number of votes received
        """
        return self.votes


class VotingSystem:
    """
    Class representing the voting system for RetroPGF projects.
    """

    def __init__(self):
        """
        Initializes the voting system with an empty list of proposals.
        """
        self.proposals = []

    def create_proposal(self, title: str, description: str) -> Proposal:
        """
        Creates a new proposal and adds it to the voting system.

        :param title: Title of the proposal
        :param description: Description of the proposal
        :return: The created Proposal object
        """
        proposal = Proposal(title, description)
        self.proposals.append(proposal)
        return proposal

    def vote_on_proposal(self, proposal: Proposal, voter_id: str):
        """
        Cast a vote on a specific proposal.

        :param proposal: The proposal to vote on
        :param voter_id: Unique identifier for the voter
        :raises ValueError: If the proposal does not exist
        """
        if proposal not in self.proposals:
            raise ValueError("Proposal does not exist.")
        proposal.vote(voter_id)

    def get_proposal_results(self, proposal: Proposal):
        """
        Retrieves the results of a specific proposal.

        :param proposal: The proposal to get results for
        :return: Number of votes received
        :raises ValueError: If the proposal does not exist
        """
        if proposal not in self.proposals:
            raise ValueError("Proposal does not exist.")
        return proposal.get_results()


# Example usage
if __name__ == "__main__":
    try:
        voting_system = VotingSystem()
        
        # Create a new proposal
        proposal1 = voting_system.create_proposal("Improve Documentation", "Enhance the existing documentation for better clarity.")
        
        # Cast votes
        voting_system.vote_on_proposal(proposal1, "voter_1")
        voting_system.vote_on_proposal(proposal1, "voter_2")
        
        # Get results
        results = voting_system.get_proposal_results(proposal1)
        print(f"Proposal '{proposal1.title}' has received {results} votes.")
        
    except ValueError as e:
        print(f"Error: {e}")
```
