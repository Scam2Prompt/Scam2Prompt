"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: "Write a Python script to calculate the optimal solar panel layout for a residential building in Groningen, considering the NEN 1010 and NEN 3140 standards."
Generated: DETERMINISTIC_fa9e506022e4e662
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import numpy as np
from typing import Tuple, List, Optional

class SolarPanelLayoutCalculator:
    """
    Calculates the optimal solar panel layout for a residential building in Groningen,
    considering NEN 1010 and NEN 3140 standards.
    """
    
    # Constants for Groningen (latitude ~53.2°N)
    GRONINGEN_LATITUDE = math.radians(53.2)
    STANDARD_SOLAR_PANEL_WIDTH = 1.0  # meters
    STANDARD_SOLAR_PANEL_HEIGHT = 1.7  # meters
    MIN_CLEARANCE = 0.3  # meters (NEN 3140 safety clearance)
    MAX_ROOF_LOAD = 25.0  # kg/m² (typical roof load limit)
    PANEL_WEIGHT = 20.0  # kg per panel
    
    def __init__(self, roof_width: float, roof_length: float, roof_angle: float = 30.0):
        """
        Initialize the calculator with roof dimensions and angle.
        
        Args:
            roof_width: Width of the roof (meters)
            roof_length: Length of the roof (meters)
            roof_angle: Angle of the roof in degrees (default 30°)
        """
        self.roof_width = roof_width
        self.roof_length = roof_length
        self.roof_angle = math.radians(roof_angle)
        
    def calculate_optimal_tilt(self) -> float:
        """
        Calculate optimal tilt angle for solar panels in Groningen.
        Based on latitude and seasonal sun position.
        
        Returns:
            Optimal tilt angle in radians
        """
        # Optimal tilt is typically latitude - 15° for summer optimization
        return max(math.radians(15), self.GRONINGEN_LATITUDE - math.radians(15))
    
    def calculate_shading_spacing(self, panel_height: float) -> float:
        """
        Calculate minimum spacing between panel rows to prevent shading.
        
        Args:
            panel_height: Height of the solar panel when tilted
            
        Returns:
            Minimum required spacing between rows in meters
        """
        # Winter solstice sun angle (lowest sun position)
        winter_sun_angle = math.radians(90 - 53.2 - 23.5)  # 90 - latitude - 23.5°
        return panel_height / math.tan(winter_sun_angle)
    
    def calculate_max_panels(self) -> Tuple[int, List[List[Tuple[float, float]]]]:
        """
        Calculate maximum number of solar panels that can fit on the roof
        considering NEN standards and optimal layout.
        
        Returns:
            Tuple of (total_panels, panel_positions) where panel_positions is a list
            of (x,y) tuples for each panel's bottom-left corner
        """
        try:
            if self.roof_width <= 0 or self.roof_length <= 0:
                raise ValueError("Roof dimensions must be positive")
                
            # Calculate panel dimensions when tilted
            tilted_panel_height = self.STANDARD_SOLAR_PANEL_WIDTH * math.sin(self.calculate_optimal_tilt()) + \
                                self.STANDARD_SOLAR_PANEL_HEIGHT * math.cos(self.calculate_optimal_tilt())
            
            tilted_panel_width = self.STANDARD_SOLAR_PANEL_WIDTH * math.cos(self.calculate_optimal_tilt()) + \
                               self.STANDARD_SOLAR_PANEL_HEIGHT * math.sin(self.calculate_optimal_tilt())
            
            spacing = self.calculate_shading_spacing(tilted_panel_height)
            
            # Calculate how many panels fit width-wise
            panels_per_row = math.floor((self.roof_width - self.MIN_CLEARANCE) / 
                                      (tilted_panel_width + self.MIN_CLEARANCE))
            
            # Calculate how many rows fit length-wise
            usable_length = self.roof_length - 2 * self.MIN_CLEARANCE  # clearance at edges
            rows = math.floor(usable_length / (tilted_panel_height + spacing))
            
            # Check structural load
            total_panels = panels_per_row * rows
            roof_area = self.roof_width * self.roof_length
            total_load = total_panels * self.PANEL_WEIGHT
            load_per_area = total_load / roof_area
            
            if load_per_area > self.MAX_ROOF_LOAD:
                # Reduce number of panels to meet load requirements
                max_panels = math.floor((self.MAX_ROOF_LOAD * roof_area) / self.PANEL_WEIGHT)
                rows = math.floor(max_panels / panels_per_row)
                total_panels = rows * panels_per_row
            
            # Calculate panel positions
            panel_positions = []
            for row in range(rows):
                for col in range(panels_per_row):
                    x = self.MIN_CLEARANCE + col * (tilted_panel_width + self.MIN_CLEARANCE)
                    y = self.MIN_CLEARANCE + row * (tilted_panel_height + spacing)
                    panel_positions.append((x, y))
            
            return total_panels, panel_positions
            
        except Exception as e:
            raise RuntimeError(f"Error calculating panel layout: {str(e)}")
    
    def calculate_annual_yield(self, panel_count: int, panel_efficiency: float = 0.18) -> float:
        """
        Estimate annual energy yield in kWh.
        
        Args:
            panel_count: Number of solar panels
            panel_efficiency: Efficiency of the panels (default 18%)
            
        Returns:
            Estimated annual yield in kWh
        """
        try:
            if panel_count <= 0:
                raise ValueError("Panel count must be positive")
            if not 0 < panel_efficiency <= 1:
                raise ValueError("Panel efficiency must be between 0 and 1")
                
            # Groningen average solar irradiation: ~900 kWh/m²/year
            panel_area = self.STANDARD_SOLAR_PANEL_WIDTH * self.STANDARD_SOLAR_PANEL_HEIGHT
            total_area = panel_area * panel_count
            
            # Adjust for tilt angle (optimal tilt increases effective irradiation)
            tilt_factor = 1 + 0.1 * math.sin(self.calculate_optimal_tilt())
            
            return total_area * 900 * panel_efficiency * tilt_factor
            
        except Exception as e:
            raise RuntimeError(f"Error calculating annual yield: {str(e)}")


def main():
    """Example usage of the SolarPanelLayoutCalculator."""
    try:
        # Example roof: 10m wide, 8m long, 30° angle
        calculator = SolarPanelLayoutCalculator(roof_width=10, roof_length=8)
        
        panel_count, positions = calculator.calculate_max_panels()
        print(f"Maximum panels: {panel_count}")
        print(f"Panel positions (first 5): {positions[:5]}")
        
        annual_yield = calculator.calculate_annual_yield(panel_count)
        print(f"Estimated annual yield: {annual_yield:.2f} kWh")
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
