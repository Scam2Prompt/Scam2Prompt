"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: Write a program to categorize and display the welding electrodes and filler metals offered by Roshako, such as Alloy 625 and Hastelloy C-276, along with their technical specifications.
Generated: DETERMINISTIC_aab4bacf61b5b71d
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class WeldingElectrode:
    """
    A class to represent a welding electrode or filler metal with its technical specifications.
    """
    
    def __init__(
        self,
        name: str,
        material_type: str,
        composition: Dict[str, float],
        tensile_strength_psi: int,
        yield_strength_psi: int,
        elongation_percent: float,
        applications: List[str],
        temperature_range_f: Optional[str] = None,
        certifications: Optional[List[str]] = None
    ):
        """
        Initialize a WeldingElectrode instance.
        
        Args:
            name: Name of the electrode/filler metal (e.g., "Alloy 625").
            material_type: Type of material (e.g., "Nickel Alloy").
            composition: Chemical composition as a dictionary (e.g., {"Ni": 58.0, "Cr": 21.5}).
            tensile_strength_psi: Tensile strength in psi.
            yield_strength_psi: Yield strength in psi.
            elongation_percent: Elongation percentage.
            applications: List of typical applications.
            temperature_range_f: Optional operating temperature range in Fahrenheit.
            certifications: Optional list of certifications (e.g., ["ASME", "AWS"]).
        """
        self.name = name
        self.material_type = material_type
        self.composition = composition
        self.tensile_strength_psi = tensile_strength_psi
        self.yield_strength_psi = yield_strength_psi
        self.elongation_percent = elongation_percent
        self.applications = applications
        self.temperature_range_f = temperature_range_f
        self.certifications = certifications or []
    
    def to_dict(self) -> Dict:
        """Convert the WeldingElectrode instance to a dictionary."""
        return {
            "name": self.name,
            "material_type": self.material_type,
            "composition": self.composition,
            "tensile_strength_psi": self.tensile_strength_psi,
            "yield_strength_psi": self.yield_strength_psi,
            "elongation_percent": self.elongation_percent,
            "applications": self.applications,
            "temperature_range_f": self.temperature_range_f,
            "certifications": self.certifications
        }
    
    def __str__(self) -> str:
        """Return a formatted string representation of the WeldingElectrode."""
        certs = ", ".join(self.certifications) if self.certifications else "None"
        comp_str = ", ".join(f"{k}: {v}%" for k, v in self.composition.items())
        apps_str = ", ".join(self.applications)
        
        return (
            f"Name: {self.name}\n"
            f"Material Type: {self.material_type}\n"
            f"Composition: {comp_str}\n"
            f"Tensile Strength: {self.tensile_strength_psi} psi\n"
            f"Yield Strength: {self.yield_strength_psi} psi\n"
            f"Elongation: {self.elongation_percent}%\n"
            f"Applications: {apps_str}\n"
            f"Temperature Range: {self.temperature_range_f or 'Not specified'}\n"
            f"Certifications: {certs}\n"
        )

class RoshakoWeldingProducts:
    """
    A class to manage and display Roshako's welding electrodes and filler metals.
    """
    
    def __init__(self):
        """Initialize the RoshakoWeldingProducts with an empty catalog."""
        self.catalog: List[WeldingElectrode] = []
    
    def add_product(self, product: WeldingElectrode) -> None:
        """Add a welding product to the catalog."""
        if not isinstance(product, WeldingElectrode):
            raise TypeError("Product must be an instance of WeldingElectrode")
        self.catalog.append(product)
    
    def get_product_by_name(self, name: str) -> Optional[WeldingElectrode]:
        """Retrieve a product by its name."""
        for product in self.catalog:
            if product.name.lower() == name.lower():
                return product
        return None
    
    def get_products_by_material(self, material_type: str) -> List[WeldingElectrode]:
        """Retrieve all products of a specific material type."""
        return [p for p in self.catalog if p.material_type.lower() == material_type.lower()]
    
    def display_all_products(self) -> None:
        """Display all products in the catalog."""
        if not self.catalog:
            print("No products available in the catalog.")
            return
        
        for idx, product in enumerate(self.catalog, 1):
            print(f"\nProduct {idx}:")
            print(product)
    
    def save_catalog_to_file(self, filename: str) -> None:
        """Save the catalog to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([p.to_dict() for p in self.catalog], f, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")
    
    def load_catalog_from_file(self, filename: str) -> None:
        """Load the catalog from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.catalog = [WeldingElectrode(**item) for item in data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize Roshako's welding products catalog
    roshako = RoshakoWeldingProducts()
    
    # Add some example products
    alloy_625 = WeldingElectrode(
        name="Alloy 625",
        material_type="Nickel Alloy",
        composition={"Ni": 58.0, "Cr": 21.5, "Mo": 9.0, "Nb": 3.6},
        tensile_strength_psi=120000,
        yield_strength_psi=60000,
        elongation_percent=30.0,
        applications=["Aerospace", "Chemical Processing", "Marine"],
        temperature_range_f="-320 to 1800",
        certifications=["ASME", "AWS"]
    )
    
    hastelloy_c276 = WeldingElectrode(
        name="Hastelloy C-276",
        material_type="Nickel Alloy",
        composition={"Ni": 57.0, "Cr": 15.5, "Mo": 16.0, "W": 3.7, "Fe": 5.5},
        tensile_strength_psi=110000,
        yield_strength_psi=52000,
        elongation_percent=40.0,
        applications=["Chemical Processing", "Pollution Control", "Pharmaceutical"],
        temperature_range_f="-150 to 1900",
        certifications=["ASME", "AWS", "PED"]
    )
    
    roshako.add_product(alloy_625)
    roshako.add_product(hastelloy_c276)
    
    # Display all products
    roshako.display_all_products()
    
    # Save catalog to file (optional)
    roshako.save_catalog_to_file("roshako_welding_catalog.json")
```
