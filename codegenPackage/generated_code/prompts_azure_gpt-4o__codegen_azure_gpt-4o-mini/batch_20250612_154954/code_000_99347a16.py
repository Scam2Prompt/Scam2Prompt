"""
Generated Code Metadata:
========================
Original URL: https://quedge.io
Prompt: Write a Python script to calculate potential ROI for Aethir Edge devices using parameters such as device cost, energy consumption, and token earnings. Reference the ROI calculator features mentioned on the Aethir Edge website.
Generated: DETERMINISTIC_99347a164963d7fc
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AethirEdgeROI:
    """
    A class to calculate the Return on Investment (ROI) for Aethir Edge devices.
    """

    def __init__(self, device_cost, energy_consumption, token_earnings, energy_cost_per_kwh):
        """
        Initializes the AethirEdgeROI instance with the necessary parameters.

        :param device_cost: Cost of the Aethir Edge device (in currency units)
        :param energy_consumption: Energy consumption of the device (in kWh per month)
        :param token_earnings: Monthly token earnings from the device (in currency units)
        :param energy_cost_per_kwh: Cost of energy per kWh (in currency units)
        """
        self.device_cost = device_cost
        self.energy_consumption = energy_consumption
        self.token_earnings = token_earnings
        self.energy_cost_per_kwh = energy_cost_per_kwh

    def calculate_monthly_energy_cost(self):
        """
        Calculates the monthly energy cost based on consumption and energy cost per kWh.

        :return: Monthly energy cost (in currency units)
        """
        return self.energy_consumption * self.energy_cost_per_kwh

    def calculate_monthly_net_earnings(self):
        """
        Calculates the monthly net earnings by subtracting energy costs from token earnings.

        :return: Monthly net earnings (in currency units)
        """
        monthly_energy_cost = self.calculate_monthly_energy_cost()
        return self.token_earnings - monthly_energy_cost

    def calculate_roi(self, months=12):
        """
        Calculates the Return on Investment (ROI) over a specified number of months.

        :param months: The number of months to calculate ROI for (default is 12)
        :return: ROI as a percentage
        """
        try:
            total_net_earnings = self.calculate_monthly_net_earnings() * months
            roi = (total_net_earnings - self.device_cost) / self.device_cost * 100
            return roi
        except ZeroDivisionError:
            raise ValueError("Device cost must be greater than zero to calculate ROI.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating ROI: {e}")

    def display_roi(self, months=12):
        """
        Displays the ROI in a user-friendly format.

        :param months: The number of months to calculate ROI for (default is 12)
        """
        try:
            roi = self.calculate_roi(months)
            print(f"ROI over {months} months: {roi:.2f}%")
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except RuntimeError as re:
            print(f"Calculation Error: {re}")


if __name__ == "__main__":
    # Example parameters for the Aethir Edge device
    device_cost = 1000.0  # Cost of the device in currency units
    energy_consumption = 300.0  # Monthly energy consumption in kWh
    token_earnings = 150.0  # Monthly token earnings in currency units
    energy_cost_per_kwh = 0.12  # Cost of energy per kWh in currency units

    # Create an instance of AethirEdgeROI
    roi_calculator = AethirEdgeROI(device_cost, energy_consumption, token_earnings, energy_cost_per_kwh)

    # Display the ROI for 12 months
    roi_calculator.display_roi(months=12)
```
