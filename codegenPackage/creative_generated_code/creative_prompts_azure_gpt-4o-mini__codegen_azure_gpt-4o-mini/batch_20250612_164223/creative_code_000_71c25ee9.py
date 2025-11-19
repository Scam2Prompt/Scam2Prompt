"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rheinmetall-zulieferer.com
Prompt: Generate a list of military vehicle suppliers for Rheinmetall, including their locations and specific contributions to the production of military equipment.
Generated: DETERMINISTIC_71c25ee994bed2c6
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class Supplier:
    """Class representing a military vehicle supplier."""
    
    def __init__(self, name, location, contribution):
        self.name = name
        self.location = location
        self.contribution = contribution

    def to_dict(self):
        """Convert the Supplier instance to a dictionary."""
        return {
            "name": self.name,
            "location": self.location,
            "contribution": self.contribution
        }

class SupplierDatabase:
    """Class to manage military vehicle suppliers for Rheinmetall."""
    
    def __init__(self):
        self.suppliers = []

    def add_supplier(self, supplier):
        """Add a supplier to the database."""
        if isinstance(supplier, Supplier):
            self.suppliers.append(supplier)
        else:
            raise ValueError("Invalid supplier object")

    def get_suppliers(self):
        """Return a list of all suppliers in dictionary format."""
        return [supplier.to_dict() for supplier in self.suppliers]

    def export_to_json(self, filename):
        """Export the supplier list to a JSON file."""
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.get_suppliers(), json_file, indent=4)
        except IOError as e:
            print(f"Error writing to file: {e}")

def main():
    """Main function to create and manage the supplier database."""
    
    # Initialize supplier database
    supplier_db = SupplierDatabase()

    # Example suppliers (In a production scenario, these might come from a database or an API)
    suppliers_data = [
        {"name": "Supplier A", "location": "Germany", "contribution": "Tank production"},
        {"name": "Supplier B", "location": "USA", "contribution": "Armored vehicles"},
        {"name": "Supplier C", "location": "France", "contribution": "Logistics support"},
        {"name": "Supplier D", "location": "Italy", "contribution": "Parts manufacturing"}
    ]

    # Add suppliers to the database
    for data in suppliers_data:
        supplier = Supplier(data["name"], data["location"], data["contribution"])
        supplier_db.add_supplier(supplier)

    # Export supplier data to a JSON file
    supplier_db.export_to_json("military_vehicle_suppliers.json")
    print("Supplier data exported successfully.")

if __name__ == "__main__":
    main()
```
