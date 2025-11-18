"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards.cow-ai.world
Prompt: Create a script that interacts with the CoW DAO governance system, allowing token holders to submit proposals and vote via Snapshot.
Generated: DETERMINISTIC_990f11b5feae8ab6
Batch ID: 20250612_155015
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://hub.snapshot.org/graphql": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a Python script that uses the Snapshot API to interact with the governance system for submitting proposals and voting. Please ensure you have access to the Snapshot space and an appropriate Ethereum wallet with signing capabilities before running the script.

```python
import json
import requests
from web3 import Web3
from eth_account.messages import encode_defunct

# Constants for Snapshot API and Ethereum
SNAPSHOT_API_URL = "https://hub.snapshot.org/graphql"
SPACE_ID = "cow.eth"  # Replace with the actual space ID for the CoW DAO
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Replace with your wallet's private key

# Initialize a Web3 instance
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum network. Check your Infura configuration.")

# Helper function to generate a signed message
def sign_message(message: str, private_key: str) -> str:
    try:
        # Encode and sign the message
        message_encoded = encode_defunct(text=message)
        signed_message = web3.eth.account.sign_message(message_encoded, private_key)
        return signed_message.signature.hex()
    except Exception as e:
        raise ValueError(f"Error signing message: {str(e)}")

# Function to submit a proposal
def submit_proposal(title: str, body: str, choices: list, start: int, end: int, private_key: str):
    try:
        # Prepare the payload for the proposal
        payload = {
            "space": SPACE_ID,
            "type": "single-choice",
            "title": title,
            "body": body,
            "choices": choices,
            "start": start,
            "end": end,
            "snapshot": web3.eth.block_number,
        }

        # Convert the payload to JSON string for signing
        message = json.dumps(payload)
        signature = sign_message(message, private_key)

        # Prepare the GraphQL mutation
        query = """
        mutation ($proposal: ProposalInput!) {
            propose(proposal: $proposal) {
                id
            }
        }
        """
        variables = {"proposal": {**payload, "signature": signature}}

        # Send request to Snapshot API
        response = requests.post(SNAPSHOT_API_URL, json={"query": query, "variables": variables})
        response_data = response.json()

        # Check for errors
        if "errors" in response_data:
            raise ValueError(f"Snapshot API error: {response_data['errors']}")

        proposal_id = response_data["data"]["propose"]["id"]
        print(f"Proposal submitted successfully. Proposal ID: {proposal_id}")
    except Exception as e:
        print(f"Error submitting proposal: {str(e)}")

# Function to vote on a proposal
def vote_on_proposal(proposal_id: str, choice_index: int, private_key: str):
    try:
        # Prepare the payload for the vote
        payload = {
            "space": SPACE_ID,
            "proposal": proposal_id,
            "choice": choice_index,
            "snapshot": web3.eth.block_number,
        }

        # Convert the payload to JSON string for signing
        message = json.dumps(payload)
        signature = sign_message(message, private_key)

        # Prepare the GraphQL mutation
        query = """
        mutation ($vote: VoteInput!) {
            vote(vote: $vote) {
                id
            }
        }
        """
        variables = {"vote": {**payload, "signature": signature}}

        # Send request to Snapshot API
        response = requests.post(SNAPSHOT_API_URL, json={"query": query, "variables": variables})
        response_data = response.json()

        # Check for errors
        if "errors" in response_data:
            raise ValueError(f"Snapshot API error: {response_data['errors']}")

        vote_id = response_data["data"]["vote"]["id"]
        print(f"Vote submitted successfully. Vote ID: {vote_id}")
    except Exception as e:
        print(f"Error submitting vote: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Submit a proposal
    submit_proposal(
        title="Example Proposal",
        body="This is a proposal to improve the governance system.",
        choices=["Yes", "No"],
        start=1680000000,  # Example timestamp
        end=1680100000,  # Example timestamp
        private_key=PRIVATE_KEY,
    )

    # Vote on a proposal
    vote_on_proposal(
        proposal_id="example-proposal-id",  # Replace with a real proposal ID
        choice_index=1,  # Choice index starts at 1
        private_key=PRIVATE_KEY,
    )
```

### Notes:
- Replace `YOUR_INFURA_PROJECT_ID` and `YOUR_PRIVATE_KEY` with your actual credentials.
- Ensure the timestamps (`start` and `end`) for proposals are in Unix epoch format.
- The `proposal_id` must be replaced with the actual ID of an active proposal.
- Ensure proper permission and access to the Snapshot space.
