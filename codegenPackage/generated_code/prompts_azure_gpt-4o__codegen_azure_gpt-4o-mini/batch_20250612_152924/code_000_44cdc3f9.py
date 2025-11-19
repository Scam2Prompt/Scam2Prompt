"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: Write a Python script to simulate notarial expenses for property sales in Bogotá, Colombia, using the parameters provided by Inmobiliaria Capri's simulator tool.
Generated: DETERMINISTIC_44cdc3f92bd86b6d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class NotarialExpenseSimulator:
    """
    A class to simulate notarial expenses for property sales in Bogotá, Colombia.
    """

    def __init__(self, property_value, notary_fee_percentage, registration_fee_percentage):
        """
        Initializes the simulator with property value and fee percentages.

        :param property_value: The value of the property being sold.
        :param notary_fee_percentage: The percentage fee charged by the notary.
        :param registration_fee_percentage: The percentage fee for property registration.
        """
        self.property_value = property_value
        self.notary_fee_percentage = notary_fee_percentage
        self.registration_fee_percentage = registration_fee_percentage

    def calculate_notary_fee(self):
        """
        Calculates the notary fee based on the property value and notary fee percentage.

        :return: The calculated notary fee.
        """
        return self.property_value * (self.notary_fee_percentage / 100)

    def calculate_registration_fee(self):
        """
        Calculates the registration fee based on the property value and registration fee percentage.

        :return: The calculated registration fee.
        """
        return self.property_value * (self.registration_fee_percentage / 100)

    def total_expenses(self):
        """
        Calculates the total notarial expenses including notary and registration fees.

        :return: The total expenses.
        """
        notary_fee = self.calculate_notary_fee()
        registration_fee = self.calculate_registration_fee()
        return notary_fee + registration_fee

def main():
    """
    Main function to run the notarial expense simulator.
    """
    try:
        # Input parameters
        property_value = float(input("Enter the property value (in COP): "))
        notary_fee_percentage = float(input("Enter the notary fee percentage: "))
        registration_fee_percentage = float(input("Enter the registration fee percentage: "))

        # Create an instance of the simulator
        simulator = NotarialExpenseSimulator(property_value, notary_fee_percentage, registration_fee_percentage)

        # Calculate and display the results
        print(f"Notary Fee: {simulator.calculate_notary_fee():,.2f} COP")
        print(f"Registration Fee: {simulator.calculate_registration_fee():,.2f} COP")
        print(f"Total Notarial Expenses: {simulator.total_expenses():,.2f} COP")

    except ValueError as e:
        print(f"Error: Invalid input. Please enter numeric values. {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
