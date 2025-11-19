"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Write a Python script to calculate the cost of exchanging an old Suzuki car for a new one, incorporating features from Suzuki Capital Motors' Certified Used Car Program, such as free evaluation and up to one-year warranty.
Generated: DETERMINISTIC_c55ba55f4a4638c5
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class SuzukiCarExchangeCalculator:
    """
    A class to calculate the cost of exchanging an old Suzuki car for a new one,
    incorporating features from Suzuki Capital Motors' Certified Used Car Program.
    """
    
    def __init__(self):
        """
        Initialize the calculator with default values.
        """
        self.current_year = datetime.datetime.now().year
        self.warranty_duration = 1  # Default warranty duration in years
        self.evaluation_fee = 0     # Free evaluation
        self.base_warranty_cost = 500  # Base cost for warranty (if not free)
        
    def calculate_exchange_cost(self, new_car_price, old_car_value, old_car_year, apply_warranty=True):
        """
        Calculate the total cost of exchanging an old Suzuki car for a new one.
        
        Args:
            new_car_price (float): Price of the new Suzuki car.
            old_car_value (float): Estimated value of the old car.
            old_car_year (int): Manufacturing year of the old car.
            apply_warranty (bool): Whether to include the warranty in the calculation.
            
        Returns:
            dict: A dictionary containing the breakdown of costs and the total cost.
            
        Raises:
            ValueError: If any input is invalid.
        """
        try:
            # Validate inputs
            if not all(isinstance(val, (int, float)) for val in [new_car_price, old_car_value]):
                raise ValueError("Prices must be numeric values.")
            if not isinstance(old_car_year, int) or old_car_year > self.current_year:
                raise ValueError("Invalid car year.")
            if new_car_price <= 0 or old_car_value < 0:
                raise ValueError("Prices must be positive values.")
                
            # Calculate age of old car
            car_age = self.current_year - old_car_year
            
            # Calculate warranty cost (free for certified program)
            warranty_cost = 0 if apply_warranty else self.base_warranty_cost
            
            # Calculate total cost
            total_cost = new_car_price - old_car_value + warranty_cost
            
            return {
                'new_car_price': new_car_price,
                'old_car_value': old_car_value,
                'car_age': car_age,
                'warranty_included': apply_warranty,
                'warranty_cost': warranty_cost,
                'evaluation_fee': self.evaluation_fee,
                'total_cost': total_cost
            }
            
        except ValueError as e:
            raise ValueError(f"Input validation error: {str(e)}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        calculator = SuzukiCarExchangeCalculator()
        
        # Sample inputs
        new_price = 25000.0
        old_value = 8000.0
        old_year = 2018
        
        # Calculate with warranty
        result = calculator.calculate_exchange_cost(new_price, old_value, old_year)
        print("Exchange Cost with Warranty:")
        for key, value in result.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
            
        # Calculate without warranty
        result_no_warranty = calculator.calculate_exchange_cost(new_price, old_value, old_year, False)
        print("\nExchange Cost without Warranty:")
        for key, value in result_no_warranty.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
