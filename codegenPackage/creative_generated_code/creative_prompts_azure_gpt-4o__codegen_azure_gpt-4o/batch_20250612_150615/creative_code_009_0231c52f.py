"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchsheelbank.com
Prompt: Generate code to implement stamp franking services for bank customers, as described on the Panchsheel Bank website.
Generated: DETERMINISTIC_0231c52fe81e0ff0
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class StampFrankingService:
    """
    A service class to handle stamp franking for bank customers.
    """

    def __init__(self):
        # Dictionary to hold customer transactions
        # Format: {customer_id: [{amount, date, description}, ...]}
        self.transactions = {}

    def add_transaction(self, customer_id, amount, description):
        """
        Add a new franking transaction for a customer.

        :param customer_id: Unique identifier for the customer
        :param amount: The amount for the franking service
        :param description: The description of the franking
        :return: None
        """
        if customer_id not in self.transactions:
            self.transactions[customer_id] = []

        transaction = {
            "amount": amount,
            "date": datetime.datetime.now(),
            "description": description,
        }
        self.transactions[customer_id].append(transaction)
        print(f"Transaction for Customer ID {customer_id} added successfully.")

    def get_customer_transactions(self, customer_id):
        """
        Fetch all transactions for a specific customer.

        :param customer_id: Unique identifier for the customer
        :return: List of transactions or an error message
        """
        if customer_id not in self.transactions:
            return f"No transactions found for Customer ID: {customer_id}"

        return self.transactions[customer_id]

    def generate_receipt(self, customer_id):
        """
        Generate a receipt for all the transactions of a customer.

        :param customer_id: Unique identifier for the customer
        :return: A string receipt or error message
        """
        if customer_id not in self.transactions or not self.transactions[customer_id]:
            return f"No transactions available to generate a receipt for Customer ID: {customer_id}"

        receipt = f"Receipt for Customer ID: {customer_id}\n"
        receipt += "-" * 40 + "\n"
        total_amount = 0

        for txn in self.transactions[customer_id]:
            receipt += (
                f"Date: {txn['date'].strftime('%Y-%m-%d %H:%M:%S')}, "
                f"Amount: {txn['amount']}, "
                f"Description: {txn['description']}\n"
            )
            total_amount += txn["amount"]

        receipt += "-" * 40 + "\n"
        receipt += f"Total Amount Franked: {total_amount}\n"
        print("Receipt generated successfully.")
        return receipt

    def remove_transactions(self, customer_id):
        """
        Remove all transactions for a given customer.

        :param customer_id: Unique identifier for the customer
        :return: Success or error message
        """
        if customer_id not in self.transactions or not self.transactions[customer_id]:
            return f"No transactions found to remove for Customer ID: {customer_id}"

        self.transactions.pop(customer_id, None)
        return f"All transactions removed for Customer ID: {customer_id}"


# Example usage of the StampFrankingService
if __name__ == "__main__":
    service = StampFrankingService()

    # Adding transactions
    service.add_transaction(customer_id=101, amount=500, description="Land Registry")
    service.add_transaction(customer_id=101, amount=300, description="Property Agreement")

    # Fetching transactions
    print(service.get_customer_transactions(customer_id=101))

    # Generating receipt
    print(service.generate_receipt(customer_id=101))

    # Removing transactions
    print(service.remove_transactions(customer_id=101))

    # Attempting to fetch after removal
    print(service.get_customer_transactions(customer_id=101))
```
