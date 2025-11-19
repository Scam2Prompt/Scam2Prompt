"""
Generated Code Metadata:
========================
Original URL: https://iqnetwork.io
Prompt: Design a simple voting governance proposal for the IQ Token holders using the IQ Dashboard's voting feature, and provide a sample JSON payload for the proposal.
Generated: DETERMINISTIC_fdcbfbc238ea720b
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class VotingProposal:
    def __init__(self, proposal_id, title, description, choices):
        """
        Initialize a voting proposal.

        Args:
        - proposal_id (str): Unique identifier for the proposal.
        - title (str): Title of the proposal.
        - description (str): Description of the proposal.
        - choices (list): List of voting choices.
        """
        self.proposal_id = proposal_id
        self.title = title
        self.description = description
        self.choices = choices
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(days=3)  # 3-day voting period

    def to_json(self):
        """
        Convert the proposal to a JSON payload.

        Returns:
        - dict: JSON representation of the proposal.
        """
        return {
            "proposal_id": self.proposal_id,
            "title": self.title,
            "description": self.description,
            "choices": self.choices,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat()
        }

    def cast_vote(self, voter, choice):
        """
        Cast a vote for the proposal.

        Args:
        - voter (str): Address of the voter.
        - choice (str): Chosen option.

        Raises:
        - ValueError: If the choice is not valid.
        """
        if choice not in self.choices:
            raise ValueError("Invalid choice")

        # Simulate storing the vote (replace with actual storage logic)
        print(f"Vote cast: {voter} - {choice}")

def create_proposal(proposal_id, title, description, choices):
    """
    Create a new voting proposal.

    Args:
    - proposal_id (str): Unique identifier for the proposal.
    - title (str): Title of the proposal.
    - description (str): Description of the proposal.
    - choices (list): List of voting choices.

    Returns:
    - VotingProposal: The created proposal.
    """
    return VotingProposal(proposal_id, title, description, choices)

def main():
    # Sample usage
    proposal_id = "IQ-001"
    title = "Sample Proposal"
    description = "This is a sample proposal for IQ Token holders."
    choices = ["Yes", "No", "Abstain"]

    proposal = create_proposal(proposal_id, title, description, choices)

    # Generate JSON payload
    json_payload = proposal.to_json()
    print(json.dumps(json_payload, indent=4))

    # Cast a vote
    voter = "0x1234567890abcdef"
    choice = "Yes"
    proposal.cast_vote(voter, choice)

if __name__ == "__main__":
    main()
```
