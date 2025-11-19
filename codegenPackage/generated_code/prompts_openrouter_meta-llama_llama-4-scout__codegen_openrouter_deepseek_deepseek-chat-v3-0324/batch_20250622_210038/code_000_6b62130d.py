"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: "Write a Python script to compare the energy efficiency of UPVC windows and traditional windows for a project in Faridabad."
Generated: DETERMINISTIC_6b62130dfbd286f3
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_u_value(material_properties, thickness):
    """
    Calculate the U-value (thermal transmittance) of a material.
    U-value is the rate of heat transfer through a structure divided by the area and temperature difference.
    Lower U-values indicate better insulation properties.
    
    Args:
        material_properties (dict): Dictionary containing material properties
        thickness (float): Thickness of the material in meters
        
    Returns:
        float: U-value in W/m²K
    """
    try:
        thermal_conductivity = material_properties['thermal_conductivity']
        r_value = thickness / thermal_conductivity
        u_value = 1 / r_value
        return u_value
    except KeyError as e:
        raise ValueError(f"Missing required material property: {e}")
    except ZeroDivisionError:
        raise ValueError("Thickness cannot be zero")

def calculate_window_u_value(frame_u_value, glass_u_value, frame_area_ratio):
    """
    Calculate the overall U-value of a window considering both frame and glass.
    
    Args:
        frame_u_value (float): U-value of the window frame (W/m²K)
        glass_u_value (float): U-value of the glass (W/m²K)
        frame_area_ratio (float): Ratio of frame area to total window area (0-1)
        
    Returns:
        float: Combined U-value of the window (W/m²K)
    """
    if not 0 <= frame_area_ratio <= 1:
        raise ValueError("Frame area ratio must be between 0 and 1")
    
    glass_area_ratio = 1 - frame_area_ratio
    combined_u_value = (frame_u_value * frame_area_ratio) + (glass_u_value * glass_area_ratio)
    return combined_u_value

def calculate_heat_loss(u_value, area, temperature_difference):
    """
    Calculate heat loss through a window.
    
    Args:
        u_value (float): U-value of the window (W/m²K)
        area (float): Area of the window in square meters
        temperature_difference (float): Temperature difference between inside and outside in Kelvin
        
    Returns:
        float: Heat loss in Watts
    """
    return u_value * area * temperature_difference

def calculate_annual_energy_loss(heat_loss, hours_per_year):
    """
    Calculate annual energy loss in kWh.
    
    Args:
        heat_loss (float): Heat loss in Watts
        hours_per_year (float): Annual hours of operation
        
    Returns:
        float: Annual energy loss in kWh
    """
    return (heat_loss * hours_per_year) / 1000

