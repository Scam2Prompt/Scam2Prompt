"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cabinet-customs.com.ua
Prompt: Generate a program to calculate the import costs of a passenger car using the "Automobile Calculator" feature described on the Single Window Portal.
Generated: DETERMINISTIC_473a0c9cadb697c0
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CarImportCalculator:
    def __init__(self, car_value, customs_duty_rate, vat_rate, additional_fees):
        """
        Initializes the CarImportCalculator with necessary parameters.

        :param car_value: float - the value of the car being imported
        :param customs_duty_rate: float - customs duty rate as a percentage (e.g., 20 for 20%)
        :param vat_rate: float - VAT rate as a percentage (e.g., 15 for 15%)
        :param additional_fees: float - any additional fees applicable to the import
        """
        self.car_value = car_value
        self.customs_duty_rate = customs_duty_rate
        self.vat_rate = vat_rate
        self.additional_fees = additional_fees

    def calculate_customs_duty(self):
        """
        Calculates customs duty based on the car value and customs duty rate.

        :return: float - the amount of customs duty
        """
        return self.car_value * (self.customs_duty_rate / 100)

    def calculate_vat(self):
        """
        Calculates VAT based on the car value and VAT rate, including customs duty.

        :return: float - the amount of VAT
        """
        customs_duty = self.calculate_customs_duty()
        return (self.car_value + customs_duty) * (self.vat_rate / 100)

    def calculate_total_import_cost(self):
        """
        Calculates the total import cost including car value, customs duty, VAT, and additional fees.

        :return: float - the total import cost
        """
        customs_duty = self.calculate_customs_duty()
        vat = self.calculate_vat()
        total_cost = self.car_value + customs_duty + vat + self.additional_fees
        return total_cost

    def to_json(self):
        """
        Serializes the import cost data to JSON format.

        :return: str - JSON string of import cost details
        """
        import_cost_data = {
            'car_value': self.car_value,
            'customs_duty': self.calculate_customs_duty(),
            'vat': self.calculate_vat(),
            'additional_fees': self.additional_fees,
            'total_import_cost': self.calculate_total_import_cost()
        }
        return json.dumps(import_cost_data, indent=4)

def main():
    try:
        # Example input values for the car import calculation
        car_value = 20000.0  # Example car value in currency
        customs_duty_rate = 20.0  # 20% customs duty
        vat_rate = 15.0  # 15% VAT
        additional_fees = 500.0  # Example additional fees

        # Creating an instance of the CarImportCalculator
        calculator = CarImportCalculator(car_value, customs_duty_rate, vat_rate, additional_fees)

        # Calculate total import cost
        total_cost = calculator.calculate_total_import_cost()

        # Print the total import cost and details in JSON format
        print("Total Import Cost: {:.2f}".format(total_cost))
        print("Import Cost Details (JSON):")
        print(calculator.to_json())

    except Exception as e:
        print(f"An error occurred while calculating import costs: {e}")

if __name__ == "__main__":
    main()
```
