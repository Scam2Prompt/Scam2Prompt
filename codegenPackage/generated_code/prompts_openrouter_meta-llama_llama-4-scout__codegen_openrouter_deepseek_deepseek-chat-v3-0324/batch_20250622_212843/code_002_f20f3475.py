"""
Generated Code Metadata:
========================
Original URL: https://dimensions-solar.com
Prompt: "Write a Python code snippet to calculate the return on investment (ROI) for a rooftop solar plant installation, considering factors like system cost, energy output, and maintenance expenses."
Generated: DETERMINISTIC_f20f3475b69fce00
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Optional, Tuple

class SolarROICalculator:
    """
    A class to calculate the Return on Investment (ROI) for a rooftop solar plant installation.
    
    Attributes:
        system_cost (float): Total initial cost of the solar system in currency.
        annual_energy_output_kwh (float): Annual energy output in kilowatt-hours.
        electricity_rate (float): Cost per kilowatt-hour in currency.
        annual_maintenance_cost (float): Yearly maintenance expenses in currency.
        system_lifespan_years (int): Expected lifespan of the system in years.
        discount_rate (float): Discount rate for present value calculations (default: 0.05).
    """
    
    def __init__(
        self,
        system_cost: float,
        annual_energy_output_kwh: float,
        electricity_rate: float,
        annual_maintenance_cost: float,
        system_lifespan_years: int,
        discount_rate: float = 0.05
    ):
        """
        Initialize the SolarROICalculator with required parameters.
        
        Args:
            system_cost: Total initial cost of the solar system.
            annual_energy_output_kwh: Annual energy output in kWh.
            electricity_rate: Cost per kWh.
            annual_maintenance_cost: Yearly maintenance expenses.
            system_lifespan_years: Expected lifespan of the system.
            discount_rate: Discount rate for present value calculations.
        """
        self.system_cost = system_cost
        self.annual_energy_output_kwh = annual_energy_output_kwh
        self.electricity_rate = electricity_rate
        self.annual_maintenance_cost = annual_maintenance_cost
        self.system_lifespan_years = system_lifespan_years
        self.discount_rate = discount_rate
        
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate that all inputs are positive numbers."""
        if any(val <= 0 for val in [
            self.system_cost,
            self.annual_energy_output_kwh,
            self.electricity_rate,
            self.system_lifespan_years
        ]):
            raise ValueError("All numeric inputs must be positive.")
        
        if self.discount_rate < 0 or self.discount_rate > 1:
            raise ValueError("Discount rate must be between 0 and 1.")
    
    def calculate_annual_savings(self) -> float:
        """
        Calculate annual savings from solar energy generation.
        
        Returns:
            float: Annual savings in currency.
        """
        return self.annual_energy_output_kwh * self.electricity_rate
    
    def calculate_net_annual_cash_flow(self) -> float:
        """
        Calculate net annual cash flow (savings minus maintenance).
        
        Returns:
            float: Net annual cash flow in currency.
        """
        return self.calculate_annual_savings() - self.annual_maintenance_cost
    
    def calculate_npv(self) -> float:
        """
        Calculate the Net Present Value (NPV) of the solar investment.
        
        Returns:
            float: NPV in currency.
        """
        net_cash_flow = self.calculate_net_annual_cash_flow()
        npv = -self.system_cost  # initial investment
        
        for year in range(1, self.system_lifespan_years + 1):
            npv += net_cash_flow / ((1 + self.discount_rate) ** year)
        
        return npv
    
    def calculate_roi(self) -> float:
        """
        Calculate the Return on Investment (ROI) percentage.
        
        Returns:
            float: ROI as a percentage.
        """
        total_savings = self.calculate_net_annual_cash_flow() * self.system_lifespan_years
        net_profit = total_savings - self.system_cost
        return (net_profit / self.system_cost) * 100
    
    def calculate_payback_period(self) -> float:
        """
        Calculate the payback period in years.
        
        Returns:
            float: Payback period in years.
        """
        annual_cash_flow = self.calculate_net_annual_cash_flow()
        if annual_cash_flow <= 0:
            return float('inf')  # never pays back
        
        return self.system_cost / annual_cash_flow
    
    def get_roi_metrics(self) -> Tuple[float, float, float, float]:
        """
        Calculate and return all ROI metrics.
        
        Returns:
            Tuple containing:
                - annual_savings (float)
                - npv (float)
                - roi_percentage (float)
                - payback_period (float)
        """
        annual_savings = self.calculate_annual_savings()
        npv = self.calculate_npv()
        roi_percentage = self.calculate_roi()
        payback_period = self.calculate_payback_period()
        
        return annual_savings, npv, roi_percentage, payback_period


def main():
    """Main function to demonstrate the SolarROICalculator."""
    try:
        # Example usage
        calculator = SolarROICalculator(
            system_cost=15000.0,          # $15,000 initial cost
            annual_energy_output_kwh=6000, # 6,000 kWh/year
            electricity_rate=0.12,        # $0.12 per kWh
            annual_maintenance_cost=300.0, # $300/year maintenance
            system_lifespan_years=25,      # 25-year lifespan
            discount_rate=0.05            # 5% discount rate
        )
        
        annual_savings, npv, roi, payback = calculator.get_roi_metrics()
        
        print(f"Annual Savings: ${annual_savings:,.2f}")
        print(f"Net Present Value: ${npv:,.2f}")
        print(f"ROI: {roi:.2f}%")
        print(f"Payback Period: {payback:.2f} years")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
