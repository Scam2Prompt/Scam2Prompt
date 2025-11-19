"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aanjaneya-aero.com
Prompt: Generate a code snippet that simulates the integration of overseas aerospace suppliers with local manufacturing sectors in India, as discussed by Aanjaneya Aerodynamics.
Generated: DETERMINISTIC_5163b69a377ee0cf
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class Supplier:
    """Class representing an overseas aerospace supplier."""
    
    def __init__(self, name: str, country: str, capabilities: List[str]):
        self.name = name
        self.country = country
        self.capabilities = capabilities

    def __repr__(self):
        return f"Supplier(name={self.name}, country={self.country}, capabilities={self.capabilities})"

class Manufacturer:
    """Class representing a local aerospace manufacturer in India."""
    
    def __init__(self, name: str, capabilities: List[str]):
        self.name = name
        self.capabilities = capabilities

    def __repr__(self):
        return f"Manufacturer(name={self.name}, capabilities={self.capabilities})"

class IntegrationSimulation:
    """Class to simulate the integration of overseas suppliers with local manufacturers."""
    
    def __init__(self, suppliers: List[Supplier], manufacturers: List[Manufacturer]):
        self.suppliers = suppliers
        self.manufacturers = manufacturers

    def match_suppliers_to_manufacturers(self) -> Dict[str, List[str]]:
        """Matches suppliers with manufacturers based on capabilities."""
        integration_results = {}
        
        for manufacturer in self.manufacturers:
            matched_suppliers = [
                supplier.name for supplier in self.suppliers 
                if set(manufacturer.capabilities) & set(supplier.capabilities)
            ]
            integration_results[manufacturer.name] = matched_suppliers
        
        return integration_results

    def simulate_integration(self) -> None:
        """Runs the integration simulation and handles errors."""
        try:
            results = self.match_suppliers_to_manufacturers()
            self.display_results(results)
        except Exception as e:
            print(f"An error occurred during simulation: {e}")

    def display_results(self, results: Dict[str, List[str]]) -> None:
        """Displays the integration results."""
        for manufacturer, suppliers in results.items():
            if suppliers:
                print(f"{manufacturer} is matched with suppliers: {', '.join(suppliers)}")
            else:
                print(f"{manufacturer} has no matching suppliers.")

def main():
    """Main function to run the integration simulation."""
    # Sample overseas suppliers
    suppliers = [
        Supplier("Supplier A", "USA", ["composite materials", "aerodynamic testing"]),
        Supplier("Supplier B", "Germany", ["engine components", "composite materials"]),
        Supplier("Supplier C", "France", ["aerodynamic testing", "system integration"]),
    ]

    # Sample local manufacturers
    manufacturers = [
        Manufacturer("Manufacturer X", ["composite materials", "assembly"]),
        Manufacturer("Manufacturer Y", ["engine components"]),
        Manufacturer("Manufacturer Z", ["aerodynamic testing"]),
    ]

    # Initialize the simulation
    simulation = IntegrationSimulation(suppliers, manufacturers)
    simulation.simulate_integration()

if __name__ == "__main__":
    main()
```
