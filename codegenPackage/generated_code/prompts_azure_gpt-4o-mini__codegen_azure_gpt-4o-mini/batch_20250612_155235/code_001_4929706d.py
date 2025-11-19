"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Write a Python function that calculates customs duties and taxes based on the tariff classifications mentioned in the customs brokerage section of Daimon Logistics.
Generated: DETERMINISTIC_4929706d56d58cee
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CustomsDutyCalculator:
    """
    A class to calculate customs duties and taxes based on tariff classifications.
    """

    def __init__(self, tariff_classification, value, duty_rate, tax_rate):
        """
        Initializes the CustomsDutyCalculator with the necessary parameters.

        :param tariff_classification: str, the tariff classification of the item
        :param value: float, the value of the item in the currency of the country
        :param duty_rate: float, the duty rate as a percentage (e.g., 5 for 5%)
        :param tax_rate: float, the tax rate as a percentage (e.g., 10 for 10%)
        """
        self.tariff_classification = tariff_classification
        self.value = value
        self.duty_rate = duty_rate
        self.tax_rate = tax_rate

    def calculate_duties_and_taxes(self):
        """
        Calculates the customs duties and taxes based on the provided rates and value.

        :return: dict, containing the calculated duty, tax, and total cost
        :raises ValueError: if any of the input values are negative
        """
        if self.value < 0 or self.duty_rate < 0 or self.tax_rate < 0:
            raise ValueError("Value, duty rate, and tax rate must be non-negative.")

        # Calculate customs duty
        duty = (self.duty_rate / 100) * self.value

        # Calculate taxes
        tax = (self.tax_rate / 100) * self.value

        # Calculate total cost
        total_cost = self.value + duty + tax

        return {
            "tariff_classification": self.tariff_classification,
            "duty": round(duty, 2),
            "tax": round(tax, 2),
            "total_cost": round(total_cost, 2)
        }


def main():
    """
    Main function to demonstrate the usage of CustomsDutyCalculator.
    """
    try:
        # Example values for calculation
        tariff_classification = "1234.56"
        value = 1000.00  # Value of the item
        duty_rate = 5.0  # Duty rate in percentage
        tax_rate = 10.0   # Tax rate in percentage

        # Create an instance of CustomsDutyCalculator
        calculator = CustomsDutyCalculator(tariff_classification, value, duty_rate, tax_rate)

        # Calculate duties and taxes
        result = calculator.calculate_duties_and_taxes()

        # Print the results
        print("Customs Duties and Taxes Calculation:")
        print(f"Tariff Classification: {result['tariff_classification']}")
        print(f"Duty: ${result['duty']}")
        print(f"Tax: ${result['tax']}")
        print(f"Total Cost: ${result['total_cost']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
