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
# Governance Proposal Template for ORB Token Holders

class GovernanceProposal:
    """
    A class to represent a governance proposal for ORB token holders in the Zealy ecosystem.
    
    Attributes:
        title (str): The title of the proposal.
        description (str): A detailed description of the proposal.
        proposed_features (list): A list of features being proposed.
        voting_deadline (str): The deadline for voting on the proposal in ISO 8601 format.
        votes_for (int): Number of votes in favor of the proposal.
        votes_against (int): Number of votes against the proposal.
        total_votes (int): Total votes cast.
        status (str): Status of the proposal ('Open', 'Closed').
    """

    def __init__(self, title: str, description: str, proposed_features: list, voting_deadline: str):
        """
        Initializes a new governance proposal.
        
        Args:
            title (str): The title of the proposal.
            description (str): The detailed description of the proposal.
            proposed_features (list): The features to be proposed.
            voting_deadline (str): The deadline for voting.
        """
        self.title = title
        self.description = description
        self.proposed_features = proposed_features
        self.voting_deadline = voting_deadline
        self.votes_for = 0
        self.votes_against = 0
        self.total_votes = 0
        self.status = 'Open'

    def cast_vote(self, vote: str):
        """
        Cast a vote on the proposal.
        
        Args:
            vote (str): The vote to cast ('for' or 'against').
        
        Raises:
            ValueError: If the proposal is closed or vote is not recognized.
        """
        if self.status != 'Open':
            raise ValueError("Voting is closed for this proposal.")
        
        if vote.lower() == 'for':
            self.votes_for += 1
        elif vote.lower() == 'against':
            self.votes_against += 1
        else:
            raise ValueError("Vote must be 'for' or 'against'.")
        
        self.total_votes += 1

    def close_voting(self):
        """
        Closes the voting for the proposal and sets the status to 'Closed'.
        
        Raises:
            RuntimeError: If the proposal is already closed.
        """
        if self.status == 'Closed':
            raise RuntimeError("Voting is already closed.")
        
        self.status = 'Closed'

    def get_results(self):
        """
        Returns the voting results of the proposal.

        Returns:
            dict: A dictionary containing the results of the votes.
        """
        return {
            'title': self.title,
            'votes_for': self.votes_for,
            'votes_against': self.votes_against,
            'total_votes': self.total_votes,
            'status': self.status
        }

# Example usage:
if __name__ == "__main__":
    try:
        proposal = GovernanceProposal(
            title="New Feature Proposal: Enhanced Security",
            description="This proposal suggests implementing advanced security measures in the Zealy ecosystem.",
            proposed_features=["Multi-factor authentication", "Encryption of user data"],
            voting_deadline="2023-12-31T23:59:59Z"
        )
        
        # Cast some votes
        proposal.cast_vote('for')
        proposal.cast_vote('against')
        
        # Close voting
        proposal.close_voting()
        
        # Get the results
        results = proposal.get_results()
        print(results)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
