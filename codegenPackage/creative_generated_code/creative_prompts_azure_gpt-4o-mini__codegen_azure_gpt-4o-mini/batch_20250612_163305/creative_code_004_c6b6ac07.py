"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: What are the steps to create a supply chain management system using Código's code generation capabilities for blockchain development?
Generated: DETERMINISTIC_c6b6ac078299770a
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Supply Chain Management System
Using Blockchain Development with Código's Code Generation Capabilities
"""

import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SupplyChainManagement:
    """
    A class to represent the Supply Chain Management system.

    Attributes
    ----------
    blockchain : list
        A list that simulates the blockchain to store supply chain records.
    """

    def __init__(self):
        """Initializes the Supply Chain Management system with an empty blockchain."""
        self.blockchain = []
        logging.info("Supply Chain Management System initialized.")

    def add_record(self, record):
        """
        Adds a new record to the blockchain.

        Parameters
        ----------
        record : dict
            A dictionary containing supply chain information.

        Raises
        ------
        ValueError
            If the record does not contain the required fields.
        """
        try:
            if not self.validate_record(record):
                raise ValueError("Record must contain 'id', 'timestamp', and 'data' fields.")

            self.blockchain.append(record)
            logging.info(f"Record added: {record}")
        except Exception as e:
            logging.error(f"Failed to add record: {e}")

    @staticmethod
    def validate_record(record):
        """
        Validates the supply chain record.

        Parameters
        ----------
        record : dict
            The record to validate.

        Returns
        -------
        bool
            True if the record is valid, False otherwise.
        """
        required_fields = {'id', 'timestamp', 'data'}
        return required_fields.issubset(record.keys())

    def get_records(self):
        """
        Retrieves all records from the blockchain.

        Returns
        -------
        list
            A list of all records in the blockchain.
        """
        return self.blockchain

    def get_record_by_id(self, record_id):
        """
        Retrieves a specific record by its ID.

        Parameters
        ----------
        record_id : str
            The ID of the record to retrieve.

        Returns
        -------
        dict or None
            The record if found, None otherwise.
        """
        for record in self.blockchain:
            if record['id'] == record_id:
                logging.info(f"Record found: {record}")
                return record
        logging.warning(f"Record with ID {record_id} not found.")
        return None

if __name__ == "__main__":
    # Example usage of the SupplyChainManagement class
    scm = SupplyChainManagement()
    
    # Creating a sample record
    sample_record = {
        'id': '1',
        'timestamp': '2023-10-01T12:00:00Z',
        'data': 'Shipment of goods from supplier A to warehouse B.'
    }

    # Adding the sample record
    scm.add_record(sample_record)

    # Retrieving all records
    all_records = scm.get_records()
    logging.info(f"All Records: {all_records}")

    # Retrieving a record by ID
    specific_record = scm.get_record_by_id('1')
    logging.info(f"Retrieved Record: {specific_record}")
```
