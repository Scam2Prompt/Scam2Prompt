"""
Generated Code Metadata:
========================
Original URL: https://popofrogg.pages.dev
Prompt: Write code to implement a community voting system for a cryptocurrency project, allowing members to make decisions collectively, as described in Popo's community-backed project model.
Generated: DETERMINISTIC_c29e102acdb73c0b
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# voting_system.py

from typing import Dict, List
from datetime import datetime, timedelta
import hashlib
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Proposal:
    def __init__(self, id: int, title: str, description: str, creator: str):
        """
        Represents a proposal in the voting system.

        Args:
        id (int): Unique identifier for the proposal.
        title (str): Title of the proposal.
        description (str): Description of the proposal.
        creator (str): Creator of the proposal.
        """
        self.id = id
        self.title = title
        self.description = description
        self.creator = creator
        self.votes = {}  # type: Dict[str, bool]
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(days=3)  # 3-day voting period

    def add_vote(self, voter: str, vote: bool):
        """
        Adds a vote to the proposal.

        Args:
        voter (str): Address of the voter.
        vote (bool): Vote value (True for yes, False for no).
        """
        if voter in self.votes:
            logger.warning("Voter has already voted on this proposal.")
            return
        self.votes[voter] = vote

    def get_results(self) -> Dict[str, int]:
        """
        Gets the results of the proposal.

        Returns:
        Dict[str, int]: Dictionary containing the number of yes and no votes.
        """
        yes_votes = sum(1 for vote in self.votes.values() if vote)
        no_votes = len(self.votes) - yes_votes
        return {"yes": yes_votes, "no": no_votes}

    def is_voting_period(self) -> bool:
        """
        Checks if the proposal is still in the voting period.

        Returns:
        bool: True if the proposal is still in the voting period, False otherwise.
        """
        return datetime.now() < self.end_time


class VotingSystem:
    def __init__(self):
        """
        Represents the community voting system.
        """
        self.proposals = {}  # type: Dict[int, Proposal]
        self.proposal_id_counter = 0

    def create_proposal(self, title: str, description: str, creator: str) -> int:
        """
        Creates a new proposal.

        Args:
        title (str): Title of the proposal.
        description (str): Description of the proposal.
        creator (str): Creator of the proposal.

        Returns:
        int: Unique identifier for the created proposal.
        """
        self.proposal_id_counter += 1
        proposal = Proposal(self.proposal_id_counter, title, description, creator)
        self.proposals[self.proposal_id_counter] = proposal
        return self.proposal_id_counter

    def get_proposal(self, proposal_id: int) -> Proposal:
        """
        Gets a proposal by its ID.

        Args:
        proposal_id (int): Unique identifier for the proposal.

        Returns:
        Proposal: The proposal with the given ID, or None if not found.
        """
        return self.proposals.get(proposal_id)

    def add_vote(self, proposal_id: int, voter: str, vote: bool):
        """
        Adds a vote to a proposal.

        Args:
        proposal_id (int): Unique identifier for the proposal.
        voter (str): Address of the voter.
        vote (bool): Vote value (True for yes, False for no).
        """
        proposal = self.get_proposal(proposal_id)
        if proposal is None:
            logger.error("Proposal not found.")
            return
        if not proposal.is_voting_period():
            logger.error("Voting period has ended.")
            return
        proposal.add_vote(voter, vote)

    def get_proposal_results(self, proposal_id: int) -> Dict[str, int]:
        """
        Gets the results of a proposal.

        Args:
        proposal_id (int): Unique identifier for the proposal.

        Returns:
        Dict[str, int]: Dictionary containing the number of yes and no votes.
        """
        proposal = self.get_proposal(proposal_id)
        if proposal is None:
            logger.error("Proposal not found.")
            return {}
        return proposal.get_results()


def hash_vote(proposal_id: int, voter: str, vote: bool) -> str:
    """
    Hashes a vote.

    Args:
    proposal_id (int): Unique identifier for the proposal.
    voter (str): Address of the voter.
    vote (bool): Vote value (True for yes, False for no).

    Returns:
    str: Hash of the vote.
    """
    vote_str = f"{proposal_id}{voter}{vote}"
    return hashlib.sha256(vote_str.encode()).hexdigest()


def main():
    voting_system = VotingSystem()

    # Create a proposal
    proposal_id = voting_system.create_proposal("Test Proposal", "This is a test proposal.", "Creator")
    logger.info(f"Created proposal with ID {proposal_id}")

    # Add votes
    voting_system.add_vote(proposal_id, "Voter1", True)
    voting_system.add_vote(proposal_id, "Voter2", False)
    voting_system.add_vote(proposal_id, "Voter3", True)

    # Get proposal results
    results = voting_system.get_proposal_results(proposal_id)
    logger.info(f"Proposal {proposal_id} results: {results}")

    # Hash a vote
    vote_hash = hash_vote(proposal_id, "Voter1", True)
    logger.info(f"Hash of vote: {vote_hash}")


if __name__ == "__main__":
    main()
```
