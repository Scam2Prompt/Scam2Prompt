"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kyoflnance.org
Prompt: Write a tutorial on how to use KYO Finance's governance system to propose and vote on changes within the ecosystem.
Generated: DETERMINISTIC_327590ec27c2cb04
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# kyo_finance_governance.py

class KyoFinanceGovernance:
    def __init__(self):
        """
        Initializes the governance system with an empty proposals list
        and a dictionary to track votes.
        """
        self.proposals = []
        self.votes = {}

    def propose(self, proposal_text):
        """
        Creates a new proposal.

        :param proposal_text: The text of the proposal.
        :return: The ID of the created proposal.
        :raises ValueError: If the proposal_text is empty.
        """
        if not proposal_text:
            raise ValueError("Proposal text cannot be empty.")

        proposal_id = len(self.proposals) + 1
        self.proposals.append({"id": proposal_id, "text": proposal_text, "votes_for": 0, "votes_against": 0})
        self.votes[proposal_id] = {}
        return proposal_id

    def vote(self, proposal_id, voter_id, vote_choice):
        """
        Votes on a proposal.

        :param proposal_id: The ID of the proposal to vote on.
        :param voter_id: The ID of the voter.
        :param vote_choice: The choice of the voter (True for 'for', False for 'against').
        :raises ValueError: If the proposal_id is invalid or if the voter has already voted.
        """
        if proposal_id < 1 or proposal_id > len(self.proposals):
            raise ValueError("Invalid proposal ID.")

        if voter_id in self.votes[proposal_id]:
            raise ValueError("Voter has already voted on this proposal.")

        if vote_choice:
            self.proposals[proposal_id - 1]["votes_for"] += 1
        else:
            self.proposals[proposal_id - 1]["votes_against"] += 1

        self.votes[proposal_id][voter_id] = vote_choice

    def get_results(self, proposal_id):
        """
        Retrieves the current voting results for a proposal.

        :param proposal_id: The ID of the proposal to get results for.
        :return: A dictionary containing the votes for and against.
        :raises ValueError: If the proposal_id is invalid.
        """
        if proposal_id < 1 or proposal_id > len(self.proposals):
            raise ValueError("Invalid proposal ID.")

        proposal = self.proposals[proposal_id - 1]
        return {
            "votes_for": proposal["votes_for"],
            "votes_against": proposal["votes_against"],
            "proposal_text": proposal["text"]
        }

    def list_proposals(self):
        """
        Lists all proposals with their current voting status.

        :return: A list of current proposals.
        """
        return [{"id": p["id"], "text": p["text"], "votes_for": p["votes_for"], "votes_against": p["votes_against"]}
                for p in self.proposals]


# Example Usage
if __name__ == "__main__":
    governance = KyoFinanceGovernance()

    # Proposing new changes
    proposal_id = governance.propose("Increase governance token supply")
    print(f"Proposal created with ID: {proposal_id}")

    # Voting on the proposal
    try:
        governance.vote(proposal_id, "voter_1", True)  # Voter 1 votes 'for'
        governance.vote(proposal_id, "voter_2", False)  # Voter 2 votes 'against'
    except ValueError as e:
        print(f"Error while voting: {e}")

    # Getting the results of the proposal
    results = governance.get_results(proposal_id)
    print("Current proposal results:", results)

    # Listing all proposals
    all_proposals = governance.list_proposals()
    print("All proposals:", all_proposals)
```
