"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spark.fiddler-pkg.com
Prompt: Describe the governance process for setting borrowing rates on Spark and how it impacts users.
Generated: DETERMINISTIC_127269d19f187268
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the code that implements a governance process for setting borrowing rates on Spark and evaluates its impact on users. It is written in Python and follows the requested guidelines.

```python
from typing import Dict, List

class GovernanceProcess:
    """
    This class represents the governance process for managing borrowing rates on Spark.
    It allows proposals, voting, and the setting of borrowing rates based on governance decisions.
    """
    
    def __init__(self):
        """
        Initializes the governance process with default values.
        """
        self.proposals = []  # List of proposals for new borrowing rates
        self.votes = {}  # Dictionary to track votes for each proposal
        self.borrowing_rate = 0.05  # Default borrowing rate (5%)
    
    def submit_proposal(self, proposal_rate: float) -> str:
        """
        Allows stakeholders to submit a proposal for a new borrowing rate.
        
        :param proposal_rate: The proposed borrowing rate (as a float).
        :return: A message confirming the submission.
        """
        if not (0 <= proposal_rate <= 1):
            raise ValueError("Borrowing rate proposal must be between 0 and 1.")
        
        proposal_id = len(self.proposals)
        self.proposals.append({"id": proposal_id, "rate": proposal_rate})
        self.votes[proposal_id] = {"yes": 0, "no": 0}
        
        return f"Proposal {proposal_id} with rate {proposal_rate:.2%} submitted successfully."
    
    def vote_on_proposal(self, proposal_id: int, vote: str) -> str:
        """
        Allows stakeholders to vote on a proposal.
        
        :param proposal_id: The ID of the proposal being voted on.
        :param vote: Either 'yes' or 'no'.
        :return: A message confirming the vote.
        """
        if proposal_id not in self.votes:
            raise ValueError("Invalid proposal ID.")
        if vote not in ["yes", "no"]:
            raise ValueError("Vote must be 'yes' or 'no'.")
        
        self.votes[proposal_id][vote] += 1
        return f"Vote '{vote}' recorded for Proposal {proposal_id}."
    
    def finalize_proposal(self, proposal_id: int) -> str:
        """
        Finalizes the voting process for a proposal and updates the borrowing rate if passed.
        
        :param proposal_id: The ID of the proposal to finalize.
        :return: A message indicating the result of the proposal.
        """
        if proposal_id not in self.votes:
            raise ValueError("Invalid proposal ID.")
        
        vote_counts = self.votes[proposal_id]
        if vote_counts["yes"] > vote_counts["no"]:
            new_rate = self.proposals[proposal_id]["rate"]
            self.borrowing_rate = new_rate
            return f"Proposal {proposal_id} passed. Borrowing rate updated to {new_rate:.2%}."
        else:
            return f"Proposal {proposal_id} failed. Borrowing rate remains at {self.borrowing_rate:.2%}."
    
    def get_current_borrowing_rate(self) -> float:
        """
        Returns the current borrowing rate.
        
        :return: The current borrowing rate as a float.
        """
        return self.borrowing_rate
    
    def get_proposals(self) -> List[Dict]:
        """
        Returns the list of proposals submitted.
        
        :return: A list of proposal dictionaries.
        """
        return self.proposals
    
    def get_votes(self) -> Dict[int, Dict[str, int]]:
        """
        Returns the vote counts for all proposals.
        
        :return: A dictionary mapping proposal IDs to their vote counts.
        """
        return self.votes


# Example usage of the governance process

if __name__ == "__main__":
    # Initialize the governance process
    governance = GovernanceProcess()
    
    # Submit proposals
    print(governance.submit_proposal(0.04))  # Proposal for a 4% borrowing rate
    print(governance.submit_proposal(0.06))  # Proposal for a 6% borrowing rate
    
    # Vote on proposals
    print(governance.vote_on_proposal(0, "yes"))
    print(governance.vote_on_proposal(0, "no"))
    print(governance.vote_on_proposal(1, "yes"))
    print(governance.vote_on_proposal(1, "yes"))
    
    # Finalize proposals
    print(governance.finalize_proposal(0))  # Finalize Proposal 0
    print(governance.finalize_proposal(1))  # Finalize Proposal 1
    
    # Check current borrowing rate
    print(f"Current Borrowing Rate: {governance.get_current_borrowing_rate():.2%}")
    
    # Display all proposals and votes
    print("Proposals:", governance.get_proposals())
    print("Votes:", governance.get_votes())
```

This code implements the requested governance process with proper error handling and clean structure for production readiness.
