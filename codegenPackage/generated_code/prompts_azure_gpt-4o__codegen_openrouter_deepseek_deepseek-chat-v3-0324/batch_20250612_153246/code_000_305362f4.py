"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Write a Python script to calculate the energy savings from replacing old windows with Aluplast Ideal 3-layer windows, considering their hőszigetelési (thermal insulation) properties.
Generated: DETERMINISTIC_305362f4f8a6e031
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class WindowEnergySavingsCalculator:
    """
    A class to calculate energy savings from replacing old windows with Aluplast Ideal 3-layer windows.
    """
    
    def __init__(self, old_window_u_value, aluplast_u_value=0.8, heating_days=180, 
                 avg_outdoor_temp=0, indoor_temp=20, window_area=1.0, energy_cost=100):
        """
        Initialize the calculator with thermal properties and environmental factors.
        
        Args:
            old_window_u_value (float): U-value of old windows (W/m²K)
            aluplast_u_value (float): U-value of Aluplast Ideal 3-layer windows (default: 0.8 W/m²K)
            heating_days (int): Number of heating days per year (default: 180)
            avg_outdoor_temp (float): Average outdoor temperature during heating season (°C, default: 0)
            indoor_temp (float): Desired indoor temperature (°C, default: 20)
            window_area (float): Total window area in m² (default: 1.0)
            energy_cost (float): Cost of energy per kWh in local currency (default: 100)
        """
        self.old_window_u_value = old_window_u_value
        self.aluplast_u_value = aluplast_u_value
        self.heating_days = heating_days
        self.avg_outdoor_temp = avg_outdoor_temp
        self.indoor_temp = indoor_temp
        self.window_area = window_area
        self.energy_cost = energy_cost
        
        # Constants
        self.SECONDS_IN_DAY = 86400
        self.WATT_TO_KILOWATT = 0.001
        
    def calculate_heat_loss(self, u_value):
        """
        Calculate daily heat loss through windows.
        
        Args:
            u_value (float): U-value of the window (W/m²K)
            
        Returns:
            float: Daily heat loss in kWh
        """
        try:
            temp_difference = self.indoor_temp - self.avg_outdoor_temp
            daily_loss_watts = u_value * self.window_area * temp_difference * self.SECONDS_IN_DAY
            daily_loss_kwh = daily_loss_watts * self.WATT_TO_KILOWATT
            return daily_loss_kwh
        except Exception as e:
            raise ValueError(f"Error calculating heat loss: {str(e)}")
    
    def calculate_annual_savings(self):
        """
        Calculate annual energy and cost savings from window replacement.
        
        Returns:
            dict: Dictionary containing annual savings in kWh and monetary value
        """
        try:
            old_daily_loss = self.calculate_heat_loss(self.old_window_u_value)
            new_daily_loss = self.calculate_heat_loss(self.aluplast_u_value)
            
            daily_savings_kwh = old_daily_loss - new_daily_loss
            annual_savings_kwh = daily_savings_kwh * self.heating_days
            annual_savings_cost = annual_savings_kwh * self.energy_cost
            
            return {
                'annual_energy_savings_kwh': annual_savings_kwh,
                'annual_cost_savings': annual_savings_cost
            }
        except Exception as e:
            raise ValueError(f"Error calculating annual savings: {str(e)}")
    
    def calculate_payback_period(self, replacement_cost):
        """
        Calculate the payback period for the window replacement investment.
        
        Args:
            replacement_cost (float): Total cost of window replacement
            
        Returns:
            float: Payback period in years
        """
        try:
            savings = self.calculate_annual_savings()
            if savings['annual_cost_savings'] <= 0:
                return math.inf
            return replacement_cost / savings['annual_cost_savings']
        except Exception as e:
            raise ValueError(f"Error calculating payback period: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        calculator = WindowEnergySavingsCalculator(
            old_window_u_value=2.5,  # Typical old window U-value
            aluplast_u_value=0.8,    # Aluplast Ideal 3-layer window U-value
            window_area=10,          # 10 m² of windows
            energy_cost=50           # 50 currency units per kWh
        )
        
        # Calculate savings
        savings = calculator.calculate_annual_savings()
        print(f"Annual energy savings: {savings['annual_energy_savings_kwh']:.2f} kWh")
        print(f"Annual cost savings: {savings['annual_cost_savings']:.2f} currency units")
        
        # Calculate payback for 5000 currency unit investment
        payback = calculator.calculate_payback_period(5000)
        if payback == math.inf:
            print("The investment will not pay back based on current savings.")
        else:
            print(f"Payback period: {payback:.1f} years")
            
    except ValueError as e:
        print(f"Error: {str(e)}")
```
