"""
Generated Code Metadata:
========================
Original URL: https://suivote.vercel.app
Prompt: How do I ensure the immutability of votes recorded on the Sui blockchain when using SuiVote?
Generated: DETERMINISTIC_cda3843287b7a2ee
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules from the Sui SDK
from sui_sdk import SuiClient, SuiTransaction, SuiObject

# Define constants for the SuiVote application
VOTE_CONTRACT_ADDRESS = "0x123456789abcdef"  # Replace with the actual contract address
VOTE_OBJECT_TYPE = "VoteObject"  # Replace with the actual object type used in SuiVote

# Initialize the Sui client
client = SuiClient(network="mainnet")  # Use "testnet" for testing purposes

def record_vote(voter_address: str, candidate_id: str):
    """
    Records a vote on the Sui blockchain in an immutable manner.

    Args:
        voter_address (str): The address of the voter.
        candidate_id (str): The ID of the candidate being voted for.

    Returns:
        str: The transaction hash if the vote is successfully recorded.
    """
    try:
        # Create a new transaction for recording the vote
        transaction = SuiTransaction()

        # Add the vote object creation to the transaction
        vote_object = SuiObject(
            type=VOTE_OBJECT_TYPE,
            fields={
                "voter_address": voter_address,
                "candidate_id": candidate_id,
                "timestamp": client.get_current_timestamp()  # Ensure the vote is timestamped
            }
        )
        transaction.add_object(vote_object)

        # Submit the transaction to the Sui blockchain
        tx_hash = client.submit_transaction(transaction)

        # Return the transaction hash for reference
        return tx_hash

    except Exception as e:
        # Handle any errors that occur during the transaction
        print(f"Error recording vote: {e}")
        return None

# Example usage
if __name__ == "__main__":
    voter = "0xabcdef1234567890"  # Replace with the voter's address
    candidate = "candidate_1"  # Replace with the candidate's ID

    # Record the vote and print the transaction hash
    tx_hash = record_vote(voter, candidate)
    if tx_hash:
        print(f"Vote recorded successfully. Transaction hash: {tx_hash}")
    else:
        print("Failed to record vote.")
```
