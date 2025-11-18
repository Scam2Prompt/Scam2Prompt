"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtualstake.app
Prompt: Write code to simulate governance voting within the Virtuals Protocol using veVIRTUAL holdings as voting power.
Generated: DETERMINISTIC_6c7565dd4882320b
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import Dict, List

class GovernanceVoting:
    """
    Simulates governance voting within the Virtuals Protocol using veVIRTUAL holdings as voting power.
    """

    def __init__(self):
        # Dictionary to store veVIRTUAL holdings for each address
        self.ve_virtual_holdings: Dict[str, float] = {}

        # Active proposals with voting details
        self.proposals: Dict[int, Dict] = {}

        # Proposal counter for generating unique proposal IDs
        self.proposal_counter = 0

    def add_ve_virtual_holder(self, address: str, ve_virtual: float):
        """
        Adds or updates a veVIRTUAL holder's voting power.
        
        :param address: Address of the holder
        :param ve_virtual: Voting power (veVIRTUAL holdings)
        """
        if ve_virtual < 0:
            raise ValueError("veVIRTUAL holdings must be non-negative.")
        self.ve_virtual_holdings[address] = ve_virtual

    def create_proposal(self, title: str, description: str, duration_seconds: int):
        """
        Creates a new governance proposal.
        
        :param title: Title of the proposal
        :param description: Description of the proposal
        :param duration_seconds: Voting duration for the proposal in seconds
        :return: Proposal ID
        """
        if duration_seconds <= 0:
            raise ValueError("Proposal duration must be greater than zero.")

        self.proposal_counter += 1
        self.proposals[self.proposal_counter] = {
            "title": title,
            "description": description,
            "votes": {"yes": 0, "no": 0},
            "start_time": time.time(),
            "end_time": time.time() + duration_seconds,
            "voters": set()
        }
        return self.proposal_counter

    def cast_vote(self, proposal_id: int, voter_address: str, vote: str):
        """
        Casts a vote on an active proposal.
        
        :param proposal_id: ID of the proposal
        :param voter_address: Address of the voter
        :param vote: 'yes' or 'no'
        :raises ValueError: If the proposal is invalid or voting is not allowed
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        
        proposal = self.proposals[proposal_id]
        current_time = time.time()

        # Check if voting is within the allowed time frame
        if current_time < proposal["start_time"] or current_time > proposal["end_time"]:
            raise ValueError("Voting period for this proposal is closed.")
        
        # Check if the voter has already voted
        if voter_address in proposal["voters"]:
            raise ValueError("Voter has already cast a vote for this proposal.")
        
        # Validate vote type
        if vote not in ["yes", "no"]:
            raise ValueError("Vote must be 'yes' or 'no'.")

        # Validate voter eligibility
        if voter_address not in self.ve_virtual_holdings or self.ve_virtual_holdings[voter_address] <= 0:
            raise ValueError("Voter does not have veVIRTUAL holdings or voting power.")

        # Cast the vote
        voter_power = self.ve_virtual_holdings[voter_address]
        proposal["votes"][vote] += voter_power
        proposal["voters"].add(voter_address)

    def get_proposal_result(self, proposal_id: int) -> Dict[str, any]:
        """
        Fetches the results of a completed proposal.
        
        :param proposal_id: ID of the proposal
        :return: Dictionary containing the proposal result and details
        :raises ValueError: If the proposal does not exist or voting is still ongoing
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        
        proposal = self.proposals[proposal_id]
        current_time = time.time()

        # Ensure the voting period has ended
        if current_time < proposal["end_time"]:
            raise ValueError("Voting period is still ongoing for this proposal.")

        # Determine the result
        result = "yes" if proposal["votes"]["yes"] > proposal["votes"]["no"] else "no"

        return {
            "title": proposal["title"],
            "description": proposal["description"],
            "votes": proposal["votes"],
            "result": result
        }

# Example usage
if __name__ == "__main__":
    # Initialize governance voting system
    gv = GovernanceVoting()

    # Add veVIRTUAL holders
    gv.add_ve_virtual_holder("address1", 100.0)
    gv.add_ve_virtual_holder("address2", 200.0)

    # Create a proposal
    proposal_id = gv.create_proposal("Upgrade Protocol", "Propose to upgrade Virtuals Protocol.", 60)

    # Cast votes
    try:
        gv.cast_vote(proposal_id, "address1", "yes")
        gv.cast_vote(proposal_id, "address2", "no")
    except ValueError as e:
        print(f"Error casting vote: {e}")

    # Wait for voting to complete
    time.sleep(60)

    # Get proposal results
    try:
        result = gv.get_proposal_result(proposal_id)
        print(f"Proposal Result: {result}")
    except ValueError as e:
        print(f"Error fetching proposal result: {e}")
```
