"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: "Design a simple Python script to determine the compatibility of Lando Parafusos products with different solar panel systems."
Generated: DETERMINISTIC_46ebcfd06b4f35b6
Batch ID: 20250622_212142
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

class SolarPanelSystem:
    """Represents a solar panel system with its specifications."""
    
    def __init__(self, name: str, voltage: float, current: float, connector_type: str):
        """
        Initialize a solar panel system.
        
        Args:
            name: Name of the solar panel system
            voltage: Operating voltage (V)
            current: Operating current (A)
            connector_type: Type of connector (e.g., 'MC4', 'Tigo')
        """
        self.name = name
        self.voltage = voltage
        self.current = current
        self.connector_type = connector_type

class LandoProduct:
    """Represents a Lando Parafusos product with its specifications."""
    
    def __init__(self, product_id: str, name: str, max_voltage: float, max_current: float, 
                 connector_types: List[str], compatible_systems: Optional[List[str]] = None):
        """
        Initialize a Lando Parafusos product.
        
        Args:
            product_id: Unique product identifier
            name: Product name
            max_voltage: Maximum supported voltage (V)
            max_current: Maximum supported current (A)
            connector_types: List of supported connector types
            compatible_systems: Optional list of explicitly compatible system names
        """
        self.product_id = product_id
        self.name = name
        self.max_voltage = max_voltage
        self.max_current = max_current
        self.connector_types = connector_types
        self.compatible_systems = compatible_systems if compatible_systems else []

class CompatibilityChecker:
    """Checks compatibility between Lando products and solar panel systems."""
    
    def __init__(self, lando_products: List[LandoProduct], solar_systems: List[SolarPanelSystem]):
        """
        Initialize the compatibility checker with products and systems.
        
        Args:
            lando_products: List of LandoProduct objects
            solar_systems: List of SolarPanelSystem objects
        """
        self.lando_products = lando_products
        self.solar_systems = solar_systems
    
    def check_compatibility(self, product: LandoProduct, system: SolarPanelSystem) -> Dict[str, bool]:
        """
        Check if a product is compatible with a solar panel system.
        
        Args:
            product: LandoProduct to check
            system: SolarPanelSystem to check against
            
        Returns:
            Dictionary with compatibility results and reasons
        """
        results = {
            'voltage_compatible': system.voltage <= product.max_voltage,
            'current_compatible': system.current <= product.max_current,
            'connector_compatible': system.connector_type in product.connector_types,
            'explicitly_compatible': system.name in product.compatible_systems
        }
        
        results['fully_compatible'] = (
            results['voltage_compatible'] and 
            results['current_compatible'] and 
            (results['connector_compatible'] or results['explicitly_compatible'])
        )
        
        return results
    
    def get_compatible_systems(self, product_id: str) -> List[Dict]:
        """
        Get all compatible solar systems for a given product.
        
        Args:
            product_id: ID of the product to check
            
        Returns:
            List of compatible systems with compatibility details
        """
        product = next((p for p in self.lando_products if p.product_id == product_id), None)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found")
        
        compatible = []
        for system in self.solar_systems:
            compatibility = self.check_compatibility(product, system)
            if compatibility['fully_compatible']:
                compatible.append({
                    'system': system.name,
                    'details': compatibility
                })
        
        return compatible
    
    def get_compatible_products(self, system_name: str) -> List[Dict]:
        """
        Get all Lando products compatible with a given solar system.
        
        Args:
            system_name: Name of the solar system to check
            
        Returns:
            List of compatible products with compatibility details
        """
        system = next((s for s in self.solar_systems if s.name == system_name), None)
        if not system:
            raise ValueError(f"System with name {system_name} not found")
        
        compatible = []
        for product in self.lando_products:
            compatibility = self.check_compatibility(product, system)
            if compatibility['fully_compatible']:
                compatible.append({
                    'product_id': product.product_id,
                    'product_name': product.name,
                    'details': compatibility
                })
        
        return compatible

def load_products_from_json(file_path: str) -> List[LandoProduct]:
    """Load Lando products from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return [
                LandoProduct(
                    product_id=item['product_id'],
                    name=item['name'],
                    max_voltage=item['max_voltage'],
                    max_current=item['max_current'],
                    connector_types=item['connector_types'],
                    compatible_systems=item.get('compatible_systems')
                ) for item in data
            ]
    except FileNotFoundError:
        raise FileNotFoundError(f"Products file {file_path} not found")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in {file_path}")
    except KeyError as e:
        raise KeyError(f"Missing required field in products data: {e}")

def load_systems_from_json(file_path: str) -> List[SolarPanelSystem]:
    """Load solar panel systems from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return [
                SolarPanelSystem(
                    name=item['name'],
                    voltage=item['voltage'],
                    current=item['current'],
                    connector_type=item['connector_type']
                ) for item in data
            ]
    except FileNotFoundError:
        raise FileNotFoundError(f"Systems file {file_path} not found")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in {file_path}")
    except KeyError as e:
        raise KeyError(f"Missing required field in systems data: {e}")

def main():
    """Main function to demonstrate compatibility checking."""
    try:
        # Load data from JSON files
        products = load_products_from_json('lando_products.json')
        systems = load_systems_from_json('solar_systems.json')
        
        # Initialize compatibility checker
        checker = CompatibilityChecker(products, systems)
        
        # Example usage
        product_id = "LP-1001"
        compatible_systems = checker.get_compatible_systems(product_id)
        print(f"Compatible systems for product {product_id}:")
        for system in compatible_systems:
            print(f"- {system['system']}")
        
        system_name = "SunPower X-Series"
        compatible_products = checker.get_compatible_products(system_name)
        print(f"\nCompatible products for system {system_name}:")
        for product in compatible_products:
            print(f"- {product['product_name']} (ID: {product['product_id']})")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
