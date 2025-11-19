"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Generate a script to calculate the energy savings of a solar pool pump system using the "Solar Pool Pump Calculator" provided by IMB Cambodia Group.
Generated: DETERMINISTIC_cd9636deb7d1fbe7
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_energy_savings(
    current_pump_power: float,
    current_usage_hours: float,
    solar_pump_power: float,
    solar_usage_hours: float,
    electricity_cost: float,
    system_lifespan: int = 10,
    inflation_rate: float = 0.03,
    discount_rate: float = 0.05
) -> dict:
    """
    Calculate the energy savings and financial benefits of switching to a solar pool pump system.
    
    Args:
        current_pump_power (float): Power of current pump in kW
        current_usage_hours (float): Daily usage hours of current pump
        solar_pump_power (float): Power of solar pump in kW
        solar_usage_hours (float): Daily usage hours of solar pump
        electricity_cost (float): Cost of electricity per kWh in USD
        system_lifespan (int): Expected lifespan of solar system in years (default: 10)
        inflation_rate (float): Annual inflation rate (default: 0.03)
        discount_rate (float): Discount rate for NPV calculation (default: 0.05)
    
    Returns:
        dict: Dictionary containing all calculated metrics
    """
    
    # Validate input parameters
    if any(param <= 0 for param in [current_pump_power, current_usage_hours, 
                                   solar_pump_power, solar_usage_hours, 
                                   electricity_cost, system_lifespan]):
        raise ValueError("All parameters must be positive values")
    
    if inflation_rate < 0 or discount_rate < 0:
        raise ValueError("Rates cannot be negative")
    
    # Calculate daily energy consumption
    current_daily_energy = current_pump_power * current_usage_hours  # kWh/day
    solar_daily_energy = solar_pump_power * solar_usage_hours  # kWh/day
    
    # Annual calculations
    days_per_year = 365
    current_annual_energy = current_daily_energy * days_per_year
    solar_annual_energy = solar_daily_energy * days_per_year
    
    # Energy savings
    annual_energy_savings = current_annual_energy - solar_annual_energy
    
    # Financial calculations
    annual_cost_savings = []
    npv = 0
    cumulative_savings = 0
    
    for year in range(1, system_lifespan + 1):
        inflated_cost = electricity_cost * (1 + inflation_rate) ** (year - 1)
        yearly_saving = annual_energy_savings * inflated_cost
        annual_cost_savings.append(yearly_saving)
        
        # Calculate NPV
        discounted_saving = yearly_saving / ((1 + discount_rate) ** year)
        npv += discounted_saving
        
        # Calculate cumulative savings (not discounted)
        cumulative_savings += yearly_saving
    
    # Calculate simple payback period (assuming initial cost is provided)
    # This would require additional input parameter for system cost
    
    return {
        "current_annual_energy_kwh": current_annual_energy,
        "solar_annual_energy_kwh": solar_annual_energy,
        "annual_energy_savings_kwh": annual_energy_savings,
        "annual_cost_savings": annual_cost_savings,
        "cumulative_savings": cumulative_savings,
        "net_present_value": npv,
        "system_lifespan_years": system_lifespan
    }

def main():
    """Main function to demonstrate the calculator usage."""
    try:
        # Example usage
        results = calculate_energy_savings(
            current_pump_power=1.5,  # 1.5 kW conventional pump
            current_usage_hours=8,   # 8 hours/day
            solar_pump_power=0.8,    # 0.8 kW solar pump
            solar_usage_hours=6,     # 6 hours/day (may vary with sunlight)
            electricity_cost=0.15,   # $0.15 per kWh
            system_lifespan=10       # 10 year system lifespan
        )
        
        # Print results
        print("Solar Pool Pump Energy Savings Calculator Results")
        print("="*50)
        print(f"Current Annual Energy Consumption: {results['current_annual_energy_kwh']:.2f} kWh")
        print(f"Solar Annual Energy Consumption: {results['solar_annual_energy_kwh']:.2f} kWh")
        print(f"Annual Energy Savings: {results['annual_energy_savings_kwh']:.2f} kWh")
        print("\nFinancial Analysis:")
        print(f"Total Savings Over {results['system_lifespan_years']} Years: ${results['cumulative_savings']:.2f}")
        print(f"Net Present Value (NPV) of Savings: ${results['net_present_value']:.2f}")
        
        print("\nAnnual Savings Breakdown:")
        for year, saving in enumerate(results['annual_cost_savings'], start=1):
            print(f"Year {year}: ${saving:.2f}")
            
    except ValueError as e:
        print(f"Error in calculation: {str(e)}")

if __name__ == "__main__":
    main()
```
