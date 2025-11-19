"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: "Write a code snippet to automate the process of generating quotes for custom stainless steel fabrication projects, considering factors like material cost, labor, and equipment usage."
Generated: DETERMINISTIC_3c4fe415e69b5118
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional

class MaterialGrade(Enum):
    """Enum representing different grades of stainless steel."""
    GRADE_304 = "304"
    GRADE_316 = "316"
    GRADE_420 = "420"

class FabricationProcess(Enum):
    """Enum representing different fabrication processes."""
    CUTTING = "cutting"
    WELDING = "welding"
    POLISHING = "polishing"
    BENDING = "bending"

class QuoteCalculator:
    """Class to calculate quotes for stainless steel fabrication projects."""
    
    # Material costs per kg (example values)
    MATERIAL_COSTS = {
        MaterialGrade.GRADE_304: 5.50,
        MaterialGrade.GRADE_316: 7.75,
        MaterialGrade.GRADE_420: 6.25
    }
    
    # Labor costs per hour
    LABOR_COST = 45.00
    
    # Equipment costs per hour
    EQUIPMENT_COSTS = {
        FabricationProcess.CUTTING: 25.00,
        FabricationProcess.WELDING: 30.00,
        FabricationProcess.POLISHING: 20.00,
        FabricationProcess.BENDING: 15.00
    }
    
    def __init__(self):
        """Initialize the quote calculator with default values."""
        self.material_weight = 0.0
        self.material_grade = MaterialGrade.GRADE_304
        self.processes = []
        self.labor_hours = 0.0
    
    def set_material(self, weight: float, grade: MaterialGrade) -> None:
        """Set the material details for the quote.
        
        Args:
            weight: Weight of the material in kilograms.
            grade: Grade of stainless steel.
        """
        if weight <= 0:
            raise ValueError("Material weight must be positive.")
        self.material_weight = weight
        self.material_grade = grade
    
    def add_process(self, process: FabricationProcess, hours: float) -> None:
        """Add a fabrication process to the quote.
        
        Args:
            process: Fabrication process to add.
            hours: Hours required for the process.
        """
        if hours <= 0:
            raise ValueError("Process hours must be positive.")
        self.processes.append((process, hours))
        self.labor_hours += hours
    
    def calculate_material_cost(self) -> float:
        """Calculate the material cost based on weight and grade.
        
        Returns:
            Calculated material cost.
        """
        return self.material_weight * self.MATERIAL_COSTS[self.material_grade]
    
    def calculate_labor_cost(self) -> float:
        """Calculate the labor cost based on hours.
        
        Returns:
            Calculated labor cost.
        """
        return self.labor_hours * self.LABOR_COST
    
    def calculate_equipment_cost(self) -> float:
        """Calculate the equipment cost based on processes.
        
        Returns:
            Calculated equipment cost.
        """
        total = 0.0
        for process, hours in self.processes:
            total += hours * self.EQUIPMENT_COSTS[process]
        return total
    
    def calculate_total_cost(self, markup_percentage: float = 0.2) -> float:
        """Calculate the total cost including markup.
        
        Args:
            markup_percentage: Percentage markup for profit (default 20%).
        
        Returns:
            Total cost including markup.
        """
        if markup_percentage < 0:
            raise ValueError("Markup percentage cannot be negative.")
        
        material_cost = self.calculate_material_cost()
        labor_cost = self.calculate_labor_cost()
        equipment_cost = self.calculate_equipment_cost()
        
        subtotal = material_cost + labor_cost + equipment_cost
        return subtotal * (1 + markup_percentage)
    
    def generate_quote(self, customer_name: str, markup_percentage: float = 0.2) -> Dict:
        """Generate a detailed quote for the customer.
        
        Args:
            customer_name: Name of the customer.
            markup_percentage: Percentage markup for profit (default 20%).
        
        Returns:
            Dictionary containing the quote details.
        """
        if not customer_name:
            raise ValueError("Customer name cannot be empty.")
        
        quote = {
            "customer": customer_name,
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "material": {
                "grade": self.material_grade.value,
                "weight_kg": self.material_weight,
                "cost": round(self.calculate_material_cost(), 2)
            },
            "labor": {
                "hours": self.labor_hours,
                "cost": round(self.calculate_labor_cost(), 2)
            },
            "equipment": {
                "processes": [{"process": p.value, "hours": h} for p, h in self.processes],
                "cost": round(self.calculate_equipment_cost(), 2)
            },
            "subtotal": round(
                self.calculate_material_cost() + 
                self.calculate_labor_cost() + 
                self.calculate_equipment_cost(), 
                2
            ),
            "markup_percentage": markup_percentage * 100,
            "total_cost": round(self.calculate_total_cost(markup_percentage), 2)
        }
        
        return quote

# Example usage
if __name__ == "__main__":
    try:
        calculator = QuoteCalculator()
        calculator.set_material(10.5, MaterialGrade.GRADE_316)
        calculator.add_process(FabricationProcess.CUTTING, 2.0)
        calculator.add_process(FabricationProcess.WELDING, 3.5)
        calculator.add_process(FabricationProcess.POLISHING, 1.0)
        
        quote = calculator.generate_quote("Acme Corp", 0.15)
        print("Generated Quote:")
        print(quote)
    except ValueError as e:
        print(f"Error generating quote: {e}")
```
