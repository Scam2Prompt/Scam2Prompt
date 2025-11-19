"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-git-update-doc-419labs.vercel.app
Prompt: Create a governance smart contract for a project on StarkNet, referencing the ecosystem's unique features.
Generated: DETERMINISTIC_bc77ad4076e4a177
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Governance Smart Contract for StarkNet

# Importing necessary modules and libraries
from starkware.cairo.common.cairo_cairo import Cairo
from starkware.cairo.common.uint256 import Uint256
from starkware.starknet.common.storage import Storage
from starkware.starknet.common.events import Event
from starkware.starknet.business_logic.state import State
from starkware.starknet.business_logic.execution import Execution
from starkware.starknet.business_logic.exceptions import StarkException

# Define the Governance contract
class GovernanceContract:
    def __init__(self):
        self.proposals = {}  # Dictionary to hold proposals
        self.votes = {}      # Dictionary to hold votes by address
        self.owner = self.get_caller_address()  # Store the owner of the contract

    # Function to create a proposal
    def create_proposal(self, proposal_id: int, description: str):
        if proposal_id in self.proposals:
            raise StarkException("Proposal already exists")
        
        self.proposals[proposal_id] = {
            "description": description,
            "vote_count": 0
        }

    # Function to cast a vote on a proposal
    def vote(self, proposal_id: int):
        if proposal_id not in self.proposals:
            raise StarkException("Proposal does not exist")

        caller_address = self.get_caller_address()
        if caller_address in self.votes and self.votes[caller_address] == proposal_id:
            raise StarkException("You have already voted for this proposal")

        self.proposals[proposal_id]["vote_count"] += 1
        self.votes[caller_address] = proposal_id

    # Function to get the results of a proposal
    def get_results(self, proposal_id: int):
        if proposal_id not in self.proposals:
            raise StarkException("Proposal does not exist")

        return {
            "description": self.proposals[proposal_id]["description"],
            "vote_count": self.proposals[proposal_id]["vote_count"]
        }

    # Helper function to get the caller's address (stubbed for this example)
    def get_caller_address(self):
        # In a real contract, this would return the address of the caller
        return "0x1234567890abcdef"

    # Function to retrieve all proposals
    def get_all_proposals(self):
        return self.proposals

# Events for logging actions
class Events:
    @staticmethod
    def proposal_created(proposal_id: int, description: str):
        Event.emit("ProposalCreated", {"proposal_id": proposal_id, "description": description})

    @staticmethod
    def voted(proposal_id: int, voter: str):
        Event.emit("Voted", {"proposal_id": proposal_id, "voter": voter})

# Handling errors in the smart contract
try:
    governance = GovernanceContract()
except Exception as e:
    print(f"Error initializing GovernanceContract: {str(e)}")
```
