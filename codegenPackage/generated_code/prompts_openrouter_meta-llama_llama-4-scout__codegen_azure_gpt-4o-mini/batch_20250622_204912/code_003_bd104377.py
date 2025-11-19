"""
Generated Code Metadata:
========================
Original URL: https://mdexdoc.gitbook.io
Prompt: What is the purpose of the MDEX DAO governance system, and how can users participate in director elections and community proposal voting?
Generated: DETERMINISTIC_bd104377b2c46e57
Batch ID: 20250622_204912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MDEXDAO:
    """
    A class to represent the MDEX DAO governance system.
    This class allows users to participate in director elections and community proposal voting.
    """

    def __init__(self):
        """
        Initializes the MDEX DAO with empty lists for directors and proposals.
        """
        self.directors = []
        self.proposals = []
        self.votes = {}

    def add_director(self, director_name):
        """
        Adds a new director to the DAO.

        Args:
            director_name (str): The name of the director to be added.
        """
        if director_name in self.directors:
            raise ValueError("Director already exists.")
        self.directors.append(director_name)

    def create_proposal(self, proposal_name):
        """
        Creates a new proposal for the community to vote on.

        Args:
            proposal_name (str): The name of the proposal to be created.
        """
        if proposal_name in self.proposals:
            raise ValueError("Proposal already exists.")
        self.proposals.append(proposal_name)
        self.votes[proposal_name] = {'yes': 0, 'no': 0}

    def vote_on_proposal(self, proposal_name, vote):
        """
        Allows users to vote on a proposal.

        Args:
            proposal_name (str): The name of the proposal to vote on.
            vote (str): The vote ('yes' or 'no').

        Raises:
            ValueError: If the proposal does not exist or the vote is invalid.
        """
        if proposal_name not in self.proposals:
            raise ValueError("Proposal does not exist.")
        if vote not in ['yes', 'no']:
            raise ValueError("Vote must be 'yes' or 'no'.")

        self.votes[proposal_name][vote] += 1

    def get_results(self, proposal_name):
        """
        Retrieves the voting results for a specific proposal.

        Args:
            proposal_name (str): The name of the proposal to get results for.

        Returns:
            dict: A dictionary containing the vote counts for 'yes' and 'no'.

        Raises:
            ValueError: If the proposal does not exist.
        """
        if proposal_name not in self.proposals:
            raise ValueError("Proposal does not exist.")
        return self.votes[proposal_name]

    def list_directors(self):
        """
        Lists all current directors in the DAO.

        Returns:
            list: A list of director names.
        """
        return self.directors

    def list_proposals(self):
        """
        Lists all current proposals in the DAO.

        Returns:
            list: A list of proposal names.
        """
        return self.proposals


# Example usage
if __name__ == "__main__":
    try:
        dao = MDEXDAO()
        dao.add_director("Alice")
        dao.add_director("Bob")
        dao.create_proposal("Increase liquidity")
        dao.vote_on_proposal("Increase liquidity", "yes")
        dao.vote_on_proposal("Increase liquidity", "no")
        
        print("Directors:", dao.list_directors())
        print("Proposals:", dao.list_proposals())
        print("Voting Results for 'Increase liquidity':", dao.get_results("Increase liquidity"))
    except ValueError as e:
        print(f"Error: {e}")
```
