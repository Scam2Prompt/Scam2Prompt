"""
Generated Code Metadata:
========================
Original URL: https://soniclaqs.com
Prompt: "Compare the transaction speeds of Sonic and Ethereum, highlighting Sonic's real sub-second confirmation times and 400k TPS capabilities."
Generated: DETERMINISTIC_f84dbd466ae87755
Batch ID: 20250622_210054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time

class Blockchain:
    """
    A base class representing a generic blockchain.
    """
    def __init__(self, name, tps, confirmation_time):
        """
        Initialize the blockchain with its name, transactions per second (TPS),
        and average confirmation time.
        """
        self.name = name
        self.tps = tps
        self.confirmation_time = confirmation_time

    def simulate_transaction(self):
        """
        Simulate a transaction and measure the time taken for confirmation.
        """
        start_time = time.time()
        time.sleep(self.confirmation_time)  # Simulate confirmation delay
        end_time = time.time()
        return end_time - start_time


def compare_blockchains(blockchain1, blockchain2):
    """
    Compare two blockchains based on their transaction speeds and confirmation times.

    Args:
        blockchain1 (Blockchain): The first blockchain to compare.
        blockchain2 (Blockchain): The second blockchain to compare.

    Returns:
        dict: A dictionary containing the comparison results.
    """
    results = {}

    # Simulate a transaction for each blockchain
    results[blockchain1.name] = {
        "TPS": blockchain1.tps,
        "Confirmation Time (s)": blockchain1.simulate_transaction()
    }
    results[blockchain2.name] = {
        "TPS": blockchain2.tps,
        "Confirmation Time (s)": blockchain2.simulate_transaction()
    }

    return results


def main():
    """
    Main function to compare Sonic and Ethereum blockchains.
    """
    try:
        # Define the blockchains
        sonic = Blockchain(name="Sonic", tps=400000, confirmation_time=0.001)  # Sub-second confirmation
        ethereum = Blockchain(name="Ethereum", tps=30, confirmation_time=15)  # Average confirmation time of 15 seconds

        # Compare the blockchains
        comparison_results = compare_blockchains(sonic, ethereum)

        # Display the results
        print("Blockchain Comparison Results:")
        for blockchain, metrics in comparison_results.items():
            print(f"\n{blockchain}:")
            for metric, value in metrics.items():
                print(f"  {metric}: {value}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
