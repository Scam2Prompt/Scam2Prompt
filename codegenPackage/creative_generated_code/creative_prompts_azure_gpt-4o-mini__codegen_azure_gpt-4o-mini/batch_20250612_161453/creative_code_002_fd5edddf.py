"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorodshansona.ru
Prompt: Generate a code snippet that demonstrates how to use the IMX token for voting on protocol developments within the Immutable X ecosystem.
Generated: DETERMINISTIC_fd5edddf9f5e3a52
Batch ID: 20250612_161453
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.immutable.com/v1": {
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

class ImmutableX:
    BASE_URL = "https://api.immutable.com/v1"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_votes(self):
        """
        Retrieve the current voting data from the Immutable X ecosystem.
        Returns a list of votes or raises an error if the request fails.
        """
        url = f"{self.BASE_URL}/votes"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def vote_on_proposal(self, proposal_id, vote_value):
        """
        Cast a vote on a specific proposal within the Immutable X ecosystem.
        
        :param proposal_id: The ID of the proposal to vote on.
        :param vote_value: The value of the vote (e.g., 'YES' or 'NO').
        :raises ValueError: If the vote_value is not valid.
        :raises Exception: If the vote cannot be cast due to an error.
        """
        valid_votes = ['YES', 'NO']
        if vote_value not in valid_votes:
            raise ValueError(f"Invalid vote value. Choose from {valid_votes}.")

        url = f"{self.BASE_URL}/votes"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"proposal_id": proposal_id, "vote_value": vote_value}

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    imx = ImmutableX(API_KEY)

    # Fetch and print current votes
    print(imx.get_votes())

    # Cast a vote on a proposal (example usage)
    try:
        proposal_id = "12345"  # Replace with a valid proposal ID
        vote_value = "YES"  # Choose either 'YES' or 'NO'
        response = imx.vote_on_proposal(proposal_id, vote_value)
        print("Vote cast successfully:", response)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("Failed to cast vote:", e)
```
