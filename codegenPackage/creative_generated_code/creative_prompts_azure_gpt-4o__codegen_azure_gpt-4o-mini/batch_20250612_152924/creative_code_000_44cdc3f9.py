"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Write a Python script to simulate notarial expenses for property sales in Bogotá, Colombia, using the parameters provided by Inmobiliaria Capri's simulator tool.
Generated: DETERMINISTIC_44cdc3f92bd86b6d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class NotarialExpenseSimulator:
    """
    A class to simulate notarial expenses for property sales in Bogotá, Colombia.
    """
    
    def __init__(self, property_value: float, tax_rate: float = 0.01, notary_fee_rate: float = 0.01):
        """
        Initializes the simulator with the property value, tax rate, and notary fee rate.

        :param property_value: The total value of the property being sold.
        :param tax_rate: The applicable tax rate for the transaction (default is 1%).
        :param notary_fee_rate: The notary fee rate for the transaction (default is 1%).
        """
        self.property_value = property_value
        self.tax_rate = tax_rate
        self.notary_fee_rate = notary_fee_rate

    def calculate_tax(self) -> float:
        """
        Calculates the tax based on the property value and tax rate.

        :return: The calculated tax amount.
        """
        return self.property_value * self.tax_rate

    def calculate_notary_fee(self) -> float:
        """
        Calculates the notary fee based on the property value and notary fee rate.

        :return: The calculated notary fee amount.
        """
        return self.property_value * self.notary_fee_rate

    def total_notarial_expenses(self) -> float:
        """
        Calculates the total notarial expenses including tax and notary fees.

        :return: The total notarial expenses.
        """
        return self.calculate_tax() + self.calculate_notary_fee()

    def simulate(self) -> dict:
        """
        Simulates the notarial expenses and returns a detailed breakdown.

        :return: A dictionary containing the breakdown of expenses.
        """
        return {
            "Property Value": self.property_value,
            "Tax": self.calculate_tax(),
            "Notary Fee": self.calculate_notary_fee(),
            "Total Notarial Expenses": self.total_notarial_expenses(),
        }

def main():
    """
    Main function to run the notarial expense simulator.
    """
    try:
        # Input: Property value (in Colombian Pesos)
        property_value = float(input("Enter the property value in COP: "))
        
        # Create the simulator instance
        simulator = NotarialExpenseSimulator(property_value)

        # Simulate the notarial expenses
        expenses = simulator.simulate()

        # Print results
        print("\nNotarial Expenses Summary:")
        print(json.dumps(expenses, indent=4))

    except ValueError as ve:
        print(f"Error: Invalid input. Please enter a numeric value. {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
