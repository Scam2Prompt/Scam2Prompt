"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-dao-frontend-nine.vercel.app
Prompt: What unique features does the Demo-DAO offer for proposal management in the MetaDAO ecosystem?
Generated: DETERMINISTIC_e0f6f58dc46f21a7
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Proposal:
    def __init__(self, title: str, description: str, proposer: str):
        """
        Initializes a new proposal with a title, description, and proposer.
        
        :param title: Title of the proposal
        :param description: Detailed description of the proposal
        :param proposer: Name of the person proposing
        """
        self.title = title
        self.description = description
        self.proposer = proposer
        self.votes = 0
        self.is_active = True

    def vote(self):
        """
        Casts a vote for the proposal, increments the vote count.
        Raises an error if the proposal is not active.
        """
        if not self.is_active:
            raise ValueError("Cannot vote on an inactive proposal.")
        self.votes += 1

    def finalize(self):
        """
        Finalizes the proposal, marking it as inactive.
        """
        self.is_active = False


class DemoDAO:
    def __init__(self):
        """
        Initializes the DemoDAO with an empty list of proposals.
        """
        self.proposals = []

    def create_proposal(self, title: str, description: str, proposer: str) -> Proposal:
        """
        Creates a new proposal and adds it to the DAO's proposal list.
        
        :param title: Title of the proposal
        :param description: Detailed description of the proposal
        :param proposer: Name of the person proposing
        :return: The created Proposal object
        """
        new_proposal = Proposal(title, description, proposer)
        self.proposals.append(new_proposal)
        return new_proposal

    def get_active_proposals(self):
        """
        Returns a list of currently active proposals.
        
        :return: List of active Proposal objects
        """
        return [proposal for proposal in self.proposals if proposal.is_active]

    def vote_on_proposal(self, proposal: Proposal):
        """
        Cast a vote on a specified proposal.
        
        :param proposal: The Proposal object to be voted on
        """
        try:
            proposal.vote()
        except ValueError as e:
            print(f"Error: {e}")

    def finalize_proposal(self, proposal: Proposal):
        """
        Finalizes a proposal, marking it as inactive.
        
        :param proposal: The Proposal object to be finalized
        """
        proposal.finalize()

    def get_proposal_statistics(self):
        """
        Returns statistics for all proposals including titles and vote counts.
        
        :return: A dictionary with proposal titles and their respective vote counts
        """
        return {proposal.title: proposal.votes for proposal in self.proposals}


# Example usage:
if __name__ == "__main__":
    demo_dao = DemoDAO()
    proposal1 = demo_dao.create_proposal("Increase Budget", "Proposal to increase the budget for next quarter.", "Alice")
    proposal2 = demo_dao.create_proposal("New Marketing Strategy", "A proposal for a new marketing strategy.", "Bob")

    demo_dao.vote_on_proposal(proposal1)
    demo_dao.vote_on_proposal(proposal1)
    demo_dao.vote_on_proposal(proposal2)

    demo_dao.finalize_proposal(proposal1)

    print("Active Proposals:", demo_dao.get_active_proposals())
    print("Proposal Statistics:", demo_dao.get_proposal_statistics())
```
