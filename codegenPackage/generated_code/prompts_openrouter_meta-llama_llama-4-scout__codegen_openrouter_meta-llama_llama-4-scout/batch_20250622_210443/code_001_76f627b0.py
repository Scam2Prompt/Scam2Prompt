"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Write a Python script to manage rental collections and tenant management for a property management company like Alphamor.
Generated: DETERMINISTIC_76f627b0bb995d1b
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rental_management.py

class Tenant:
    """Represents a tenant in the rental management system."""

    def __init__(self, tenant_id, name, email, phone):
        """
        Initializes a Tenant object.

        Args:
            tenant_id (int): Unique identifier for the tenant.
            name (str): Name of the tenant.
            email (str): Email address of the tenant.
            phone (str): Phone number of the tenant.
        """
        self.tenant_id = tenant_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Tenant {self.tenant_id}: {self.name}, {self.email}, {self.phone}"


class RentalUnit:
    """Represents a rental unit in the rental management system."""

    def __init__(self, unit_id, address, rent):
        """
        Initializes a RentalUnit object.

        Args:
            unit_id (int): Unique identifier for the rental unit.
            address (str): Address of the rental unit.
            rent (float): Monthly rent for the rental unit.
        """
        self.unit_id = unit_id
        self.address = address
        self.rent = rent
        self.tenant = None

    def assign_tenant(self, tenant):
        """
        Assigns a tenant to the rental unit.

        Args:
            tenant (Tenant): Tenant object to assign to the rental unit.
        """
        self.tenant = tenant

    def __str__(self):
        return f"Rental Unit {self.unit_id}: {self.address}, Rent: ${self.rent:.2f}"


class RentalCollection:
    """Manages rental collections and tenant management."""

    def __init__(self):
        self.rental_units = {}
        self.tenants = {}

    def add_rental_unit(self, unit_id, address, rent):
        """
        Adds a rental unit to the system.

        Args:
            unit_id (int): Unique identifier for the rental unit.
            address (str): Address of the rental unit.
            rent (float): Monthly rent for the rental unit.
        """
        if unit_id in self.rental_units:
            raise ValueError("Rental unit already exists")
        self.rental_units[unit_id] = RentalUnit(unit_id, address, rent)

    def add_tenant(self, tenant_id, name, email, phone):
        """
        Adds a tenant to the system.

        Args:
            tenant_id (int): Unique identifier for the tenant.
            name (str): Name of the tenant.
            email (str): Email address of the tenant.
            phone (str): Phone number of the tenant.
        """
        if tenant_id in self.tenants:
            raise ValueError("Tenant already exists")
        self.tenants[tenant_id] = Tenant(tenant_id, name, email, phone)

    def assign_tenant_to_unit(self, tenant_id, unit_id):
        """
        Assigns a tenant to a rental unit.

        Args:
            tenant_id (int): Unique identifier for the tenant.
            unit_id (int): Unique identifier for the rental unit.
        """
        if tenant_id not in self.tenants:
            raise ValueError("Tenant does not exist")
        if unit_id not in self.rental_units:
            raise ValueError("Rental unit does not exist")
        self.rental_units[unit_id].assign_tenant(self.tenants[tenant_id])

    def collect_rent(self, unit_id, amount):
        """
        Records a rent collection for a rental unit.

        Args:
            unit_id (int): Unique identifier for the rental unit.
            amount (float): Amount of rent collected.

        Returns:
            bool: True if rent collection was successful, False otherwise.
        """
        if unit_id not in self.rental_units:
            raise ValueError("Rental unit does not exist")
        if amount <= 0:
            raise ValueError("Invalid rent amount")
        print(f"Collected ${amount:.2f} from Rental Unit {unit_id}")
        return True

    def __str__(self):
        rental_units_str = "\n".join(str(unit) for unit in self.rental_units.values())
        tenants_str = "\n".join(str(tenant) for tenant in self.tenants.values())
        return f"Rental Units:\n{rental_units_str}\n\nTenants:\n{tenants_str}"


def main():
    try:
        rental_collection = RentalCollection()

        # Add rental units
        rental_collection.add_rental_unit(1, "123 Main St", 1000.0)
        rental_collection.add_rental_unit(2, "456 Elm St", 1200.0)

        # Add tenants
        rental_collection.add_tenant(1, "John Doe", "john.doe@example.com", "123-456-7890")
        rental_collection.add_tenant(2, "Jane Smith", "jane.smith@example.com", "987-654-3210")

        # Assign tenants to rental units
        rental_collection.assign_tenant_to_unit(1, 1)
        rental_collection.assign_tenant_to_unit(2, 2)

        # Collect rent
        rental_collection.collect_rent(1, 1000.0)
        rental_collection.collect_rent(2, 1200.0)

        # Print rental collection and tenant information
        print(rental_collection)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
