"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Write Python code to simulate the performance of Niobium Oxide OxiCap® capacitors using the SpiCAT simulation tool provided by KYOCERA AVX. Include parameters such as ESR, CV, and temperature ratings up to 125°C.
Generated: DETERMINISTIC_a5ce8ed176ef6be0
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

class NiobiumOxideCapacitor:
    """
    Simulate the performance of Niobium Oxide OxiCap® capacitors using SpiCAT-like modeling.
    """
    
    def __init__(self, capacitance, voltage_rating, esr_25c, esr_125c, 
                 leakage_current_25c, leakage_current_125c, 
                 df_25c, df_125c, lifetime_hours=1000):
        """
        Initialize capacitor parameters.
        
        Args:
            capacitance (float): Capacitance value in uF
            voltage_rating (float): Rated voltage in V
            esr_25c (float): Equivalent Series Resistance at 25°C in ohms
            esr_125c (float): Equivalent Series Resistance at 125°C in ohms
            leakage_current_25c (float): Leakage current at 25°C in uA
            leakage_current_125c (float): Leakage current at 125°C in uA
            df_25c (float): Dissipation factor at 25°C in %
            df_125c (float): Dissipation factor at 125°C in %
            lifetime_hours (int): Expected lifetime in hours at rated voltage and 125°C
        """
        self.capacitance = capacitance
        self.voltage_rating = voltage_rating
        self.esr_25c = esr_25c
        self.esr_125c = esr_125c
        self.leakage_current_25c = leakage_current_25c
        self.leakage_current_125c = leakage_current_125c
        self.df_25c = df_25c
        self.df_125c = df_125c
        self.lifetime_hours = lifetime_hours
        
        # Temperature points for interpolation
        self.temp_points = np.array([25, 85, 105, 125])
        
    def calculate_esr_vs_temp(self):
        """Calculate ESR vs temperature curve."""
        esr_points = np.array([
            self.esr_25c,
            self.esr_25c * 1.2,  # Estimated at 85°C
            self.esr_25c * 1.5,  # Estimated at 105°C
            self.esr_125c
        ])
        return interp1d(self.temp_points, esr_points, kind='quadratic')
    
    def calculate_leakage_vs_temp(self):
        """Calculate leakage current vs temperature curve."""
        leakage_points = np.array([
            self.leakage_current_25c,
            self.leakage_current_25c * 5,  # Estimated at 85°C
            self.leakage_current_25c * 10,  # Estimated at 105°C
            self.leakage_current_125c
        ])
        return interp1d(self.temp_points, leakage_points, kind='quadratic')
    
    def calculate_df_vs_temp(self):
        """Calculate dissipation factor vs temperature curve."""
        df_points = np.array([
            self.df_25c,
            self.df_25c * 1.3,  # Estimated at 85°C
            self.df_25c * 1.7,  # Estimated at 105°C
            self.df_125c
        ])
        return interp1d(self.temp_points, df_points, kind='quadratic')
    
    def calculate_lifetime(self, operating_temp, operating_voltage):
        """
        Calculate expected lifetime based on operating conditions.
        
        Args:
            operating_temp (float): Operating temperature in °C
            operating_voltage (float): Operating voltage in V
            
        Returns:
            float: Estimated lifetime in hours
        """
        if operating_temp > 125:
            raise ValueError("Operating temperature exceeds maximum rating of 125°C")
        if operating_voltage > self.voltage_rating:
            raise ValueError("Operating voltage exceeds rated voltage")
            
        # Simplified lifetime estimation model
        temp_factor = 2 ** ((125 - operating_temp) / 10)
        voltage_factor = (self.voltage_rating / operating_voltage) ** 3
        return self.lifetime_hours * temp_factor * voltage_factor
    
    def plot_performance_curves(self):
        """Generate performance curves for visualization."""
        temps = np.linspace(25, 125, 50)
        
        esr_func = self.calculate_esr_vs_temp()
        leakage_func = self.calculate_leakage_vs_temp()
        df_func = self.calculate_df_vs_temp()
        
        plt.figure(figsize=(12, 8))
        
        # ESR plot
        plt.subplot(2, 2, 1)
        plt.plot(temps, esr_func(temps))
        plt.title('ESR vs Temperature')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('ESR (Ω)')
        plt.grid(True)
        
        # Leakage current plot
        plt.subplot(2, 2, 2)
        plt.plot(temps, leakage_func(temps))
        plt.title('Leakage Current vs Temperature')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Leakage Current (μA)')
        plt.grid(True)
        
        # Dissipation factor plot
        plt.subplot(2, 2, 3)
        plt.plot(temps, df_func(temps))
        plt.title('Dissipation Factor vs Temperature')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('DF (%)')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Parameters for a typical Niobium Oxide OxiCap® capacitor
    cap = NiobiumOxideCapacitor(
        capacitance=47,          # uF
        voltage_rating=10,       # V
        esr_25c=0.1,            # Ω at 25°C
        esr_125c=0.15,          # Ω at 125°C
        leakage_current_25c=5,   # μA at 25°C
        leakage_current_125c=50, # μA at 125°C
        df_25c=5,               # % at 25°C
        df_125c=8,              # % at 125°C
        lifetime_hours=1000     # hours at rated conditions
    )
    
    # Generate performance curves
    cap.plot_performance_curves()
    
    # Calculate lifetime at specific conditions
    try:
        lifetime = cap.calculate_lifetime(operating_temp=85, operating_voltage=8)
        print(f"Estimated lifetime at 85°C and 8V: {lifetime:.0f} hours")
    except ValueError as e:
        print(f"Error: {e}")
```
