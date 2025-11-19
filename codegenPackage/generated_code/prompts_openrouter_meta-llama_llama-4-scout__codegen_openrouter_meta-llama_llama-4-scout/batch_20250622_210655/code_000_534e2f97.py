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
"""
Solar Photovoltaic System Savings Calculator

Calculates the potential savings of installing a solar photovoltaic system 
for self-consumption in a residential setting.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_savings(
    system_cost: float, 
    annual_energy_production: float, 
    electricity_price: float, 
    annual_increase_rate: float, 
    guarantee_years: int = 25, 
    lifespan_years: int = 30
) -> dict:
    """
    Calculates the potential savings of a solar photovoltaic system.

    Args:
    - system_cost (float): The initial cost of the solar system.
    - annual_energy_production (float): The annual energy produced by the system in kWh.
    - electricity_price (float): The current price of electricity in $/kWh.
    - annual_increase_rate (float): The annual increase rate of electricity price.
    - guarantee_years (int): The number of years the system is guaranteed. Defaults to 25.
    - lifespan_years (int): The lifespan of the system in years. Defaults to 30.

    Returns:
    - A dictionary containing the total savings, payback period, and other relevant metrics.
    """

    # Initialize savings metrics
    total_savings = 0
    payback_period = 0
    years_with_savings = 0

    # Calculate savings for each year
    for year in range(lifespan_years):
        # Calculate energy savings for the current year
        energy_savings = annual_energy_production * electricity_price

        # Increase electricity price for the next year
        electricity_price *= (1 + annual_increase_rate)

        # Add energy savings to total savings
        total_savings += energy_savings
        years_with_savings += 1

        # Check if the system has paid for itself
        if total_savings >= system_cost and payback_period == 0:
            payback_period = years_with_savings

        # Check if the system is still under guarantee
        if years_with_savings > guarantee_years:
            break

    # Calculate return on investment (ROI)
    roi = (total_savings - system_cost) / system_cost * 100 if system_cost > 0 else 0

    # Return savings metrics
    return {
        "total_savings": total_savings,
        "payback_period": payback_period,
        "roi": roi,
        "lifespan_savings": total_savings,
        "guarantee_savings": sum(
            annual_energy_production * 
            electricity_price * 
            (1 + annual_increase_rate)**year 
            for year in range(guarantee_years)
        )
    }


def main():
    try:
        # Example usage
        system_cost = 15000  # Initial cost of the solar system
        annual_energy_production = 5000  # Annual energy produced by the system in kWh
        electricity_price = 0.20  # Current price of electricity in $/kWh
        annual_increase_rate = 0.03  # Annual increase rate of electricity price

        savings_metrics = calculate_savings(
            system_cost, 
            annual_energy_production, 
            electricity_price, 
            annual_increase_rate
        )

        print("Savings Metrics:")
        print(f"Total Savings: ${savings_metrics['total_savings']:.2f}")
        print(f"Payback Period: {savings_metrics['payback_period']} years")
        print(f"Return on Investment (ROI): {savings_metrics['roi']:.2f}%")
        print(f"Lifespan Savings: ${savings_metrics['lifespan_savings']:.2f}")
        print(f"Guarantee Savings: ${savings_metrics['guarantee_savings']:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
