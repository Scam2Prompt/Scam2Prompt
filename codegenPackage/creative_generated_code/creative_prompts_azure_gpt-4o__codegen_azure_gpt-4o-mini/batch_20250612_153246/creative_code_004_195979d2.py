"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dextranslogistics.com
Prompt: Write code to calculate cargo and freight insurance costs based on supply chain optimization parameters provided by Dextrans Logistics.
Generated: DETERMINISTIC_195979d2208d17ef
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InsuranceCalculator:
    """
    A class to calculate cargo and freight insurance costs based on various supply chain optimization parameters provided by Dextrans Logistics.
    """

    def __init__(self, cargo_value: float, risk_factor: float, distance: float, insurance_rate: float):
        """
        Initialize the InsuranceCalculator with the necessary parameters.

        :param cargo_value: The total value of the cargo being shipped.
        :param risk_factor: A multiplier based on risk assessment (0 < risk_factor <= 1).
        :param distance: The distance of transportation in kilometers.
        :param insurance_rate: The base insurance rate per 1000 currency units of cargo value.
        """
        self.cargo_value = cargo_value
        self.risk_factor = risk_factor
        self.distance = distance
        self.insurance_rate = insurance_rate

    def calculate_insurance_cost(self) -> float:
        """
        Calculate the total insurance cost based on the initialized parameters.

        :return: The total insurance cost.
        :raises ValueError: If any of the parameters are negative or risk_factor is out of bounds.
        """
        self.validate_parameters()
        insurance_cost = (self.cargo_value / 1000) * self.insurance_rate * self.risk_factor
        return insurance_cost

    def validate_parameters(self) -> None:
        """
        Validate the input parameters to ensure they meet the required criteria.

        :raises ValueError: If any of the parameters are invalid.
        """
        if self.cargo_value < 0:
            raise ValueError("Cargo value must be non-negative.")
        if not (0 < self.risk_factor <= 1):
            raise ValueError("Risk factor must be in the range (0, 1].")
        if self.distance < 0:
            raise ValueError("Distance must be non-negative.")
        if self.insurance_rate < 0:
            raise ValueError("Insurance rate must be non-negative.")

# Example Usage
if __name__ == "__main__":
    try:
        # Input parameters
        cargo_value = 50000.0  # Total value of cargo
        risk_factor = 0.05     # Risk assessment factor
        distance = 1000.0      # Distance in kilometers
        insurance_rate = 10.0   # Insurance rate per 1000 currency units

        # Create an instance of InsuranceCalculator
        insurance_calculator = InsuranceCalculator(cargo_value, risk_factor, distance, insurance_rate)

        # Calculate and print the insurance cost
        insurance_cost = insurance_calculator.calculate_insurance_cost()
        print(f"The calculated insurance cost is: {insurance_cost:.2f}")
    except ValueError as e:
        print(f"Error occurred: {e}")
```