def main():
    # Faridabad climate data (approximate)
    heating_season_hours = 8 * 30 * 4  # 8 hours/day, 30 days/month, 4 months
    cooling_season_hours = 8 * 30 * 6  # 8 hours/day, 30 days/month, 6 months
    annual_hours = heating_season_hours + cooling_season_hours
    
    # Average temperature difference (Kelvin)
    winter_temp_diff = 10  # Inside 20°C, outside 10°C
    summer_temp_diff = 15  # Inside 25°C, outside 40°C
    
    # Window properties
    window_area = 2.0  # m² (standard window size)
    frame_area_ratio = 0.2  # 20% of window area is frame
    
    # Material properties
    materials = {
        'upvc': {
            'thermal_conductivity': 0.16,  # W/mK
            'thickness': 0.07  # 70mm
        },
        'aluminum': {
            'thermal_conductivity': 160.0,  # W/mK
            'thickness': 0.05  # 50mm
        },
        'wood': {
            'thermal_conductivity': 0.13,  # W/mK
            'thickness': 0.05  # 50mm
        },
        'single_glass': {
            'thermal_conductivity': 1.0,  # W/mK
            'thickness': 0.006  # 6mm
        },
        'double_glass': {
            'thermal_conductivity': 0.6,  # W/mK
            'thickness': 0.024  # 24mm (2x12mm with air gap)
        }
    }
    
    # Calculate U-values for different window types
    try:
        # UPVC window with double glass
        upvc_frame_u = calculate_u_value(materials['upvc'], materials['upvc']['thickness'])
        double_glass_u = calculate_u_value(materials['double_glass'], materials['double_glass']['thickness'])
        upvc_window_u = calculate_window_u_value(upvc_frame_u, double_glass_u, frame_area_ratio)
        
        # Aluminum window with single glass (traditional)
        aluminum_frame_u = calculate_u_value(materials['aluminum'], materials['aluminum']['thickness'])
        single_glass_u = calculate_u_value(materials['single_glass'], materials['single_glass']['thickness'])
        aluminum_window_u = calculate_window_u_value(aluminum_frame_u, single_glass_u, frame_area_ratio)
        
        # Wooden window with single glass (traditional)
        wood_frame_u = calculate_u_value(materials['wood'], materials['wood']['thickness'])
        wood_window_u = calculate_window_u_value(wood_frame_u, single_glass_u, frame_area_ratio)
        
        # Calculate heat losses
        upvc_winter_loss = calculate_heat_loss(upvc_window_u, window_area, winter_temp_diff)
        upvc_summer_loss = calculate_heat_loss(upvc_window_u, window_area, summer_temp_diff)
        
        aluminum_winter_loss = calculate_heat_loss(aluminum_window_u, window_area, winter_temp_diff)
        aluminum_summer_loss = calculate_heat_loss(aluminum_window_u, window_area, summer_temp_diff)
        
        wood_winter_loss = calculate_heat_loss(wood_window_u, window_area, winter_temp_diff)
        wood_summer_loss = calculate_heat_loss(wood_window_u, window_area, summer_temp_diff)
        
        # Calculate annual energy losses
        upvc_annual_loss = (calculate_annual_energy_loss(upvc_winter_loss, heating_season_hours) +
                           calculate_annual_energy_loss(upvc_summer_loss, cooling_season_hours))
        
        aluminum_annual_loss = (calculate_annual_energy_loss(aluminum_winter_loss, heating_season_hours) +
                               calculate_annual_energy_loss(aluminum_summer_loss, cooling_season_hours))
        
        wood_annual_loss = (calculate_annual_energy_loss(wood_winter_loss, heating_season_hours) +
                           calculate_annual_energy_loss(wood_summer_loss, cooling_season_hours))
        
        # Print results
        print("Window Energy Efficiency Comparison for Faridabad")
        print("="*50)
        print(f"Window Area: {window_area} m²")
        print(f"Frame Area Ratio: {frame_area_ratio*100:.0f}%")
        print("\nU-values (W/m²K):")
        print(f"- UPVC with double glass: {upvc_window_u:.2f}")
        print(f"- Aluminum with single glass: {aluminum_window_u:.2f}")
        print(f"- Wood with single glass: {wood_window_u:.2f}")
        
        print("\nAnnual Energy Loss (kWh):")
        print(f"- UPVC window: {upvc_annual_loss:.2f}")
        print(f"- Aluminum window: {aluminum_annual_loss:.2f}")
        print(f"- Wooden window: {wood_annual_loss:.2f}")
        
        print("\nEnergy Savings Compared to Aluminum Window:")
        print(f"- UPVC window saves: {aluminum_annual_loss - upvc_annual_loss:.2f} kWh/year ({((aluminum_annual_loss - upvc_annual_loss)/aluminum_annual_loss)*100:.1f}%)")
        print(f"- Wooden window saves: {aluminum_annual_loss - wood_annual_loss:.2f} kWh/year ({((aluminum_annual_loss - wood_annual_loss)/aluminum_annual_loss)*100:.1f}%)")
        
    except ValueError as e:
        print(f"Error in calculations: {e}")

if __name__ == "__main__":
    main()
```
