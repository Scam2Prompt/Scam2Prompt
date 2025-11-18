"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdfi-git-kyberswap-widget-tbot.vercel.app
Prompt: Suggest tools or libraries for building a voting mechanism in a DeFi ecosystem, referencing the content on the website.
Generated: DETERMINISTIC_1dd189ac624c89f8
Batch ID: 20250612_154637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
VotingMechanism.py

This module provides a basic structure for implementing a voting mechanism in a DeFi ecosystem.
It includes functionality to create proposals, vote on them, and tally results.
"""

class Proposal:
    def __init__(self, title, description):
        """
        Initialize a new proposal.

        :param title: Title of the proposal
        :param description: Description of the proposal
        """
        self.title = title
        self.description = description
        self.votes = 0
        self.voters = set()  # To track unique voters

    def vote(self, voter_id):
        """
        Cast a vote for the proposal.

        :param voter_id: Unique identifier for the voter
        :raises ValueError: If the voter has already voted
        """
        if voter_id in self.voters:
            raise ValueError("This voter has already voted.")
        self.voters.add(voter_id)
        self.votes += 1

    def get_votes(self):
        """
        Get the total number of votes for the proposal.

        :return: Number of votes
        """
        return self.votes


class VotingSystem:
    def __init__(self):
        """Initialize the voting system with an empty list of proposals."""
        self.proposals = []

    def create_proposal(self, title, description):
        """
        Create a new proposal and add it to the list.

        :param title: Title of the proposal
        :param description: Description of the proposal
        """
        proposal = Proposal(title, description)
        self.proposals.append(proposal)

    def vote(self, proposal_index, voter_id):
        """
        Vote on a specific proposal.

        :param proposal_index: Index of the proposal in the list
        :param voter_id: Unique identifier for the voter
        :raises IndexError: If the proposal index is out of range
        :raises ValueError: If the voter has already voted
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index out of range.")
        self.proposals[proposal_index].vote(voter_id)

    def tally_votes(self):
        """
        Tally the votes for all proposals.

        :return: A dictionary with proposal titles and their corresponding vote counts
        """
        results = {proposal.title: proposal.get_votes() for proposal in self.proposals}
        return results

    def get_proposals(self):
        """
        Get a list of all proposals.

        :return: List of proposal titles
        """
        return [proposal.title for proposal in self.proposals]


# Example usage:
if __name__ == "__main__":
    try:
        voting_system = VotingSystem()
        voting_system.create_proposal("Proposal 1", "Description of Proposal 1")
        voting_system.create_proposal("Proposal 2", "Description of Proposal 2")

        # Voter IDs can be any unique string or integer
        voting_system.vote(0, "voter_1")
        voting_system.vote(1, "voter_2")
        voting_system.vote(0, "voter_2")  # This will raise a ValueError

    except ValueError as ve:
        print(f"Error: {ve}")
    except IndexError as ie:
        print(f"Error: {ie}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        # Output the results of the voting
        results = voting_system.tally_votes()
        print("Voting Results:", results)
```
