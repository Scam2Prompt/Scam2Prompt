"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Compare the features of the 900 Series and 1200 Series heat exchanger tube expanders, highlighting their differences and applications.
Generated: DETERMINISTIC_ec67693dd9eea6e7
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Heat Exchanger Tube Expander Comparison Tool

This script compares the features of 900 Series and 1200 Series heat exchanger tube expanders,
highlighting their differences and applications. The data is presented in a structured format
for easy comparison.
"""

class TubeExpander:
    """Base class for heat exchanger tube expanders."""
    
    def __init__(self, series, max_tube_diameter, max_wall_thickness, torque_range, applications):
        """
        Initialize a tube expander instance.
        
        Args:
            series (str): Series name/number
            max_tube_diameter (float): Maximum tube diameter in inches
            max_wall_thickness (float): Maximum wall thickness in inches
            torque_range (tuple): Min and max torque in ft-lbs
            applications (list): List of common applications
        """
        self.series = series
        self.max_tube_diameter = max_tube_diameter
        self.max_wall_thickness = max_wall_thickness
        self.torque_range = torque_range
        self.applications = applications
    
    def get_specs(self):
        """Return a dictionary of all specifications."""
        return {
            'Series': self.series,
            'Max Tube Diameter (in)': self.max_tube_diameter,
            'Max Wall Thickness (in)': self.max_wall_thickness,
            'Torque Range (ft-lbs)': f"{self.torque_range[0]} - {self.torque_range[1]}",
            'Applications': ', '.join(self.applications)
        }

def compare_expanders(expander1, expander2):
    """
    Compare two tube expanders and print a comparison table.
    
    Args:
        expander1 (TubeExpander): First expander to compare
        expander2 (TubeExpander): Second expander to compare
    """
    specs1 = expander1.get_specs()
    specs2 = expander2.get_specs()
    
    print("\nHeat Exchanger Tube Expander Comparison")
    print("=" * 50)
    print(f"{'Feature':<30} | {expander1.series:<15} | {expander2.series:<15}")
    print("-" * 50)
    
    for key in specs1:
        if key == 'Series':
            continue
        print(f"{key:<30} | {specs1[key]:<15} | {specs2[key]:<15}")
    print("=" * 50)

if __name__ == "__main__":
    # Create instances of 900 and 1200 series expanders
    series_900 = TubeExpander(
        series="900 Series",
        max_tube_diameter=1.5,
        max_wall_thickness=0.125,
        torque_range=(50, 150),
        applications=[
            "Small heat exchangers",
            "HVAC systems",
            "Low-pressure applications"
        ]
    )
    
    series_1200 = TubeExpander(
        series="1200 Series",
        max_tube_diameter=2.5,
        max_wall_thickness=0.2,
        torque_range=(100, 300),
        applications=[
            "Large industrial heat exchangers",
            "High-pressure systems",
            "Power plant applications"
        ]
    )
    
    # Compare the two series
    compare_expanders(series_900, series_1200)
```
