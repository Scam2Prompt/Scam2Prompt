"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ikogwelimited.com
Prompt: Create a program to calculate the total cost for a student planning to study abroad, factoring in visa fees, travel expenses, and discounts offered by Ikogwe International Limited.
Generated: DETERMINISTIC_c586aa4f5f39a976
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StudyAbroadCostCalculator:
    """
    A class to calculate the total cost for a student planning to study abroad.
    
    Attributes:
        visa_fee (float): The fee required for a visa application.
        travel_expenses (float): The cost of travel to the study destination.
        discount_percentage (float): The discount offered by Ikogwe International Limited.
    """

    def __init__(self, visa_fee: float, travel_expenses: float, discount_percentage: float):
        """
        Initializes the cost calculator with visa fee, travel expenses, and discount percentage.
        
        Args:
            visa_fee (float): The fee for the visa.
            travel_expenses (float): The travel expenses.
            discount_percentage (float): The discount percentage offered.
        """
        if visa_fee < 0 or travel_expenses < 0 or not (0 <= discount_percentage <= 100):
            raise ValueError("Invalid input: Ensure that fees and discounts are non-negative and percentage is between 0 and 100.")
        
        self.visa_fee = visa_fee
        self.travel_expenses = travel_expenses
        self.discount_percentage = discount_percentage

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost after applying the discount.
        
        Returns:
            float: The total cost after applying the discount.
        """
        total_cost = self.visa_fee + self.travel_expenses
        discount_amount = (self.discount_percentage / 100) * total_cost
        total_cost_after_discount = total_cost - discount_amount
        return total_cost_after_discount

if __name__ == "__main__":
    try:
        # Example inputs
        visa_fee = float(input("Enter the visa fee: "))
        travel_expenses = float(input("Enter the travel expenses: "))
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Create an instance of the calculator
        cost_calculator = StudyAbroadCostCalculator(visa_fee, travel_expenses, discount_percentage)
        
        # Calculate and display total cost
        total_cost = cost_calculator.calculate_total_cost()
        print(f"The total cost for studying abroad is: ${total_cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
