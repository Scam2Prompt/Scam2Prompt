"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fixsynchweb3.pages.dev
Prompt: Create a function to handle transaction delays, utilizing the troubleshooting steps from the FixSynch web3 content.
Generated: DETERMINISTIC_a1123eb5732f05d8
Batch ID: 20250612_164217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from web3.exceptions import TransactionNotFound, TimeExhausted

def wait_for_transaction_receipt(web3, tx_hash, timeout=120, poll_interval=5):
    """
    Wait for a transaction receipt with proper handling for delays.
    
    Args:
        web3 (Web3): An instance of Web3.
        tx_hash (str): The transaction hash to wait for.
        timeout (int): Maximum time (in seconds) to wait for the receipt.
        poll_interval (int): Time interval (in seconds) between receipt checks.
    
    Returns:
        dict: The transaction receipt if found.
    
    Raises:
        RuntimeError: If the transaction receipt is not found within the timeout period.
    """
    start_time = time.time()
    
    while True:
        try:
            # Try to fetch the transaction receipt
            receipt = web3.eth.get_transaction_receipt(tx_hash)
            if receipt:
                return receipt  # Return the receipt if found
        except TransactionNotFound:
            # Handle case where the transaction is not yet mined
            pass
        
        # Check if timeout has been exceeded
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            raise RuntimeError(
                f"Transaction receipt for hash {tx_hash} not found within {timeout} seconds."
            )
        
        # Sleep before the next poll
        time.sleep(poll_interval)
```

This code assumes you have a properly initialized `web3` instance and a valid transaction hash (`tx_hash`).
