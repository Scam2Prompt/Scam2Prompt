"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-mixer.to
Prompt: Write a script to automate the process of splitting large TON transactions into smaller chunks to meet the TON Coin Mixer requirement of a minimum transaction size of 20 TON.
Generated: DETERMINISTIC_ddf8f8b9749f4f32
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def split_transaction(amount: float, min_chunk_size: float = 20.0) -> list:
    """
    Splits a large TON transaction into smaller chunks to meet the TON Coin Mixer requirement.

    Parameters:
        amount (float): Total transaction amount in TON.
        min_chunk_size (float): Minimum allowed size for each chunk (default is 20 TON).

    Returns:
        list: A list of chunks representing the split transaction amounts.
    """
    if amount <= 0:
        raise ValueError("Transaction amount must be greater than 0 TON.")
    if min_chunk_size <= 0:
        raise ValueError("Minimum chunk size must be greater than 0 TON.")
    if amount < min_chunk_size:
        raise ValueError(f"Transaction amount ({amount} TON) is less than the minimum chunk size ({min_chunk_size} TON).")

    # Calculate the number of chunks required
    num_chunks = math.ceil(amount / min_chunk_size)

    # Create the chunks
    chunks = [min_chunk_size] * (num_chunks - 1)
    remaining_amount = amount - sum(chunks)
    chunks.append(remaining_amount)

    return chunks

def main():
    """
    Main function to demonstrate the process of splitting a large TON transaction.
    """
    try:
        # Example: Large transaction amount
        total_amount = 105.0  # Example value (in TON)
        minimum_chunk_size = 20.0  # TON Coin Mixer minimum transaction size

        print(f"Splitting {total_amount} TON into chunks of at least {minimum_chunk_size} TON...")

        chunks = split_transaction(total_amount, minimum_chunk_size)
        print("Transaction has been split into chunks:")
        for i, chunk in enumerate(chunks, 1):
            print(f"  Chunk {i}: {chunk:.2f} TON")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
