"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: "What are the advantages of using Schüco or Rehau windows over standard plastic windows, and how can their energy efficiency be calculated programmatically?"
Generated: DETERMINISTIC_6303344b3b8a2065
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script calculates the energy efficiency of windows based on U-value (thermal transmittance)
and solar heat gain coefficient (SHGC). It compares standard plastic windows with premium brands
like Schüco and Rehau.
"""

class Window:
    """Represents a window with thermal properties."""
    
    def __init__(self, name, u_value, shgc, frame_material, cost):
        """
        Initialize a window with its properties.
        
        Args:
            name (str): Brand/type of window
            u_value (float): Thermal transmittance (W/m²K)
            shgc (float): Solar heat gain coefficient (0-1)
            frame_material (str): Material of window frame
            cost (float): Cost per square meter
        """
        self.name = name
        self.u_value = u_value
        self.shgc = shgc
        self.frame_material = frame_material
        self.cost = cost
    
    def calculate_heat_loss(self, area, temp_difference):
        """
        Calculate heat loss through the window.
        
        Args:
            area (float): Window area in m²
            temp_difference (float): Temperature difference between inside and outside (°C)
            
        Returns:
            float: Heat loss in watts
        """
        return self.u_value * area * temp_difference
    
    def calculate_solar_gain(self, area, solar_radiation):
        """
        Calculate solar heat gain through the window.
        
        Args:
            area (float): Window area in m²
            solar_radiation (float): Solar radiation in W/m²
            
        Returns:
            float: Solar heat gain in watts
        """
        return self.shgc * area * solar_radiation
    
    def calculate_net_energy(self, area, temp_difference, solar_radiation):
        """
        Calculate net energy impact (heat loss minus solar gain).
        
        Args:
            area (float): Window area in m²
            temp_difference (float): Temperature difference (°C)
            solar_radiation (float): Solar radiation in W/m²
            
        Returns:
            float: Net energy impact in watts
        """
        heat_loss = self.calculate_heat_loss(area, temp_difference)
        solar_gain = self.calculate_solar_gain(area, solar_radiation)
        return heat_loss - solar_gain
    
    def __str__(self):
        """Return string representation of the window."""
        return (f"{self.name} Window (U-value: {self.u_value} W/m²K, "
                f"SHGC: {self.shgc}, Frame: {self.frame_material}, "
                f"Cost: ${self.cost}/m²)")


def compare_windows(windows, area, temp_difference, solar_radiation):
    """
    Compare multiple windows based on energy efficiency and cost.
    
    Args:
        windows (list): List of Window objects
        area (float): Window area in m²
        temp_difference (float): Temperature difference (°C)
        solar_radiation (float): Solar radiation in W/m²
        
    Returns:
        dict: Dictionary with comparison results
    """
    results = []
    
    for window in windows:
        net_energy = window.calculate_net_energy(area, temp_difference, solar_radiation)
        total_cost = window.cost * area
        
        results.append({
            'window': window.name,
            'u_value': window.u_value,
            'shgc': window.shgc,
            'net_energy': net_energy,
            'total_cost': total_cost,
            'cost_per_watt': abs(total_cost / net_energy) if net_energy != 0 else float('inf')
        })
    
    # Sort by net energy (most efficient first)
    results.sort(key=lambda x: x['net_energy'])
    
    return results


def main():
    """Demonstrate window comparison with example data."""
    try:
        # Example window specifications
        standard_plastic = Window(
            "Standard Plastic", 
            u_value=2.7, 
            shgc=0.75, 
            frame_material="PVC", 
            cost=150
        )
        
        rehau_window = Window(
            "Rehau", 
            u_value=1.1, 
            shgc=0.62, 
            frame_material="PVC with thermal breaks", 
            cost=300
        )
        
        schuco_window = Window(
            "Schüco", 
            u_value=0.8, 
            shgc=0.5, 
            frame_material="Aluminum with thermal breaks", 
            cost=400
        )
        
        windows = [standard_plastic, rehau_window, schuco_window]
        
        # Example conditions
        area = 2.5  # m²
        temp_difference = 20  # °C (indoor vs outdoor)
        solar_radiation = 500  # W/m²
        
        # Compare windows
        comparison = compare_windows(windows, area, temp_difference, solar_radiation)
        
        # Print results
        print("Window Energy Efficiency Comparison:")
        print(f"Area: {area}m², Temp Δ: {temp_difference}°C, Solar Radiation: {solar_radiation}W/m²\n")
        
        for result in comparison:
            print(f"{result['window']}:")
            print(f"  U-value: {result['u_value']} W/m²K")
            print(f"  SHGC: {result['shgc']}")
            print(f"  Net Energy: {result['net_energy']:.2f} W")
            print(f"  Total Cost: ${result['total_cost']:.2f}")
            print(f"  Cost per Watt: ${result['cost_per_watt']:.2f}\n")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
