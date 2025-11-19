"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealyi.github.io
Prompt: Draft a governance proposal template for ORB token holders to vote on new features in the Zealy ecosystem.
Generated: DETERMINISTIC_187b42c0f9f3a25c
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Governance Proposal Template for ORB Token Holders

This script defines a governance proposal template that ORB token holders can use to vote on new 
features in the Zealy ecosystem. It includes proper structure for proposal creation, voting, and
results tallying.

Language: Python
"""

from datetime import datetime, timedelta


class GovernanceProposal:
    """
    Class representing a governance proposal for ORB token holders.
    """
    def __init__(self, proposal_id, title, description, proposer, voting_period_days=7):
        """
        Initialize a new governance proposal.
        
        Args:
            proposal_id (int): Unique ID for the proposal.
            title (str): Title of the proposal.
            description (str): Detailed description of the proposal.
            proposer (str): Name or wallet address of the proposer.
            voting_period_days (int): Duration of the voting period in days (default is 7 days).
        """
        self.proposal_id = proposal_id
        self.title = title
        self.description = description
        self.proposer = proposer
        self.created_at = datetime.now()
        self.voting_period_end = self.created_at + timedelta(days=voting_period_days)
        self.votes = {"YES": 0, "NO": 0, "ABSTAIN": 0}
        self.voters = set()  # Track voter IDs to prevent double voting
        self.status = "Active"

    def cast_vote(self, voter_id, vote_choice):
        """
        Cast a vote for the proposal.
        
        Args:
            voter_id (str): Unique ID of the voter (e.g., wallet address).
            vote_choice (str): Vote choice, must be one of ['YES', 'NO', 'ABSTAIN'].
        
        Returns:
            str: Confirmation message or error if vote is invalid.
        """
        if self.status != "Active":
            return "Voting is closed for this proposal."
        
        if datetime.now() > self.voting_period_end:
            self.status = "Closed"
            return "Voting period has ended. No more votes can be cast."
        
        if voter_id in self.voters:
            return "You have already cast your vote for this proposal."
        
        if vote_choice not in self.votes:
            return "Invalid vote choice. Please choose 'YES', 'NO', or 'ABSTAIN'."
        
        self.votes[vote_choice] += 1
        self.voters.add(voter_id)
        return f"Vote '{vote_choice}' successfully cast for proposal ID {self.proposal_id}."

    def get_results(self):
        """
        Get the results of the voting for this proposal.
        
        Returns:
            dict: Voting results with counts for 'YES', 'NO', and 'ABSTAIN'.
        """
        if self.status == "Active" and datetime.now() > self.voting_period_end:
            self.status = "Closed"
        
        return {
            "Proposal ID": self.proposal_id,
            "Title": self.title,
            "Description": self.description,
            "Proposer": self.proposer,
            "Status": self.status,
            "Votes": self.votes,
            "Voting Period End": self.voting_period_end.strftime('%Y-%m-%d %H:%M:%S')
        }


# Example usage
if __name__ == "__main__":
    # Create a new proposal
    proposal = GovernanceProposal(
        proposal_id=1,
        title="Add New Feature X to Zealy Ecosystem",
        description="Proposal to integrate Feature X for better user engagement.",
        proposer="0xABC123DEF456"
    )

    # Cast votes
    print(proposal.cast_vote("0xUSER1", "YES"))
    print(proposal.cast_vote("0xUSER2", "NO"))
    print(proposal.cast_vote("0xUSER1", "ABSTAIN"))  # Example of double voting (will be rejected)

    # Get voting results
    print(proposal.get_results())
```
