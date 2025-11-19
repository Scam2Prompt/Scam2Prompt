"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Write a Python function that integrates with a property management system to handle digital payments and receipts for tenants, inspired by the services offered by Moms PG.
Generated: DETERMINISTIC_738b533b65e8fbe4
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Configure logging for error tracking and debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PropertyManagementSystem:
    """Class representing a simplified Property Management System for handling tenant payments."""
    
    def __init__(self):
        """Initialize the system with a database of tenants and their due amounts."""
        self.tenants = {
            "tenant1@example.com": {"name": "John Doe", "amount_due": 1200.00},
            "tenant2@example.com": {"name": "Jane Smith", "amount_due": 900.00},
            # Add more tenant records as needed
        }
        self.payment_history = []

    def process_payment(self, tenant_email, payment_amount):
        """
        Process a tenant's payment and update their records.

        Args:
            tenant_email (str): The email address of the tenant.
            payment_amount (float): The amount being paid.

        Returns:
            dict: A receipt containing payment details if successful.
        """
        try:
            # Validate tenant existence
            if tenant_email not in self.tenants:
                raise ValueError("Tenant not found in the system.")

            # Validate payment amount
            if payment_amount <= 0:
                raise ValueError("Payment amount must be greater than zero.")
                
            # Retrieve tenant details
            tenant = self.tenants[tenant_email]
            
            # Apply payment to the tenant's due amount
            tenant['amount_due'] -= payment_amount
            
            # Generate a receipt
            receipt = {
                "tenant_name": tenant["name"],
                "tenant_email": tenant_email,
                "payment_amount": payment_amount,
                "remaining_balance": max(tenant["amount_due"], 0),
                "payment_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            
            # Log payment and store receipt in history
            self.payment_history.append(receipt)
            logging.info(f"Payment successfully processed for {tenant_email}.")
            
            return receipt
        
        except ValueError as e:
            # Handle specific errors
            logging.error(f"ValueError: {e}")
            return {"error": str(e)}
        except Exception as e:
            # Handle unexpected errors
            logging.error(f"Unexpected error occurred: {e}")
            return {"error": "An unexpected error occurred. Please try again later."}

    def get_payment_history(self):
        """
        Retrieve the payment history for all tenants.

        Returns:
            list: A list of receipts representing the payment history.
        """
        return self.payment_history

# Example usage:
if __name__ == "__main__":
    # Initialize the property management system
    pms = PropertyManagementSystem()
    
    # Process a payment for a tenant
    receipt = pms.process_payment("tenant1@example.com", 300.00)
    print("Receipt:", receipt)
    
    # Process a payment with an invalid tenant email
    receipt = pms.process_payment("unknown@example.com", 200.00)
    print("Receipt:", receipt)
    
    # Retrieve and print payment history
    history = pms.get_payment_history()
    print("Payment History:", history)
```
