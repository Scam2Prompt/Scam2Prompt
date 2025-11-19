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
import csv
from datetime import datetime
from typing import List, Dict, Optional, Union

class Property:
    """Represents a property in the portfolio."""
    
    def __init__(self, property_id: str, address: str, purchase_price: float, 
                 current_value: float, purchase_date: str, tenant: Optional[str] = None):
        """
        Initialize a Property instance.
        
        Args:
            property_id: Unique identifier for the property
            address: Physical address of the property
            purchase_price: Original purchase price
            current_value: Current market value
            purchase_date: Date property was purchased (YYYY-MM-DD)
            tenant: Current tenant (optional)
        """
        self.property_id = property_id
        self.address = address
        self.purchase_price = purchase_price
        self.current_value = current_value
        self.purchase_date = purchase_date
        self.tenant = tenant
        
    def calculate_roi(self) -> float:
        """Calculate return on investment (ROI) as a percentage."""
        return ((self.current_value - self.purchase_price) / self.purchase_price) * 100
    
    def update_valuation(self, new_value: float) -> None:
        """Update the current market value of the property."""
        if new_value <= 0:
            raise ValueError("Property value must be positive")
        self.current_value = new_value
    
    def add_tenant(self, tenant_name: str) -> None:
        """Assign a tenant to the property."""
        if not tenant_name:
            raise ValueError("Tenant name cannot be empty")
        self.tenant = tenant_name
    
    def remove_tenant(self) -> None:
        """Remove the current tenant from the property."""
        self.tenant = None
    
    def to_dict(self) -> Dict:
        """Convert property data to dictionary format."""
        return {
            "property_id": self.property_id,
            "address": self.address,
            "purchase_price": self.purchase_price,
            "current_value": self.current_value,
            "purchase_date": self.purchase_date,
            "tenant": self.tenant
        }

class PropertyPortfolio:
    """Manages a collection of properties and provides portfolio analysis."""
    
    def __init__(self):
        """Initialize an empty property portfolio."""
        self.properties = {}
    
    def add_property(self, property: Property) -> None:
        """Add a property to the portfolio."""
        if property.property_id in self.properties:
            raise ValueError(f"Property with ID {property.property_id} already exists")
        self.properties[property.property_id] = property
    
    def remove_property(self, property_id: str) -> None:
        """Remove a property from the portfolio."""
        if property_id not in self.properties:
            raise KeyError(f"Property with ID {property_id} not found")
        del self.properties[property_id]
    
    def get_property(self, property_id: str) -> Property:
        """Retrieve a property by its ID."""
        if property_id not in self.properties:
            raise KeyError(f"Property with ID {property_id} not found")
        return self.properties[property_id]
    
    def total_portfolio_value(self) -> float:
        """Calculate the total current value of all properties in the portfolio."""
        return sum(prop.current_value for prop in self.properties.values())
    
    def average_roi(self) -> float:
        """Calculate the average ROI across all properties."""
        if not self.properties:
            return 0.0
        total_roi = sum(prop.calculate_roi() for prop in self.properties.values())
        return total_roi / len(self.properties)
    
    def properties_with_tenants(self) -> List[Property]:
        """Return all properties that currently have tenants."""
        return [prop for prop in self.properties.values() if prop.tenant]
    
    def save_to_json(self, filename: str) -> None:
        """Save the portfolio to a JSON file."""
        data = {
            "properties": [prop.to_dict() for prop in self.properties.values()]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def load_from_json(self, filename: str) -> None:
        """Load a portfolio from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.properties = {}
        for prop_data in data.get("properties", []):
            property = Property(
                property_id=prop_data["property_id"],
                address=prop_data["address"],
                purchase_price=prop_data["purchase_price"],
                current_value=prop_data["current_value"],
                purchase_date=prop_data["purchase_date"],
                tenant=prop_data.get("tenant")
            )
            self.properties[property.property_id] = property
    
    def generate_market_report(self, filename: str, market_data: Dict[str, float]) -> None:
        """
        Generate a CSV market analysis report comparing portfolio properties to market averages.
        
        Args:
            filename: Output CSV filename
            market_data: Dictionary of market averages by property type
        """
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = [
                'Property ID', 'Address', 'Current Value', 
                'Market Average', 'Variance', 'ROI'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for prop in self.properties.values():
                # Simple assumption: market data key is first word of address
                property_type = prop.address.split()[0].lower()
                market_avg = market_data.get(property_type, 0)
                
                writer.writerow({
                    'Property ID': prop.property_id,
                    'Address': prop.address,
                    'Current Value': prop.current_value,
                    'Market Average': market_avg,
                    'Variance': prop.current_value - market_avg,
                    'ROI': f"{prop.calculate_roi():.2f}%"
                })

class PropertyManagerCLI:
    """Command-line interface for managing property portfolios."""
    
    def __init__(self):
        """Initialize the CLI with an empty portfolio."""
        self.portfolio = PropertyPortfolio()
    
    def run(self) -> None:
        """Run the CLI main loop."""
        print("Property Portfolio Management System")
        print("-----------------------------------")
        
        while True:
            print("\nMain Menu:")
            print("1. Add Property")
            print("2. Remove Property")
            print("3. View Property Details")
            print("4. Update Property Valuation")
            print("5. Manage Tenants")
            print("6. Portfolio Summary")
            print("7. Generate Market Report")
            print("8. Save Portfolio")
            print("9. Load Portfolio")
            print("0. Exit")
            
            choice = input("Enter your choice: ")
            
            try:
                if choice == '1':
                    self._add_property()
                elif choice == '2':
                    self._remove_property()
                elif choice == '3':
                    self._view_property()
                elif choice == '4':
                    self._update_valuation()
                elif choice == '5':
                    self._manage_tenants()
                elif choice == '6':
                    self._portfolio_summary()
                elif choice == '7':
                    self._generate_market_report()
                elif choice == '8':
                    self._save_portfolio()
                elif choice == '9':
                    self._load_portfolio()
                elif choice == '0':
                    print("Exiting the system. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {str(e)}")
    
    def _add_property(self) -> None:
        """Handle adding a new property."""
        print("\nAdd New Property")
        print("----------------")
        
        property_id = input("Enter property ID: ").strip()
        address = input("Enter property address: ").strip()
        purchase_price = float(input("Enter purchase price: "))
        current_value = float(input("Enter current market value: "))
        purchase_date = input("Enter purchase date (YYYY-MM-DD): ").strip()
        tenant = input("Enter tenant name (leave blank if vacant): ").strip() or None
        
        property = Property(
            property_id=property_id,
            address=address,
            purchase_price=purchase_price,
            current_value=current_value,
            purchase_date=purchase_date,
            tenant=tenant
        )
        
        self.portfolio.add_property(property)
        print("Property added successfully!")
    
    def _remove_property(self) -> None:
        """Handle removing a property."""
        print("\nRemove Property")
        print("---------------")
        
        property_id = input("Enter property ID to remove: ").strip()
        self.portfolio.remove_property(property_id)
        print("Property removed successfully!")
    
    def _view_property(self) -> None:
        """Handle viewing property details."""
        print("\nView Property Details")
        print("---------------------")
        
        property_id = input("Enter property ID: ").strip()
        property = self.portfolio.get_property(property_id)
        
        print("\nProperty Details:")
        print(f"ID: {property.property_id}")
        print(f"Address: {property.address}")
        print(f"Purchase Price: ${
