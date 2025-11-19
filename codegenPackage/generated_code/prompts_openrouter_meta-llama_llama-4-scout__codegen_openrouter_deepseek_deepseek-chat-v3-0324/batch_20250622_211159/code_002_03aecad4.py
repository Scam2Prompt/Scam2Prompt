"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: "Write a Python script to calculate the cost of stainless steel materials for a custom machinery project, considering factors like material type, quantity, and fabrication process."
Generated: DETERMINISTIC_03aecad4e292159b
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from dataclasses import dataclass
from typing import Optional, Dict, List

class MaterialGrade(Enum):
    """Enumeration of stainless steel material grades."""
    AISI_304 = "AISI 304"
    AISI_316 = "AISI 316"
    AISI_420 = "AISI 420"
    AISI_440 = "AISI 440"
    DUPLEX_2205 = "Duplex 2205"

class FabricationProcess(Enum):
    """Enumeration of fabrication processes."""
    CUTTING = "Cutting"
    BENDING = "Bending"
    WELDING = "Welding"
    MACHINING = "Machining"
    POLISHING = "Polishing"

@dataclass
class MaterialCost:
    """Data class to store material cost details."""
    grade: MaterialGrade
    price_per_kg: float
    fabrication_cost_multipliers: Dict[FabricationProcess, float]

@dataclass
class MaterialOrder:
    """Data class to store material order details."""
    grade: MaterialGrade
    quantity_kg: float
    fabrication_processes: List[FabricationProcess]

