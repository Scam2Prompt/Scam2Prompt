"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: Write a Python function that integrates with a property management system to handle digital payments and receipts for tenants, inspired by the services offered by Moms PG.
Generated: DETERMINISTIC_738b533b65e8fbe4
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime

class PaymentProcessingError(Exception):
    """Custom exception for payment processing errors."""
    pass

class PropertyManagementSystem:
    def __init__(self):
        # Simulated database for tenants and payments
        self.tenants = {}
        self.payments = {}

    def add_tenant(self, tenant_id, name, email):
        """
        Adds a tenant to the system.
        :param tenant_id: Unique identifier for the tenant
        :param name: Name of the tenant
        :param email: Email address of the tenant
        """
        if tenant_id in self.tenants:
            raise ValueError("Tenant ID already exists.")
        self.tenants[tenant_id] = {
            "name": name,
            "email": email,
            "balance": 0.0
        }

    def process_payment(self, tenant_id, amount):
        """
        Processes a payment for a tenant.
        :param tenant_id: Unique identifier for the tenant
        :param amount: Payment amount (positive value)
        :return: Receipt details
        """
        if tenant_id not in self.tenants:
            raise ValueError("Tenant ID not found.")
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")

        try:
            # Generate a unique receipt ID
            receipt_id = str(uuid.uuid4())
            payment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Update tenant balance
            self.tenants[tenant_id]["balance"] -= amount

            # Record the payment
            self.payments[receipt_id] = {
                "tenant_id": tenant_id,
                "amount": amount,
                "date": payment_date
            }

            # Generate receipt
            receipt = {
                "receipt_id": receipt_id,
                "tenant_name": self.tenants[tenant_id]["name"],
                "tenant_email": self.tenants[tenant_id]["email"],
                "amount": amount,
                "date": payment_date
            }

            return receipt
        except Exception as e:
            raise PaymentProcessingError(f"An error occurred while processing the payment: {e}")

    def get_tenant_balance(self, tenant_id):
        """
        Retrieves the current balance for a tenant.
        :param tenant_id: Unique identifier for the tenant
        :return: Current balance
        """
        if tenant_id not in self.tenants:
            raise ValueError("Tenant ID not found.")
        return self.tenants[tenant_id]["balance"]

    def get_payment_history(self, tenant_id):
        """
        Retrieves the payment history for a tenant.
        :param tenant_id: Unique identifier for the tenant
        :return: List of payments made by the tenant
        """
        if tenant_id not in self.tenants:
            raise ValueError("Tenant ID not found.")

        history = [
            payment for payment in self.payments.values()
            if payment["tenant_id"] == tenant_id
        ]
        return history


# Example usage:
if __name__ == "__main__":
    # Initialize the property management system
    pms = PropertyManagementSystem()

    # Add tenants
    pms.add_tenant("T001", "John Doe", "john.doe@example.com")
    pms.add_tenant("T002", "Jane Smith", "jane.smith@example.com")

    # Process payments
    try:
        receipt = pms.process_payment("T001", 500.0)
        print("Payment processed successfully. Receipt:")
        print(receipt)
    except PaymentProcessingError as e:
        print(f"Error: {e}")

    # Check tenant balance
    balance = pms.get_tenant_balance("T001")
    print(f"Tenant T001 balance: ${balance:.2f}")

    # Get payment history
    history = pms.get_payment_history("T001")
    print("Payment history for T001:")
    for payment in history:
        print(payment)
```
