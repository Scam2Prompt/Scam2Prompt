"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Develop a script that automates the process of calculating notary fees for property transactions using the guidelines provided by Inmobiliaria Nueva Ciudad.
Generated: DETERMINISTIC_43beab7c2e2f31c9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class NotaryFeeCalculator:
    """
    A class to calculate notary fees for property transactions based on Inmobiliaria Nueva Ciudad guidelines.
    """

    def __init__(self, base_fee: float, property_value: float):
        """
        Initializes the NotaryFeeCalculator with the base fee and property value.

        :param base_fee: The base fee for notary services.
        :param property_value: The total value of the property being transacted.
        """
        self.base_fee = base_fee
        self.property_value = property_value

    def calculate_fee(self) -> float:
        """
        Calculates the total notary fee based on the property value.

        :return: The calculated notary fee.
        """
        if self.property_value <= 0:
            raise ValueError("Property value must be greater than zero.")

        # Example fee structure based on property value thresholds
        if self.property_value < 100000:
            fee_percentage = 0.01  # 1% for properties under 100,000
        elif self.property_value < 300000:
            fee_percentage = 0.007  # 0.7% for properties between 100,000 and 300,000
        else:
            fee_percentage = 0.005  # 0.5% for properties above 300,000

        calculated_fee = self.base_fee + (self.property_value * fee_percentage)
        return round(calculated_fee, 2)  # Round to 2 decimal places

def main():
    """
    Main function to execute the notary fee calculation.
    """
    # Input validation
    try:
        base_fee = float(input("Enter the base notary fee: "))
        property_value = float(input("Enter the property value: "))
        
        if base_fee < 0:
            raise ValueError("Base fee must be non-negative.")

    except ValueError as e:
        print(f"Input error: {e}")
        sys.exit(1)

    # Calculate and display the notary fee
    calculator = NotaryFeeCalculator(base_fee, property_value)
    try:
        total_fee = calculator.calculate_fee()
        print(f"The total notary fee for the transaction is: ${total_fee}")
    except Exception as e:
        print(f"Error calculating fee: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
