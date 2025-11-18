"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkbridge.pages.dev
Prompt: Provide an example of batching multiple transaction verifications into a single zero-knowledge proof using zkBridge's zkLightClient.
Generated: DETERMINISTIC_0b8179a52c2a659c
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import zkbridge
from zkbridge import zkLightClient, Transaction, ZeroKnowledgeProof

def batch_verify_transactions(transactions):
    """
    Verifies multiple transactions using a single zero-knowledge proof.

    Args:
        transactions (list of Transaction): A list of transactions to be verified.

    Returns:
        ZeroKnowledgeProof: The proof object if verification is successful, otherwise raises an error.
    
    Raises:
        ValueError: If the input transactions list is empty.
        Exception: For any other errors during the verification process.
    """
    
    # Validate input
    if not transactions:
        raise ValueError("The transactions list cannot be empty.")
    
    # Initialize the zkLightClient
    client = zkLightClient()

    try:
        # Create a batch of transactions to be processed
        batch = client.create_transaction_batch(transactions)
        
        # Generate a zero-knowledge proof for the transaction batch
        proof = client.generate_proof(batch)

        # Return the generated proof
        return proof

    except Exception as e:
        # Log the exception or handle it appropriately
        print(f"Error during batch verification: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    # Sample transactions (assuming Transaction is a valid class)
    transactions = [
        Transaction(id="tx1", data="transaction_data_1"),
        Transaction(id="tx2", data="transaction_data_2"),
        Transaction(id="tx3", data="transaction_data_3"),
    ]
    
    try:
        # Batch verify the transactions
        proof = batch_verify_transactions(transactions)
        print("Batch verification successful. Proof:", proof)
    except Exception as e:
        print("Batch verification failed:", str(e))
```
