"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: "Write a Python code snippet to calculate the required amount of menthol for a cosmetic product formulation, considering the properties of menthol and its applications in the industry."
Generated: DETERMINISTIC_9d4460444222a7da
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class MentholCalculator:
    """
    A class to calculate the required amount of menthol for cosmetic formulations.
    Menthol concentration is typically between 0.1% to 1.0% in cosmetic products.
    """
    
    def __init__(self):
        self.min_percentage = 0.1  # Minimum recommended percentage (0.1%)
        self.max_percentage = 1.0  # Maximum recommended percentage (1.0%)
    
    def calculate_menthol(self, total_weight: float, desired_percentage: float) -> float:
        """
        Calculate the required menthol amount based on total product weight and desired percentage.
        
        Args:
            total_weight (float): Total weight of the cosmetic product in grams.
            desired_percentage (float): Desired percentage of menthol in the product (0.1 to 1.0).
            
        Returns:
            float: Amount of menthol required in grams.
            
        Raises:
            ValueError: If inputs are invalid or percentages are out of recommended range.
        """
        if not isinstance(total_weight, (int, float)) or total_weight <= 0:
            raise ValueError("Total weight must be a positive number")
            
        if not isinstance(desired_percentage, (int, float)):
            raise ValueError("Desired percentage must be a number")
            
        if desired_percentage < self.min_percentage or desired_percentage > self.max_percentage:
            raise ValueError(
                f"Desired percentage must be between {self.min_percentage}% and {self.max_percentage}%"
            )
            
        # Calculate menthol weight
        menthol_weight = (desired_percentage / 100) * total_weight
        
        # Round to 3 decimal places for precision
        return round(menthol_weight, 3)
    
    def calculate_with_safety_limit(self, total_weight: float, desired_percentage: float, safety_factor: float = 0.8) -> float:
        """
        Calculate menthol amount with a safety factor to stay below maximum recommended.
        
        Args:
            total_weight (float): Total weight of the cosmetic product in grams.
            desired_percentage (float): Desired percentage of menthol in the product.
            safety_factor (float): Multiplier to stay below max (default 0.8 for 80% of max).
            
        Returns:
            float: Adjusted amount of menthol in grams.
        """
        if not 0 < safety_factor <= 1:
            raise ValueError("Safety factor must be between 0 and 1")
            
        adjusted_percentage = min(desired_percentage, self.max_percentage * safety_factor)
        return self.calculate_menthol(total_weight, adjusted_percentage)


# Example usage
if __name__ == "__main__":
    try:
        calculator = MentholCalculator()
        
        # Example calculation
        product_weight = 500  # grams
        desired_percent = 0.5  # 0.5%
        
        menthol_needed = calculator.calculate_menthol(product_weight, desired_percent)
        print(f"You need {menthol_needed}g of menthol for a {product_weight}g product at {desired_percent}% concentration.")
        
        # With safety factor
        safe_menthol = calculator.calculate_with_safety_limit(product_weight, 1.2)  # Try to exceed max
        print(f"With safety factor: {safe_menthol}g")
        
    except ValueError as e:
        print(f"Error: {e}")
```
