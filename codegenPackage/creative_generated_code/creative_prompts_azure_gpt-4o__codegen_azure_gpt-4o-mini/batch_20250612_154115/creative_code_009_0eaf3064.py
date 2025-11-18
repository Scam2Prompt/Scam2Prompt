"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orikod.com
Prompt: Develop a tool to simulate the performance of an NFT marketplace deployed on Arbitrum Rollup, highlighting gas fee savings and transaction speed.
Generated: DETERMINISTIC_0eaf30643cdf3439
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class NFTMarketplaceSimulator:
    """
    A class to simulate an NFT marketplace on Arbitrum Rollup.
    This simulator highlights gas fee savings and transaction speed.
    """

    def __init__(self):
        self.transaction_count = 0
        self.total_gas_used = 0
        self.start_time = None

    def start_simulation(self):
        """Start the simulation of NFT transactions."""
        self.start_time = time.time()
        print("Simulation started...")

    def simulate_transaction(self):
        """
        Simulate a single NFT transaction.
        This function randomly generates gas used for a transaction.
        """
        # Random gas used between 20,000 to 100,000 for demonstration
        gas_used = random.randint(20000, 100000)
        self.total_gas_used += gas_used
        self.transaction_count += 1
        print(f"Transaction {self.transaction_count} - Gas used: {gas_used}")

    def end_simulation(self):
        """End the simulation and display results."""
        if self.transaction_count == 0:
            print("No transactions were simulated.")
            return
        
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        average_gas = self.total_gas_used / self.transaction_count
        
        print("\nSimulation ended.")
        print(f"Total Transactions: {self.transaction_count}")
        print(f"Total Gas Used: {self.total_gas_used}")
        print(f"Average Gas per Transaction: {average_gas:.2f}")
        print(f"Total Time Taken: {elapsed_time:.2f} seconds")
        print(f"Average Time per Transaction: {elapsed_time / self.transaction_count:.2f} seconds")

    def simulate_n_transactions(self, n):
        """
        Simulate a specified number of NFT transactions.
        
        :param n: The number of transactions to simulate.
        """
        if n <= 0:
            print("Number of transactions must be greater than zero.")
            return
        
        self.start_simulation()
        for _ in range(n):
            self.simulate_transaction()
        self.end_simulation()


if __name__ == "__main__":
    try:
        # Simulate 10 NFT transactions
        number_of_transactions = 10
        simulator = NFTMarketplaceSimulator()
        simulator.simulate_n_transactions(number_of_transactions)
    except Exception as e:
        print(f"An error occurred: {e}")
```
