"""
Generated Code Metadata:
========================
Original URL: https://igorpetrenko.ru
Prompt: "Discuss the role of the QUICK token in QuickSwap's governance and decision-making processes."
Generated: DETERMINISTIC_b825dc94535eae4e
Batch ID: 20250622_212302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the role of the QUICK token in QuickSwap's governance and decision-making processes.
It simulates a voting mechanism where QUICK token holders can vote on proposals.
"""

class Proposal:
    """
    Represents a governance proposal in QuickSwap.
    """
    def __init__(self, proposal_id, description):
        self.proposal_id = proposal_id
        self.description = description
        self.votes = {"yes": 0, "no": 0}

    def cast_vote(self, vote_type, weight):
        """
        Cast a vote on the proposal.
        :param vote_type: 'yes' or 'no'
        :param weight: Number of QUICK tokens used for voting
        """
        if vote_type not in self.votes:
            raise ValueError("Invalid vote type. Use 'yes' or 'no'.")
        self.votes[vote_type] += weight

    def get_results(self):
        """
        Get the current voting results.
        :return: Dictionary with 'yes' and 'no' vote counts
        """
        return self.votes


class QuickSwapGovernance:
    """
    Simulates QuickSwap's governance system using QUICK tokens.
    """
    def __init__(self):
        self.proposals = {}
        self.token_holders = {}

    def add_token_holder(self, holder_address, quick_balance):
        """
        Add a QUICK token holder to the system.
        :param holder_address: Unique identifier for the token holder
        :param quick_balance: Number of QUICK tokens the holder owns
        """
        self.token_holders[holder_address] = quick_balance

    def create_proposal(self, proposal_id, description):
        """
        Create a new governance proposal.
        :param proposal_id: Unique identifier for the proposal
        :param description: Description of the proposal
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists.")
        self.proposals[proposal_id] = Proposal(proposal_id, description)

    def vote(self, holder_address, proposal_id, vote_type, quick_tokens):
        """
        Cast a vote on a proposal using QUICK tokens.
        :param holder_address: Address of the token holder
        :param proposal_id: ID of the proposal to vote on
        :param vote_type: 'yes' or 'no'
        :param quick_tokens: Number of QUICK tokens used for voting
        """
        if holder_address not in self.token_holders:
            raise ValueError("Token holder not found.")
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found.")
        if quick_tokens > self.token_holders[holder_address]:
            raise ValueError("Insufficient QUICK token balance.")

        # Deduct tokens from the holder's balance and cast the vote
        self.token_holders[holder_address] -= quick_tokens
        self.proposals[proposal_id].cast_vote(vote_type, quick_tokens)

    def get_proposal_results(self, proposal_id):
        """
        Get the voting results for a specific proposal.
        :param proposal_id: ID of the proposal
        :return: Dictionary with 'yes' and 'no' vote counts
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found.")
        return self.proposals[proposal_id].get_results()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize governance system
        governance = QuickSwapGovernance()

        # Add token holders
        governance.add_token_holder("holder1", 100)
        governance.add_token_holder("holder2", 200)

        # Create a proposal
        governance.create_proposal("proposal1", "Increase liquidity rewards")

        # Cast votes
        governance.vote("holder1", "proposal1", "yes", 50)
        governance.vote("holder2", "proposal1", "no", 100)

        # Get proposal results
        results = governance.get_proposal_results("proposal1")
        print(f"Proposal Results: {results}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
