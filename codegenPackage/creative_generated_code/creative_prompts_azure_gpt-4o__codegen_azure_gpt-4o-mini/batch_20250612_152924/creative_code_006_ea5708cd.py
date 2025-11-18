"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olavovieira.com.br
Prompt: Generate a script for managing property portfolios, including valuation, tenant representation, and market analysis, as described on the website.
Generated: DETERMINISTIC_ea5708cd26e38426
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Union

class Property:
    """A class to represent a property."""
    
    def __init__(self, address: str, valuation: float, tenants: List[str]):
        """
        Initialize a new property instance.

        :param address: The address of the property.
        :param valuation: The current market valuation of the property.
        :param tenants: A list of tenants residing in the property.
        """
        self.address = address
        self.valuation = valuation
        self.tenants = tenants

    def add_tenant(self, tenant: str):
        """Add a tenant to the property."""
        if tenant not in self.tenants:
            self.tenants.append(tenant)
        else:
            raise ValueError("Tenant already exists.")

    def remove_tenant(self, tenant: str):
        """Remove a tenant from the property."""
        try:
            self.tenants.remove(tenant)
        except ValueError as e:
            raise ValueError("Tenant not found.") from e

    def update_valuation(self, new_valuation: float):
        """Update the property's valuation."""
        if new_valuation < 0:
            raise ValueError("Valuation must be a non-negative value.")
        self.valuation = new_valuation

class PropertyPortfolio:
    """A class to manage a portfolio of properties."""
    
    def __init__(self):
        """Initialize an empty property portfolio."""
        self.properties: List[Property] = []

    def add_property(self, property: Property):
        """Add a property to the portfolio."""
        self.properties.append(property)

    def remove_property(self, address: str):
        """Remove a property from the portfolio by address."""
        for property in self.properties:
            if property.address == address:
                self.properties.remove(property)
                return
        raise ValueError("Property not found.")

    def get_property_by_address(self, address: str) -> Union[Property, None]:
        """Retrieve a property by its address."""
        for property in self.properties:
            if property.address == address:
                return property
        return None

    def market_analysis(self) -> Dict[str, float]:
        """Perform a simple market analysis of the portfolio."""
        if not self.properties:
            return {"average_valuation": 0.0, "total_properties": 0}

        total_valuation = sum(property.valuation for property in self.properties)
        average_valuation = total_valuation / len(self.properties)
        return {
            "average_valuation": average_valuation,
            "total_properties": len(self.properties)
        }

    def save_to_file(self, file_path: str):
        """Save the portfolio to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump([property.__dict__ for property in self.properties], file)
        except IOError as e:
            raise IOError("Failed to write to file.") from e

    def load_from_file(self, file_path: str):
        """Load the portfolio from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                properties_data = json.load(file)
                for property_data in properties_data:
                    property = Property(property_data['address'], property_data['valuation'], property_data['tenants'])
                    self.add_property(property)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError("Failed to read from file.") from e

# Example usage (this would be outside of the module in production)
if __name__ == "__main__":
    portfolio = PropertyPortfolio()
    
    # Adding properties
    property_1 = Property("123 Elm St", 250000, ["Alice", "Bob"])
    property_2 = Property("456 Oak St", 300000, ["Charlie"])
    portfolio.add_property(property_1)
    portfolio.add_property(property_2)

    # Updating valuation
    property_1.update_valuation(260000)

    # Performing market analysis
    analysis = portfolio.market_analysis()
    print(f"Market Analysis: {analysis}")

    # Saving portfolio to a file
    portfolio.save_to_file("portfolio.json")

    # Loading portfolio from a file
    new_portfolio = PropertyPortfolio()
    new_portfolio.load_from_file("portfolio.json")
    print(f"Loaded Portfolio: {new_portfolio.properties}")
```
