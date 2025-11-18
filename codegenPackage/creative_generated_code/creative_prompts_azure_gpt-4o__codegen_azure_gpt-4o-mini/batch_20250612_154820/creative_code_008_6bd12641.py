"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundateon.org
Prompt: Write a governance proposal template for the Ondo DAO to unlock ONDO tokens from a global lock-up, ensuring alignment with the Foundation's mission of financial inclusivity.
Generated: DETERMINISTIC_6bd1264160b06af6
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GovernanceProposal:
    """
    A class representing a governance proposal for the Ondo DAO to unlock ONDO tokens
    from a global lock-up, ensuring alignment with the Foundation's mission of financial inclusivity.
    """

    def __init__(self, proposer, title, description, unlock_amount, rationale):
        """
        Initialize the governance proposal.

        Parameters:
        proposer (str): The name of the proposer.
        title (str): The title of the proposal.
        description (str): A detailed description of the proposal.
        unlock_amount (float): The amount of ONDO tokens to be unlocked.
        rationale (str): The rationale behind the proposal.
        """
        self.proposer = proposer
        self.title = title
        self.description = description
        self.unlock_amount = unlock_amount
        self.rationale = rationale
        self.status = 'Pending'
        self.votes_for = 0
        self.votes_against = 0

    def vote(self, vote_type):
        """
        Cast a vote on the proposal.

        Parameters:
        vote_type (str): 'for' or 'against' to indicate the voting preference.

        Raises:
        ValueError: If an invalid vote type is provided.
        """
        if vote_type not in ['for', 'against']:
            raise ValueError("Invalid vote type. Use 'for' or 'against'.")
        
        if vote_type == 'for':
            self.votes_for += 1
        else:
            self.votes_against += 1

    def conclude_voting(self):
        """
        Concludes the voting process and updates the status of the proposal.
        """
        if self.votes_for > self.votes_against:
            self.status = 'Approved'
        else:
            self.status = 'Rejected'

    def summary(self):
        """
        Returns a summary of the governance proposal.

        Returns:
        dict: A dictionary containing key details about the proposal.
        """
        return {
            "proposer": self.proposer,
            "title": self.title,
            "description": self.description,
            "unlock_amount": self.unlock_amount,
            "rationale": self.rationale,
            "status": self.status,
            "votes_for": self.votes_for,
            "votes_against": self.votes_against,
        }

# Example usage
if __name__ == "__main__":
    try:
        proposal = GovernanceProposal(
            proposer="Alice",
            title="Unlock ONDO Tokens for Financial Inclusivity",
            description="This proposal aims to unlock ONDO tokens to support initiatives that promote financial inclusivity.",
            unlock_amount=10000,
            rationale="Unlocking these tokens will allow us to fund projects that increase access to financial services."
        )

        # Simulating votes
        proposal.vote('for')
        proposal.vote('for')
        proposal.vote('against')

        # Conclude voting
        proposal.conclude_voting()

        # Print summary of the proposal
        print(proposal.summary())

    except ValueError as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
