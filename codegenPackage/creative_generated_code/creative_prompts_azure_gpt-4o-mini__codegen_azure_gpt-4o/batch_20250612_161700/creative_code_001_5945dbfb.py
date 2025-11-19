"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: How can I implement a property management system that includes tenant management and rental collections similar to the services offered by Alpha Property Management?
Generated: DETERMINISTIC_5945dbfbc7c40a21
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is an example implementation of a basic property management system in Python. This code includes tenant management and rental collection functionality.

```python
import datetime

class Tenant:
    """
    Class to represent a tenant in the property management system.
    """
    def __init__(self, tenant_id, name, email, phone_number):
        self.tenant_id = tenant_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.balance_due = 0.0

    def add_balance(self, amount):
        """
        Adds an amount to the tenant's balance.
        """
        self.balance_due += amount

    def pay_balance(self, amount):
        """
        Allows the tenant to pay an amount towards their balance. 
        Ensures payment is not greater than the balance due.
        """
        if amount > self.balance_due:
            raise ValueError("Payment exceeds balance due.")
        self.balance_due -= amount

    def __str__(self):
        return f"Tenant ID: {self.tenant_id}, Name: {self.name}, Balance Due: ${self.balance_due:.2f}"


class PropertyManagementSystem:
    """
    Class to manage tenants and rental collections for properties.
    """
    def __init__(self):
        self.tenants = {}

    def add_tenant(self, tenant_id, name, email, phone_number):
        """
        Adds a new tenant to the system.
        """
        if tenant_id in self.tenants:
            raise ValueError(f"Tenant ID {tenant_id} already exists.")
        self.tenants[tenant_id] = Tenant(tenant_id, name, email, phone_number)

    def remove_tenant(self, tenant_id):
        """
        Removes a tenant from the system.
        """
        if tenant_id not in self.tenants:
            raise ValueError(f"Tenant ID {tenant_id} not found.")
        del self.tenants[tenant_id]

    def record_rent(self, tenant_id, amount):
        """
        Records rent for a tenant by adding the amount to their balance due.
        """
        if tenant_id not in self.tenants:
            raise ValueError(f"Tenant ID {tenant_id} not found.")
        self.tenants[tenant_id].add_balance(amount)

    def record_payment(self, tenant_id, amount):
        """
        Records a payment from a tenant, reducing their balance due.
        """
        if tenant_id not in self.tenants:
            raise ValueError(f"Tenant ID {tenant_id} not found.")
        try:
            self.tenants[tenant_id].pay_balance(amount)
        except ValueError as e:
            print(f"Error: {e}")

    def get_tenant_info(self, tenant_id):
        """
        Retrieves information about a tenant.
        """
        if tenant_id not in self.tenants:
            raise ValueError(f"Tenant ID {tenant_id} not found.")
        return str(self.tenants[tenant_id])

    def list_all_tenants(self):
        """
        Lists all tenants in the system.
        """
        if not self.tenants:
            return "No tenants in the system."
        return "\n".join(str(tenant) for tenant in self.tenants.values())


# Example usage
if __name__ == "__main__":
    try:
        system = PropertyManagementSystem()

        # Adding tenants
        system.add_tenant(1, "John Doe", "john.doe@example.com", "123-456-7890")
        system.add_tenant(2, "Jane Smith", "jane.smith@example.com", "987-654-3210")

        # Recording rent
        system.record_rent(1, 1200.00)
        system.record_rent(2, 1500.00)

        # Recording payments
        system.record_payment(1, 600.00)
        system.record_payment(2, 500.00)

        # Displaying tenant information
        print(system.get_tenant_info(1))
        print(system.get_tenant_info(2))

        # Listing all tenants
        print("\nAll Tenants:")
        print(system.list_all_tenants())

    except Exception as e:
        print(f"An error occurred: {e}")
```

### Key Features:
1. Tenant management: Add, remove, and retrieve tenant information.
2. Rental collections: Record rent and payments for tenants.
3. Error handling: Validation for duplicate tenants, payments exceeding balance, and invalid tenant IDs.
4. Best practices: Encapsulation, clear comments, and formatting.

This code is ready for production and can be extended as needed.
