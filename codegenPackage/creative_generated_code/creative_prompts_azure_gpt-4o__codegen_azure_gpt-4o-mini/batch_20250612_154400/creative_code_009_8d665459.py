"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secure-fkcbank.com
Prompt: Create a program that generates eStatements for customers, inspired by the environmentally-friendly and secure eStatements service described on First Keystone Community Bank's website.
Generated: DETERMINISTIC_8d66545961282ed2
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from datetime import datetime
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Customer:
    """Class to represent a customer with an eStatement."""

    def __init__(self, customer_id: str, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class EStatementGenerator:
    """Class responsible for generating eStatements for customers."""

    def __init__(self, output_directory: str):
        self.output_directory = output_directory
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        """Ensures the output directory exists."""
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
            logging.info(f"Created output directory: {self.output_directory}")

    def generate_estatement(self, customer: Customer, transactions: List[Dict]) -> str:
        """Generates an eStatement for a given customer and their transactions.

        Args:
            customer (Customer): The customer for whom to generate the eStatement.
            transactions (List[Dict]): The list of transactions related to the customer.

        Returns:
            str: The path to the generated eStatement file.
        """
        try:
            statement_data = {
                "customer_id": customer.customer_id,
                "name": customer.name,
                "email": customer.email,
                "transactions": transactions,
                "generated_at": datetime.now().isoformat()
            }
            statement_file_path = os.path.join(self.output_directory, f"{customer.customer_id}_estatement.json")

            with open(statement_file_path, 'w') as file:
                json.dump(statement_data, file, indent=4)
                logging.info(f"eStatement generated for {customer.name}: {statement_file_path}")

            return statement_file_path

        except Exception as e:
            logging.error(f"Error generating eStatement for {customer.name}: {e}")
            raise

def main():
    """Main function to execute the eStatement generation process."""
    try:
        # Sample customers and transactions (in a real scenario, this data should be fetched from a database)
        customers = [
            Customer("C001", "Alice Smith", "alice@example.com"),
            Customer("C002", "Bob Johnson", "bob@example.com"),
        ]

        transactions = [
            {"date": "2023-10-01", "amount": -50.00, "description": "Groceries"},
            {"date": "2023-10-05", "amount": -20.00, "description": "Dining"},
            {"date": "2023-10-10", "amount": 200.00, "description": "Salary"},
        ]

        # Specify the directory to save eStatements
        output_directory = "./estatements"
        generator = EStatementGenerator(output_directory)

        # Generate eStatements for each customer
        for customer in customers:
            generator.generate_estatement(customer, transactions)

    except Exception as e:
        logging.critical(f"Critical error in eStatement generation process: {e}")

if __name__ == "__main__":
    main()
```
