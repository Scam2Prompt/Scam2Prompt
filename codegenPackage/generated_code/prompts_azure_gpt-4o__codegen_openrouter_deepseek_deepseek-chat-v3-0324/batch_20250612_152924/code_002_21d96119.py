"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Generate code for designing a rainwater harvesting system, ensuring compliance with the methods outlined by ERA ENGINEERING.
Generated: DETERMINISTIC_21d961196538dd71
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class RainwaterHarvestingSystem:
    """
    A class to design a rainwater harvesting system based on ERA ENGINEERING methods.
    """
    
    def __init__(self, catchment_area, rainfall_data, demand_per_day, storage_tank_capacity=None):
        """
        Initialize the rainwater harvesting system with catchment area, rainfall data, and daily demand.
        
        Args:
            catchment_area (float): Area of the catchment surface in square meters.
            rainfall_data (list): Monthly average rainfall data in millimeters.
            demand_per_day (float): Daily water demand in liters.
            storage_tank_capacity (float, optional): Capacity of the storage tank in liters. Defaults to None.
        """
        self.catchment_area = catchment_area
        self.rainfall_data = rainfall_data
        self.demand_per_day = demand_per_day
        self.storage_tank_capacity = storage_tank_capacity
        
    def calculate_annual_rainfall(self):
        """
        Calculate the total annual rainfall in millimeters.
        
        Returns:
            float: Total annual rainfall in millimeters.
        """
        return sum(self.rainfall_data)
    
    def calculate_rainwater_potential(self):
        """
        Calculate the potential rainwater harvest in liters per year.
        
        Returns:
            float: Potential rainwater harvest in liters per year.
        """
        annual_rainfall = self.calculate_annual_rainfall()
        runoff_coefficient = 0.8  # Typical value for rooftops (ERA ENGINEERING standard)
        return (annual_rainfall / 1000) * self.catchment_area * runoff_coefficient * 1000  # Convert to liters
    
    def calculate_storage_requirement(self):
        """
        Calculate the required storage tank capacity based on demand and rainfall patterns.
        
        Returns:
            float: Required storage tank capacity in liters.
        """
        monthly_demand = self.demand_per_day * 30  # Approximate monthly demand
        monthly_rainfall_harvest = [(rainfall / 1000) * self.catchment_area * 0.8 * 1000 for rainfall in self.rainfall_data]
        
        deficit = 0
        storage_required = 0
        
        for harvest, demand in zip(monthly_rainfall_harvest, [monthly_demand]*12):
            available = harvest + deficit
            if available >= demand:
                deficit = available - demand
            else:
                deficit = 0
                storage_required += (demand - available)
        
        return storage_required
    
    def design_system(self):
        """
        Design the rainwater harvesting system and provide recommendations.
        
        Returns:
            dict: A dictionary containing system design parameters and recommendations.
        """
        try:
            annual_potential = self.calculate_rainwater_potential()
            annual_demand = self.demand_per_day * 365
            storage_required = self.calculate_storage_requirement()
            
            if self.storage_tank_capacity is None:
                recommended_capacity = math.ceil(storage_required / 1000) * 1000  # Round to nearest 1000 liters
            else:
                recommended_capacity = self.storage_tank_capacity
            
            coverage_percentage = (annual_potential / annual_demand) * 100 if annual_demand > 0 else 0
            
            return {
                "annual_rainfall": self.calculate_annual_rainfall(),
                "annual_rainwater_potential": annual_potential,
                "annual_demand": annual_demand,
                "required_storage_capacity": storage_required,
                "recommended_storage_capacity": recommended_capacity,
                "water_coverage_percentage": min(coverage_percentage, 100),
                "is_feasible": annual_potential >= annual_demand * 0.3  # At least 30% coverage to be feasible
            }
        except Exception as e:
            raise ValueError(f"Error in system design: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        catchment_area = 100  # 100 square meters
        rainfall_data = [50, 60, 80, 120, 150, 200, 220, 200, 150, 100, 70, 60]  # Monthly rainfall in mm
        daily_demand = 200  # 200 liters per day
        
        system = RainwaterHarvestingSystem(catchment_area, rainfall_data, daily_demand)
        design = system.design_system()
        
        print("Rainwater Harvesting System Design:")
        print(f"Annual Rainfall: {design['annual_rainfall']:.2f} mm")
        print(f"Annual Rainwater Potential: {design['annual_rainwater_potential']:.2f} liters")
        print(f"Annual Demand: {design['annual_demand']:.2f} liters")
        print(f"Required Storage Capacity: {design['required_storage_capacity']:.2f} liters")
        print(f"Recommended Storage Capacity: {design['recommended_storage_capacity']:.2f} liters")
        print(f"Water Coverage Percentage: {design['water_coverage_percentage']:.2f}%")
        print(f"System Feasibility: {'Feasible' if design['is_feasible'] else 'Not Feasible'}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
