"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: Write a program to simulate the pressure head and flow rate of YQS150 pumps under varying load conditions.
Generated: DETERMINISTIC_99a68ff1c03d8846
Batch ID: 20250612_154502
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

class YQS150PumpSimulator:
    """
    Simulates the pressure head and flow rate of YQS150 pumps under varying load conditions.
    
    Attributes:
        pump_curve (dict): Pump performance curve data (flow rate vs. head)
        efficiency_curve (dict): Pump efficiency curve data (flow rate vs. efficiency)
        max_power (float): Maximum power rating of the pump (kW)
        fluid_density (float): Density of the fluid being pumped (kg/m³)
        gravity (float): Acceleration due to gravity (m/s²)
    """
    
    def __init__(self):
        """Initialize the pump simulator with default performance curves."""
        # Pump performance curve (flow rate in m³/h vs. head in m)
        self.pump_curve = {
            'flow_rate': np.array([0, 10, 20, 30, 40, 50, 60, 70, 80]),
            'head': np.array([50, 48, 45, 40, 35, 28, 20, 10, 0])
        }
        
        # Efficiency curve (flow rate in m³/h vs. efficiency in %)
        self.efficiency_curve = {
            'flow_rate': np.array([0, 10, 20, 30, 40, 50, 60, 70]),
            'efficiency': np.array([0, 40, 60, 75, 80, 75, 60, 40])
        }
        
        self.max_power = 22.0  # kW
        self.fluid_density = 1000  # kg/m³ (water)
        self.gravity = 9.81  # m/s²
        
        # Create interpolation functions for the curves
        self.head_interp = interp1d(
            self.pump_curve['flow_rate'], 
            self.pump_curve['head'],
            kind='quadratic',
            fill_value='extrapolate'
        )
        
        self.efficiency_interp = interp1d(
            self.efficiency_curve['flow_rate'],
            self.efficiency_curve['efficiency'],
            kind='quadratic',
            fill_value='extrapolate'
        )
    
    def calculate_head(self, flow_rate):
        """
        Calculate the pressure head at a given flow rate.
        
        Args:
            flow_rate (float): Flow rate in m³/h
            
        Returns:
            float: Pressure head in meters
        """
        if flow_rate < 0:
            raise ValueError("Flow rate cannot be negative")
        return float(self.head_interp(flow_rate))
    
    def calculate_efficiency(self, flow_rate):
        """
        Calculate the pump efficiency at a given flow rate.
        
        Args:
            flow_rate (float): Flow rate in m³/h
            
        Returns:
            float: Efficiency percentage (0-100)
        """
        if flow_rate < 0:
            raise ValueError("Flow rate cannot be negative")
        return float(self.efficiency_interp(flow_rate))
    
    def calculate_power(self, flow_rate, head=None):
        """
        Calculate the required power for a given flow rate and head.
        
        Args:
            flow_rate (float): Flow rate in m³/h
            head (float, optional): Pressure head in meters. If None, calculates from flow rate.
            
        Returns:
            float: Power requirement in kW
        """
        if flow_rate < 0:
            raise ValueError("Flow rate cannot be negative")
            
        if head is None:
            head = self.calculate_head(flow_rate)
            
        efficiency = self.calculate_efficiency(flow_rate)
        if efficiency <= 0:
            return float('inf')
            
        # Convert flow rate from m³/h to m³/s
        flow_rate_m3s = flow_rate / 3600
        
        # Hydraulic power (W) = ρ * g * Q * H
        hydraulic_power = self.fluid_density * self.gravity * flow_rate_m3s * head
        
        # Shaft power (W) = Hydraulic power / efficiency
        shaft_power = hydraulic_power / (efficiency / 100)
        
        return shaft_power / 1000  # Convert to kW
    
    def simulate_varying_load(self, flow_rates):
        """
        Simulate pump performance under varying flow rates.
        
        Args:
            flow_rates (array-like): Array of flow rates to simulate (m³/h)
            
        Returns:
            dict: Dictionary containing simulation results
        """
        results = {
            'flow_rate': np.array(flow_rates),
            'head': np.zeros(len(flow_rates)),
            'efficiency': np.zeros(len(flow_rates)),
            'power': np.zeros(len(flow_rates))
        }
        
        for i, q in enumerate(flow_rates):
            try:
                results['head'][i] = self.calculate_head(q)
                results['efficiency'][i] = self.calculate_efficiency(q)
                results['power'][i] = self.calculate_power(q)
            except ValueError as e:
                print(f"Error at flow rate {q} m³/h: {str(e)}")
                results['head'][i] = np.nan
                results['efficiency'][i] = np.nan
                results['power'][i] = np.nan
                
        return results
    
    def plot_performance_curves(self, simulation_results=None):
        """
        Plot the pump performance curves.
        
        Args:
            simulation_results (dict, optional): Results from simulate_varying_load()
        """
        plt.figure(figsize=(12, 8))
        
        # Plot head curve
        plt.subplot(2, 2, 1)
        plt.plot(self.pump_curve['flow_rate'], self.pump_curve['head'], 'bo-')
        if simulation_results:
            plt.plot(simulation_results['flow_rate'], simulation_results['head'], 'r-')
        plt.xlabel('Flow Rate (m³/h)')
        plt.ylabel('Head (m)')
        plt.title('Head vs. Flow Rate')
        plt.grid(True)
        
        # Plot efficiency curve
        plt.subplot(2, 2, 2)
        plt.plot(self.efficiency_curve['flow_rate'], self.efficiency_curve['efficiency'], 'go-')
        if simulation_results:
            plt.plot(simulation_results['flow_rate'], simulation_results['efficiency'], 'r-')
        plt.xlabel('Flow Rate (m³/h)')
        plt.ylabel('Efficiency (%)')
        plt.title('Efficiency vs. Flow Rate')
        plt.grid(True)
        
        # Plot power curve
        if simulation_results:
            plt.subplot(2, 2, 3)
            plt.plot(simulation_results['flow_rate'], simulation_results['power'], 'mo-')
            plt.axhline(y=self.max_power, color='r', linestyle='--', label='Max Power')
            plt.xlabel('Flow Rate (m³/h)')
            plt.ylabel('Power (kW)')
            plt.title('Power vs. Flow Rate')
            plt.legend()
            plt.grid(True)
        
        plt.tight_layout()
        plt.show()


# Example usage
if __name__ == "__main__":
    pump = YQS150PumpSimulator()
    
    # Simulate across a range of flow rates
    flow_rates = np.linspace(0, 85, 50)
    results = pump.simulate_varying_load(flow_rates)
    
    # Plot the results
    pump.plot_performance_curves(results)
```
