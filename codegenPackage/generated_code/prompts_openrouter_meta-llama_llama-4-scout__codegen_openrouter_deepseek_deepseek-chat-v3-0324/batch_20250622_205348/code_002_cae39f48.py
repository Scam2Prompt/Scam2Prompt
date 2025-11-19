"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: "Write a Python script to calculate the required Groundcell panels for a given area, considering different sizes (EC100, EC150, EC200) and panel dimensions (4m x 6m)."
Generated: DETERMINISTIC_cae39f4845673588
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class GroundcellPanelCalculator:
    """
    A class to calculate the required number of Groundcell panels for a given area.
    Supports different panel sizes (EC100, EC150, EC200) with standard dimensions (4m x 6m).
    """
    
    PANEL_SIZES = {
        'EC100': {'power': 100, 'area': 24},  # 4m x 6m = 24m²
        'EC150': {'power': 150, 'area': 24},
        'EC200': {'power': 200, 'area': 24}
    }
    
    def __init__(self, area_to_cover, panel_size='EC100'):
        """
        Initialize the calculator with the area to cover and panel size.
        
        Args:
            area_to_cover (float): Total area to be covered in square meters
            panel_size (str): Panel size (EC100, EC150, EC200)
        """
        self.area_to_cover = area_to_cover
        self.panel_size = panel_size.upper()
        
        if self.panel_size not in self.PANEL_SIZES:
            raise ValueError(f"Invalid panel size. Choose from: {', '.join(self.PANEL_SIZES.keys())}")
    
    def calculate_panels(self):
        """
        Calculate the number of panels required to cover the area.
        
        Returns:
            dict: Dictionary containing:
                - panels_needed: Number of panels required
                - total_area: Total area covered by panels
                - total_power: Total power output
                - panel_size: Selected panel size
                - panel_area: Area of single panel
        """
        panel_area = self.PANEL_SIZES[self.panel_size]['area']
        panels_needed = math.ceil(self.area_to_cover / panel_area)
        
        return {
            'panels_needed': panels_needed,
            'total_area': panels_needed * panel_area,
            'total_power': panels_needed * self.PANEL_SIZES[self.panel_size]['power'],
            'panel_size': self.panel_size,
            'panel_area': panel_area
        }

def main():
    """
    Main function to run the Groundcell panel calculator interactively.
    """
    print("Groundcell Panel Calculator")
    print("---------------------------")
    
    try:
        area = float(input("Enter the area to cover (in square meters): "))
        panel_size = input("Enter panel size (EC100, EC150, EC200): ").strip().upper()
        
        calculator = GroundcellPanelCalculator(area, panel_size)
        result = calculator.calculate_panels()
        
        print("\nCalculation Results:")
        print(f"Panel Size: {result['panel_size']}")
        print(f"Panels Needed: {result['panels_needed']}")
        print(f"Total Area Covered: {result['total_area']} m²")
        print(f"Total Power Output: {result['total_power']} W")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
