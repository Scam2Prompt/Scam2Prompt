"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-buck.pages.dev
Prompt: Create a Python program to simulate CoinBuck's cost-effective marketing analysis using group transaction tagging features.
Generated: DETERMINISTIC_9bb12477aa2635b5
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from datetime import datetime
from collections import defaultdict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Transaction:
    """
    Class to represent a transaction in the CoinBuck marketing analysis.
    Each transaction has a unique ID, amount, and a list of tags associated with it.
    """
    def __init__(self, transaction_id: int, amount: float, tags: list):
        self.transaction_id = transaction_id
        self.amount = amount
        self.tags = tags
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"Transaction(ID: {self.transaction_id}, Amount: {self.amount}, Tags: {self.tags})"


class MarketingAnalysis:
    """
    Class to analyze transactions for cost-effective marketing strategies.
    It groups transactions by tags and computes total amounts for each group.
    """
    def __init__(self):
        self.transactions = []
        self.tagged_groups = defaultdict(float)

    def add_transaction(self, transaction: Transaction):
        """
        Add a transaction to the analysis.
        
        :param transaction: An instance of the Transaction class to be added.
        """
        self.transactions.append(transaction)

        # Group transactions by tags and accumulate their amounts
        for tag in transaction.tags:
            self.tagged_groups[tag] += transaction.amount

        logging.info(f"Transaction added: {transaction}")

    def get_grouped_analysis(self):
        """
        Get a summary of total amounts grouped by tags.
        
        :return: A dictionary with tags as keys and total amounts as values.
        """
        return dict(self.tagged_groups)

    def simulate_transactions(self, num_transactions: int):
        """
        Simulate a number of random transactions for testing the analysis.
        
        :param num_transactions: The number of transactions to simulate.
        """
        for i in range(num_transactions):
            amount = round(random.uniform(1.0, 100.0), 2)
            tags = random.sample(['Social Media', 'Email', 'SEO', 'PPC', 'Content Marketing'], k=random.randint(1, 3))
            transaction = Transaction(transaction_id=i + 1, amount=amount, tags=tags)
            self.add_transaction(transaction)

    def display_analysis(self):
        """
        Display the analysis results in a readable format.
        """
        analysis = self.get_grouped_analysis()
        logging.info("Grouped Transaction Analysis:")
        for tag, total in analysis.items():
            logging.info(f"Tag: {tag}, Total Amount: {total:.2f}")


if __name__ == "__main__":
    # Initialize marketing analysis
    analysis = MarketingAnalysis()
    
    # Simulate 10 transactions
    analysis.simulate_transactions(num_transactions=10)
    
    # Display the results of the analysis
    analysis.display_analysis()
```
