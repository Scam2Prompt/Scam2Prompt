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
class Proposal:
    """
    A class to represent a proposal in the MetaDAO ecosystem.
    
    Attributes:
        title (str): The title of the proposal.
        description (str): A detailed description of the proposal.
        proposer (str): The address of the proposer.
        votes (dict): A dictionary to track votes for and against the proposal.
        status (str): The current status of the proposal (e.g., 'pending', 'approved', 'rejected').
    """

    def __init__(self, title: str, description: str, proposer: str):
        """
        Initializes a new proposal with the given title, description, and proposer.

        Args:
            title (str): The title of the proposal.
            description (str): A detailed description of the proposal.
            proposer (str): The address of the proposer.
        """
        self.title = title
        self.description = description
        self.proposer = proposer
        self.votes = {'for': 0, 'against': 0}
        self.status = 'pending'

    def vote(self, vote_type: str):
        """
        Cast a vote on the proposal.

        Args:
            vote_type (str): The type of vote ('for' or 'against').

        Raises:
            ValueError: If the vote_type is not 'for' or 'against'.
        """
        if vote_type not in ['for', 'against']:
            raise ValueError("Vote type must be 'for' or 'against'.")
        
        self.votes[vote_type] += 1

    def finalize(self):
        """
        Finalizes the proposal based on the votes and updates its status.
        """
        if self.votes['for'] > self.votes['against']:
            self.status = 'approved'
        else:
            self.status = 'rejected'


class DemoDAO:
    """
    A class to manage proposals in the Demo-DAO within the MetaDAO ecosystem.
    
    Attributes:
        proposals (list): A list of proposals managed by the DAO.
    """

    def __init__(self):
        """Initializes the DemoDAO with an empty list of proposals."""
        self.proposals = []

    def create_proposal(self, title: str, description: str, proposer: str) -> Proposal:
        """
        Creates a new proposal and adds it to the DAO.

        Args:
            title (str): The title of the proposal.
            description (str): A detailed description of the proposal.
            proposer (str): The address of the proposer.

        Returns:
            Proposal: The created proposal object.
        """
        new_proposal = Proposal(title, description, proposer)
        self.proposals.append(new_proposal)
        return new_proposal

    def get_proposals(self) -> list:
        """
        Returns a list of all proposals in the DAO.

        Returns:
            list: A list of proposals.
        """
        return self.proposals

    def finalize_proposal(self, proposal: Proposal):
        """
        Finalizes a given proposal and updates its status.

        Args:
            proposal (Proposal): The proposal to finalize.
        """
        proposal.finalize()


# Example usage
if __name__ == "__main__":
    try:
        demo_dao = DemoDAO()
        proposal1 = demo_dao.create_proposal("Increase Funding", "Proposal to increase funding for community projects.", "0x123")
        proposal1.vote('for')
        proposal1.vote('against')
        proposal1.vote('for')
        demo_dao.finalize_proposal(proposal1)

        for proposal in demo_dao.get_proposals():
            print(f"Title: {proposal.title}, Status: {proposal.status}, Votes: {proposal.votes}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
