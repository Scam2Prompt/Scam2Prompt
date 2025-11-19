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

def create_voting_proposal(title, description, options, start_time, end_time, creator_address):
    """
    Creates a voting proposal for IQ Token holders.

    Args:
        title (str): The title of the proposal.
        description (str): A detailed description of the proposal.
        options (list): A list of voting options (e.g., ["Yes", "No", "Abstain"]).
        start_time (datetime): The start time of the voting period.
        end_time (datetime): The end time of the voting period.
        creator_address (str): The wallet address of the proposal creator.

    Returns:
        dict: A JSON-compatible dictionary representing the proposal.
    """
    # Validate inputs
    if not title or not description or not options or not creator_address:
        raise ValueError("Title, description, options, and creator address are required.")
    if not isinstance(options, list) or len(options) < 2:
        raise ValueError("Options must be a list with at least two items.")
    if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
        raise ValueError("Start and end times must be valid datetime objects.")
    if start_time >= end_time:
        raise ValueError("Start time must be earlier than end time.")

    # Construct the proposal payload
    proposal = {
        "title": title,
        "description": description,
        "options": options,
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
        "creator_address": creator_address,
        "created_at": datetime.utcnow().isoformat(),
    }

    return proposal


# Example usage
if __name__ == "__main__":
    try:
        # Define proposal details
        proposal_title = "Increase Staking Rewards"
        proposal_description = (
            "This proposal suggests increasing the staking rewards for IQ Token holders "
            "from 5% to 7% annually to incentivize long-term holding."
        )
        voting_options = ["Yes", "No", "Abstain"]
        proposal_start_time = datetime.utcnow() + timedelta(days=1)  # Voting starts in 1 day
        proposal_end_time = proposal_start_time + timedelta(days=7)  # Voting lasts for 7 days
        creator_wallet_address = "0x1234567890abcdef1234567890abcdef12345678"

        # Create the proposal
        proposal_payload = create_voting_proposal(
            title=proposal_title,
            description=proposal_description,
            options=voting_options,
            start_time=proposal_start_time,
            end_time=proposal_end_time,
            creator_address=creator_wallet_address,
        )

        # Convert the proposal to JSON format
        proposal_json = json.dumps(proposal_payload, indent=4)

        # Print the JSON payload
        print("Generated Proposal JSON Payload:")
        print(proposal_json)

    except Exception as e:
        print(f"Error creating proposal: {e}")
```

### Sample JSON Payload Output:
```json
{
    "title": "Increase Staking Rewards",
    "description": "This proposal suggests increasing the staking rewards for IQ Token holders from 5% to 7% annually to incentivize long-term holding.",
    "options": [
        "Yes",
        "No",
        "Abstain"
    ],
    "start_time": "2023-10-11T12:00:00Z",
    "end_time": "2023-10-18T12:00:00Z",
    "creator_address": "0x1234567890abcdef1234567890abcdef12345678",
    "created_at": "2023-10-10T12:00:00Z"
}
```
