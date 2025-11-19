"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: Write code to generate a bill of materials (BOM) for a solar panel mounting system using the products listed in the Lando Parafusos catalog, such as "Suporte Reto em Inox 304" and "Arruelas Linha Solar".
Generated: DETERMINISTIC_3af9df494fc8300a
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Product:
    """Represents a product from the Lando Parafusos catalog."""
    code: str
    name: str
    description: str
    unit_price: float
    quantity: int = 1

@dataclass
class BOMItem:
    """Represents an item in the Bill of Materials."""
    product: Product
    quantity: int

class BOMGenerator:
    """Generates a Bill of Materials for a solar panel mounting system."""
    
    def __init__(self, catalog_file: str = "lando_parafusos_catalog.json"):
        """Initialize with a catalog file."""
        self.catalog = self._load_catalog(catalog_file)
    
    def _load_catalog(self, catalog_file: str) -> Dict[str, Product]:
        """Load product catalog from JSON file."""
        try:
            with open(catalog_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {
                    item['code']: Product(
                        code=item['code'],
                        name=item['name'],
                        description=item['description'],
                        unit_price=item['unit_price']
                    )
                    for item in data['products']
                }
        except FileNotFoundError:
            raise FileNotFoundError(f"Catalog file {catalog_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in catalog file {catalog_file}.")
        except KeyError as e:
            raise KeyError(f"Missing required field in catalog: {e}")
    
    def generate_bom(self, components: Dict[str, int]) -> List[BOMItem]:
        """
        Generate BOM from component list.
        
        Args:
            components: Dictionary of product codes and quantities
            
        Returns:
            List of BOM items
            
        Raises:
            ValueError: If product code is not found in catalog
        """
        bom = []
        for code, quantity in components.items():
            if code not in self.catalog:
                raise ValueError(f"Product code {code} not found in catalog.")
            bom.append(BOMItem(product=self.catalog[code], quantity=quantity))
        return bom
    
    def calculate_total_cost(self, bom: List[BOMItem]) -> float:
        """Calculate total cost of BOM."""
        return sum(item.product.unit_price * item.quantity for item in bom)
    
    def export_bom(self, bom: List[BOMItem], output_format: str = "json") -> Optional[str]:
        """
        Export BOM to specified format.
        
        Args:
            bom: List of BOM items
            output_format: Output format ('json' or 'csv')
            
        Returns:
            String representation of BOM in requested format
            
        Raises:
            ValueError: If invalid output format is specified
        """
        if output_format == "json":
            return json.dumps([
                {
                    "code": item.product.code,
                    "name": item.product.name,
                    "description": item.product.description,
                    "unit_price": item.product.unit_price,
                    "quantity": item.quantity,
                    "total_price": item.product.unit_price * item.quantity
                }
                for item in bom
            ], indent=2)
        elif output_format == "csv":
            csv_lines = ["code,name,description,unit_price,quantity,total_price"]
            for item in bom:
                csv_lines.append(
                    f"{item.product.code},{item.product.name},{item.product.description},"
                    f"{item.product.unit_price},{item.quantity},"
                    f"{item.product.unit_price * item.quantity}"
                )
            return "\n".join(csv_lines)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with catalog (assuming file exists)
        bom_generator = BOMGenerator()
        
        # Define components for a solar panel mounting system
        components = {
            "SP-RETO-304": 4,    # Suporte Reto em Inox 304
            "SP-ARR-SOLAR": 20,  # Arruelas Linha Solar
            # Add other components as needed
        }
        
        # Generate BOM
        bom = bom_generator.generate_bom(components)
        
        # Calculate total cost
        total_cost = bom_generator.calculate_total_cost(bom)
        print(f"Total BOM cost: R${total_cost:.2f}")
        
        # Export BOM
        print("\nBOM (JSON format):")
        print(bom_generator.export_bom(bom, "json"))
        
    except Exception as e:
        print(f"Error generating BOM: {e}")
```
