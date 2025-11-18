"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lenderlibrary.ca
Prompt: Generate code to calculate down payment requirements for mobile homes and three-season chalets using Dominion Lending's standards as outlined in their documentation.
Generated: DETERMINISTIC_8ba5e981a9dd90b8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DownPaymentCalculator:
    def __init__(self, property_type: str, purchase_price: float):
        """
        Initialize the DownPaymentCalculator with the type of property and its purchase price.
        
        :param property_type: The type of property ('mobile_home' or 'three_season_chalet')
        :param purchase_price: The purchase price of the property
        """
        self.property_type = property_type.lower()
        self.purchase_price = purchase_price

    def calculate_down_payment(self) -> float:
        """
        Calculate the required down payment based on Dominion Lending standards.
        
        :return: The down payment amount required.
        :raises ValueError: If the property type is not recognized or the purchase price is invalid.
        """
        if self.purchase_price <= 0:
            raise ValueError("Purchase price must be greater than zero.")
        
        # Define down payment percentages based on property type
        if self.property_type == 'mobile_home':
            down_payment_percentage = 0.05  # 5% down payment for mobile homes
        elif self.property_type == 'three_season_chalet':
            down_payment_percentage = 0.10  # 10% down payment for three-season chalets
        else:
            raise ValueError("Invalid property type. Must be 'mobile_home' or 'three_season_chalet'.")

        # Calculate down payment
        down_payment = self.purchase_price * down_payment_percentage
        return down_payment

# Example usage
if __name__ == "__main__":
    try:
        property_type = input("Enter property type (mobile_home/three_season_chalet): ")
        purchase_price = float(input("Enter purchase price: "))
        
        calculator = DownPaymentCalculator(property_type, purchase_price)
        required_down_payment = calculator.calculate_down_payment()
        
        print(f"The required down payment for the {property_type} is: ${required_down_payment:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
