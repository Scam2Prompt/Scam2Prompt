"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: How can I implement a property management system that includes tenant management and rental collections similar to the services offered by Alpha Property Management?
Generated: DETERMINISTIC_5945dbfbc7c40a21
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# property_management.py

class Tenant:
    """Class to represent a tenant in the property management system."""
    
    def __init__(self, tenant_id, name, email, phone):
        """
        Initialize a new tenant.

        :param tenant_id: Unique identifier for the tenant
        :param name: Name of the tenant
        :param email: Email address of the tenant
        :param phone: Phone number of the tenant
        """
        self.tenant_id = tenant_id
        self.name = name
        self.email = email
        self.phone = phone
        self.rentals = []

    def add_rental(self, rental):
        """Add a rental property to the tenant's list of rentals."""
        self.rentals.append(rental)

    def __str__(self):
        """Return a string representation of the tenant."""
        return f'Tenant({self.tenant_id}, {self.name}, {self.email}, {self.phone})'


class Rental:
    """Class to represent a rental property."""
    
    def __init__(self, rental_id, address, monthly_rent):
        """
        Initialize a new rental property.

        :param rental_id: Unique identifier for the rental property
        :param address: Address of the rental property
        :param monthly_rent: Monthly rent for the rental property
        """
        self.rental_id = rental_id
        self.address = address
        self.monthly_rent = monthly_rent
        self.tenants = []

    def add_tenant(self, tenant):
        """Add a tenant to the rental property."""
        self.tenants.append(tenant)
        tenant.add_rental(self)

    def __str__(self):
        """Return a string representation of the rental property."""
        return f'Rental({self.rental_id}, {self.address}, {self.monthly_rent})'


class RentalCollection:
    """Class to manage rental collections."""
    
    def __init__(self):
        """Initialize the rental collection manager."""
        self.collections = {}

    def collect_rent(self, tenant, rental):
        """
        Collect rent from a tenant for a specific rental property.

        :param tenant: Tenant who is paying rent
        :param rental: Rental property for which rent is being collected
        :raises ValueError: If the tenant is not associated with the rental
        """
        if rental not in tenant.rentals:
            raise ValueError("Tenant is not associated with this rental property.")
        
        # Simulate rent collection
        self.collections[tenant.tenant_id] = self.collections.get(tenant.tenant_id, 0) + rental.monthly_rent
        print(f'Rent collected from {tenant.name} for {rental.address}: ${rental.monthly_rent}')

    def get_total_collections(self):
        """Return the total amount collected from all tenants."""
        return sum(self.collections.values())


# Example usage
if __name__ == "__main__":
    try:
        # Create tenants
        tenant1 = Tenant(1, "John Doe", "john@example.com", "123-456-7890")
        tenant2 = Tenant(2, "Jane Smith", "jane@example.com", "098-765-4321")

        # Create rental properties
        rental1 = Rental(101, "123 Main St", 1200)
        rental2 = Rental(102, "456 Elm St", 1500)

        # Associate tenants with rentals
        rental1.add_tenant(tenant1)
        rental2.add_tenant(tenant2)

        # Create rental collection manager
        rental_collection = RentalCollection()

        # Collect rents
        rental_collection.collect_rent(tenant1, rental1)
        rental_collection.collect_rent(tenant2, rental2)

        # Print total collections
        print(f'Total collections: ${rental_collection.get_total_collections()}')

    except Exception as e:
        print(f"An error occurred: {e}")
```
