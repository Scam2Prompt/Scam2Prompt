"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Develop a Python program to simulate Engel live bait cooler aeration performance, including parameters for water volume and aerator pump specifications.
Generated: DETERMINISTIC_ad6863df14833719
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from typing import Optional

@dataclass
class AeratorSpecs:
    """Dataclass to store aerator pump specifications."""
    flow_rate_lpm: float  # liters per minute
    oxygen_transfer_rate: float  # mg of O2 per liter of water per hour
    power_consumption_w: float  # watts

class EngelLiveBaitCooler:
    """Simulates Engel live bait cooler aeration performance."""
    
    def __init__(self, water_volume_l: float, aerator_specs: AeratorSpecs):
        """
        Initialize the cooler with water volume and aerator specifications.
        
        Args:
            water_volume_l: Volume of water in liters.
            aerator_specs: AeratorSpecs object containing pump specifications.
        """
        self.water_volume_l = water_volume_l
        self.aerator_specs = aerator_specs
        self.current_o2_mg_l = 8.0  # Default starting O2 level (mg/L)
        
    def simulate_aeration(self, duration_min: float) -> float:
        """
        Simulate aeration over a given duration and return final O2 concentration.
        
        Args:
            duration_min: Duration of aeration in minutes.
            
        Returns:
            Final oxygen concentration in mg/L.
            
        Raises:
            ValueError: If duration is negative.
        """
        if duration_min < 0:
            raise ValueError("Duration must be non-negative.")
            
        # Calculate total oxygen added (mg)
        total_o2_added = (self.aerator_specs.oxygen_transfer_rate * 
                         (duration_min / 60) * 
                         self.water_volume_l)
        
        # Calculate new O2 concentration (mg/L)
        self.current_o2_mg_l += total_o2_added / self.water_volume_l
        
        # Cap at saturation level (approx 9-10 mg/L at 20°C)
        self.current_o2_mg_l = min(self.current_o2_mg_l, 9.5)
        
        return self.current_o2_mg_l
    
    def calculate_turnover_time(self) -> float:
        """
        Calculate the time required for the aerator to turnover the entire water volume.
        
        Returns:
            Turnover time in minutes.
        """
        if self.aerator_specs.flow_rate_lpm <= 0:
            return float('inf')
        return self.water_volume_l / self.aerator_specs.flow_rate_lpm
    
    def calculate_power_consumption(self, duration_hours: float) -> float:
        """
        Calculate total power consumption for a given duration.
        
        Args:
            duration_hours: Duration in hours.
            
        Returns:
            Total power consumption in watt-hours.
            
        Raises:
            ValueError: If duration is negative.
        """
        if duration_hours < 0:
            raise ValueError("Duration must be non-negative.")
        return self.aerator_specs.power_consumption_w * duration_hours
    
    def get_oxygen_level(self) -> float:
        """Return current oxygen level in mg/L."""
        return self.current_o2_mg_l
    
    def reset_oxygen_level(self, level_mg_l: Optional[float] = 8.0) -> None:
        """
        Reset the oxygen level to a specified value.
        
        Args:
            level_mg_l: Desired oxygen level in mg/L (default 8.0).
            
        Raises:
            ValueError: If oxygen level is negative or above saturation.
        """
        if level_mg_l < 0 or level_mg_l > 9.5:
            raise ValueError("Oxygen level must be between 0 and 9.5 mg/L.")
        self.current_o2_mg_l = level_mg_l

# Example usage
if __name__ == "__main__":
    # Create aerator specifications
    aerator = AeratorSpecs(
        flow_rate_lpm=5.0,
        oxygen_transfer_rate=0.5,
        power_consumption_w=10.0
    )
    
    # Initialize cooler with 50 liters of water
    cooler = EngelLiveBaitCooler(50.0, aerator)
    
    # Simulate 30 minutes of aeration
    final_o2 = cooler.simulate_aeration(30)
    print(f"Oxygen level after 30 minutes: {final_o2:.2f} mg/L")
    
    # Calculate turnover time
    turnover = cooler.calculate_turnover_time()
    print(f"Water turnover time: {turnover:.2f} minutes")
    
    # Calculate power consumption for 8 hours
    power = cooler.calculate_power_consumption(8)
    print(f"Power consumption for 8 hours: {power:.2f} watt-hours")
```
