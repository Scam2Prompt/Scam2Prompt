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
class CargoInsurance:
    """
    A class to calculate marine cargo insurance premiums based on shipment value and risk factors.
    """

    def __init__(self, shipment_value: float, risk_factor: float):
        """
        Initializes the CargoInsurance object with shipment value and risk factor.

        :param shipment_value: The total value of the shipment in currency units.
        :param risk_factor: A multiplier representing overall risk (1.0 for low risk, higher for increased risk).
        """
        self.shipment_value = shipment_value
        self.risk_factor = risk_factor

    def validate_inputs(self):
        """
        Validates the input values for shipment and risk factor.

        Raises ValueError if inputs are not valid.
        """
        if self.shipment_value <= 0:
            raise ValueError("Shipment value must be greater than zero.")
        if self.risk_factor <= 0:
            raise ValueError("Risk factor must be greater than zero.")

    def calculate_premium(self) -> float:
        """
        Calculates the insurance premium based on shipment value and risk factor.

        :return: The calculated premium as a float.
        """
        self.validate_inputs()
        base_rate = 0.01  # Example base rate for insurance
        premium = self.shipment_value * base_rate * self.risk_factor
        return premium

    def generate_premium_report(self) -> str:
        """
        Generates a report detailing the shipment and calculated premium.

        :return: A formatted string report.
        """
        try:
            premium = self.calculate_premium()
            report = (
                f"Shipment Value: ${self.shipment_value:,.2f}\n"
                f"Risk Factor: {self.risk_factor}\n"
                f"Calculated Premium: ${premium:,.2f}\n"
            )
            return report
        except ValueError as e:
            # Log the error and return an appropriate message
            return f"Error calculating premium: {str(e)}"


if __name__ == "__main__":
    # Example usage of the CargoInsurance class
    try:
        # Sample values for shipment value and risk factor
        shipment_value = 100000.00  # The value of the shipment
        risk_factor = 1.5  # Risk factor indicating the level of risk

        # Create an instance of CargoInsurance
        insurance = CargoInsurance(shipment_value, risk_factor)

        # Generate and print the premium report
        report = insurance.generate_premium_report()
        print(report)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
