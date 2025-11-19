"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.ghost.io
Prompt: What are the steps to participate in governance for W token holders via the Tally Governance Portal?
Generated: DETERMINISTIC_10be71b87407ddbd
Batch ID: 20250612_135401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://tally.xyz/api/governance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class TallyGovernance:
    """
    A class to represent the Tally Governance Portal for W token holders.
    """

    BASE_URL = "https://tally.xyz/api/governance"

    def __init__(self, wallet_address, token_symbol='W'):
        """
        Initializes the TallyGovernance instance.

        Parameters:
        wallet_address (str): The wallet address of the user.
        token_symbol (str): The symbol of the governance token, default is 'W'.
        """
        self.wallet_address = wallet_address
        self.token_symbol = token_symbol

    def get_governance_proposals(self):
        """
        Fetches the current governance proposals for W token holders.

        Returns:
        list: A list of governance proposals.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/{self.token_symbol}/proposals")
            response.raise_for_status()
            return response.json()  # Returns the JSON response as a Python list/dict
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def vote_on_proposal(self, proposal_id, vote_choice):
        """
        Casts a vote on a given proposal.

        Parameters:
        proposal_id (str): The ID of the proposal to vote on.
        vote_choice (str): The choice of vote ('yes', 'no', 'abstain').

        Returns:
        dict: The response from the vote action.
        """
        payload = {
            'wallet_address': self.wallet_address,
            'proposal_id': proposal_id,
            'vote_choice': vote_choice
        }
        
        try:
            response = requests.post(f"{self.BASE_URL}/{self.token_symbol}/vote", json=payload)
            response.raise_for_status()
            return response.json()  # Returns the JSON response with vote confirmation
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def participate_in_governance(self):
        """
        Main method to participate in governance by fetching proposals and voting.

        This method demonstrates how to use the class methods in a workflow.
        """
        proposals = self.get_governance_proposals()
        if not proposals:
            print("No proposals available for voting.")
            return

        # Example for voting on the first proposal
        first_proposal = proposals[0]
        print(f"Proposal ID: {first_proposal['id']}, Title: {first_proposal['title']}")
        
        # Voting on the first proposal (this is just an example; implement actual logic as needed)
        vote_response = self.vote_on_proposal(first_proposal['id'], 'yes')
        print("Vote response:", vote_response)


# Example of using the TallyGovernance class
if __name__ == "__main__":
    wallet_address = "0xYourWalletAddressHere"  # Replace with actual wallet address
    governance = TallyGovernance(wallet_address)
    governance.participate_in_governance()
```
