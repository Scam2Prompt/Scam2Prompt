"""
Generated Code Metadata:
========================
Original URL: https://tao717.com
Prompt: Write a Python script that automates the documentation of various flooring products, including their specifications and applications in sectors like healthcare and education.
Generated: DETERMINISTIC_d0e2d080ca4ad8a9
Batch ID: 20250612_155732
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
import os
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, asdict

@dataclass
class FlooringProduct:
    """Dataclass representing a flooring product with its specifications."""
    product_id: str
    name: str
    material: str
    thickness: float
    width: float
    length: float
    color_options: List[str]
    applications: List[str]
    sector_suitability: List[str]
    warranty_years: int
    maintenance_level: str  # low, medium, high
    price_per_sqft: float
    fire_rating: Optional[str] = None
    slip_resistance: Optional[str] = None
    acoustic_properties: Optional[str] = None

class FlooringDocumentationGenerator:
    """Automates documentation of flooring products for various sectors."""
    
    def __init__(self):
        self.products: List[FlooringProduct] = []
    
    def add_product(self, product: FlooringProduct) -> None:
        """Add a flooring product to the documentation system."""
        self.products.append(product)
    
    def export_to_json(self, filename: str) -> None:
        """Export products to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([asdict(product) for product in self.products], f, indent=4)
            print(f"Successfully exported to {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error exporting to JSON: {e}")
    
    def export_to_csv(self, filename: str) -> None:
        """Export products to a CSV file."""
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=vars(self.products[0]).keys())
                writer.writeheader()
                for product in self.products:
                    writer.writerow(asdict(product))
            print(f"Successfully exported to {filename}")
        except (IOError, csv.Error) as e:
            print(f"Error exporting to CSV: {e}")
    
    def generate_sector_report(self, sector: str) -> Dict[str, List[Dict]]:
        """Generate a report of products suitable for a specific sector."""
        sector_products = [
            asdict(product) for product in self.products 
            if sector.lower() in [s.lower() for s in product.sector_suitability]
        ]
        return {
            "sector": sector,
            "product_count": len(sector_products),
            "products": sector_products
        }
    
    def load_from_json(self, filename: str) -> None:
        """Load products from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.products = [FlooringProduct(**item) for item in data]
            print(f"Successfully loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from JSON: {e}")
    
    def print_product_summary(self) -> None:
        """Print a summary of all products."""
        for product in self.products:
            print(f"\nProduct ID: {product.product_id}")
            print(f"Name: {product.name}")
            print(f"Material: {product.material}")
            print(f"Suitable Sectors: {', '.join(product.sector_suitability)}")

# Example usage
if __name__ == "__main__":
    generator = FlooringDocumentationGenerator()
    
    # Add sample products
    product1 = FlooringProduct(
        product_id="FP-1001",
        name="Healthcare Vinyl Flooring",
        material="Vinyl",
        thickness=2.5,
        width=6.0,
        length=36.0,
        color_options=["White", "Beige", "Light Grey"],
        applications=["Hospital Wards", "Clinics", "Laboratories"],
        sector_suitability=["Healthcare", "Education"],
        warranty_years=10,
        maintenance_level="low",
        price_per_sqft=2.99,
        fire_rating="Class A",
        slip_resistance="R10"
    )
    
    product2 = FlooringProduct(
        product_id="FP-2002",
        name="Educational Carpet Tiles",
        material="Nylon",
        thickness=0.5,
        width=24.0,
        length=24.0,
        color_options=["Blue", "Green", "Red", "Yellow"],
        applications=["Classrooms", "Libraries", "Administrative Offices"],
        sector_suitability=["Education"],
        warranty_years=15,
        maintenance_level="medium",
        price_per_sqft=3.49,
        acoustic_properties="High noise reduction"
    )
    
    generator.add_product(product1)
    generator.add_product(product2)
    
    # Export to files
    generator.export_to_json("flooring_products.json")
    generator.export_to_csv("flooring_products.csv")
    
    # Generate sector report
    healthcare_report = generator.generate_sector_report("Healthcare")
    print("\nHealthcare Sector Report:")
    print(json.dumps(healthcare_report, indent=4))
    
    # Print summary
    print("\nProduct Summary:")
    generator.print_product_summary()
```
