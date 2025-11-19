"""
Generated Code Metadata:
========================
Original URL: https://vinaroy.com.vn
Prompt: Generate a script in Python to calculate the energy savings of using VinaRoy air blowers in wastewater treatment applications.
Generated: DETERMINISTIC_0647f4f61c311085
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to calculate energy savings of using VinaRoy air blowers in wastewater treatment applications.
"""

import argparse
import sys
from typing import Tuple, Optional


class EnergyCalculator:
    """
    A class to calculate energy savings when using VinaRoy air blowers.
    """

    def __init__(self, current_power: float, vinaroy_power: float, operating_hours: float, energy_cost: float):
        """
        Initialize the calculator with operational parameters.

        Args:
            current_power (float): Current power consumption in kW
            vinaroy_power (float): VinaRoy blower power consumption in kW
            operating_hours (float): Annual operating hours
            energy_cost (float): Cost of energy per kWh in USD
        """
        self.current_power = current_power
        self.vinaroy_power = vinaroy_power
        self.operating_hours = operating_hours
        self.energy_cost = energy_cost

        self._validate_inputs()

    def _validate_inputs(self) -> None:
        """Validate that all inputs are positive numbers."""
        if any(val <= 0 for val in [self.current_power, self.vinaroy_power, self.operating_hours, self.energy_cost]):
            raise ValueError("All input values must be positive numbers")

    def calculate_savings(self) -> Tuple[float, float, float]:
        """
        Calculate energy and cost savings.

        Returns:
            Tuple[float, float, float]: (energy_savings_kwh, cost_savings_usd, percent_savings)
        """
        current_energy = self.current_power * self.operating_hours
        vinaroy_energy = self.vinaroy_power * self.operating_hours

        energy_savings_kwh = current_energy - vinaroy_energy
        cost_savings_usd = energy_savings_kwh * self.energy_cost
        percent_savings = ((self.current_power - self.vinaroy_power) / self.current_power) * 100

        return energy_savings_kwh, cost_savings_usd, percent_savings


def main() -> None:
    """Main function to handle command line arguments and display results."""
    parser = argparse.ArgumentParser(
        description="Calculate energy savings of using VinaRoy air blowers in wastewater treatment applications."
    )
    parser.add_argument("current_power", type=float, help="Current power consumption in kW")
    parser.add_argument("vinaroy_power", type=float, help="VinaRoy blower power consumption in kW")
    parser.add_argument("operating_hours", type=float, help="Annual operating hours")
    parser.add_argument("energy_cost", type=float, help="Cost of energy per kWh in USD")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")

    try:
        args = parser.parse_args()

        calculator = EnergyCalculator(
            current_power=args.current_power,
            vinaroy_power=args.vinaroy_power,
            operating_hours=args.operating_hours,
            energy_cost=args.energy_cost
        )

        energy_savings, cost_savings, percent_savings = calculator.calculate_savings()

        if args.verbose:
            print("\nEnergy Savings Analysis:")
            print(f"Current System Power: {args.current_power:.2f} kW")
            print(f"VinaRoy Blower Power: {args.vinaroy_power:.2f} kW")
            print(f"Operating Hours/Year: {args.operating_hours:.0f} hours")
            print(f"Energy Cost: ${args.energy_cost:.4f}/kWh\n")
            print(f"Annual Energy Savings: {energy_savings:,.0f} kWh")
            print(f"Annual Cost Savings: ${cost_savings:,.2f}")
            print(f"Power Reduction: {percent_savings:.1f}%")
        else:
            print(f"Annual Energy Savings: {energy_savings:,.0f} kWh")
            print(f"Annual Cost Savings: ${cost_savings:,.2f}")

    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
