"""
Generated Code Metadata:
========================
Original URL: https://iconelevator.in
Prompt: Generate a Python script to calculate the energy savings of an elevator system, inspired by the energy-efficient features mentioned on ICON Elevator's website.
Generated: DETERMINISTIC_3a9f5043de527067
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Tuple, Optional

class ElevatorEnergyCalculator:
    """
    A class to calculate energy savings for an elevator system based on various parameters.
    Inspired by energy-efficient features from ICON Elevator's website.
    """
    
    def __init__(
        self,
        num_floors: int,
        elevator_capacity_kg: float,
        average_trips_per_day: int,
        average_distance_per_trip_floors: float,
        motor_power_kw: float,
        standby_power_kw: float,
        operational_hours_per_day: float = 12.0,
        days_per_year: int = 365
    ):
        """
        Initialize the elevator energy calculator with system parameters.
        
        Args:
            num_floors: Total number of floors in the building
            elevator_capacity_kg: Maximum load capacity in kilograms
            average_trips_per_day: Average number of trips per day
            average_distance_per_trip_floors: Average floors traveled per trip
            motor_power_kw: Rated power of elevator motor in kW
            standby_power_kw: Power consumption during standby in kW
            operational_hours_per_day: Hours per day the elevator operates (default: 12)
            days_per_year: Days per year the elevator operates (default: 365)
        """
        self.num_floors = num_floors
        self.elevator_capacity_kg = elevator_capacity_kg
        self.average_trips_per_day = average_trips_per_day
        self.average_distance_per_trip_floors = average_distance_per_trip_floors
        self.motor_power_kw = motor_power_kw
        self.standby_power_kw = standby_power_kw
        self.operational_hours_per_day = operational_hours_per_day
        self.days_per_year = days_per_year
        
        # Constants
        self.FLOOR_HEIGHT_M = 3.0  # Average floor height in meters
        self.GRAVITY = 9.81  # m/s²
        self.MOTOR_EFFICIENCY = 0.85  # Typical motor efficiency
        self.REGENERATIVE_BRAKING_EFFICIENCY = 0.35  # Energy recovery efficiency
        
    def calculate_baseline_energy(self) -> Dict[str, float]:
        """
        Calculate baseline annual energy consumption without any energy-saving features.
        
        Returns:
            Dictionary containing:
                - 'annual_energy_kwh': Total annual energy in kWh
                - 'daily_energy_kwh': Daily energy in kWh
                - 'standby_energy_kwh': Annual standby energy in kWh
                - 'operational_energy_kwh': Annual operational energy in kWh
        """
        try:
            # Calculate operational energy (moving energy)
            distance_per_trip_m = self.average_distance_per_trip_floors * self.FLOOR_HEIGHT_M
            energy_per_trip_kwh = (
                (self.elevator_capacity_kg * self.GRAVITY * distance_per_trip_m) / 
                (self.MOTOR_EFFICIENCY * 3600 * 1000)
            )
            
            daily_operational_energy = energy_per_trip_kwh * self.average_trips_per_day
            annual_operational_energy = daily_operational_energy * self.days_per_year
            
            # Calculate standby energy
            standby_hours_per_day = self.operational_hours_per_day - (
                self.average_trips_per_day * (distance_per_trip_m / 2) / 3600
            )  # Simplified assumption
            
            daily_standby_energy = self.standby_power_kw * standby_hours_per_day
            annual_standby_energy = daily_standby_energy * self.days_per_year
            
            # Total energy
            annual_total_energy = annual_operational_energy + annual_standby_energy
            daily_total_energy = daily_operational_energy + daily_standby_energy
            
            return {
                'annual_energy_kwh': annual_total_energy,
                'daily_energy_kwh': daily_total_energy,
                'standby_energy_kwh': annual_standby_energy,
                'operational_energy_kwh': annual_operational_energy
            }
            
        except Exception as e:
            raise ValueError(f"Error calculating baseline energy: {str(e)}")
    
    def calculate_energy_savings(
        self,
        regenerative_braking: bool = True,
        sleep_mode: bool = True,
        efficient_motor: bool = True,
        traffic_management: bool = True
    ) -> Dict[str, float]:
        """
        Calculate potential energy savings with various energy-efficient features.
        
        Args:
            regenerative_braking: Whether regenerative braking is enabled
            sleep_mode: Whether sleep mode during idle is enabled
            efficient_motor: Whether high-efficiency motor is used
            traffic_management: Whether smart traffic management is used
            
        Returns:
            Dictionary containing:
                - 'annual_savings_kwh': Total annual savings in kWh
                - 'annual_energy_kwh': Total annual energy with savings in kWh
                - 'savings_percentage': Percentage savings compared to baseline
                - 'savings_breakdown': Breakdown of savings by feature
        """
        try:
            baseline = self.calculate_baseline_energy()
            savings_breakdown = {}
            total_savings = 0.0
            
            # Regenerative braking savings (operational energy only)
            if regenerative_braking:
                regen_savings = baseline['operational_energy_kwh'] * self.REGENERATIVE_BRAKING_EFFICIENCY * 0.5
                savings_breakdown['regenerative_braking'] = regen_savings
                total_savings += regen_savings
            
            # Sleep mode savings (standby energy only)
            if sleep_mode:
                sleep_savings = baseline['standby_energy_kwh'] * 0.4  # 40% reduction
                savings_breakdown['sleep_mode'] = sleep_savings
                total_savings += sleep_savings
            
            # Efficient motor savings (operational energy only)
            if efficient_motor:
                motor_savings = baseline['operational_energy_kwh'] * 0.15  # 15% more efficient
                savings_breakdown['efficient_motor'] = motor_savings
                total_savings += motor_savings
            
            # Traffic management savings (reduces trips)
            if traffic_management:
                traffic_savings = baseline['annual_energy_kwh'] * 0.1  # 10% reduction in trips
                savings_breakdown['traffic_management'] = traffic_savings
                total_savings += traffic_savings
            
            # Calculate final energy with savings
            annual_energy_with_savings = baseline['annual_energy_kwh'] - total_savings
            savings_percentage = (total_savings / baseline['annual_energy_kwh']) * 100
            
            return {
                'annual_savings_kwh': total_savings,
                'annual_energy_kwh': annual_energy_with_savings,
                'savings_percentage': savings_percentage,
                'savings_breakdown': savings_breakdown,
                'baseline_annual_energy_kwh': baseline['annual_energy_kwh']
            }
            
        except Exception as e:
            raise ValueError(f"Error calculating energy savings: {str(e)}")
    
    def calculate_carbon_savings(self, annual_savings_kwh: float, carbon_intensity_kg_per_kwh: float = 0.5) -> float:
        """
        Calculate carbon emissions savings based on energy savings.
        
        Args:
            annual_savings_kwh: Annual energy savings in kWh
            carbon_intensity_kg_per_kwh: Carbon intensity of electricity (default: 0.5 kg/kWh)
            
        Returns:
            Annual carbon savings in kg CO2
        """
        try:
            return annual_savings_kwh * carbon_intensity_kg_per_kwh
        except Exception as e:
            raise ValueError(f"Error calculating carbon savings: {str(e)}")


def main():
    """Example usage of the ElevatorEnergyCalculator class."""
    try:
        # Example parameters for a mid-rise office building
        calculator = ElevatorEnergyCalculator(
            num_floors=10,
            elevator_capacity_kg=1000,
            average_trips_per_day=150,
            average_distance_per_trip_floors=5,
            motor_power_kw=15,
            standby_power_kw=1.5
        )
        
        # Calculate baseline energy
        baseline = calculator.calculate_baseline_energy()
        print("\nBaseline Energy Consumption:")
        print(f"Annual: {baseline['annual_energy_kwh']:,.2f} kWh")
        print(f"Daily: {baseline['daily_energy_kwh']:,.2f} kWh")
        print(f"Standby: {baseline['standby_energy_kwh']:,.2f} kWh/year")
        print(f"Operational: {baseline['oper
