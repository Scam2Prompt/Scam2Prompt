"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safetransfreight.com
Prompt: Develop a script to calculate marine cargo insurance premiums for shipments, considering Safetrans Freight Solutions' guidelines for protecting goods against risks.
Generated: DETERMINISTIC_3b0261abb767d075
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class MarineCargoInsuranceCalculator:
    """
    A class to calculate marine cargo insurance premiums for shipments
    based on Safetrans Freight Solutions' guidelines.
    """

    def __init__(self, shipment_value, risk_level):
        """
        Initialize the calculator with shipment value and risk level.
        
        :param shipment_value: Total monetary value of the shipment (float).
        :param risk_level: Risk level associated with the shipment (str). 
                           Acceptable values: 'low', 'medium', 'high'.
        """
        self.shipment_value = shipment_value
        self.risk_level = risk_level.lower()
        self.risk_rate = {
            'low': 0.005,    # 0.5% premium for low risk
            'medium': 0.01,  # 1% premium for medium risk
            'high': 0.02     # 2% premium for high risk
        }

    def validate_inputs(self):
        """
        Validates user inputs.
        
        :raises ValueError: If shipment_value is non-positive or risk_level is invalid.
        """
        if self.shipment_value <= 0:
            raise ValueError("Shipment value must be greater than zero.")
        
        if self.risk_level not in self.risk_rate:
            raise ValueError(f"Invalid risk level '{self.risk_level}'. "
                             "Choose from 'low', 'medium', or 'high'.")

    def calculate_premium(self):
        """
        Calculate the insurance premium based on shipment value and risk level.
        
        :return: Premium amount (float).
        """
        self.validate_inputs()
        # Calculate premium based on risk level
        premium = self.shipment_value * self.risk_rate[self.risk_level]
        return premium


def main():
    """
    Entry point for the marine cargo insurance premium calculator.
    Prompts user for input and calculates premium.
    """
    try:
        # Prompt user for shipment value and risk level
        shipment_value = float(input("Enter the total shipment value (USD): "))
        risk_level = input("Enter the risk level ('low', 'medium', or 'high'): ")

        # Create calculator instance
        calculator = MarineCargoInsuranceCalculator(shipment_value, risk_level)
        
        # Calculate premium
        premium = calculator.calculate_premium()
        
        # Display result
        print(f"The calculated insurance premium is: ${premium:.2f}")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Start the program
    main()
```
