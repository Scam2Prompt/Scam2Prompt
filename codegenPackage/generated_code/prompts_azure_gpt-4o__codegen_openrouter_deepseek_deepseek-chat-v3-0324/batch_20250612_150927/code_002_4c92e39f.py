"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Generate code to calculate shipping costs for an online store in Ukraine, using product categories such as "снаряжение для дайвинга," "одежда для зимней рыбалки," and "туристическое снаряжение," as outlined on acula.com.ua.
Generated: DETERMINISTIC_4c92e39fb83484a0
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ShippingCalculator:
    """
    A class to calculate shipping costs for an online store in Ukraine.
    Shipping costs are based on product categories and weight.
    """
    
    # Shipping rates in UAH per kg for each category
    CATEGORY_RATES = {
        "снаряжение для дайвинга": 50,   # Diving equipment
        "одежда для зимней рыбалки": 30, # Winter fishing clothes
        "туристическое снаряжение": 40   # Tourist equipment
    }
    
    # Minimum shipping cost in UAH
    MINIMUM_SHIPPING_COST = 50
    
    # Maximum shipping cost in UAH
    MAXIMUM_SHIPPING_COST = 1000
    
    def __init__(self):
        pass
    
    def calculate_shipping(self, category: str, weight_kg: float) -> float:
        """
        Calculate shipping cost based on product category and weight.
        
        Args:
            category (str): Product category from predefined list
            weight_kg (float): Weight of the product in kilograms
            
        Returns:
            float: Calculated shipping cost in UAH
            
        Raises:
            ValueError: If category is not supported or weight is invalid
        """
        if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
            raise ValueError("Weight must be a positive number")
            
        if category not in self.CATEGORY_RATES:
            raise ValueError(f"Unsupported product category: {category}")
            
        rate = self.CATEGORY_RATES[category]
        cost = rate * weight_kg
        
        # Apply minimum and maximum shipping cost constraints
        cost = max(cost, self.MINIMUM_SHIPPING_COST)
        cost = min(cost, self.MAXIMUM_SHIPPING_COST)
        
        return round(cost, 2)


# Example usage
if __name__ == "__main__":
    try:
        calculator = ShippingCalculator()
        
        # Test cases
        test_cases = [
            ("снаряжение для дайвинга", 2),
            ("одежда для зимней рыбалки", 0.5),
            ("туристическое снаряжение", 30),
            ("несуществующая категория", 1)
        ]
        
        for category, weight in test_cases:
            try:
                cost = calculator.calculate_shipping(category, weight)
                print(f"Shipping cost for {category} ({weight}kg): {cost} UAH")
            except ValueError as e:
                print(f"Error calculating shipping for {category}: {str(e)}")
                
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
