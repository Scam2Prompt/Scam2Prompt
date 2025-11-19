"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: Write a program to generate personalized renting plans for businesses based on their fleet size, operational needs, and budget, inspired by Innova Renting's tailored solutions.
Generated: DETERMINISTIC_f944cc8a9b7c85a0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional

class VehicleType(Enum):
    """Enum representing different types of vehicles available for rent."""
    SEDAN = auto()
    SUV = auto()
    TRUCK = auto()
    VAN = auto()
    ELECTRIC = auto()

class RentalDuration(Enum):
    """Enum representing different rental duration options."""
    SHORT_TERM = auto()  # 1-30 days
    MEDIUM_TERM = auto()  # 1-6 months
    LONG_TERM = auto()  # 6+ months

@dataclass
class Vehicle:
    """Class representing a vehicle available for rent."""
    type: VehicleType
    daily_rate: float
    monthly_rate: float
    yearly_rate: float
    available: bool = True

@dataclass
class BusinessProfile:
    """Class representing a business's rental needs."""
    name: str
    fleet_size: int
    preferred_vehicle_types: List[VehicleType]
    operational_hours: int  # Weekly operational hours
    budget: float  # Monthly budget
    rental_duration: RentalDuration

@dataclass
class RentalPlan:
    """Class representing a personalized rental plan for a business."""
    business_name: str
    recommended_vehicles: List[VehicleType]
    total_cost: float
    cost_per_vehicle: float
    duration: RentalDuration
    savings: Optional[float] = None  # Potential savings compared to standard rates

class RentalPlanGenerator:
    """Generates personalized renting plans for businesses."""
    
    def __init__(self, vehicles: List[Vehicle]):
        """
        Initialize the plan generator with available vehicles.
        
        Args:
            vehicles: List of available vehicles for rent
        """
        self.vehicles = vehicles
        self.vehicle_type_map = {v.type: v for v in vehicles}
    
    def _calculate_vehicle_cost(self, vehicle_type: VehicleType, duration: RentalDuration) -> float:
        """
        Calculate the cost for a vehicle based on rental duration.
        
        Args:
            vehicle_type: Type of vehicle
            duration: Rental duration
            
        Returns:
            float: Calculated cost
            
        Raises:
            ValueError: If vehicle type is not available
        """
        if vehicle_type not in self.vehicle_type_map:
            raise ValueError(f"Vehicle type {vehicle_type} not available")
        
        vehicle = self.vehicle_type_map[vehicle_type]
        
        if duration == RentalDuration.SHORT_TERM:
            return vehicle.daily_rate * 30  # Approximate monthly cost
        elif duration == RentalDuration.MEDIUM_TERM:
            return vehicle.monthly_rate
        else:  # LONG_TERM
            return vehicle.yearly_rate / 12  # Monthly cost
    
    def _get_optimal_vehicle(self, preferred_types: List[VehicleType], budget_per_vehicle: float, duration: RentalDuration) -> Optional[VehicleType]:
        """
        Find the optimal vehicle type based on preferences and budget.
        
        Args:
            preferred_types: List of preferred vehicle types
            budget_per_vehicle: Budget per vehicle
            duration: Rental duration
            
        Returns:
            Optional[VehicleType]: Best matching vehicle type or None if none fit
        """
        for vehicle_type in preferred_types:
            if vehicle_type in self.vehicle_type_map:
                cost = self._calculate_vehicle_cost(vehicle_type, duration)
                if cost <= budget_per_vehicle:
                    return vehicle_type
        return None
    
    def generate_plan(self, business: BusinessProfile) -> RentalPlan:
        """
        Generate a personalized rental plan for a business.
        
        Args:
            business: Business profile with rental needs
            
        Returns:
            RentalPlan: Generated rental plan
            
        Raises:
            ValueError: If no suitable vehicles are found for the budget
        """
        budget_per_vehicle = business.budget / business.fleet_size if business.fleet_size > 0 else 0
        
        # Try preferred vehicles first
        optimal_vehicle = self._get_optimal_vehicle(
            business.preferred_vehicle_types,
            budget_per_vehicle,
            business.rental_duration
        )
        
        # If no preferred vehicles fit, try all available vehicles
        if optimal_vehicle is None:
            all_vehicles = list(self.vehicle_type_map.keys())
            optimal_vehicle = self._get_optimal_vehicle(
                all_vehicles,
                budget_per_vehicle,
                business.rental_duration
            )
            
            if optimal_vehicle is None:
                raise ValueError("No vehicles available within the specified budget")
        
        vehicle_cost = self._calculate_vehicle_cost(optimal_vehicle, business.rental_duration)
        total_cost = vehicle_cost * business.fleet_size
        
        # Calculate potential savings compared to short-term rental
        if business.rental_duration != RentalDuration.SHORT_TERM:
            short_term_cost = self._calculate_vehicle_cost(optimal_vehicle, RentalDuration.SHORT_TERM) * business.fleet_size
            savings = short_term_cost - total_cost
        else:
            savings = None
        
        return RentalPlan(
            business_name=business.name,
            recommended_vehicles=[optimal_vehicle] * business.fleet_size,
            total_cost=total_cost,
            cost_per_vehicle=vehicle_cost,
            duration=business.rental_duration,
            savings=savings
        )

def load_vehicles_from_config(config_file: str) -> List[Vehicle]:
    """
    Load vehicle data from a JSON configuration file.
    
    Args:
        config_file: Path to JSON configuration file
        
    Returns:
        List[Vehicle]: List of Vehicle objects
        
    Raises:
        FileNotFoundError: If config file doesn't exist
        json.JSONDecodeError: If config file has invalid JSON
        KeyError: If required fields are missing in config
    """
    try:
        with open(config_file, 'r') as f:
            data = json.load(f)
        
        vehicles = []
        for item in data['vehicles']:
            vehicle = Vehicle(
                type=VehicleType[item['type']],
                daily_rate=item['rates']['daily'],
                monthly_rate=item['rates']['monthly'],
                yearly_rate=item['rates']['yearly'],
                available=item.get('available', True)
            )
            vehicles.append(vehicle)
        
        return vehicles
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file {config_file} not found")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Invalid JSON in configuration file", doc="", pos=0)
    except KeyError as e:
        raise KeyError(f"Missing required field in configuration: {str(e)}")

def main():
    """Example usage of the rental plan generator."""
    try:
        # Load vehicle data from config
        vehicles = load_vehicles_from_config('vehicles_config.json')
        
        # Initialize plan generator
        generator = RentalPlanGenerator(vehicles)
        
        # Create a sample business profile
        business = BusinessProfile(
            name="Acme Corp",
            fleet_size=10,
            preferred_vehicle_types=[VehicleType.SUV, VehicleType.VAN],
            operational_hours=60,
            budget=15000,
            rental_duration=RentalDuration.MEDIUM_TERM
        )
        
        # Generate rental plan
        plan = generator.generate_plan(business)
        
        # Print results
        print(f"Rental Plan for {plan.business_name}:")
        print(f"Recommended Vehicles: {[v.name for v in plan.recommended_vehicles]}")
        print(f"Total Monthly Cost: ${plan.total_cost:.2f}")
        print(f"Cost per Vehicle: ${plan.cost_per_vehicle:.2f}")
        print(f"Rental Duration: {plan.duration.name}")
        if plan.savings:
            print(f"Potential Savings vs Short-term: ${plan.savings:.2f}")
    
    except Exception as e:
        print(f"Error generating rental plan: {str(e)}")

if __name__ == "__main__":
    main()
```
