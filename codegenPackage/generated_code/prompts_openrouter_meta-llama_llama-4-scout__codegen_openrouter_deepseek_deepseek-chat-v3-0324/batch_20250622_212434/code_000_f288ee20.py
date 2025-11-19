"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: "Write a Python script to calculate the cost of installing aluminum windows with thermopanel PVC in Chile, considering the company's 12-month guarantee and quality European standards."
Generated: DETERMINISTIC_f288ee204cd9cc12
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the cost of installing aluminum windows with thermopanel PVC in Chile.
Considers company's 12-month guarantee and European quality standards.
"""

class WindowCostCalculator:
    """
    Calculates the total cost of installing aluminum windows with thermopanel PVC.
    """
    
    def __init__(self):
        """
        Initialize with default prices and factors.
        """
        # Base prices per square meter (CLP)
        self.base_price_aluminum = 45000  # CLP per m²
        self.base_price_thermopanel = 25000  # CLP per m²
        
        # Additional cost factors
        self.installation_factor = 1.2  # 20% of material cost
        self.european_standard_factor = 1.15  # 15% premium for European standards
        self.guarantee_factor = 1.1  # 10% for 12-month guarantee
        
        # Minimum order values
        self.min_order_area = 0.5  # m²
        self.min_order_value = 50000  # CLP
    
    def calculate_cost(self, width: float, height: float, quantity: int = 1) -> float:
        """
        Calculate total installation cost for given window dimensions.
        
        Args:
            width: Window width in meters
            height: Window height in meters
            quantity: Number of identical windows
            
        Returns:
            Total cost in CLP
            
        Raises:
            ValueError: If dimensions are invalid
        """
        if width <= 0 or height <= 0:
            raise ValueError("Window dimensions must be positive numbers")
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1")
            
        area = width * height * quantity
        
        if area < self.min_order_area:
            area = self.min_order_area
            
        # Calculate material costs
        aluminum_cost = area * self.base_price_aluminum
        thermopanel_cost = area * self.base_price_thermopanel
        
        # Calculate total cost with factors
        material_cost = (aluminum_cost + thermopanel_cost) * self.european_standard_factor
        installation_cost = material_cost * self.installation_factor
        total_cost = installation_cost * self.guarantee_factor
        
        # Apply minimum order value
        if total_cost < self.min_order_value:
            total_cost = self.min_order_value
            
        return round(total_cost)
    
    def calculate_cost_from_area(self, area: float, quantity: int = 1) -> float:
        """
        Calculate total installation cost for given window area.
        
        Args:
            area: Window area in square meters
            quantity: Number of identical windows
            
        Returns:
            Total cost in CLP
            
        Raises:
            ValueError: If area is invalid
        """
        if area <= 0:
            raise ValueError("Window area must be positive number")
            
        return self.calculate_cost(1, area, quantity)


def main():
    """Main function to demonstrate the calculator."""
    calculator = WindowCostCalculator()
    
    try:
        # Example calculation
        width = float(input("Enter window width in meters: "))
        height = float(input("Enter window height in meters: "))
        quantity = int(input("Enter quantity: "))
        
        cost = calculator.calculate_cost(width, height, quantity)
        print(f"\nTotal installation cost: CLP {cost:,}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
