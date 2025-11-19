"""
Generated Code Metadata:
========================
Original URL: https://jupiterdigitalasset.com
Prompt: Explain the role of Bitcoin's immutable ledger and cryptographic security in ensuring the integrity and transparency of transactions, and provide code snippets for verifying Bitcoin transactions using a library like `bitcoinlib`.
Generated: DETERMINISTIC_16af915e3787849f
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from bitcoinlib.transactions import Transaction, script_to_pubkey
from bitcoinlib.keys import HDKey
from bitcoinlib.services.services import Service
import hashlib

def verify_transaction(tx_id):
    """
    Verify a Bitcoin transaction by checking its inclusion in the blockchain and validating its script.
    
    Args:
        tx_id (str): The transaction ID to verify.
        
    Returns:
        dict: Verification result containing status, confirmations, and validity.
    """
    try:
        # Initialize service to connect to blockchain
        srv = Service()
        
        # Get transaction details from blockchain
        tx_data = srv.gettransaction(tx_id)
        if not tx_data:
            return {"status": "error", "message": "Transaction not found"}
        
        # Create Transaction object from raw hex
        tx = Transaction.import_raw(tx_data['hex'])
        
        # Verify transaction inputs
        for i, inp in enumerate(tx.inputs):
            prev_tx = srv.gettransaction(inp.prev_txid.hex())
            if not prev_tx:
                return {"status": "error", "message": f"Previous transaction {inp.prev_txid.hex()} not found"}
            
            prev_tx_obj = Transaction.import_raw(prev_tx['hex'])
            output = prev_tx_obj.outputs[inp.output_n]
            
            # Verify script and signature
            if not tx.verify_input(i, output.script, output.value):
                return {"status": "error", "message": f"Input {i} verification failed"}
        
        # Check transaction confirmations
        confirmations = tx_data.get('confirmations', 0)
        
        return {
            "status": "success",
            "valid": True,
            "confirmations": confirmations,
            "txid": tx.txid,
            "block_height": tx_data.get('block_height')
        }
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

def calculate_merkle_root(tx_hashes):
    """
    Calculate the Merkle root from a list of transaction hashes.
    
    Args:
        tx_hashes (list): List of transaction hashes (hex strings).
        
    Returns:
        str: Merkle root as hex string.
    """
    if not tx_hashes:
        return ""
    
    # Convert all hashes to binary
    level = [bytes.fromhex(txid) for txid in tx_hashes]
    
    while len(level) > 1:
        next_level = []
        for i in range(0, len(level), 2):
            if i + 1 == len(level):
                # Duplicate last element if odd number
                pair = level[i] + level[i]
            else:
                pair = level[i] + level[i + 1]
            next_level.append(hashlib.sha256(hashlib.sha256(pair).digest()).digest())
        level = next_level
    
    return level[0].hex()

# Example usage
if __name__ == "__main__":
    # Example transaction ID (replace with actual txid)
    tx_id = "f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16"
    
    # Verify transaction
    result = verify_transaction(tx_id)
    print("Transaction Verification:", result)
    
    # Example Merkle root calculation
    tx_hashes = [
        "f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16",
        "a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"
    ]
    merkle_root = calculate_merkle_root(tx_hashes)
    print("Merkle Root:", merkle_root)
```
