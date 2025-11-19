"""
Generated Code Metadata:
========================
Original URL: https://web3multiconnectdapp.pages.dev
Prompt: Recommend a suitable protocol for governance and decision-making in a decentralized autonomous organization (DAO) built on the DARP Network.
Generated: DETERMINISTIC_59111fadb42290ef
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# DAO Governance Protocol for DARP Network

class DAOGovernance:
    """
    A class to represent the governance protocol for a Decentralized Autonomous Organization (DAO).
    This protocol facilitates decision-making and voting among members of the DAO.
    """

    def __init__(self):
        """
        Initializes the DAO governance with an empty list of proposals and members.
        """
        self.proposals = []  # List to store proposals
        self.members = set()  # Set to store unique members

    def add_member(self, member_id):
        """
        Adds a new member to the DAO.

        Args:
            member_id (str): Unique identifier for the member.

        Raises:
            ValueError: If the member already exists.
        """
        if member_id in self.members:
            raise ValueError("Member already exists.")
        self.members.add(member_id)

    def create_proposal(self, proposal):
        """
        Creates a new proposal for the DAO.

        Args:
            proposal (dict): A dictionary containing proposal details.

        Raises:
            ValueError: If the proposal is invalid.
        """
        if not isinstance(proposal, dict) or 'title' not in proposal or 'description' not in proposal:
            raise ValueError("Invalid proposal format.")
        self.proposals.append(proposal)

    def vote(self, proposal_title, member_id, vote):
        """
        Allows a member to vote on a proposal.

        Args:
            proposal_title (str): The title of the proposal to vote on.
            member_id (str): Unique identifier for the member voting.
            vote (bool): The vote (True for support, False for oppose).

        Raises:
            ValueError: If the member is not part of the DAO or the proposal does not exist.
        """
        if member_id not in self.members:
            raise ValueError("Member not found in the DAO.")
        
        proposal = next((p for p in self.proposals if p['title'] == proposal_title), None)
        if proposal is None:
            raise ValueError("Proposal not found.")

        # Store the vote in the proposal
        if 'votes' not in proposal:
            proposal['votes'] = {'support': 0, 'oppose': 0}
        
        if vote:
            proposal['votes']['support'] += 1
        else:
            proposal['votes']['oppose'] += 1

    def get_results(self, proposal_title):
        """
        Retrieves the voting results for a specific proposal.

        Args:
            proposal_title (str): The title of the proposal.

        Returns:
            dict: A dictionary containing the voting results.

        Raises:
            ValueError: If the proposal does not exist.
        """
        proposal = next((p for p in self.proposals if p['title'] == proposal_title), None)
        if proposal is None:
            raise ValueError("Proposal not found.")
        
        return proposal.get('votes', {})

# Example usage
if __name__ == "__main__":
    dao = DAOGovernance()
    
    # Adding members
    try:
        dao.add_member("member1")
        dao.add_member("member2")
    except ValueError as e:
        print(e)

    # Creating a proposal
    try:
        dao.create_proposal({"title": "Proposal 1", "description": "Description of Proposal 1"})
    except ValueError as e:
        print(e)

    # Voting on a proposal
    try:
        dao.vote("Proposal 1", "member1", True)
        dao.vote("Proposal 1", "member2", False)
    except ValueError as e:
        print(e)

    # Getting results
    try:
        results = dao.get_results("Proposal 1")
        print("Voting Results:", results)
    except ValueError as e:
        print(e)
```
