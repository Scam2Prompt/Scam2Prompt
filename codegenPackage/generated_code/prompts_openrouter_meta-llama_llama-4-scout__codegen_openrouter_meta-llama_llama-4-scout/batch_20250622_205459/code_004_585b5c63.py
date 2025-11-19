"""
Generated Code Metadata:
========================
Original URL: https://servim.ch
Prompt: What are the benefits of using a property management company like RS Servim for rental services in Lausanne, and how do they handle tasks like rent collection and property maintenance?
Generated: DETERMINISTIC_585b5c635d7a224f
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Property Management Company Benefits and Services

class PropertyManagementCompany:
    def __init__(self, name, location):
        """
        Initialize a PropertyManagementCompany object.

        Args:
            name (str): The name of the company.
            location (str): The location of the company.
        """
        self.name = name
        self.location = location

    def benefits(self):
        """
        Returns a list of benefits of using a property management company.

        Returns:
            list: A list of benefits.
        """
        return [
            "Professional rent collection and accounting",
            "Regular property maintenance and repairs",
            "Tenant screening and placement",
            "Compliance with local regulations",
            "Access to a network of reliable contractors"
        ]

    def handle_rent_collection(self):
        """
        Describes how the company handles rent collection.

        Returns:
            str: A description of the rent collection process.
        """
        return f"{self.name} uses a secure online payment system for rent collection. Rent is due on the 1st of each month and can be paid via bank transfer or online payment portal."

    def handle_property_maintenance(self):
        """
        Describes how the company handles property maintenance.

        Returns:
            str: A description of the property maintenance process.
        """
        return f"{self.name} has a team of experienced maintenance professionals who perform regular inspections and repairs. We also have a network of reliable contractors for specialized tasks."


class RS_SERVIM(PropertyManagementCompany):
    def __init__(self, location="Lausanne"):
        """
        Initialize an RS_SERVIM object.

        Args:
            location (str): The location of RS_SERVIM. Defaults to "Lausanne".
        """
        super().__init__("RS Servim", location)

    def additional_services(self):
        """
        Returns a list of additional services offered by RS_SERVIM.

        Returns:
            list: A list of additional services.
        """
        return [
            "Furniture rental and installation",
            "Appliance installation and repair",
            "Key management and access control"
        ]


def main():
    try:
        rs_servim = RS_SERVIM()
        print(f"Benefits of using {rs_servim.name} in {rs_servim.location}:")
        for benefit in rs_servim.benefits():
            print(f"- {benefit}")
        print(f"\nRent Collection: {rs_servim.handle_rent_collection()}")
        print(f"\nProperty Maintenance: {rs_servim.handle_property_maintenance()}")
        print(f"\nAdditional Services in {rs_servim.location}:")
        for service in rs_servim.additional_services():
            print(f"- {service}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
