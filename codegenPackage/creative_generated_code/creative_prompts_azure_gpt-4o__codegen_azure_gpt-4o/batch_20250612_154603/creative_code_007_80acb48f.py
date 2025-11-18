"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tslaspacetrade.com
Prompt: Write a Python script to simulate the computational problem-solving process used by cryptocurrency miners to secure blockchain transactions, as described on Tslaspacetrade's website.
Generated: DETERMINISTIC_80acb48fe1fe8260
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time

def calculate_hash(block_data, nonce):
    """
    Calculate SHA-256 hash for the given block data and nonce.
    
    Args:
        block_data (str): The block data to hash (transaction details, previous hash, etc.).
        nonce (int): The nonce value used in the hashing process.

    Returns:
        str: The resulting hash as a hexadecimal string.
    """
    data_to_hash = f"{block_data}{nonce}"
    return hashlib.sha256(data_to_hash.encode('utf-8')).hexdigest()

def mine_block(block_data, difficulty):
    """
    Simulates the mining process to find a valid hash for a block.
    A valid hash must start with a specific number of zeros defined by the difficulty.

    Args:
        block_data (str): The block data to hash (transaction details, previous hash, etc.).
        difficulty (int): The number of leading zeros required in the hash.

    Returns:
        tuple: The valid hash and the nonce value that produced it.
    """
    # The target prefix is a string of leading zeros equal to the difficulty
    target_prefix = '0' * difficulty
    nonce = 0
    
    while True:
        # Compute the hash with the current nonce
        current_hash = calculate_hash(block_data, nonce)
        
        # Check if the hash satisfies the difficulty criteria
        if current_hash.startswith(target_prefix):
            return current_hash, nonce
        
        # Increment nonce and continue searching for the valid hash
        nonce += 1

def main():
    """
    Main entry point for the mining simulation script.
    Creates a sample block, mines it, and outputs the results.
    """
    # Simulated block data (e.g., transaction details, previous block hash)
    block_data = "Transaction: Alice pays Bob 5 BTC | PreviousHash: 000000abcdef1234567890"
    
    # Define mining difficulty (number of leading zeros required)
    difficulty = 4  # Increase this value for higher difficulty
    
    # Log start time for performance measurement
    print("Starting mining process...")
    start_time = time.time()
    
    try:
        # Perform the mining process
        mined_hash, nonce = mine_block(block_data, difficulty)
        
        # Log mining results
        elapsed_time = time.time() - start_time
        print(f"Mining successful!")
        print(f"Block Data: {block_data}")
        print(f"Valid Hash: {mined_hash}")
        print(f"Nonce: {nonce}")
        print(f"Elapsed Time: {elapsed_time:.2f} seconds")
    except Exception as e:
        # Handle any unexpected errors during mining
        print(f"An error occurred during mining: {e}")

if __name__ == "__main__":
    main()
```
