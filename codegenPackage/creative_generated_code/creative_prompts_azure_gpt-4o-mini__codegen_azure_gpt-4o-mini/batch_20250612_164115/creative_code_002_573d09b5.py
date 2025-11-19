"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-3tvf739hr-voteagora.vercel.app
Prompt: What are the key features of the Agora platform for managing voter proposals in blockchain governance?
Generated: DETERMINISTIC_573d09b551cb543f
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AgoraPlatform:
    """
    A class representing the Agora platform for managing voter proposals in blockchain governance.
    """

    def __init__(self):
        """
        Initializes the Agora platform with an empty list of proposals and voters.
        """
        self.proposals = []
        self.voters = set()

    def add_proposal(self, proposal):
        """
        Adds a new proposal to the Agora platform.

        Args:
            proposal (dict): A dictionary containing proposal details. Must include 'id', 'title', and 'description'.
        
        Raises:
            ValueError: If the proposal does not contain the required fields.
        """
        required_fields = ['id', 'title', 'description']
        if not all(field in proposal for field in required_fields):
            raise ValueError("Proposal must contain 'id', 'title', and 'description'")
        
        self.proposals.append(proposal)

    def vote(self, voter_id, proposal_id):
        """
        Allows a voter to cast a vote on a proposal.

        Args:
            voter_id (str): The unique identifier for the voter.
            proposal_id (str): The unique identifier for the proposal.
        
        Raises:
            ValueError: If the voter has already voted or if the proposal does not exist.
        """
        if voter_id in self.voters:
            raise ValueError("Voter has already voted.")
        
        proposal = self.get_proposal(proposal_id)
        if proposal is None:
            raise ValueError("Proposal does not exist.")
        
        # Assuming we store votes in the proposal
        if 'votes' not in proposal:
            proposal['votes'] = 0
        proposal['votes'] += 1
        
        self.voters.add(voter_id)

    def get_proposal(self, proposal_id):
        """
        Retrieves a proposal by its ID.

        Args:
            proposal_id (str): The ID of the proposal to retrieve.
        
        Returns:
            dict: The proposal if found, else None.
        """
        for proposal in self.proposals:
            if proposal['id'] == proposal_id:
                return proposal
        return None

    def get_all_proposals(self):
        """
        Returns a list of all proposals.

        Returns:
            list: A list of all proposals in the platform.
        """
        return self.proposals

    def reset_votes(self):
        """
        Resets the votes for all proposals.
        """
        for proposal in self.proposals:
            proposal['votes'] = 0
        self.voters.clear()


# Example usage
if __name__ == "__main__":
    try:
        agora = AgoraPlatform()
        
        # Adding proposals
        agora.add_proposal({'id': '1', 'title': 'Proposal A', 'description': 'Description of Proposal A'})
        agora.add_proposal({'id': '2', 'title': 'Proposal B', 'description': 'Description of Proposal B'})

        # Voting on a proposal
        agora.vote('voter_1', '1')

        # Fetching proposals
        print(agora.get_all_proposals())
        
        # Resetting votes
        agora.reset_votes()
        
    except ValueError as e:
        print(f"Error: {e}")
```
