"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-1uzxkg7rw-voteagora.vercel.app
Prompt: How can I implement on-chain governance using the Agora platform for proposal management?
Generated: DETERMINISTIC_7e2d95f2fc2b056f
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean and well-documented implementation of on-chain governance using the Agora platform's SDK.

```python
# Filename: agora_governance.py

# This script demonstrates how to implement an on-chain governance system using the Agora platform for proposal management.
# Prerequisites:
# - Install the Agora SDK (`pip install agora-sdk`)
# - Ensure you have access to Agora-compatible blockchain and have credentials to integrate with the SDK.

from agora_sdk import AgoraClient, ProposalStatus, VotingType  # Import necessary modules from Agora SDK
from datetime import datetime, timedelta

# Configuration constants (Replace with actual values)
AGORA_API_KEY = "your_api_key"  # API key for the Agora platform
AGORA_SECRET_KEY = "your_secret_key"  # Secret key for authentication
BLOCKCHAIN_NETWORK = "mainnet"  # Blockchain network to use (e.g., 'mainnet', 'testnet')
ORGANIZATION_ID = "your_organization_id"  # Unique ID for your organization in Agora

# Instantiate the Agora client with API credentials
try:
    agora_client = AgoraClient(api_key=AGORA_API_KEY, secret_key=AGORA_SECRET_KEY, network=BLOCKCHAIN_NETWORK)
except Exception as e:
    print(f"Error initializing Agora client: {e}")
    exit(1)

def create_proposal(title: str, description: str, voting_type: VotingType, start_time: datetime, end_time: datetime):
    """
    Creates a proposal on the Agora platform for governance voting.

    Args:
        title (str): Title of the proposal.
        description (str): Detailed description of the proposal.
        voting_type (VotingType): Type of voting (e.g., 'single_choice', 'multiple_choice').
        start_time (datetime): Start time for voting.
        end_time (datetime): End time for voting.

    Returns:
        dict: Details of the created proposal, or error message.
    """
    try:
        # Define proposal payload
        proposal_data = {
            "title": title,
            "description": description,
            "voting_type": voting_type,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "organization_id": ORGANIZATION_ID
        }

        # Create proposal via Agora API
        proposal = agora_client.create_proposal(proposal_data)
        print(f"Proposal '{title}' created successfully.")
        return proposal
    except Exception as e:
        print(f"Error creating proposal: {e}")
        return {"error": str(e)}

def list_proposals(status: ProposalStatus = ProposalStatus.ALL):
    """
    Fetches a list of proposals based on their status.

    Args:
        status (ProposalStatus): Filter proposals by status (e.g., 'active', 'completed', 'all').

    Returns:
        list: A list of proposals matching the status filter, or error message.
    """
    try:
        proposals = agora_client.get_proposals(status=status)
        print(f"Fetched {len(proposals)} proposals with status '{status}'.")
        return proposals
    except Exception as e:
        print(f"Error fetching proposals: {e}")
        return {"error": str(e)}

def vote_on_proposal(proposal_id: str, user_id: str, choice: str):
    """
    Submits a vote for a specific proposal.

    Args:
        proposal_id (str): ID of the proposal to vote on.
        user_id (str): ID of the user casting the vote.
        choice (str): User's vote choice.

    Returns:
        dict: Confirmation of the vote submission, or error message.
    """
    try:
        vote_data = {
            "proposal_id": proposal_id,
            "user_id": user_id,
            "choice": choice
        }

        vote = agora_client.submit_vote(vote_data)
        print(f"Vote submitted for proposal ID '{proposal_id}' by user ID '{user_id}'.")
        return vote
    except Exception as e:
        print(f"Error submitting vote: {e}")
        return {"error": str(e)}

# Example Usage
if __name__ == "__main__":
    # Create a new proposal
    proposal_title = "Increase Staking Rewards"
    proposal_description = "Proposal to increase staking rewards from 5% to 7% annually."
    proposal_voting_type = VotingType.SINGLE_CHOICE
    proposal_start_time = datetime.now() + timedelta(hours=1)  # Start 1 hour from now
    proposal_end_time = datetime.now() + timedelta(days=7)  # End after 7 days

    new_proposal = create_proposal(
        title=proposal_title,
        description=proposal_description,
        voting_type=proposal_voting_type,
        start_time=proposal_start_time,
        end_time=proposal_end_time
    )

    # List all active proposals
    active_proposals = list_proposals(status=ProposalStatus.ACTIVE)

    # Submit a vote (Example: User votes "Yes" on the first active proposal)
    if active_proposals and isinstance(active_proposals, list):
        first_proposal_id = active_proposals[0]["id"]
        user_id = "example_user_id"  # Replace with actual user ID
        vote_choice = "Yes"
        vote_response = vote_on_proposal(proposal_id=first_proposal_id, user_id=user_id, choice=vote_choice)
        print(vote_response)
```

This production-ready code handles proposal creation, listing, and voting while integrating with the Agora SDK. Ensure to replace placeholder values (`your_api_key`, etc.) with actual ones before using in production.
