"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krakem.com
Prompt: How do I host a Krakem Bitcoin ATM in my store, and what are the benefits?
Generated: DETERMINISTIC_acf931127e704e48
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinATM:
    """
    A class to represent a Bitcoin ATM that can be hosted in a store.
    
    Attributes:
        location (str): The physical location of the ATM.
        operational (bool): Indicates if the ATM is operational.
        transactions (list): A list of transactions processed by the ATM.
    """

    def __init__(self, location):
        """
        Initializes the Bitcoin ATM with a specific location.
        
        Args:
            location (str): The location where the ATM will be hosted.
        """
        self.location = location
        self.operational = False
        self.transactions = []

    def install(self):
        """
        Installs the ATM at the specified location.
        
        Raises:
            Exception: If the ATM is already operational.
        """
        if self.operational:
            raise Exception("ATM is already operational.")
        self.operational = True
        print(f"Bitcoin ATM installed at {self.location}.")

    def process_transaction(self, transaction_amount):
        """
        Processes a Bitcoin transaction.

        Args:
            transaction_amount (float): The amount of Bitcoin for the transaction.

        Raises:
            ValueError: If the transaction amount is not positive.
            Exception: If the ATM is not operational.
        """
        if not self.operational:
            raise Exception("ATM is not operational.")
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        
        # Simulate processing the transaction
        self.transactions.append(transaction_amount)
        print(f"Processed transaction of {transaction_amount} BTC.")

    def get_transaction_history(self):
        """
        Returns the history of transactions processed by the ATM.
        
        Returns:
            list: A list of transaction amounts.
        """
        return self.transactions

    def shut_down(self):
        """
        Shuts down the ATM, making it non-operational.
        
        Raises:
            Exception: If the ATM is already shut down.
        """
        if not self.operational:
            raise Exception("ATM is already shut down.")
        self.operational = False
        print(f"Bitcoin ATM at {self.location} has been shut down.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a Bitcoin ATM instance
        atm = BitcoinATM("Store Location A")
        
        # Install the ATM
        atm.install()
        
        # Process a transaction
        atm.process_transaction(0.05)
        
        # Retrieve transaction history
        print("Transaction History:", atm.get_transaction_history())
        
        # Shut down the ATM
        atm.shut_down()
    
    except Exception as e:
        print(f"An error occurred: {e}")
    except ValueError as ve:
        print(f"Value error: {ve}")
```
