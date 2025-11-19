"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Write a Python script to calculate the cost of owning a hot tub, including maintenance and energy costs, for a customer in El Paso County.
Generated: DETERMINISTIC_b0a7009df02811a3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class HotTubCostCalculator:
    """
    A class to calculate the cost of owning a hot tub including purchase, maintenance, and energy costs.
    """
    
    def __init__(self, electricity_rate=0.12, water_rate=0.004, chemical_cost=20, hot_tub_price=5000):
        """
        Initialize the calculator with default rates for El Paso County.
        
        Args:
            electricity_rate (float): Cost per kWh in dollars. Default is El Paso average.
            water_rate (float): Cost per gallon of water in dollars. Default is El Paso average.
            chemical_cost (float): Monthly chemical cost in dollars. Default estimate.
            hot_tub_price (float): Initial purchase price of hot tub in dollars.
        """
        self.electricity_rate = electricity_rate
        self.water_rate = water_rate
        self.chemical_cost = chemical_cost
        self.hot_tub_price = hot_tub_price
        
    def calculate_energy_cost(self, tub_volume=400, heating_power=5.5, usage_hours=3, ambient_temp=65, desired_temp=104, days_per_month=30):
        """
        Calculate monthly energy cost to heat the hot tub.
        
        Args:
            tub_volume (int): Volume of hot tub in gallons.
            heating_power (float): Heater power in kW.
            usage_hours (int): Daily usage hours.
            ambient_temp (int): Average ambient temperature in Fahrenheit.
            desired_temp (int): Desired water temperature in Fahrenheit.
            days_per_month (int): Days in calculation period.
            
        Returns:
            float: Monthly energy cost in dollars.
        """
        try:
            # Calculate temperature difference
            temp_diff = desired_temp - ambient_temp
            
            # Calculate energy to heat water (Q = mcΔT converted to kWh)
            # 1 gallon = 8.34 lbs, specific heat of water = 1 BTU/lb°F
            # 1 kWh = 3412 BTU
            energy_btu = tub_volume * 8.34 * temp_diff
            energy_kwh = energy_btu / 3412
            
            # Calculate heating time (assuming heater can maintain temperature)
            heating_time_hours = energy_kwh / heating_power
            
            # Total energy cost (heating + pump operation)
            total_kwh = (heating_time_hours + usage_hours) * days_per_month * heating_power
            return total_kwh * self.electricity_rate
        except Exception as e:
            print(f"Error calculating energy cost: {e}")
            return 0
    
    def calculate_water_cost(self, tub_volume=400, refills_per_year=4):
        """
        Calculate annual water cost for refilling the hot tub.
        
        Args:
            tub_volume (int): Volume of hot tub in gallons.
            refills_per_year (int): Number of times tub is drained and refilled annually.
            
        Returns:
            float: Annual water cost in dollars.
        """
        try:
            return tub_volume * refills_per_year * self.water_rate
        except Exception as e:
            print(f"Error calculating water cost: {e}")
            return 0
    
    def calculate_total_cost(self, years=5):
        """
        Calculate total cost of ownership over specified years.
        
        Args:
            years (int): Number of years to calculate costs for.
            
        Returns:
            dict: Dictionary containing breakdown of costs.
        """
        try:
            monthly_energy = self.calculate_energy_cost()
            annual_energy = monthly_energy * 12
            annual_water = self.calculate_water_cost()
            annual_chemicals = self.chemical_cost * 12
            
            total_energy = annual_energy * years
            total_water = annual_water * years
            total_chemicals = annual_chemicals * years
            
            return {
                'initial_cost': self.hot_tub_price,
                'total_energy_cost': total_energy,
                'total_water_cost': total_water,
                'total_chemical_cost': total_chemicals,
                'total_cost': self.hot_tub_price + total_energy + total_water + total_chemicals,
                'annual_cost': (total_energy + total_water + total_chemicals) / years,
                'monthly_cost': ((total_energy + total_water + total_chemicals) / years) / 12
            }
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return {}

def main():
    """
    Main function to demonstrate the HotTubCostCalculator.
    """
    try:
        calculator = HotTubCostCalculator()
        cost_breakdown = calculator.calculate_total_cost(years=5)
        
        print("Hot Tub Ownership Cost Breakdown (5 Years)")
        print("-----------------------------------------")
        print(f"Initial Purchase: ${cost_breakdown['initial_cost']:,.2f}")
        print(f"Total Energy Cost: ${cost_breakdown['total_energy_cost']:,.2f}")
        print(f"Total Water Cost: ${cost_breakdown['total_water_cost']:,.2f}")
        print(f"Total Chemical Cost: ${cost_breakdown['total_chemical_cost']:,.2f}")
        print(f"\nTotal 5-Year Cost: ${cost_breakdown['total_cost']:,.2f}")
        print(f"Average Annual Cost: ${cost_breakdown['annual_cost']:,.2f}")
        print(f"Average Monthly Cost: ${cost_breakdown['monthly_cost']:,.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
