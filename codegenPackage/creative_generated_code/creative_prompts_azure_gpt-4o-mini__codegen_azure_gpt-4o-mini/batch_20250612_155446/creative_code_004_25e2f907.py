"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pantherappai.pages.dev
Prompt: How do I set up a community governance model for a DeFi project like PantherAI?
Generated: DETERMINISTIC_25e2f907c21daa6b
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# community_governance.py

class CommunityGovernance:
    """
    A class to manage community governance for a DeFi project.
    """

    def __init__(self):
        """
        Initializes the governance model with empty proposals and voters.
        """
        self.proposals = []
        self.voters = set()

    def create_proposal(self, proposal_title, proposal_details):
        """
        Creates a new proposal.

        :param proposal_title: Title of the proposal
        :param proposal_details: Detailed description of the proposal
        :raises ValueError: If proposal title is empty
        """
        if not proposal_title:
            raise ValueError("Proposal title cannot be empty.")
        
        proposal = {
            'title': proposal_title,
            'details': proposal_details,
            'votes_for': 0,
            'votes_against': 0,
            'voted_members': set()
        }
        self.proposals.append(proposal)

    def vote(self, proposal_index, member_id, vote_choice):
        """
        Allows a community member to vote on a proposal.

        :param proposal_index: Index of the proposal in the proposals list
        :param member_id: Unique identifier for the voting member
        :param vote_choice: 'for' or 'against' the proposal
        :raises IndexError: If proposal_index is out of range
        :raises ValueError: If vote_choice is not 'for' or 'against'
        :raises Exception: If the member has already voted on the proposal
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index out of range.")
        
        proposal = self.proposals[proposal_index]

        if member_id in proposal['voted_members']:
            raise Exception("Member has already voted on this proposal.")
        
        if vote_choice == 'for':
            proposal['votes_for'] += 1
        elif vote_choice == 'against':
            proposal['votes_against'] += 1
        else:
            raise ValueError("Vote choice must be 'for' or 'against'.")

        proposal['voted_members'].add(member_id)
        self.voters.add(member_id)

    def get_results(self, proposal_index):
        """
        Gets the voting results for a proposal.

        :param proposal_index: Index of the proposal in the proposals list
        :raises IndexError: If proposal_index is out of range
        :return: Dictionary containing the results of the proposal
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index out of range.")
        
        proposal = self.proposals[proposal_index]
        results = {
            'title': proposal['title'],
            'votes_for': proposal['votes_for'],
            'votes_against': proposal['votes_against'],
            'total_voters': len(proposal['voted_members']),
        }
        return results

# Example of usage
if __name__ == "__main__":
    governance_model = CommunityGovernance()
    
    # Create a proposal
    try:
        governance_model.create_proposal("Increase Liquidity", "Proposal to increase liquidity in the pool.")
        governance_model.create_proposal("Governance Token Distribution", "Proposal to distribute governance tokens.")
        
        # Members voting
        governance_model.vote(0, 'member_1', 'for')
        governance_model.vote(0, 'member_2', 'against')
        
        # Retrieve proposal results
        results = governance_model.get_results(0)
        print("Proposal Results:", results)
    except (ValueError, IndexError, Exception) as e:
        print(f"Error occurred: {e}")
```
