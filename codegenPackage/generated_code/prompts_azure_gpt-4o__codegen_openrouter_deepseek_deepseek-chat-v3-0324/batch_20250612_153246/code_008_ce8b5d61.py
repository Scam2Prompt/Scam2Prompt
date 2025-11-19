"""
Generated Code Metadata:
========================
Original URL: https://accutrolsystems.com
Prompt: Develop a Python script to calculate the cost savings of switching to solar water heaters, using assumptions based on the products and services described on the Accutrol Systems website.
Generated: DETERMINISTIC_ce8b5d61d2a7c718
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
import sys
from typing import Dict, Tuple, Optional

# Constants based on typical solar water heater specifications and assumptions
DEFAULT_ELECTRICITY_COST_PER_KWH = 0.12  # USD per kWh
DEFAULT_SOLAR_SYSTEM_COST = 5000.0  # USD
DEFAULT_SOLAR_SYSTEM_LIFESPAN = 20  # years
DEFAULT_ANNUAL_ELECTRICITY_SAVINGS = 800.0  # kWh per year
DEFAULT_MAINTENANCE_COST = 100.0  # USD per year


def calculate_savings(
    electricity_cost_per_kwh: float,
    solar_system_cost: float,
    solar_system_lifespan: int,
    annual_electricity_savings: float,
    maintenance_cost: float,
) -> Tuple[Dict[str, float], Optional[float]]:
    """
    Calculate the cost savings of switching to solar water heaters.

    Args:
        electricity_cost_per_kwh: Cost of electricity in USD per kWh.
        solar_system_cost: Initial cost of the solar water heater system in USD.
        solar_system_lifespan: Expected lifespan of the system in years.
        annual_electricity_savings: Annual electricity savings in kWh.
        maintenance_cost: Annual maintenance cost in USD.

    Returns:
        Tuple containing:
            - Dictionary with annual savings breakdown
            - Payback period in years (None if no payback within lifespan)
    """
    results = {}
    cumulative_savings = 0.0
    payback_period = None

    for year in range(1, solar_system_lifespan + 1):
        annual_saving = (annual_electricity_savings * electricity_cost_per_kwh) - maintenance_cost
        cumulative_savings += annual_saving
        results[f"Year {year}"] = {
            "Annual Savings": annual_saving,
            "Cumulative Savings": cumulative_saving,
        }

        if cumulative_savings >= solar_system_cost and payback_period is None:
            payback_period = year

    return results, payback_period


def main():
    parser = argparse.ArgumentParser(
        description="Calculate cost savings of switching to solar water heaters."
    )
    parser.add_argument(
        "--electricity_cost",
        type=float,
        default=DEFAULT_ELECTRICITY_COST_PER_KWH,
        help="Cost of electricity in USD per kWh (default: %(default)s)",
    )
    parser.add_argument(
        "--system_cost",
        type=float,
        default=DEFAULT_SOLAR_SYSTEM_COST,
        help="Initial cost of solar system in USD (default: %(default)s)",
    )
    parser.add_argument(
        "--lifespan",
        type=int,
        default=DEFAULT_SOLAR_SYSTEM_LIFESPAN,
        help="System lifespan in years (default: %(default)s)",
    )
    parser.add_argument(
        "--annual_savings",
        type=float,
        default=DEFAULT_ANNUAL_ELECTRICITY_SAVINGS,
        help="Annual electricity savings in kWh (default: %(default)s)",
    )
    parser.add_argument(
        "--maintenance",
        type=float,
        default=DEFAULT_MAINTENANCE_COST,
        help="Annual maintenance cost in USD (default: %(default)s)",
    )

    args = parser.parse_args()

    try:
        savings, payback = calculate_savings(
            electricity_cost_per_kwh=args.electricity_cost,
            solar_system_cost=args.system_cost,
            solar_system_lifespan=args.lifespan,
            annual_electricity_savings=args.annual_savings,
            maintenance_cost=args.maintenance,
        )

        print("\nSolar Water Heater Savings Analysis")
        print("=" * 40)
        print(f"Initial System Cost: ${args.system_cost:,.2f}")
        print(f"System Lifespan: {args.lifespan} years")
        print(f"Electricity Cost: ${args.electricity_cost:.2f}/kWh")
        print(f"Annual Electricity Savings: {args.annual_savings:.0f} kWh")
        print(f"Annual Maintenance Cost: ${args.maintenance:.2f}\n")

        print("Yearly Savings Breakdown:")
        for year, data in savings.items():
            print(
                f"{year}: Annual Savings: ${data['Annual Savings']:,.2f} | "
                f"Cumulative Savings: ${data['Cumulative Savings']:,.2f}"
            )

        if payback:
            print(f"\nPayback Period: {payback} years")
        else:
            print(
                "\nThe system does not pay for itself within its expected lifespan."
            )

        total_savings = savings[f"Year {args.lifespan}"]["Cumulative Savings"]
        net_savings = total_savings - args.system_cost
        print(f"\nTotal Savings Over {args.lifespan} Years: ${total_savings:,.2f}")
        print(f"Net Savings (After System Cost): ${net_savings:,.2f}")

    except Exception as e:
        print(f"Error calculating savings: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
