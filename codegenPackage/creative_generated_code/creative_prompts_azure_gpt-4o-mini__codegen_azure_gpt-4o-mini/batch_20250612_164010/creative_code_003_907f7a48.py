"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cabinet-customs.com.ua
Prompt: Create a function that calculates customs duties for importing a vehicle based on the guidelines provided by the State Customs Service of Ukraine.
Generated: DETERMINISTIC_907f7a48544d5e39
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CustomsDutyCalculator:
    """
    A class to calculate customs duties for importing a vehicle 
    based on the guidelines provided by the State Customs Service of Ukraine.
    """

    def __init__(self, customs_rate, vehicle_value, age_years):
        """
        Initializes the CustomsDutyCalculator with required parameters.

        :param customs_rate: The percentage rate applied for customs duty
        :param vehicle_value: The declared value of the vehicle in UAH
        :param age_years: The age of the vehicle in years
        """
        self.customs_rate = customs_rate
        self.vehicle_value = vehicle_value
        self.age_years = age_years

    def calculate_duties(self):
        """
        Calculate the customs duties based on the vehicle's value and age.

        :return: The calculated customs duties in UAH
        :raises ValueError: If vehicle_value or customs_rate is negative
        """
        if self.vehicle_value < 0:
            raise ValueError("Vehicle value must be a non-negative number.")
        if self.customs_rate < 0:
            raise ValueError("Customs rate must be a non-negative percentage.")

        # Assuming a depreciation of 10% per year for vehicles older than 5 years
        depreciation_rate = 0.1
        if self.age_years > 5:
            depreciation = min(self.vehicle_value * depreciation_rate * (self.age_years - 5), self.vehicle_value)
            taxable_value = self.vehicle_value - depreciation
        else:
            taxable_value = self.vehicle_value

        # Ensure taxable value does not go below zero
        taxable_value = max(taxable_value, 0)

        # Calculate customs duty
        customs_duty = taxable_value * (self.customs_rate / 100)
        return customs_duty

if __name__ == "__main__":
    try:
        # Example inputs
        customs_rate = 10.0  # 10%
        vehicle_value = 500000  # Value in UAH
        age_years = 8  # Vehicle age in years

        # Create an instance of CustomsDutyCalculator
        calculator = CustomsDutyCalculator(customs_rate, vehicle_value, age_years)

        # Calculate the customs duty
        duties = calculator.calculate_duties()
        print(f"The customs duties to be paid for the vehicle is: {duties:.2f} UAH")
    except ValueError as e:
        print(f"Error: {e}")
```
