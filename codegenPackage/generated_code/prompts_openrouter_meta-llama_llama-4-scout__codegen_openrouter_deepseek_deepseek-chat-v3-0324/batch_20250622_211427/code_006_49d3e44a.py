"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.com
Prompt: Suggest a reliable sourcing strategy for a cooking oil company that aims to provide consistent availability and fresh products to its customers, based on Authentic Oil's approach.
Generated: DETERMINISTIC_49d3e44a686a2e55
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import datetime
from typing import List, Dict, Optional
from enum import Enum

class SourcingStrategy:
    """
    Defines the sourcing strategy for a cooking oil company to ensure consistent availability
    and fresh products, inspired by Authentic Oil's approach.
    """
    
    class SupplierReliability(Enum):
        """Enum to categorize supplier reliability."""
        HIGH = "High"
        MEDIUM = "Medium"
        LOW = "Low"
    
    class OilType(Enum):
        """Enum to categorize types of cooking oil."""
        OLIVE = "Olive"
        SUNFLOWER = "Sunflower"
        CANOLA = "Canola"
        COCONUT = "Coconut"
        OTHER = "Other"
    
    def __init__(self):
        """Initialize the sourcing strategy with default values."""
        self.suppliers: Dict[str, Dict] = {}  # Key: supplier name, Value: supplier details
        self.min_inventory_levels: Dict[OilType, int] = {
            self.OilType.OLIVE: 1000,
            self.OilType.SUNFLOWER: 1500,
            self.OilType.CANOLA: 1200,
            self.OilType.COCONUT: 800,
            self.OilType.OTHER: 500,
        }
        self.freshness_threshold_days: int = 30  # Max days before oil is considered not fresh
    
    def add_supplier(
        self,
        name: str,
        oil_types: List[OilType],
        reliability: SupplierReliability,
        lead_time_days: int,
        capacity_per_month: int,
    ) -> None:
        """
        Add a supplier to the sourcing strategy.
        
        Args:
            name: Name of the supplier.
            oil_types: List of oil types the supplier provides.
            reliability: Reliability level of the supplier.
            lead_time_days: Average lead time in days for deliveries.
            capacity_per_month: Monthly production capacity in liters.
        """
        if name in self.suppliers:
            raise ValueError(f"Supplier '{name}' already exists.")
        
        self.suppliers[name] = {
            "oil_types": oil_types,
            "reliability": reliability,
            "lead_time_days": lead_time_days,
            "capacity_per_month": capacity_per_month,
        }
    
    def get_reliable_suppliers(self, oil_type: OilType) -> List[str]:
        """
        Retrieve suppliers for a given oil type with HIGH or MEDIUM reliability.
        
        Args:
            oil_type: Type of oil to filter suppliers.
            
        Returns:
            List of supplier names meeting the criteria.
        """
        reliable_suppliers = []
        for name, details in self.suppliers.items():
            if (
                oil_type in details["oil_types"]
                and details["reliability"] in [self.SupplierReliability.HIGH, self.SupplierReliability.MEDIUM]
            ):
                reliable_suppliers.append(name)
        
        if not reliable_suppliers:
            raise ValueError(f"No reliable suppliers found for {oil_type.value} oil.")
        
        return reliable_suppliers
    
    def check_inventory_freshness(self, inventory: Dict[OilType, Dict[str, datetime.date]]) -> Dict[OilType, bool]:
        """
        Check if inventory is fresh based on the freshness threshold.
        
        Args:
            inventory: Dictionary with oil types as keys and values as {"quantity": int, "production_date": date}.
            
        Returns:
            Dictionary with oil types as keys and freshness status (True/False) as values.
        """
        freshness_status = {}
        today = datetime.date.today()
        
        for oil_type, details in inventory.items():
            production_date = details["production_date"]
            days_since_production = (today - production_date).days
            freshness_status[oil_type] = days_since_production <= self.freshness_threshold_days
        
        return freshness_status
    
    def recommend_order_quantity(
        self,
        oil_type: OilType,
        current_inventory: int,
        projected_demand: int,
        supplier_name: Optional[str] = None,
    ) -> int:
        """
        Calculate recommended order quantity to maintain inventory levels and meet demand.
        
        Args:
            oil_type: Type of oil to order.
            current_inventory: Current inventory in liters.
            projected_demand: Projected demand for the next period in liters.
            supplier_name: Optional supplier name to check capacity.
            
        Returns:
            Recommended order quantity in liters.
            
        Raises:
            ValueError: If no reliable suppliers or insufficient capacity.
        """
        min_level = self.min_inventory_levels[oil_type]
        required = max(0, projected_demand + min_level - current_inventory)
        
        if supplier_name:
            supplier = self.suppliers.get(supplier_name)
            if not supplier:
                raise ValueError(f"Supplier '{supplier_name}' not found.")
            if oil_type not in supplier["oil_types"]:
                raise ValueError(f"Supplier '{supplier_name}' does not provide {oil_type.value} oil.")
            if required > supplier["capacity_per_month"]:
                raise ValueError(f"Supplier '{supplier_name}' cannot meet the required quantity.")
        
        return required

# Example usage
if __name__ == "__main__":
    strategy = SourcingStrategy()
    
    # Add suppliers
    strategy.add_supplier(
        "Mediterranean Oils",
        [strategy.OilType.OLIVE, strategy.OilType.SUNFLOWER],
        strategy.SupplierReliability.HIGH,
        10,
        5000,
    )
    strategy.add_supplier(
        "Tropical Harvest",
        [strategy.OilType.COCONUT],
        strategy.SupplierReliability.MEDIUM,
        15,
        3000,
    )
    
    # Check reliable suppliers for Olive oil
    reliable_suppliers = strategy.get_reliable_suppliers(strategy.OilType.OLIVE)
    print(f"Reliable suppliers for Olive oil: {reliable_suppliers}")
    
    # Check inventory freshness
    inventory = {
        strategy.OilType.OLIVE: {
            "quantity": 800,
            "production_date": datetime.date(2023, 10, 1),
        },
        strategy.OilType.COCONUT: {
            "quantity": 400,
            "production_date": datetime.date(2023, 9, 15),
        },
    }
    freshness = strategy.check_inventory_freshness(inventory)
    print(f"Inventory freshness status: {freshness}")
    
    # Recommend order quantity
    try:
        order_qty = strategy.recommend_order_quantity(
            strategy.OilType.OLIVE,
            current_inventory=800,
            projected_demand=2000,
            supplier_name="Mediterranean Oils",
        )
        print(f"Recommended order quantity: {order_qty} liters")
    except ValueError as e:
        print(f"Error: {e}")
```
