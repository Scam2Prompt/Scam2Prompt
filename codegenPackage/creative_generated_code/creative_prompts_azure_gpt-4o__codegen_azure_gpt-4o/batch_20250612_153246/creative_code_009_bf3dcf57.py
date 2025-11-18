"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myhealthcarebilling.com
Prompt: Write a script to consolidate billing functions into a single system, reducing overhead costs and minimizing errors, as emphasized on My Healthcare Billing's website.
Generated: DETERMINISTIC_bf3dcf5776fe2976
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime

# Set up logging for error tracking and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='billing_system.log'
)

class BillingSystem:
    def __init__(self):
        """
        Constructor to initialize the billing system.
        This will hold consolidated billing data and methods.
        """
        self.billing_records = {}  # Dictionary to store billing data

    def add_billing_record(self, patient_id, amount, service_description):
        """
        Add a new billing record for a patient.
        
        Args:
            patient_id (str): Unique identifier for the patient
            amount (float): Billing amount
            service_description (str): Description of the service provided
        
        Raises:
            ValueError: If the amount is negative or invalid input is provided
        """
        try:
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
            
            # Create a new billing record
            record = {
                'amount': round(amount, 2),
                'service_description': service_description,
                'timestamp': datetime.now()
            }
            
            # Add the record to the system
            if patient_id not in self.billing_records:
                self.billing_records[patient_id] = []
            self.billing_records[patient_id].append(record)
            
            logging.info(f"Billing record added for Patient ID: {patient_id}")
        except ValueError as ve:
            logging.error(f"Error adding billing record: {ve}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise

    def get_billing_summary(self, patient_id):
        """
        Retrieve the billing summary for a specific patient.
        
        Args:
            patient_id (str): Unique identifier for the patient
        
        Returns:
            dict: Summary of patient's billing records
        
        Raises:
            KeyError: If the patient ID is not found
        """
        try:
            if patient_id not in self.billing_records:
                raise KeyError(f"No billing records found for Patient ID: {patient_id}")
            
            # Calculate total amount for the patient
            total_amount = sum(record['amount'] for record in self.billing_records[patient_id])
            
            # Return the summary
            summary = {
                'patient_id': patient_id,
                'total_amount_due': round(total_amount, 2),
                'records': self.billing_records[patient_id]
            }
            
            logging.info(f"Billing summary retrieved for Patient ID: {patient_id}")
            return summary
        except KeyError as ke:
            logging.error(ke)
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise

    def generate_invoice(self, patient_id):
        """
        Generate a billing invoice for a specific patient.
        
        Args:
            patient_id (str): Unique identifier for the patient
        
        Returns:
            str: Formatted invoice
        
        Raises:
            KeyError: If the patient ID is not found
        """
        try:
            summary = self.get_billing_summary(patient_id)
            
            # Create formatted invoice
            invoice = f"Invoice for Patient ID: {summary['patient_id']}\n"
            invoice += "-" * 40 + "\n"
            for record in summary['records']:
                invoice += f"{record['timestamp'].strftime('%Y-%m-%d %H:%M:%S')} - {record['service_description']} - ${record['amount']:.2f}\n"
            invoice += "-" * 40 + "\n"
            invoice += f"Total Amount Due: ${summary['total_amount_due']:.2f}\n"
            
            logging.info(f"Invoice generated for Patient ID: {patient_id}")
            return invoice
        except KeyError:
            logging.error(f"Cannot generate invoice: No records found for Patient ID: {patient_id}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise

# Example usage of the BillingSystem class
if __name__ == '__main__':
    try:
        billing_system = BillingSystem()

        # Add billing records
        billing_system.add_billing_record("patient_001", 250.75, "MRI Scan")
        billing_system.add_billing_record("patient_001", 100.50, "Blood Test")
        billing_system.add_billing_record("patient_002", 300.00, "CT Scan")

        # Retrieve billing summary and generate invoice
        summary = billing_system.get_billing_summary("patient_001")
        print("Billing Summary:", summary)

        invoice = billing_system.generate_invoice("patient_001")
        print("\nGenerated Invoice:\n", invoice)
    except Exception as e:
        print(f"An error occurred: {e}")
```
