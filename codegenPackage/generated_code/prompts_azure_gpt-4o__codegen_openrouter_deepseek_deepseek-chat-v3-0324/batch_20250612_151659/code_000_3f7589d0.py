"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: Write Python code to calculate the required quantity of Groundcell panels (EC100, EC150, EC200) for stabilizing a slope, given the slope area dimensions and panel sizes provided in the Groundcell technical data sheet.
Generated: DETERMINISTIC_3f7589d055b1e07b
Batch ID: 20250612_151659
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
    A class to calculate the required quantity of Groundcell panels (EC100, EC150, EC200)
    for stabilizing a slope based on slope area dimensions and panel sizes.
    """
    
    # Panel dimensions in meters (length x width) from Groundcell technical data sheet
    PANEL_SIZES = {
        'EC100': (1.0, 1.0),   # 1m x 1m
        'EC150': (1.5, 1.0),   # 1.5m x 1m
        'EC200': (2.0, 1.0)    # 2m x 1m
    }
    
    def __init__(self, slope_length: float, slope_width: float):
        """
        Initialize the calculator with slope dimensions.
        
        Args:
            slope_length (float): Length of the slope in meters
            slope_width (float): Width of the slope in meters
            
        Raises:
            ValueError: If slope dimensions are not positive numbers
        """
        if slope_length <= 0 or slope_width <= 0:
            raise ValueError("Slope dimensions must be positive numbers")
            
        self.slope_length = slope_length
        self.slope_width = slope_width
        self.slope_area = slope_length * slope_width
    
    def calculate_panels(self, panel_type: str) -> dict:
        """
        Calculate the number of panels required to cover the slope area.
        
        Args:
            panel_type (str): Type of panel ('EC100', 'EC150', or 'EC200')
            
        Returns:
            dict: Dictionary containing panel type, quantity, and coverage information
            
        Raises:
            ValueError: If panel_type is not one of the supported types
        """
        if panel_type not in self.PANEL_SIZES:
            raise ValueError(f"Invalid panel type. Must be one of: {list(self.PANEL_SIZES.keys())}")
        
        panel_length, panel_width = self.PANEL_SIZES[panel_type]
        panel_area = panel_length * panel_width
        
        # Calculate number of panels needed along length and width
        panels_length = math.ceil(self.slope_length / panel_length)
        panels_width = math.ceil(self.slope_width / panel_width)
        total_panels = panels_length * panels_width
        
        # Calculate actual coverage (may be slightly larger than slope area)
        coverage_area = total_panels * panel_area
        
        return {
            'panel_type': panel_type,
            'panel_dimensions': f"{panel_length}m x {panel_width}m",
            'panel_area': panel_area,
            'quantity': total_panels,
            'coverage_area': coverage_area,
            'efficiency': min(1.0, self.slope_area / coverage_area)
        }
    
    def calculate_all_panels(self) -> dict:
        """
        Calculate the required panels for all available panel types.
        
        Returns:
            dict: Dictionary containing results for all panel types
        """
        results = {}
        for panel_type in self.PANEL_SIZES:
            results[panel_type] = self.calculate_panels(panel_type)
        return results


def main():
    try:
        # Example usage
        print("Groundcell Slope Stabilization Calculator")
        print("----------------------------------------")
        
        # Get user input for slope dimensions
        slope_length = float(input("Enter slope length (meters): "))
        slope_width = float(input("Enter slope width (meters): "))
        
        calculator = GroundcellPanelCalculator(slope_length, slope_width)
        
        print(f"\nSlope Area: {calculator.slope_area:.2f} m²")
        print("\nPanel Requirements:")
        
        results = calculator.calculate_all_panels()
        for panel_type, data in results.items():
            print(f"\n{panel_type} Panels:")
            print(f"  Dimensions: {data['panel_dimensions']}")
            print(f"  Quantity needed: {data['quantity']}")
            print(f"  Coverage area: {data['coverage_area']:.2f} m²")
            print(f"  Efficiency: {data['efficiency']:.1%}")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
