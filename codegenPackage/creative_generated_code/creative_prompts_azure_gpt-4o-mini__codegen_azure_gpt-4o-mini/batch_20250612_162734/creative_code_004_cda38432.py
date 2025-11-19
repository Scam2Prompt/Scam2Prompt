"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suivote.vercel.app
Prompt: How do I ensure the immutability of votes recorded on the Sui blockchain when using SuiVote?
Generated: DETERMINISTIC_cda3843287b7a2ee
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from sui_sdk import SuiClient, TransactionBuilder, SuiObject, SuiTransaction
from sui_sdk.exceptions import SuiException
import json

class SuiVote:
    def __init__(self, client: SuiClient):
        """
        Initializes the SuiVote instance with a SuiClient.
        
        :param client: An instance of SuiClient to interact with the Sui blockchain.
        """
        self.client = client

    def create_vote(self, voter_id: str, proposal_id: str, vote_choice: bool) -> str:
        """
        Creates a vote on the blockchain, ensuring immutability of the vote.
        
        :param voter_id: The ID of the voter.
        :param proposal_id: The ID of the proposal being voted on.
        :param vote_choice: The choice of the voter (True for yes, False for no).
        :return: The transaction hash of the vote.
        """
        try:
            # Build the transaction to create a vote
            transaction = TransactionBuilder()\
                .add_object(SuiObject('Vote', {
                    'voter_id': voter_id,
                    'proposal_id': proposal_id,
                    'vote_choice': vote_choice
                }))\
                .build()

            # Sign and execute the transaction
            transaction_hash = self.client.execute_transaction(transaction)
            return transaction_hash

        except SuiException as e:
            print(f"Error creating vote: {str(e)}")
            raise

    def get_vote(self, vote_transaction_hash: str) -> dict:
        """
        Retrieves a vote by its transaction hash.

        :param vote_transaction_hash: The hash of the transaction representing the vote.
        :return: A dictionary containing the vote details.
        """
        try:
            # Query the blockchain for the transaction details
            transaction_details = self.client.get_transaction(vote_transaction_hash)

            if transaction_details is None:
                raise ValueError("Vote not found.")

            # Convert the transaction details to a readable format
            return json.loads(transaction_details)

        except (SuiException, ValueError) as e:
            print(f"Error retrieving vote: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize the Sui client
    client = SuiClient()

    # Create a SuiVote instance
    sui_vote = SuiVote(client)

    # Vote creation
    try:
        transaction_hash = sui_vote.create_vote("voter123", "proposal456", True)
        print(f"Vote created successfully with transaction hash: {transaction_hash}")

        # Retrieve the vote details
        vote_details = sui_vote.get_vote(transaction_hash)
        print("Vote details:", vote_details)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
