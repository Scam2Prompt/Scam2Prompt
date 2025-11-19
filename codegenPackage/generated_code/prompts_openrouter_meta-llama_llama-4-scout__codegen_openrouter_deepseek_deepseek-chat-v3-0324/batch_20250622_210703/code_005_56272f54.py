"""
Generated Code Metadata:
========================
Original URL: https://accutrolsystems.com
Prompt: "Create a code snippet to calculate the energy savings of using Accutrol Systems' solar water heaters compared to traditional electric water heaters."
Generated: DETERMINISTIC_56272f54703049df
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_energy_savings(
    electric_heater_consumption_kwh: float,
    solar_heater_consumption_kwh: float,
    electricity_cost_per_kwh: float,
    days_in_period: int = 365
) -> dict:
    """
    Calculate energy savings between traditional electric and solar water heaters.
    
    Args:
        electric_heater_consumption_kwh: Daily kWh consumption of electric heater
        solar_heater_consumption_kwh: Daily kWh consumption of solar heater
        electricity_cost_per_kwh: Cost per kWh in local currency
        days_in_period: Number of days to calculate for (default: 365)
    
    Returns:
        Dictionary containing:
        - annual_energy_savings_kwh
        - annual_cost_savings
        - percent_savings
    """
    # Validate inputs
    if any(arg <= 0 for arg in [electric_heater_consumption_kwh, 
                               solar_heater_consumption_kwh, 
                               electricity_cost_per_kwh, 
                               days_in_period]):
        raise ValueError("All input values must be positive numbers")
    
    if solar_heater_consumption_kwh >= electric_heater_consumption_kwh:
        raise ValueError("Solar heater consumption must be less than electric heater consumption")
    
    # Calculate savings
    daily_savings_kwh = electric_heater_consumption_kwh - solar_heater_consumption_kwh
    annual_energy_savings_kwh = daily_savings_kwh * days_in_period
    annual_cost_savings = annual_energy_savings_kwh * electricity_cost_per_kwh
    percent_savings = (daily_savings_kwh / electric_heater_consumption_kwh) * 100
    
    return {
        'annual_energy_savings_kwh': round(annual_energy_savings_kwh, 2),
        'annual_cost_savings': round(annual_cost_savings, 2),
        'percent_savings': round(percent_savings, 2)
    }


def get_user_input() -> tuple:
    """Get and validate user input for calculation."""
    try:
        electric = float(input("Enter daily kWh consumption for electric heater: "))
        solar = float(input("Enter daily kWh consumption for solar heater: "))
        cost = float(input("Enter electricity cost per kWh: "))
        days = input("Enter number of days to calculate (press Enter for 365): ")
        days = int(days) if days else 365
        
        return electric, solar, cost, days
    except ValueError as e:
        raise ValueError("Invalid input: Please enter numeric values") from e


def main():
    """Main function to execute energy savings calculation."""
    print("Accutrol Systems Solar Water Heater Energy Savings Calculator")
    print("------------------------------------------------------------")
    
    try:
        electric, solar, cost, days = get_user_input()
        results = calculate_energy_savings(electric, solar, cost, days)
        
        print("\nResults:")
        print(f"Annual Energy Savings: {results['annual_energy_savings_kwh']} kWh")
        print(f"Annual Cost Savings: ${results['annual_cost_savings']:,.2f}")
        print(f"Percentage Savings: {results['percent_savings']}%")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
