"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-overlay.pages.dev
Prompt: Develop a governance voting system for Overlay Protocol contributors, incorporating Planck Cat NFTs as a mechanism for special privileges and rewards.
Generated: DETERMINISTIC_df6a30b70e33b291
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Governance Voting System for Overlay Protocol Contributors
# This system uses Planck Cat NFTs as a mechanism for special privileges and rewards.

from typing import List, Dict, Optional
from dataclasses import dataclass, field

# Exception for handling errors in the voting process
class VotingError(Exception):
    pass

@dataclass
class Contributor:
    """
    Represents a contributor in the governance voting system.
    """
    name: str
    has_planck_cat_nft: bool = False
    vote: Optional[str] = None

@dataclass
class Proposal:
    """
    Represents a proposal in the governance voting system.
    """
    title: str
    description: str
    votes_for: int = 0
    votes_against: int = 0
    total_votes: int = 0
    has_passed: bool = False

    def cast_vote(self, vote: str):
        """
        Cast a vote for the proposal.
        
        Parameters:
        vote (str): The vote ('for' or 'against').
        """
        if vote not in ["for", "against"]:
            raise VotingError("Invalid vote. Must be 'for' or 'against'.")
        
        if vote == "for":
            self.votes_for += 1
        else:
            self.votes_against += 1
        self.total_votes += 1
    
    def finalize(self):
        """
        Finalizes the voting by determining if the proposal has passed.
        A proposal passes if it has more votes for than against.
        """
        if self.total_votes > 0:
            self.has_passed = self.votes_for > self.votes_against

class GovernanceVotingSystem:
    """
    Manages the governance voting system for contributors.
    """
    def __init__(self):
        self.contributors: List[Contributor] = []
        self.proposals: List[Proposal] = []

    def add_contributor(self, name: str, has_planck_cat_nft: bool = False):
        """
        Adds a new contributor to the system.
        
        Parameters:
        name (str): The name of the contributor.
        has_planck_cat_nft (bool): Indicates if the contributor has a Planck Cat NFT.
        """
        self.contributors.append(Contributor(name, has_planck_cat_nft))

    def create_proposal(self, title: str, description: str):
        """
        Creates a new proposal for voting.
        
        Parameters:
        title (str): The title of the proposal.
        description (str): A description of the proposal.
        """
        self.proposals.append(Proposal(title, description))

    def cast_vote(self, contributor_name: str, proposal_title: str, vote: str):
        """
        Allows a contributor to cast a vote on a proposal.
        
        Parameters:
        contributor_name (str): The name of the contributor voting.
        proposal_title (str): The title of the proposal being voted on.
        vote (str): The vote ('for' or 'against').
        """
        contributor = next((c for c in self.contributors if c.name == contributor_name), None)
        proposal = next((p for p in self.proposals if p.title == proposal_title), None)

        if not contributor:
            raise VotingError("Contributor not found.")
        if not proposal:
            raise VotingError("Proposal not found.")
        if contributor.vote is not None:
            raise VotingError("Contributor has already voted.")
        
        # Allow contributors with Planck Cat NFTs to vote
        if contributor.has_planck_cat_nft or contributor.vote is None:
            proposal.cast_vote(vote)
            contributor.vote = vote
        else:
            raise VotingError("Contributor does not have permission to vote.")

    def finalize_proposal(self, proposal_title: str):
        """
        Finalizes the voting for a specific proposal.
        
        Parameters:
        proposal_title (str): The title of the proposal to finalize.
        """
        proposal = next((p for p in self.proposals if p.title == proposal_title), None)
        if not proposal:
            raise VotingError("Proposal not found.")
        
        proposal.finalize()

    def get_results(self) -> Dict[str, Dict[str, int]]:
        """
        Returns the results of all proposals.
        
        Returns:
        Dict[str, Dict[str, int]]: A dictionary containing each proposal's results.
        """
        results = {}
        for proposal in self.proposals:
            results[proposal.title] = {
                "votes_for": proposal.votes_for,
                "votes_against": proposal.votes_against,
                "has_passed": proposal.has_passed
            }
        return results

# Example Usage (not part of the production code)
if __name__ == "__main__":
    voting_system = GovernanceVotingSystem()
    voting_system.add_contributor("Alice", has_planck_cat_nft=True)
    voting_system.add_contributor("Bob")
    
    voting_system.create_proposal("Increase Funding", "Proposal to increase funding for the project.")
    
    voting_system.cast_vote("Alice", "Increase Funding", "for")
    voting_system.cast_vote("Bob", "Increase Funding", "against")
    
    voting_system.finalize_proposal("Increase Funding")
    
    results = voting_system.get_results()
    print(results)
```
