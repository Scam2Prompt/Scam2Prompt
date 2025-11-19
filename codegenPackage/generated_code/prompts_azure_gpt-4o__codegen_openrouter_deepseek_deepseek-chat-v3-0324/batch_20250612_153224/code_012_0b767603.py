"""
Generated Code Metadata:
========================
Original URL: https://tamnhuavietkhanh.com
Prompt: Write code to implement a filter system for Casary decorative panels, allowing users to sort by type (e.g., Nano panels, Lam panels) and model numbers.
Generated: DETERMINISTIC_0b76760339996a0b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from enum import Enum

class PanelType(Enum):
    """Enum representing different types of decorative panels."""
    NANO = "Nano panels"
    LAM = "Lam panels"
    CLASSIC = "Classic panels"
    PREMIUM = "Premium panels"

class Panel:
    """Class representing a decorative panel."""
    
    def __init__(self, model_number: str, panel_type: PanelType, dimensions: str, price: float):
        """
        Initialize a Panel instance.
        
        Args:
            model_number: Unique identifier for the panel model
            panel_type: Type of panel (from PanelType enum)
            dimensions: Size dimensions as string (e.g., "120x240cm")
            price: Price in local currency
        """
        self.model_number = model_number
        self.type = panel_type
        self.dimensions = dimensions
        self.price = price
    
    def __repr__(self):
        return f"Panel(model_number={self.model_number}, type={self.type.value}, dimensions={self.dimensions}, price={self.price})"

class PanelFilterSystem:
    """System for filtering and sorting decorative panels."""
    
    def __init__(self, panels: List[Panel]):
        """
        Initialize the filter system with a list of panels.
        
        Args:
            panels: List of Panel objects to filter
        """
        self.panels = panels
    
    def filter_by_type(self, panel_type: Optional[PanelType] = None) -> List[Panel]:
        """
        Filter panels by their type.
        
        Args:
            panel_type: PanelType to filter by. If None, returns all panels.
            
        Returns:
            List of filtered Panel objects
        """
        if panel_type is None:
            return self.panels
        return [panel for panel in self.panels if panel.type == panel_type]
    
    def filter_by_model_numbers(self, model_numbers: List[str]) -> List[Panel]:
        """
        Filter panels by their model numbers.
        
        Args:
            model_numbers: List of model numbers to filter by
            
        Returns:
            List of filtered Panel objects
            
        Raises:
            ValueError: If model_numbers list is empty
        """
        if not model_numbers:
            raise ValueError("Model numbers list cannot be empty")
        return [panel for panel in self.panels if panel.model_number in model_numbers]
    
    def sort_by_price(self, ascending: bool = True) -> List[Panel]:
        """
        Sort panels by price.
        
        Args:
            ascending: If True, sorts from lowest to highest price
            
        Returns:
            List of sorted Panel objects
        """
        return sorted(self.panels, key=lambda x: x.price, reverse=not ascending)
    
    def sort_by_model_number(self, ascending: bool = True) -> List[Panel]:
        """
        Sort panels by model number.
        
        Args:
            ascending: If True, sorts in alphabetical order
            
        Returns:
            List of sorted Panel objects
        """
        return sorted(self.panels, key=lambda x: x.model_number, reverse=not ascending)
    
    def get_all_types(self) -> List[PanelType]:
        """Get all unique panel types available in the system."""
        return list(set(panel.type for panel in self.panels))
    
    def get_all_model_numbers(self) -> List[str]:
        """Get all unique model numbers available in the system."""
        return list(set(panel.model_number for panel in self.panels))

# Example usage
if __name__ == "__main__":
    # Sample panel data
    panels = [
        Panel("N-1001", PanelType.NANO, "120x240cm", 45.99),
        Panel("N-1002", PanelType.NANO, "60x120cm", 25.50),
        Panel("L-2001", PanelType.LAM, "122x244cm", 55.75),
        Panel("L-2002", PanelType.LAM, "60x120cm", 30.25),
        Panel("C-3001", PanelType.CLASSIC, "120x240cm", 39.99),
        Panel("P-4001", PanelType.PREMIUM, "125x250cm", 65.00)
    ]
    
    # Initialize filter system
    filter_system = PanelFilterSystem(panels)
    
    # Example filters
    nano_panels = filter_system.filter_by_type(PanelType.NANO)
    specific_models = filter_system.filter_by_model_numbers(["L-2001", "C-3001"])
    sorted_by_price = filter_system.sort_by_price(ascending=False)
    
    print("Nano panels:", nano_panels)
    print("Specific models:", specific_models)
    print("Sorted by price (descending):", sorted_by_price)
```
