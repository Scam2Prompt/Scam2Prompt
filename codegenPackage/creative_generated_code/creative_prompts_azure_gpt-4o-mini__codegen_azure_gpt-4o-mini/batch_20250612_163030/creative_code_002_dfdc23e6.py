"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upshift.fi
Prompt: What are the steps to vote on Upshift Finance's rewards proposal and how does it impact yield generation?
Generated: DETERMINISTIC_dfdc23e6179234d1
Batch ID: 20250612_163030
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.upshift.finance": {
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
from requests.exceptions import HTTPError

class UpshiftFinanceVoting:
    def __init__(self, api_url):
        """
        Initialize the UpshiftFinanceVoting class with the API URL.
        
        :param api_url: The base URL for the Upshift Finance API
        """
        self.api_url = api_url

    def fetch_proposals(self):
        """
        Fetch the current proposals from the Upshift Finance API.

        :return: List of proposals or an empty list if an error occurs.
        """
        try:
            response = requests.get(f"{self.api_url}/proposals")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming the response is in JSON format
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
        return []  # Return an empty list on failure

    def vote_on_proposal(self, proposal_id, user_id, vote):
        """
        Submit a vote for a specific proposal.
        
        :param proposal_id: The ID of the proposal to vote on
        :param user_id: The ID of the user submitting the vote
        :param vote: The vote value (e.g., "yes" or "no")
        :return: Response message from the API or an error message
        """
        payload = {
            "user_id": user_id,
            "vote": vote
        }
        
        try:
            response = requests.post(f"{self.api_url}/proposals/{proposal_id}/vote", json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return API response on success
        except HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"  # Log HTTP errors and return message
        except Exception as err:
            return f"An error occurred: {err}"  # Log other errors and return message

# Example usage of the UpshiftFinanceVoting class
if __name__ == "__main__":
    api_url = "https://api.upshift.finance"  # Example API URL
    voting_system = UpshiftFinanceVoting(api_url)
    
    # Fetch proposals
    proposals = voting_system.fetch_proposals()
    if proposals:
        print("Current Proposals:")
        for proposal in proposals:
            print(f"ID: {proposal['id']}, Title: {proposal['title']}")
        
        # Example voting on a proposal
        proposal_id = proposals[0]['id']  # Vote on the first proposal
        user_id = "user123"  # Example user ID
        vote = "yes"  # Example vote choice
        result = voting_system.vote_on_proposal(proposal_id, user_id, vote)
        print("Vote Result:", result)
    else:
        print("No proposals available or an error occurred.")
```
