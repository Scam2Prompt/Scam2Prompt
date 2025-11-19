"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Develop a program to calculate the total cost and energy efficiency of installing LED Explosion Proof Flood Lights in a factory setting, using the specifications from Credible BD.
Generated: DETERMINISTIC_561d8cc21c95bf5b
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
LED Explosion Proof Flood Light Cost and Efficiency Calculator

This program calculates the total cost and energy efficiency of installing
LED Explosion Proof Flood Lights in a factory setting, using specifications
from Credible BD.

Features:
- Calculates total installation cost based on number of lights and unit price
- Computes energy savings compared to traditional lighting
- Estimates payback period based on energy savings
"""

class LEDLightCalculator:
    """
    A class to calculate cost and efficiency metrics for LED Explosion Proof Flood Lights.
    
    Attributes:
        unit_price (float): Price per LED light unit (in local currency)
        wattage (float): Power consumption per light in watts
        lifespan (int): Rated lifespan in hours
        daily_usage (float): Hours of usage per day
        electricity_rate (float): Cost per kWh in local currency
    """
    
    def __init__(self, unit_price, wattage, lifespan, daily_usage=12, electricity_rate=7.5):
        """
        Initialize the calculator with LED light specifications.
        
        Args:
            unit_price: Price per LED light unit
            wattage: Power consumption per light in watts
            lifespan: Rated lifespan in hours
            daily_usage: Hours of usage per day (default 12)
            electricity_rate: Cost per kWh (default 7.5 BDT)
        """
        self.unit_price = unit_price
        self.wattage = wattage
        self.lifespan = lifespan
        self.daily_usage = daily_usage
        self.electricity_rate = electricity_rate
        
        # Traditional light specifications (halogen as baseline)
        self.traditional_wattage = wattage * 4  # Traditional lights typically use 4x more power
        self.traditional_lifespan = lifespan / 10  # Traditional lights last about 1/10 as long
    
    def calculate_installation_cost(self, num_lights, installation_cost_per_unit=500):
        """
        Calculate total installation cost including lights and labor.
        
        Args:
            num_lights: Number of LED lights to install
            installation_cost_per_unit: Labor cost per light (default 500 BDT)
            
        Returns:
            float: Total installation cost
        """
        try:
            if num_lights <= 0:
                raise ValueError("Number of lights must be positive")
                
            total_cost = (self.unit_price + installation_cost_per_unit) * num_lights
            return round(total_cost, 2)
        except ValueError as e:
            print(f"Error calculating installation cost: {e}")
            return 0
    
    def calculate_annual_energy_cost(self, num_lights):
        """
        Calculate annual energy cost for the LED lights.
        
        Args:
            num_lights: Number of LED lights installed
            
        Returns:
            float: Annual energy cost in local currency
        """
        try:
            if num_lights <= 0:
                raise ValueError("Number of lights must be positive")
                
            daily_kwh = (self.wattage * num_lights * self.daily_usage) / 1000
            annual_cost = daily_kwh * 365 * self.electricity_rate
            return round(annual_cost, 2)
        except ValueError as e:
            print(f"Error calculating energy cost: {e}")
            return 0
    
    def calculate_energy_savings(self, num_lights):
        """
        Calculate annual energy savings compared to traditional lighting.
        
        Args:
            num_lights: Number of LED lights installed
            
        Returns:
            float: Annual savings in local currency
        """
        try:
            if num_lights <= 0:
                raise ValueError("Number of lights must be positive")
                
            led_cost = self.calculate_annual_energy_cost(num_lights)
            
            # Calculate traditional lighting cost
            daily_kwh = (self.traditional_wattage * num_lights * self.daily_usage) / 1000
            traditional_cost = daily_kwh * 365 * self.electricity_rate
            
            savings = traditional_cost - led_cost
            return round(savings, 2)
        except ValueError as e:
            print(f"Error calculating energy savings: {e}")
            return 0
    
    def calculate_payback_period(self, num_lights):
        """
        Calculate payback period in years based on energy savings.
        
        Args:
            num_lights: Number of LED lights installed
            
        Returns:
            float: Payback period in years
        """
        try:
            if num_lights <= 0:
                raise ValueError("Number of lights must be positive")
                
            installation_cost = self.calculate_installation_cost(num_lights)
            annual_savings = self.calculate_energy_savings(num_lights)
            
            if annual_savings <= 0:
                return float('inf')  # No payback if no savings
                
            payback_years = installation_cost / annual_savings
            return round(payback_years, 2)
        except ValueError as e:
            print(f"Error calculating payback period: {e}")
            return 0
    
    def calculate_lifespan_years(self):
        """
        Calculate the lifespan of the LED lights in years.
        
        Returns:
            float: Lifespan in years
        """
        try:
            if self.daily_usage <= 0:
                raise ValueError("Daily usage must be positive")
                
            lifespan_years = self.lifespan / (self.daily_usage * 365)
            return round(lifespan_years, 2)
        except ValueError as e:
            print(f"Error calculating lifespan: {e}")
            return 0

def main():
    """Main function to demonstrate the LED light calculator."""
    try:
        # Example specifications (Credible BD LED Explosion Proof Flood Light)
        unit_price = 12000  # BDT
        wattage = 100  # watts
        lifespan = 50000  # hours
        
        calculator = LEDLightCalculator(
            unit_price=unit_price,
            wattage=wattage,
            lifespan=lifespan
        )
        
        num_lights = int(input("Enter number of LED lights to install: "))
        
        # Calculate and display results
        print("\n=== LED Explosion Proof Flood Light Analysis ===")
        print(f"Number of lights: {num_lights}")
        print(f"Total installation cost: {calculator.calculate_installation_cost(num_lights)} BDT")
        print(f"Annual energy cost: {calculator.calculate_annual_energy_cost(num_lights)} BDT")
        print(f"Annual energy savings: {calculator.calculate_energy_savings(num_lights)} BDT")
        print(f"Payback period: {calculator.calculate_payback_period(num_lights)} years")
        print(f"Estimated lifespan: {calculator.calculate_lifespan_years()} years")
        
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
