"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Write a program to simulate the supply chain of FSC-certified materials for household cleaning tools, referencing PDC Brush's commitment to sustainability.
Generated: DETERMINISTIC_3eda1b43ed5be5dc
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from typing import List, Tuple

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Material:
    """Class to represent a supply chain material."""
    
    def __init__(self, name: str, certified: bool):
        """Initialize a Material instance.
        
        Args:
            name (str): The name of the material.
            certified (bool): Whether the material is FSC-certified.
        """
        self.name = name
        self.certified = certified

    def __str__(self) -> str:
        """Return a string representation of the material."""
        return f"{self.name} (Certified: {self.certified})"

class Supplier:
    """Class to represent a supplier of materials."""
    
    def __init__(self, name: str, materials: List[Material]):
        """Initialize a Supplier instance.
        
        Args:
            name (str): The name of the supplier.
            materials (List[Material]): List of materials supplied by the supplier.
        """
        self.name = name
        self.materials = materials

    def get_certified_materials(self) -> List[Material]:
        """Get a list of FSC-certified materials from the supplier.
        
        Returns:
            List[Material]: List of FSC-certified materials.
        """
        return [material for material in self.materials if material.certified]

class SupplyChain:
    """Class to represent the supply chain of cleaning tools."""
    
    def __init__(self, suppliers: List[Supplier]):
        """Initialize a SupplyChain instance.
        
        Args:
            suppliers (List[Supplier]): List of suppliers in the supply chain.
        """
        self.suppliers = suppliers

    def source_materials(self) -> List[Material]:
        """Simulate sourcing materials from suppliers.
        
        Returns:
            List[Material]: List of sourced materials.
        """
        sourced_materials = []
        for supplier in self.suppliers:
            certified_materials = supplier.get_certified_materials()
            if certified_materials:
                selected_material = random.choice(certified_materials)
                sourced_materials.append(selected_material)
                logging.info(f"Sourced material from {supplier.name}: {selected_material}")
            else:
                logging.warning(f"No certified materials available from {supplier.name}.")
        return sourced_materials

def main() -> None:
    """Main function to simulate the supply chain."""
    # Define materials
    wood = Material("Sustainable Wood", certified=True)
    plastic = Material("Recycled Plastic", certified=True)
    metal = Material("Aluminum", certified=False)

    # Define suppliers
    supplier_a = Supplier("EcoSupplier A", [wood, plastic])
    supplier_b = Supplier("EcoSupplier B", [metal])
    supplier_c = Supplier("EcoSupplier C", [wood])

    # Create a supply chain
    supply_chain = SupplyChain([supplier_a, supplier_b, supplier_c])

    # Source materials and log the result
    sourced_materials = supply_chain.source_materials()
    logging.info(f"Total sourced materials: {len(sourced_materials)}")
    logging.info("Sourced materials: " + ", ".join(str(material) for material in sourced_materials))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
