"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Generate a script for managing property portfolios, including valuation, tenant representation, and market analysis, as described on the website.
Generated: DETERMINISTIC_ea5708cd26e38426
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Property:
    """Class to represent a property in the portfolio."""
    
    def __init__(self, id: int, address: str, value: float, tenants: List[str]):
        self.id = id
        self.address = address
        self.value = value
        self.tenants = tenants

    def update_value(self, new_value: float):
        """Update the property value."""
        if new_value < 0:
            raise ValueError("Property value cannot be negative.")
        self.value = new_value

    def add_tenant(self, tenant: str):
        """Add a tenant to the property."""
        if tenant not in self.tenants:
            self.tenants.append(tenant)

    def remove_tenant(self, tenant: str):
        """Remove a tenant from the property."""
        if tenant in self.tenants:
            self.tenants.remove(tenant)

    def to_dict(self) -> Dict:
        """Convert the property to a dictionary for easy serialization."""
        return {
            "id": self.id,
            "address": self.address,
            "value": self.value,
            "tenants": self.tenants
        }

class Portfolio:
    """Class to manage a portfolio of properties."""
    
    def __init__(self):
        self.properties: List[Property] = []

    def add_property(self, property: Property):
        """Add a property to the portfolio."""
        self.properties.append(property)

    def remove_property(self, property_id: int):
        """Remove a property from the portfolio by ID."""
        self.properties = [p for p in self.properties if p.id != property_id]

    def get_property(self, property_id: int) -> Optional[Property]:
        """Get a property by ID."""
        for property in self.properties:
            if property.id == property_id:
                return property
        return None

    def portfolio_value(self) -> float:
        """Calculate the total value of the portfolio."""
        return sum(property.value for property in self.properties)

    def to_json(self) -> str:
        """Convert the portfolio to a JSON string."""
        return json.dumps([property.to_dict() for property in self.properties], indent=4)

def main():
    """Main function to demonstrate portfolio management."""
    portfolio = Portfolio()

    # Example properties
    property1 = Property(id=1, address="123 Main St", value=250000.0, tenants=["Alice"])
    property2 = Property(id=2, address="456 Elm St", value=300000.0, tenants=["Bob", "Charlie"])

    # Add properties to the portfolio
    portfolio.add_property(property1)
    portfolio.add_property(property2)

    # Update property value
    try:
        property1.update_value(260000.0)
    except ValueError as e:
        print(f"Error updating property value: {e}")

    # Add a tenant
    property2.add_tenant("David")

    # Remove a tenant
    property2.remove_tenant("Bob")

    # Print portfolio value
    print(f"Total portfolio value: ${portfolio.portfolio_value():,.2f}")

    # Print portfolio as JSON
    print("Portfolio JSON:")
    print(portfolio.to_json())

if __name__ == "__main__":
    main()
```
