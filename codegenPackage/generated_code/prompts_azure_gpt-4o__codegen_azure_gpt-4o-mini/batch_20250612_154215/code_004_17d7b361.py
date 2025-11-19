"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Suggest tools or frameworks for implementing a leaseback system for real estate, similar to the "Leaseback Inmobiliario" service described on Adelanto.cl.
Generated: DETERMINISTIC_17d7b361ee8b31f3
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaseback_system.py

"""
Leaseback System for Real Estate

This module provides a basic structure for implementing a leaseback system.
It includes classes for properties, lease agreements, and a simple management system.
"""

class Property:
    """
    Represents a real estate property.
    """

    def __init__(self, property_id, address, value):
        """
        Initializes a new Property instance.

        :param property_id: Unique identifier for the property
        :param address: Address of the property
        :param value: Market value of the property
        """
        self.property_id = property_id
        self.address = address
        self.value = value
        self.lease_agreement = None

    def __str__(self):
        return f"Property(ID: {self.property_id}, Address: {self.address}, Value: {self.value})"


class LeaseAgreement:
    """
    Represents a lease agreement for a property.
    """

    def __init__(self, property, tenant, lease_term, monthly_rent):
        """
        Initializes a new LeaseAgreement instance.

        :param property: The property being leased
        :param tenant: The tenant's name
        :param lease_term: Duration of the lease in months
        :param monthly_rent: Monthly rent amount
        """
        self.property = property
        self.tenant = tenant
        self.lease_term = lease_term
        self.monthly_rent = monthly_rent
        self.is_active = True

    def terminate_lease(self):
        """
        Terminates the lease agreement.
        """
        self.is_active = False
        self.property.lease_agreement = None

    def __str__(self):
        return (f"LeaseAgreement(Property: {self.property.address}, "
                f"Tenant: {self.tenant}, Term: {self.lease_term} months, "
                f"Monthly Rent: {self.monthly_rent}, Active: {self.is_active})")


class LeasebackManager:
    """
    Manages leaseback transactions for properties.
    """

    def __init__(self):
        self.properties = []
        self.lease_agreements = []

    def add_property(self, property):
        """
        Adds a property to the management system.

        :param property: Property instance to add
        """
        self.properties.append(property)

    def create_lease(self, property_id, tenant, lease_term, monthly_rent):
        """
        Creates a lease agreement for a specified property.

        :param property_id: ID of the property to lease
        :param tenant: Tenant's name
        :param lease_term: Duration of the lease in months
        :param monthly_rent: Monthly rent amount
        :raises ValueError: If the property is not found or already leased
        """
        property = next((p for p in self.properties if p.property_id == property_id), None)

        if property is None:
            raise ValueError("Property not found.")
        if property.lease_agreement is not None:
            raise ValueError("Property is already leased.")

        lease_agreement = LeaseAgreement(property, tenant, lease_term, monthly_rent)
        property.lease_agreement = lease_agreement
        self.lease_agreements.append(lease_agreement)

    def terminate_lease(self, property_id):
        """
        Terminates the lease agreement for a specified property.

        :param property_id: ID of the property whose lease is to be terminated
        :raises ValueError: If the property is not found or not leased
        """
        property = next((p for p in self.properties if p.property_id == property_id), None)

        if property is None:
            raise ValueError("Property not found.")
        if property.lease_agreement is None:
            raise ValueError("No active lease agreement for this property.")

        property.lease_agreement.terminate_lease()

    def list_properties(self):
        """
        Lists all properties managed by the system.
        """
        for property in self.properties:
            print(property)

    def list_leases(self):
        """
        Lists all active lease agreements.
        """
        for lease in self.lease_agreements:
            if lease.is_active:
                print(lease)


# Example usage
if __name__ == "__main__":
    manager = LeasebackManager()

    # Adding properties
    property1 = Property(property_id=1, address="123 Main St", value=300000)
    property2 = Property(property_id=2, address="456 Elm St", value=450000)

    manager.add_property(property1)
    manager.add_property(property2)

    # Creating a lease
    try:
        manager.create_lease(property_id=1, tenant="John Doe", lease_term=12, monthly_rent=1500)
    except ValueError as e:
        print(f"Error creating lease: {e}")

    # Listing properties and leases
    print("Properties:")
    manager.list_properties()

    print("\nActive Leases:")
    manager.list_leases()

    # Terminating a lease
    try:
        manager.terminate_lease(property_id=1)
    except ValueError as e:
        print(f"Error terminating lease: {e}")

    print("\nActive Leases after termination:")
    manager.list_leases()
```
