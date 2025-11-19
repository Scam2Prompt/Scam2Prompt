"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexus-mutual.xyz
Prompt: Explain how to create a decentralized claims assessment process similar to Nexus Mutual's, utilizing community voting.
Generated: DETERMINISTIC_d3820b9948fb7e3c
Batch ID: 20250612_155956
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Union

class ClaimsAssessment:
    """
    A class to manage decentralized claims assessment by the community.
    """

    def __init__(self):
        # Store all claims submitted
        self.claims = {}
        # Store votes for each claim
        self.votes = {}
        # Store results of each claim's assessment
        self.results = {}

    def submit_claim(self, claim_id: str, details: Dict[str, Union[str, float, datetime]]) -> None:
        """
        Submit a new claim for assessment.
        
        Args:
            claim_id (str): Unique ID for the claim.
            details (dict): Information about the claim (e.g., description, requested payout, etc.).
            
        Raises:
            ValueError: If the claim_id already exists.
        """
        if claim_id in self.claims:
            raise ValueError(f"Claim ID {claim_id} already exists.")
        
        self.claims[claim_id] = details
        self.votes[claim_id] = {"approve": 0, "deny": 0}
        print(f"Claim {claim_id} submitted successfully.")

    def vote_on_claim(self, claim_id: str, vote: str, voter_id: str) -> None:
        """
        Vote on an existing claim.
        
        Args:
            claim_id (str): ID of the claim to vote on.
            vote (str): Can be either 'approve' or 'deny'.
            voter_id (str): Unique ID for the voter.
            
        Raises:
            ValueError: If the claim does not exist or the vote is invalid.
        """
        if claim_id not in self.claims:
            raise ValueError(f"Claim ID {claim_id} does not exist.")
        
        if vote not in ["approve", "deny"]:
            raise ValueError("Invalid vote. Vote must be 'approve' or 'deny'.")
        
        voter_key = f"{claim_id}_{voter_id}"
        if voter_key in self.votes[claim_id]:
            raise ValueError(f"Voter {voter_id} has already voted on claim {claim_id}.")
        
        # Record the vote
        self.votes[claim_id][vote] += 1
        # Store voter key to prevent duplicate voting
        self.votes[claim_id][voter_key] = True
        print(f"Vote recorded: {vote} on claim {claim_id} by voter {voter_id}.")

    def finalize_claim(self, claim_id: str) -> None:
        """
        Finalize the claim based on community voting.
        
        Args:
            claim_id (str): ID of the claim to finalize.
            
        Raises:
            ValueError: If the claim does not exist or is already finalized.
        """
        if claim_id not in self.claims:
            raise ValueError(f"Claim ID {claim_id} does not exist.")
        
        if claim_id in self.results:
            raise ValueError(f"Claim ID {claim_id} has already been finalized.")
        
        # Determine the outcome based on votes
        approve_votes = self.votes[claim_id]["approve"]
        deny_votes = self.votes[claim_id]["deny"]
        if approve_votes > deny_votes:
            result = "approved"
        else:
            result = "denied"
        
        self.results[claim_id] = {
            "result": result,
            "approve_votes": approve_votes,
            "deny_votes": deny_votes,
            "finalized_at": datetime.utcnow()
        }
        
        print(f"Claim {claim_id} finalized. Result: {result}.")

    def export_results(self) -> str:
        """
        Export finalized claim results as a JSON string.
        
        Returns:
            str: JSON string containing finalized claim results.
        """
        return json.dumps(self.results, default=str, indent=4)


# Example usage:

if __name__ == "__main__":
    # Create an instance of the ClaimsAssessment system
    claims_system = ClaimsAssessment()

    # Submit a new claim
    claims_system.submit_claim("claim_001", {
        "description": "Car accident",
        "requested_payout": 5000.0,
        "date": datetime(2023, 10, 1)
    })

    # Community voting
    claims_system.vote_on_claim("claim_001", "approve", "voter_001")
    claims_system.vote_on_claim("claim_001", "deny", "voter_002")
    claims_system.vote_on_claim("claim_001", "approve", "voter_003")

    # Finalize the claim based on votes
    claims_system.finalize_claim("claim_001")

    # Export the results
    print(claims_system.export_results())
```
