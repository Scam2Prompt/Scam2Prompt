"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: "Generate a Python script to calculate the potential savings of installing a solar photovoltaic system for self-consumption in a residential setting, considering a 25-year guarantee and over 30 years of lifespan."
Generated: DETERMINISTIC_534e2f97867a4408
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_solar_savings(
    system_cost, 
    annual_energy_consumption, 
    solar_coverage_percentage, 
    electricity_rate, 
    annual_rate_increase, 
    lifespan_years=30, 
    guarantee_years=25
):
    """
    Calculate the potential savings of installing a solar photovoltaic system.

    Parameters:
        system_cost (float): Total cost of the solar system installation.
        annual_energy_consumption (float): Annual energy consumption in kWh.
        solar_coverage_percentage (float): Percentage of energy covered by solar (0-100).
        electricity_rate (float): Current electricity rate per kWh.
        annual_rate_increase (float): Annual percentage increase in electricity rate (0-100).
        lifespan_years (int): Total lifespan of the solar system in years (default: 30).
        guarantee_years (int): Guarantee period of the solar system in years (default: 25).

    Returns:
        dict: A dictionary containing total savings, payback period, and savings breakdown.
    """
    # Validate inputs
    if not (0 <= solar_coverage_percentage <= 100):
        raise ValueError("Solar coverage percentage must be between 0 and 100.")
    if not (0 <= annual_rate_increase <= 100):
        raise ValueError("Annual rate increase must be between 0 and 100.")
    if lifespan_years <= 0 or guarantee_years <= 0:
        raise ValueError("Lifespan and guarantee years must be positive integers.")

    # Convert percentages to decimals
    solar_coverage = solar_coverage_percentage / 100
    rate_increase = annual_rate_increase / 100

    # Calculate annual savings from solar energy
    annual_solar_savings = annual_energy_consumption * solar_coverage * electricity_rate

    # Calculate savings over the lifespan of the system
    total_savings = 0
    savings_breakdown = []
    for year in range(1, lifespan_years + 1):
        # Adjust electricity rate for inflation
        adjusted_rate = electricity_rate * math.pow(1 + rate_increase, year - 1)
        annual_savings = annual_energy_consumption * solar_coverage * adjusted_rate
        total_savings += annual_savings
        savings_breakdown.append({
            "year": year,
            "adjusted_rate": round(adjusted_rate, 2),
            "annual_savings": round(annual_savings, 2),
            "cumulative_savings": round(total_savings, 2)
        })

    # Calculate payback period
    payback_period = None
    cumulative_savings = 0
    for year_data in savings_breakdown:
        cumulative_savings += year_data["annual_savings"]
        if cumulative_savings >= system_cost and payback_period is None:
            payback_period = year_data["year"]

    return {
        "total_savings": round(total_savings, 2),
        "payback_period": payback_period,
        "savings_breakdown": savings_breakdown
    }


def main():
    """
    Main function to execute the solar savings calculation.
    """
    try:
        # Input parameters
        system_cost = float(input("Enter the total cost of the solar system installation ($): "))
        annual_energy_consumption = float(input("Enter your annual energy consumption (kWh): "))
        solar_coverage_percentage = float(input("Enter the percentage of energy covered by solar (0-100): "))
        electricity_rate = float(input("Enter the current electricity rate ($/kWh): "))
        annual_rate_increase = float(input("Enter the annual percentage increase in electricity rate (0-100): "))

        # Calculate savings
        results = calculate_solar_savings(
            system_cost=system_cost,
            annual_energy_consumption=annual_energy_consumption,
            solar_coverage_percentage=solar_coverage_percentage,
            electricity_rate=electricity_rate,
            annual_rate_increase=annual_rate_increase
        )

        # Display results
        print("\n--- Solar Savings Calculation Results ---")
        print(f"Total Savings Over {len(results['savings_breakdown'])} Years: ${results['total_savings']}")
        if results['payback_period']:
            print(f"Payback Period: {results['payback_period']} years")
        else:
            print("Payback Period: Not achieved within the system lifespan.")
        print("\nYearly Savings Breakdown:")
        for year_data in results['savings_breakdown']:
            print(f"Year {year_data['year']}: Annual Savings = ${year_data['annual_savings']}, "
                  f"Cumulative Savings = ${year_data['cumulative_savings']}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
