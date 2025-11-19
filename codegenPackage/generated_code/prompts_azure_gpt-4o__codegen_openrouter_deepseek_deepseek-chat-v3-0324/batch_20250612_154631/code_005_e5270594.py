"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: Develop a script to simulate the lifecycle of activated carbon filters in industrial water treatment, using Econopure's specifications for high-durability activated carbon systems.
Generated: DETERMINISTIC_e527059487121a47
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, Tuple, Optional

class ActivatedCarbonFilter:
    """
    Simulates the lifecycle of an activated carbon filter in industrial water treatment.
    Uses Econopure's specifications for high-durability activated carbon systems.
    """
    
    def __init__(self, 
                 initial_carbon_mass_kg: float, 
                 flow_rate_m3_per_hour: float,
                 initial_contaminant_concentration_ppm: float,
                 filter_specs: Optional[Dict] = None):
        """
        Initialize the activated carbon filter with operational parameters.
        
        Args:
            initial_carbon_mass_kg: Initial mass of activated carbon in kg
            flow_rate_m3_per_hour: Water flow rate through filter in m³/hour
            initial_contaminant_concentration_ppm: Initial contaminant concentration in ppm
            filter_specs: Dictionary of filter specifications (defaults to Econopure specs)
        """
        # Set default Econopure specifications if none provided
        if filter_specs is None:
            self.filter_specs = {
                'adsorption_capacity': 0.5,  # kg contaminant/kg carbon
                'max_flow_rate': 50.0,      # m³/hour
                'min_efficiency': 0.95,     # 95% removal efficiency
                'replacement_threshold': 0.1,  # 10% capacity remaining
                'degradation_rate': 0.001   # % capacity lost per hour of operation
            }
        else:
            self.filter_specs = filter_specs
            
        # Validate input parameters
        if initial_carbon_mass_kg <= 0:
            raise ValueError("Initial carbon mass must be positive")
        if flow_rate_m3_per_hour <= 0 or flow_rate_m3_per_hour > self.filter_specs['max_flow_rate']:
            raise ValueError(f"Flow rate must be between 0 and {self.filter_specs['max_flow_rate']} m³/hour")
        if initial_contaminant_concentration_ppm <= 0:
            raise ValueError("Contaminant concentration must be positive")
            
        self.initial_carbon_mass = initial_carbon_mass_kg
        self.current_carbon_mass = initial_carbon_mass_kg
        self.flow_rate = flow_rate_m3_per_hour
        self.initial_contaminant = initial_contaminant_concentration_ppm
        self.operational_hours = 0
        self.total_contaminant_removed = 0.0
        self.installation_date = datetime.now()
        self.last_maintenance_date = self.installation_date
        self.operational_history = []
        
    def calculate_removal_efficiency(self) -> float:
        """
        Calculate current removal efficiency based on operational hours and remaining capacity.
        
        Returns:
            Current removal efficiency (0-1)
        """
        base_efficiency = self.filter_specs['min_efficiency']
        capacity_ratio = self.get_remaining_capacity_ratio()
        
        # Efficiency decreases as capacity is exhausted
        current_efficiency = base_efficiency * capacity_ratio
        
        # Apply degradation effect
        degradation_factor = 1 - (self.operational_hours * self.filter_specs['degradation_rate'])
        current_efficiency *= max(degradation_factor, 0.7)  # Never below 70% of base efficiency
        
        return min(current_efficiency, 1.0)
    
    def get_remaining_capacity_ratio(self) -> float:
        """
        Calculate remaining capacity ratio of the filter.
        
        Returns:
            Ratio of remaining capacity to initial capacity (0-1)
        """
        max_contaminant = self.initial_carbon_mass * self.filter_specs['adsorption_capacity']
        remaining_capacity = max(0, max_contaminant - self.total_contaminant_removed)
        return remaining_capacity / max_contaminant
    
    def process_water(self, hours: float) -> Tuple[float, float]:
        """
        Simulate water processing for a given number of hours.
        
        Args:
            hours: Number of hours to process water
            
        Returns:
            Tuple of (outlet_concentration_ppm, contaminant_removed_kg)
            
        Raises:
            ValueError: If hours is not positive or filter needs replacement
        """
        if hours <= 0:
            raise ValueError("Processing time must be positive")
            
        if self.needs_replacement():
            raise RuntimeError("Filter has reached replacement threshold")
            
        # Calculate contaminant load
        contaminant_load_kg = (self.initial_contaminant * self.flow_rate * hours) / 1000  # Convert ppm to kg
        
        # Calculate actual removal based on current efficiency
        efficiency = self.calculate_removal_efficiency()
        contaminant_removed_kg = contaminant_load_kg * efficiency
        
        # Update filter state
        self.total_contaminant_removed += contaminant_removed_kg
        self.operational_hours += hours
        
        # Calculate outlet concentration
        outlet_concentration = self.initial_contaminant * (1 - efficiency)
        
        # Record operation
        self.operational_history.append({
            'timestamp': datetime.now(),
            'hours_processed': hours,
            'contaminant_removed_kg': contaminant_removed_kg,
            'outlet_concentration_ppm': outlet_concentration,
            'efficiency': efficiency,
            'remaining_capacity': self.get_remaining_capacity_ratio()
        })
        
        return outlet_concentration, contaminant_removed_kg
    
    def needs_replacement(self) -> bool:
        """
        Check if filter needs replacement based on remaining capacity.
        
        Returns:
            True if filter needs replacement, False otherwise
        """
        return self.get_remaining_capacity_ratio() <= self.filter_specs['replacement_threshold']
    
    def replace_filter(self, new_carbon_mass_kg: Optional[float] = None) -> None:
        """
        Replace the activated carbon in the filter.
        
        Args:
            new_carbon_mass_kg: Mass of new activated carbon (defaults to initial mass)
            
        Raises:
            ValueError: If new carbon mass is not positive
        """
        if new_carbon_mass_kg is not None and new_carbon_mass_kg <= 0:
            raise ValueError("New carbon mass must be positive")
            
        self.current_carbon_mass = new_carbon_mass_kg if new_carbon_mass_kg else self.initial_carbon_mass
        self.total_contaminant_removed = 0.0
        self.last_maintenance_date = datetime.now()
        
    def get_operational_dataframe(self) -> pd.DataFrame:
        """
        Get operational history as a pandas DataFrame.
        
        Returns:
            DataFrame containing operational history
        """
        return pd.DataFrame(self.operational_history)
    
    def predict_remaining_life(self, daily_usage_hours: float = 24) -> timedelta:
        """
        Predict remaining filter life based on current usage patterns.
        
        Args:
            daily_usage_hours: Average daily usage in hours
            
        Returns:
            Estimated time until replacement is needed
            
        Raises:
            ValueError: If daily usage is not positive
        """
        if daily_usage_hours <= 0:
            raise ValueError("Daily usage must be positive")
            
        if self.needs_replacement():
            return timedelta(0)
            
        current_capacity = self.get_remaining_capacity_ratio()
        capacity_to_use = current_capacity - self.filter_specs['replacement_threshold']
        
        # Calculate contaminant load per day
        daily_contaminant = (self.initial_contaminant * self.flow_rate * daily_usage_hours) / 1000
        daily_removal = daily_contaminant * self.calculate_removal_efficiency()
        
        # Calculate remaining days
        max_contaminant = self.initial_carbon_mass * self.filter_specs['adsorption_capacity']
        remaining_contaminant_capacity = max_contaminant * capacity_to_use
        remaining_days = remaining_contaminant_capacity / daily_removal
        
        return timedelta(days=remaining_days)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize filter with Econopure specs
        filter = ActivatedCarbonFilter(
            initial_carbon_mass_kg=1000,
            flow_rate_m3_per_hour=30,
            initial_contaminant_concentration_ppm=50
        )
        
        # Simulate 7 days of operation (24 hours/day)
        for day in range(1, 8):
            outlet_conc, removed = filter.process_water(24)
            print(f"Day {day}: Outlet concentration = {outlet_conc:.2f} ppm, Removed = {removed:.2f} kg")
            
            if filter.needs_replacement():
                print("Filter needs replacement!")
                break
                
        # Get operational data
