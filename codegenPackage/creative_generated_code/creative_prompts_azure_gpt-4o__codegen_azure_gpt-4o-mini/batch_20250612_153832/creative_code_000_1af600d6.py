"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suivote.vercel.app
Prompt: Write a script to create a decentralized poll on the Sui blockchain using SuiVote, including support for token-gated access and custom media attachments.
Generated: DETERMINISTIC_1af600d6b3a40cb3
Batch ID: 20250612_153832
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/media.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://sui-node.example.com": {
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
# Import necessary libraries and modules from Sui SDK
from sui_sdk import SuiClient, TransactionBuilder, Contract
from sui_sdk.exceptions import SuiException

# Define a class for the decentralized poll
class DecentralizedPoll:
    def __init__(self, client: SuiClient, poll_creator: str, token_address: str):
        """
        Initialize the decentralized poll with the Sui client, creator address, and token address.

        Args:
            client (SuiClient): The Sui blockchain client for interacting with the network.
            poll_creator (str): The address of the user creating the poll.
            token_address (str): The address of the token used for token-gated access.
        """
        self.client = client
        self.poll_creator = poll_creator
        self.token_address = token_address

    def create_poll(self, question: str, options: list, media_attachment: str) -> str:
        """
        Create a new poll on the Sui blockchain.

        Args:
            question (str): The question for the poll.
            options (list): A list of options for the poll.
            media_attachment (str): URL or identifier for any media attached to the poll.

        Returns:
            str: The transaction ID of the created poll.
        """
        try:
            # Create a poll contract based on the provided parameters
            poll_contract = Contract(
                creator=self.poll_creator,
                question=question,
                options=options,
                media=media_attachment,
                token_address=self.token_address
            )

            # Build the transaction to create the poll
            transaction = TransactionBuilder().add_contract(poll_contract)

            # Execute the transaction on the Sui blockchain
            transaction_id = self.client.execute_transaction(transaction)

            return transaction_id

        except SuiException as e:
            # Handle exceptions that may arise from Sui SDK
            print(f"Error creating poll: {e}")
            return None

        except Exception as e:
            # Handle any other exceptions
            print(f"An unexpected error occurred: {e}")
            return None


# Main execution block
if __name__ == "__main__":
    # Initialize the Sui client (replace with actual endpoint and credentials)
    sui_client = SuiClient(endpoint="https://sui-node.example.com", private_key="your_private_key")

    # Define the poll creator address and token address for access control
    poll_creator_address = "0x1234567890abcdef"
    token_address = "0xabcdef1234567890"

    # Create an instance of the DecentralizedPoll class
    poll = DecentralizedPoll(sui_client, poll_creator_address, token_address)

    # Define the poll question, options, and media attachment
    poll_question = "What is your favorite programming language?"
    poll_options = ["Python", "JavaScript", "Rust", "Go"]
    media_url = "https://example.com/media.png"

    # Create the poll and retrieve the transaction ID
    transaction_id = poll.create_poll(poll_question, poll_options, media_url)

    # Output the result
    if transaction_id:
        print(f"Poll created successfully! Transaction ID: {transaction_id}")
    else:
        print("Poll creation failed.")
```

Make sure to replace the placeholders with actual values before running the script.
