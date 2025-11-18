"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-guh1xmcsb-voteagora.vercel.app
Prompt: Write code to simulate the voting process for an "Approval Vote Proposal" on the Agora platform, including selecting options and submitting votes.
Generated: DETERMINISTIC_3acba492509a4ef3
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import List, Dict

class ApprovalVoteProposal:
    def __init__(self, title: str, options: List[str]):
        """
        Initializes a new Approval Vote Proposal.
        
        :param title: The title of the proposal.
        :param options: The list of options for the vote.
        """
        self.title = title
        self.options = options
        self.votes: Dict[str, List[str]] = {option: [] for option in options}
        self.voting_open = True
        self.proposal_id = str(uuid.uuid4())  # Unique ID for the proposal

    def submit_vote(self, voter_id: str, selected_options: List[str]) -> bool:
        """
        Submits a vote for the proposal.

        :param voter_id: The unique ID of the voter.
        :param selected_options: The list of selected options to vote for.
        :return: True if the vote is successfully submitted, else False.
        """
        if not self.voting_open:
            print("Voting is closed. Cannot submit vote.")
            return False

        if any(option not in self.options for option in selected_options):
            print("Invalid options selected. Vote cannot be submitted.")
            return False

        # Check if the voter has already voted
        for option in selected_options:
            if voter_id in self.votes[option]:
                print(f"Voter {voter_id} has already voted for {option}. Vote not counted.")
                return False

        # Record the vote
        for option in selected_options:
            self.votes[option].append(voter_id)
        
        print(f"Vote submitted successfully for voter {voter_id} on options {selected_options}.")
        return True

    def close_voting(self):
        """
        Closes the voting process for the proposal.
        """
        self.voting_open = False
        print("Voting has been closed.")

    def get_results(self) -> Dict[str, int]:
        """
        Retrieves the results of the voting.

        :return: A dictionary containing the options and the number of votes for each.
        """
        if self.voting_open:
            print("Voting is still open. Cannot retrieve results.")
            return {}

        # Create a results dictionary with option votes count
        results = {option: len(voters) for option, voters in self.votes.items()}
        return results

# Example usage
if __name__ == "__main__":
    # Create a new approval vote proposal
    proposal = ApprovalVoteProposal("Should we adopt a new policy?", ["Yes", "No", "Abstain"])

    # Simulate some voters submitting their votes
    proposal.submit_vote("voter1", ["Yes"])
    proposal.submit_vote("voter2", ["No"])
    proposal.submit_vote("voter1", ["No"])  # Duplicate vote by the same voter

    # Close voting and retrieve results
    proposal.close_voting()
    results = proposal.get_results()
    print("Voting Results:", results)
```
