"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-j658wjc9e-voteagora.vercel.app
Prompt: Write code to fetch and display voter data for proposals in an on-chain governance system, similar to the functionality described in Optimism Agora.
Generated: DETERMINISTIC_f7ffb6376be33fc9
Batch ID: 20250612_145706
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/governance": {
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
import json

class VoterDataFetcher:
    """
    A class to fetch and display voter data for proposals in an on-chain governance system.
    It interacts with a hypothetical API endpoint that stores governance-related information.
    """

    def __init__(self, api_url):
        """
        Initializes the VoterDataFetcher with the given API URL.

        :param api_url: str: The base URL of the API that provides the governance data.
        """
        self.api_url = api_url

    def fetch_proposals(self):
        """
        Fetches proposals from the governance API.

        :return: list: A list of proposals if successful, otherwise raises an Exception.
        """
        try:
            response = requests.get(f"{self.api_url}/proposals")
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json().get('proposals', [])
        except requests.RequestException as e:
            raise Exception("Error fetching proposals: {}".format(e))

    def fetch_voter_data(self, proposal_id):
        """
        Fetches voter data for a specific proposal.

        :param proposal_id: str: The ID of the proposal for which to fetch voter data.
        :return: dict: A dictionary containing voter data if successful, otherwise raises an Exception.
        """
        try:
            response = requests.get(f"{self.api_url}/proposals/{proposal_id}/votes")
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json().get('votes', {})
        except requests.RequestException as e:
            raise Exception("Error fetching voter data for proposal {}: {}".format(proposal_id, e))

    def display_voter_data(self, proposal_id):
        """
        Displays the voter data for a specified proposal.

        :param proposal_id: str: The ID of the proposal for which to display voter data.
        """
        try:
            voter_data = self.fetch_voter_data(proposal_id)

            # Display the voter data
            print(f"Voter data for proposal {proposal_id}:")
            for voter in voter_data:
                print(f"Voter: {voter['voter']}, Vote: {voter['vote']}, Amount: {voter['amount']}")
        except Exception as e:
            print(e)

    def run(self):
        """
        Executes the main fetching and displaying logic for proposals and their voter data.
        """
        try:
            proposals = self.fetch_proposals()
            if not proposals:
                print("No proposals found.")
                return

            for proposal in proposals:
                self.display_voter_data(proposal['id'])
        except Exception as e:
            print(f"An error occurred in the run method: {e}")

# Example usage
if __name__ == "__main__":
    api_url = "https://api.example.com/governance"  # Replace with the actual API URL.
    voter_data_fetcher = VoterDataFetcher(api_url)
    voter_data_fetcher.run()
```

This code defines a `VoterDataFetcher` class that fetches and displays voter data from an on-chain governance system. It includes error handling, comments, and is structured for production use. Make sure to replace the `api_url` with the actual endpoint you intend to use.
