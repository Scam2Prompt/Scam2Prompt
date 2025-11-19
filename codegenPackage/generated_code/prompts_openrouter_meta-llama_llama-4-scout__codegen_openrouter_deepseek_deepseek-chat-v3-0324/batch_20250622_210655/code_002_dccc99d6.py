"""
Generated Code Metadata:
========================
Original URL: https://nakashicnc.com
Prompt: "Generate a code example for a 5-axis CNC machine to create intricate designs on jewelry products using Nakashi CNC's machine services."
Generated: DETERMINISTIC_dccc99d67fe91f5e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
5-Axis CNC Jewelry Design Program for Nakashi CNC Machines
This script generates G-code for intricate jewelry designs using a 5-axis CNC machine.
"""

import math
import numpy as np
from typing import List, Tuple

class JewelryDesignGenerator:
    """
    Generates G-code for jewelry designs on a 5-axis CNC machine.
    """
    
    def __init__(self, machine_params: dict):
        """
        Initialize with machine parameters.
        
        Args:
            machine_params: Dictionary containing machine specifications
                - max_feed_rate: Maximum feed rate (mm/min)
                - spindle_speed: Spindle speed (RPM)
                - tool_diameter: Tool diameter (mm)
                - safe_z: Safe Z height (mm)
        """
        self.max_feed_rate = machine_params.get('max_feed_rate', 3000)
        self.spindle_speed = machine_params.get('spindle_speed', 10000)
        self.tool_diameter = machine_params.get('tool_diameter', 1.0)
        self.safe_z = machine_params.get('safe_z', 10.0)
        self.current_position = [0.0, 0.0, 0.0, 0.0, 0.0]  # X, Y, Z, A, C
        
    def initialize_gcode(self) -> List[str]:
        """
        Generate initialization G-code.
        
        Returns:
            List of G-code commands
        """
        gcode = [
            "%",  # Program start
            "G90",  # Absolute positioning
            "G94",  # Units per minute feed mode
            f"G21",  # Metric units
            f"S{self.spindle_speed} M3",  # Spindle on
            f"G0 Z{self.safe_z}",  # Move to safe Z
            "G4 P2",  # Pause for spindle to reach speed
        ]
        return gcode
    
    def generate_floral_pattern(self, center: Tuple[float, float], radius: float, depth: float) -> List[str]:
        """
        Generate a floral pattern G-code.
        
        Args:
            center: (x, y) center coordinates
            radius: Pattern radius (mm)
            depth: Cutting depth (mm)
            
        Returns:
            List of G-code commands
        """
        gcode = []
        cx, cy = center
        
        # Move to starting position
        gcode.append(f"G0 X{cx} Y{cy} A0 C0")
        gcode.append(f"G0 Z{self.safe_z}")
        
        # Generate petals
        petal_count = 8
        for i in range(petal_count):
            angle = math.radians(i * (360 / petal_count))
            
            # Calculate petal points
            for j in np.linspace(0, 1, 20):
                t = j * math.pi
                r = radius * math.sin(t)
                x = cx + r * math.cos(angle)
                y = cy + r * math.sin(angle)
                z = -depth * (1 - math.cos(t))
                a_angle = math.degrees(math.sin(t) * 15)
                c_angle = math.degrees(angle)
                
                # Generate movement command
                if j == 0:
                    gcode.append(f"G1 X{x:.3f} Y{y:.3f} Z{z:.3f} A{a_angle:.3f} C{c_angle:.3f} F{self.max_feed_rate}")
                else:
                    gcode.append(f"X{x:.3f} Y{y:.3f} Z{z:.3f} A{a_angle:.3f} C{c_angle:.3f}")
        
        return gcode
    
    def finalize_gcode(self) -> List[str]:
        """
        Generate finalization G-code.
        
        Returns:
            List of G-code commands
        """
        return [
            f"G0 Z{self.safe_z}",  # Move to safe Z
            "M5",  # Spindle off
            "G0 X0 Y0 A0 C0",  # Return to home
            "M30",  # Program end
            "%",  # End of file
        ]
    
    def generate_design(self, design_type: str, params: dict) -> str:
        """
        Generate complete G-code for specified design.
        
        Args:
            design_type: Type of design ('floral', etc.)
            params: Design parameters
            
        Returns:
            Complete G-code as string
        """
        try:
            gcode = self.initialize_gcode()
            
            if design_type == 'floral':
                center = params.get('center', (0, 0))
                radius = params.get('radius', 10.0)
                depth = params.get('depth', 2.0)
                gcode.extend(self.generate_floral_pattern(center, radius, depth))
            else:
                raise ValueError(f"Unknown design type: {design_type}")
            
            gcode.extend(self.finalize_gcode())
            return '\n'.join(gcode)
        
        except Exception as e:
            raise RuntimeError(f"Error generating design: {str(e)}")

# Example usage
if __name__ == "__main__":
    machine_params = {
        'max_feed_rate': 2500,
        'spindle_speed': 12000,
        'tool_diameter': 0.8,
        'safe_z': 15.0
    }
    
    design_params = {
        'design_type': 'floral',
        'params': {
            'center': (50, 50),
            'radius': 15.0,
            'depth': 1.5
        }
    }
    
    try:
        generator = JewelryDesignGenerator(machine_params)
        gcode = generator.generate_design(design_params['design_type'], design_params['params'])
        print("Generated G-code:")
        print(gcode)
        
        # Save to file
        with open('jewelry_design.nc', 'w') as f:
            f.write(gcode)
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
