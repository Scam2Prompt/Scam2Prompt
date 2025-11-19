"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Write Python code to calculate the cost of cabinetry installation based on parameters like kitchen size, number of cabinets, and additional services such as demolition or appliance relocation, referencing the services offered by United Cabinetry.
Generated: DETERMINISTIC_1027b407cd0f77ff
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CabinetryCostCalculator:
    """
    A class to calculate the cost of cabinetry installation based on various parameters.
    """
    
    def __init__(self):
        # Base prices
        self.base_cabinet_price = 200  # per cabinet
        self.wall_cabinet_price = 150  # per cabinet
        self.pantry_cabinet_price = 300  # per pantry cabinet
        
        # Additional services
        self.demolition_cost = 500  # flat rate
        self.appliance_relocation_cost = 300  # per appliance
        self.countertop_installation_cost = 40  # per sqft
        
        # Size multipliers
        self.small_kitchen_multiplier = 1.0  # < 100 sqft
        self.medium_kitchen_multiplier = 1.2  # 100-200 sqft
        self.large_kitchen_multiplier = 1.4  # > 200 sqft
        
    def calculate_installation_cost(
        self,
        base_cabinets: int,
        wall_cabinets: int,
        pantry_cabinets: int,
        kitchen_size_sqft: float,
        needs_demolition: bool = False,
        appliances_to_relocate: int = 0,
        countertop_sqft: float = 0
    ) -> float:
        """
        Calculate the total cost of cabinetry installation.
        
        Args:
            base_cabinets: Number of base cabinets
            wall_cabinets: Number of wall cabinets
            pantry_cabinets: Number of pantry cabinets
            kitchen_size_sqft: Size of kitchen in square feet
            needs_demolition: Whether demolition is required
            appliances_to_relocate: Number of appliances to relocate
            countertop_sqft: Square footage of countertop to install
            
        Returns:
            Total installation cost
        """
        try:
            # Validate inputs
            if any(arg < 0 for arg in [base_cabinets, wall_cabinets, pantry_cabinets, kitchen_size_sqft, appliances_to_relocate, countertop_sqft]):
                raise ValueError("All numeric inputs must be non-negative")
            
            # Calculate cabinet costs
            cabinet_cost = (
                (base_cabinets * self.base_cabinet_price) +
                (wall_cabinets * self.wall_cabinet_price) +
                (pantry_cabinets * self.pantry_cabinet_price)
            )
            
            # Apply kitchen size multiplier
            if kitchen_size_sqft < 100:
                size_multiplier = self.small_kitchen_multiplier
            elif 100 <= kitchen_size_sqft <= 200:
                size_multiplier = self.medium_kitchen_multiplier
            else:
                size_multiplier = self.large_kitchen_multiplier
                
            cabinet_cost *= size_multiplier
            
            # Calculate additional services
            additional_services_cost = 0
            if needs_demolition:
                additional_services_cost += self.demolition_cost
            additional_services_cost += appliances_to_relocate * self.appliance_relocation_cost
            additional_services_cost += countertop_sqft * self.countertop_installation_cost
            
            total_cost = cabinet_cost + additional_services_cost
            return round(total_cost, 2)
            
        except ValueError as e:
            print(f"Error in calculation: {e}")
            return 0.0
        except Exception as e:
            print(f"Unexpected error: {e}")
            return 0.0


# Example usage
if __name__ == "__main__":
    calculator = CabinetryCostCalculator()
    
    # Sample calculation
    cost = calculator.calculate_installation_cost(
        base_cabinets=10,
        wall_cabinets=8,
        pantry_cabinets=2,
        kitchen_size_sqft=150,
        needs_demolition=True,
        appliances_to_relocate=2,
        countertop_sqft=30
    )
    
    print(f"Total installation cost: ${cost:,.2f}")
```
