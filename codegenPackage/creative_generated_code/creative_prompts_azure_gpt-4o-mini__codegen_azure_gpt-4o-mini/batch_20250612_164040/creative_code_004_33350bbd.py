"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Suggest a library for building a tenant management system that includes features such as common amenities and digital check-in, as highlighted by Moms PG.
Generated: DETERMINISTIC_33350bbd8d1e7ac5
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# tenant_management.py

"""
Tenant Management System
This module provides a simple implementation of a tenant management system
with features for managing common amenities and digital check-in functionality.
"""

class Amenity:
    """Represents an amenity in the tenant management system."""
    
    def __init__(self, name: str, description: str):
        """
        Initializes a new Amenity instance.

        :param name: The name of the amenity.
        :param description: A brief description of the amenity.
        """
        self.name = name
        self.description = description

    def __str__(self):
        """Returns a string representation of the amenity."""
        return f"{self.name}: {self.description}"


class Tenant:
    """Represents a tenant in the management system."""
    
    def __init__(self, name: str, email: str):
        """
        Initializes a new Tenant instance.

        :param name: The full name of the tenant.
        :param email: The email address of the tenant.
        """
        self.name = name
        self.email = email
        self.check_in_status = False

    def check_in(self):
        """Marks the tenant as checked in."""
        self.check_in_status = True

    def __str__(self):
        """Returns a string representation of the tenant."""
        return f"Tenant: {self.name}, Email: {self.email}, Checked In: {self.check_in_status}"


class TenantManagementSystem:
    """Manages tenants and their amenities."""
    
    def __init__(self):
        """Initializes the tenant management system."""
        self.tenants = []
        self.amenities = []

    def add_tenant(self, name: str, email: str):
        """
        Adds a new tenant to the system.

        :param name: The full name of the tenant.
        :param email: The email address of the tenant.
        """
        try:
            tenant = Tenant(name, email)
            self.tenants.append(tenant)
            print(f"Tenant '{name}' added successfully.")
        except Exception as e:
            print(f"Error adding tenant: {str(e)}")

    def add_amenity(self, name: str, description: str):
        """
        Adds a new amenity to the system.

        :param name: The name of the amenity.
        :param description: A brief description of the amenity.
        """
        try:
            amenity = Amenity(name, description)
            self.amenities.append(amenity)
            print(f"Amenity '{name}' added successfully.")
        except Exception as e:
            print(f"Error adding amenity: {str(e)}")

    def digital_check_in(self, email: str):
        """
        Checks in a tenant digitally by email.

        :param email: The email address of the tenant to check in.
        """
        try:
            for tenant in self.tenants:
                if tenant.email == email:
                    tenant.check_in()
                    print(f"Tenant '{tenant.name}' checked in successfully.")
                    return
            print(f"No tenant found with email: {email}")
        except Exception as e:
            print(f"Error during check-in: {str(e)}")

    def list_tenants(self):
        """Lists all tenants in the system."""
        for tenant in self.tenants:
            print(tenant)

    def list_amenities(self):
        """Lists all amenities in the system."""
        for amenity in self.amenities:
            print(amenity)


# Example Usage
if __name__ == "__main__":
    tms = TenantManagementSystem()

    # Adding amenities
    tms.add_amenity("WiFi", "High-speed internet access")
    tms.add_amenity("Laundry", "On-site laundry facilities")

    # Adding tenants
    tms.add_tenant("Alice Smith", "alice@example.com")
    tms.add_tenant("Bob Johnson", "bob@example.com")

    # Checking in a tenant
    tms.digital_check_in("alice@example.com")

    # Listing tenants and amenities
    tms.list_tenants()
    tms.list_amenities()
```
