"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quedge.io
Prompt: Write a Python script to calculate potential ROI for Aethir Edge devices using parameters such as device cost, energy consumption, and token earnings. Reference the ROI calculator features mentioned on the Aethir Edge website.
Generated: DETERMINISTIC_99347a164963d7fc
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AethirEdgeROI:
    """
    A class to calculate the Return on Investment (ROI) for Aethir Edge devices.
    """

    def __init__(self, device_cost: float, energy_consumption: float, token_earnings: float, energy_cost_per_kwh: float):
        """
        Initializes the ROI calculator with the necessary parameters.

        :param device_cost: Cost of the Aethir Edge device
        :param energy_consumption: Energy consumption of the device in kWh per month
        :param token_earnings: Monthly earnings in tokens
        :param energy_cost_per_kwh: Cost of energy per kWh
        """
        self.device_cost = device_cost
        self.energy_consumption = energy_consumption
        self.token_earnings = token_earnings
        self.energy_cost_per_kwh = energy_cost_per_kwh

    def calculate_monthly_energy_cost(self) -> float:
        """
        Calculates the monthly energy cost based on consumption and energy cost per kWh.

        :return: Monthly energy cost
        """
        return self.energy_consumption * self.energy_cost_per_kwh

    def calculate_monthly_net_earnings(self) -> float:
        """
        Calculates the monthly net earnings by subtracting energy costs from token earnings.

        :return: Monthly net earnings
        """
        monthly_energy_cost = self.calculate_monthly_energy_cost()
        return self.token_earnings - monthly_energy_cost

    def calculate_roi(self, months: int) -> float:
        """
        Calculates the Return on Investment (ROI) over a specified number of months.

        :param months: Number of months to calculate ROI for
        :return: ROI as a percentage
        """
        if months <= 0:
            raise ValueError("Number of months must be a positive integer.")
        
        monthly_net_earnings = self.calculate_monthly_net_earnings()
        total_earnings = monthly_net_earnings * months
        
        # Calculate ROI
        roi = (total_earnings / self.device_cost) * 100
        return roi

    def display_results(self, months: int):
        """
        Displays the ROI calculation results.

        :param months: Number of months to calculate ROI for
        """
        try:
            roi = self.calculate_roi(months)
            print(f"ROI over {months} months: {roi:.2f}%")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Example parameters for the Aethir Edge device ROI calculation
    DEVICE_COST = 500.0  # Cost of the device in currency units
    ENERGY_CONSUMPTION = 100.0  # Energy consumption in kWh per month
    TOKEN_EARNINGS = 150.0  # Token earnings per month
    ENERGY_COST_PER_KWH = 0.12  # Cost of energy per kWh

    # Create an instance of AethirEdgeROI
    roi_calculator = AethirEdgeROI(DEVICE_COST, ENERGY_CONSUMPTION, TOKEN_EARNINGS, ENERGY_COST_PER_KWH)

    # Specify the number of months for ROI calculation
    MONTHS = 12  # Number of months to calculate ROI for

    # Display the ROI results
    roi_calculator.display_results(MONTHS)
```
