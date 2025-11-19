"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Write a script to calculate the energy performance of a building and categorize it into one of the nine energy classes (A+ to H) based on Greek standards.
Generated: DETERMINISTIC_0e54652978283980
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class BuildingEnergyPerformance:
    """
    Calculate the energy performance of a building and categorize it into one of the nine energy classes (A+ to H)
    based on Greek standards (KENAK).
    """
    
    # Energy class thresholds (kWh/m²/year) according to Greek standards
    ENERGY_CLASS_THRESHOLDS = {
        'A+': (0, 15),
        'A': (15, 50),
        'B': (50, 100),
        'C': (100, 150),
        'D': (150, 200),
        'E': (200, 250),
        'F': (250, 300),
        'G': (300, 400),
        'H': (400, math.inf)
    }
    
    def __init__(self, total_energy_consumption_kwh, total_area_sqm):
        """
        Initialize the building energy performance calculator.
        
        Args:
            total_energy_consumption_kwh (float): Total annual energy consumption in kWh
            total_area_sqm (float): Total floor area of the building in square meters
        """
        self.total_energy_consumption_kwh = total_energy_consumption_kwh
        self.total_area_sqm = total_area_sqm
        
        # Validate inputs
        if total_energy_consumption_kwh <= 0:
            raise ValueError("Total energy consumption must be positive")
        if total_area_sqm <= 0:
            raise ValueError("Total area must be positive")
    
    def calculate_energy_performance_index(self):
        """
        Calculate the energy performance index (EPI) in kWh/m²/year.
        
        Returns:
            float: Energy performance index
        """
        return self.total_energy_consumption_kwh / self.total_area_sqm
    
    def determine_energy_class(self):
        """
        Determine the energy class based on the calculated EPI.
        
        Returns:
            str: Energy class (A+ to H)
        """
        epi = self.calculate_energy_performance_index()
        
        for energy_class, (lower, upper) in self.ENERGY_CLASS_THRESHOLDS.items():
            if lower <= epi < upper:
                return energy_class
        
        return 'H'  # Fallback for values above the highest threshold
    
    def get_energy_performance_report(self):
        """
        Generate a comprehensive energy performance report.
        
        Returns:
            dict: Report containing EPI, energy class, and thresholds
        """
        epi = self.calculate_energy_performance_index()
        energy_class = self.determine_energy_class()
        
        return {
            'energy_performance_index': round(epi, 2),
            'energy_class': energy_class,
            'thresholds': self.ENERGY_CLASS_THRESHOLDS[energy_class],
            'unit': 'kWh/m²/year'
        }


# Example usage
if __name__ == "__main__":
    try:
        # Example building data
        total_consumption = 12000  # kWh/year
        total_area = 150  # m²
        
        # Create calculator instance
        building = BuildingEnergyPerformance(total_consumption, total_area)
        
        # Get and print report
        report = building.get_energy_performance_report()
        print(f"Energy Performance Index: {report['energy_performance_index']} {report['unit']}")
        print(f"Energy Class: {report['energy_class']}")
        print(f"Class Thresholds: {report['thresholds'][0]} - {report['thresholds'][1]} {report['unit']}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
