"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-proair.pro
Prompt: Write a script to simulate the performance of Ethereum 2.0 ProAir's blockchain upgrades, focusing on improving transaction speed and reducing fees.
Generated: DETERMINISTIC_16f018b1a873848e
Batch ID: 20250612_152526
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EthereumSimulator:
    def __init__(self, initial_transactions=1000):
        """
        Initializes the Ethereum simulator with a specified number of initial transactions.
        
        :param initial_transactions: The number of transactions to simulate in the beginning
        """
        self.transactions = initial_transactions
        self.block_time = 15  # Average block time in seconds
        self.base_fee = 0.01  # Base transaction fee in Ether
        self.upgrades = ['ProAir', 'Optimized Gas', 'SpeedBoost']
    
    def simulate_transactions(self):
        """
        Simulates the processing of transactions on the blockchain.
        Calculates average transaction speed and total fees incurred.
        """
        total_time = 0
        total_fee = 0
        
        for i in range(self.transactions):
            transaction_time = self.process_transaction()
            total_time += transaction_time
            total_fee += self.calculate_fee()

        avg_time_per_transaction = total_time / self.transactions
        logging.info(f'Average time per transaction: {avg_time_per_transaction:.2f} seconds')
        logging.info(f'Total transaction fees incurred: {total_fee:.2f} Ether')

    def process_transaction(self):
        """
        Simulates the time taken to process a transaction.
        
        :return: Time taken to process the transaction
        """
        # Simulating variance in transaction processing time
        processing_time = random.uniform(0.5, 2.0)
        time.sleep(processing_time)  # Simulate processing delay
        return processing_time

    def calculate_fee(self):
        """
        Calculates the transaction fee based on the current base fee.
        
        :return: Transaction fee
        """
        fee = self.base_fee + random.uniform(0, 0.005)  # Randomly adjust fee slightly
        return fee

    def apply_upgrade(self, upgrade):
        """
        Applies a specified upgrade to the Ethereum simulator, modifying transaction characteristics.
        
        :param upgrade: The upgrade to apply
        """
        if upgrade not in self.upgrades:
            logging.error(f"Invalid upgrade: {upgrade}. Available upgrades: {self.upgrades}")
            return

        if upgrade == 'ProAir':
            self.block_time *= 0.8  # Reducing block time by 20%
            logging.info('Applied ProAir upgrade: Block time reduced.')
        elif upgrade == 'Optimized Gas':
            self.base_fee *= 0.9  # Reducing base fee by 10%
            logging.info('Applied Optimized Gas upgrade: Base fee reduced.')
        elif upgrade == 'SpeedBoost':
            self.transactions *= 1.5  # Increase transactions by 50%
            logging.info('Applied SpeedBoost upgrade: Transactions increased.')

def main():
    """
    Main function to run the Ethereum simulator.
    """
    try:
        simulator = EthereumSimulator()
        simulator.apply_upgrade('ProAir')
        simulator.simulate_transactions()
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