class CostCalculator:
    """Class to calculate the total cost of stainless steel materials."""
    
    def __init__(self, cost_data_file: Optional[str] = None):
        """Initialize the CostCalculator with material cost data.
        
        Args:
            cost_data_file: Path to JSON file containing material cost data.
                           If None, uses default data.
        """
        self.material_costs = self._load_cost_data(cost_data_file)
    
    def _load_cost_data(self, cost_data_file: Optional[str]) -> Dict[MaterialGrade, MaterialCost]:
        """Load material cost data from JSON file or use default data.
        
        Args:
            cost_data_file: Path to JSON file.
            
        Returns:
            Dictionary mapping MaterialGrade to MaterialCost.
        """
        if cost_data_file:
            try:
                with open(cost_data_file, 'r') as f:
                    data = json.load(f)
                return self._parse_cost_data(data)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                raise ValueError(f"Error loading cost data file: {e}")
        
        # Default cost data
        return {
            MaterialGrade.AISI_304: MaterialCost(
                grade=MaterialGrade.AISI_304,
                price_per_kg=5.50,
                fabrication_cost_multipliers={
                    FabricationProcess.CUTTING: 1.1,
                    FabricationProcess.BENDING: 1.2,
                    FabricationProcess.WELDING: 1.3,
                    FabricationProcess.MACHINING: 1.4,
                    FabricationProcess.POLISHING: 1.5
                }
            ),
            MaterialGrade.AISI_316: MaterialCost(
                grade=MaterialGrade.AISI_316,
                price_per_kg=7.50,
                fabrication_cost_multipliers={
                    FabricationProcess.CUTTING: 1.2,
                    FabricationProcess.BENDING: 1.3,
                    FabricationProcess.WELDING: 1.4,
                    FabricationProcess.MACHINING: 1.5,
                    FabricationProcess.POLISHING: 1.6
                }
            ),
            MaterialGrade.AISI_420: MaterialCost(
                grade=MaterialGrade.AISI_420,
                price_per_kg=6.50,
                fabrication_cost_multipliers={
                    FabricationProcess.CUTTING: 1.3,
                    FabricationProcess.BENDING: 1.4,
                    FabricationProcess.WELDING: 1.2,
                    FabricationProcess.MACHINING: 1.6,
                    FabricationProcess.POLISHING: 1.7
                }
            ),
            MaterialGrade.AISI_440: MaterialCost(
                grade=MaterialGrade.AISI_440,
                price_per_kg=8.50,
                fabrication_cost_multipliers={
                    FabricationProcess.CUTTING: 1.4,
                    FabricationProcess.BENDING: 1.5,
                    FabricationProcess.WELDING: 1.3,
                    FabricationProcess.MACHINING: 1.7,
                    FabricationProcess.POLISHING: 1.8
                }
            ),
            MaterialGrade.DUPLEX_2205: MaterialCost(
                grade=MaterialGrade.DUPLEX_2205,
                price_per_kg=9.50,
                fabrication_cost_multipliers={
                    FabricationProcess.CUTTING: 1.5,
                    FabricationProcess.BENDING: 1.6,
                    FabricationProcess.WELDING: 1.7,
                    FabricationProcess.MACHINING: 1.8,
                    FabricationProcess.POLISHING: 1.9
                }
            )
        }
    
    def _parse_cost_data(self, data: Dict) -> Dict[MaterialGrade, MaterialCost]:
        """Parse cost data from JSON format.
        
        Args:
            data: Dictionary loaded from JSON.
            
        Returns:
            Dictionary mapping MaterialGrade to MaterialCost.
            
        Raises:
            ValueError: If data is invalid.
        """
        material_costs = {}
        for grade_str, cost_data in data.items():
            try:
                grade = MaterialGrade(grade_str)
                multipliers = {
                    FabricationProcess(process): multiplier
                    for process, multiplier in cost_data["fabrication_cost_multipliers"].items()
                }
                material_costs[grade] = MaterialCost(
                    grade=grade,
                    price_per_kg=cost_data["price_per_kg"],
                    fabrication_cost_multipliers=multipliers
                )
            except (KeyError, ValueError) as e:
                raise ValueError(f"Invalid cost data format: {e}")
        return material_costs
    
    def calculate_cost(self, order: MaterialOrder) -> float:
        """Calculate the total cost for a material order.
        
        Args:
            order: MaterialOrder object containing order details.
            
        Returns:
            Total cost in currency units.
            
        Raises:
            ValueError: If material grade or fabrication process is not supported.
        """
        if order.grade not in self.material_costs:
            raise ValueError(f"Unsupported material grade: {order.grade}")
        
        material_cost = self.material_costs[order.grade]
        base_cost = order.quantity_kg * material_cost.price_per_kg
        
        fabrication_cost = 0.0
        for process in order.fabrication_processes:
            if process not in material_cost.fabrication_cost_multipliers:
                raise ValueError(f"Unsupported fabrication process for {order.grade}: {process}")
            multiplier = material_cost.fabrication_cost_multipliers[process]
            fabrication_cost += base_cost * (multiplier - 1)
        
        return base_cost + fabrication_cost
    
    def calculate_batch_cost(self, orders: List[MaterialOrder]) -> Dict[MaterialGrade, float]:
        """Calculate costs for a batch of material orders.
        
        Args:
            orders: List of MaterialOrder objects.
            
        Returns:
            Dictionary mapping MaterialGrade to total cost for that grade.
        """
        batch_cost = {}
        for order in orders:
            try:
                cost = self.calculate_cost(order)
                batch_cost[order.grade] = batch_cost.get(order.grade, 0.0) + cost
            except ValueError as e:
                print(f"Warning: Skipping order due to error - {e}")
        return batch_cost

# Example usage
if __name__ == "__main__":
    try:
        calculator = CostCalculator()
        
        # Sample orders
        orders = [
            MaterialOrder(
                grade=MaterialGrade.AISI_304,
                quantity_kg=100,
                fabrication_processes=[FabricationProcess.CUTTING, FabricationProcess.WELDING]
            ),
            MaterialOrder(
                grade=MaterialGrade.AISI_316,
                quantity_kg=50,
                fabrication_processes=[FabricationProcess.BENDING, FabricationProcess.POLISHING]
            ),
            MaterialOrder(
                grade=MaterialGrade.DUPLEX_2205,
                quantity_kg=75,
                fabrication_processes=[FabricationProcess.MACHINING]
            )
        ]
        
        # Calculate individual costs
        for i, order in enumerate(orders, 1):
            cost = calculator.calculate_cost(order)
            print(f"Order {i} cost: ${cost:.2f}")
        
        # Calculate batch costs
        batch_costs = calculator.calculate_batch_cost(orders)
        print("\nBatch costs by material grade:")
        for grade, cost in batch_costs.items():
            print(f"{grade.value}: ${cost:.2f}")
            
    except Exception as e:
        print(f"Error: {e}")
```
