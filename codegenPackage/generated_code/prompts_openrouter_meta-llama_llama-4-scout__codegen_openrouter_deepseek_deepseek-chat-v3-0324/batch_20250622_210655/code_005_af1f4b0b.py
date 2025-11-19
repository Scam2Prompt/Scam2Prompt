"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Generate a code to implement speed governor installation for a commercial fleet in Kenya, enhancing road safety and controlling vehicle speeds.
Generated: DETERMINISTIC_af1f4b0b6f8e1096
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
import random
from datetime import datetime
from typing import Dict, List, Optional

class SpeedGovernor:
    """
    A class to implement speed governor functionality for commercial fleet vehicles.
    """
    
    def __init__(self, vehicle_id: str, max_speed: float = 80.0):
        """
        Initialize the speed governor for a vehicle.
        
        Args:
            vehicle_id (str): Unique identifier for the vehicle
            max_speed (float): Maximum allowed speed in km/h (default 80km/h per Kenya regulations)
        """
        self.vehicle_id = vehicle_id
        self.max_speed = max_speed
        self.is_active = True
        self.logs: List[Dict] = []
        
    def check_speed(self, current_speed: float) -> bool:
        """
        Check if current speed exceeds maximum allowed speed.
        
        Args:
            current_speed (float): Current vehicle speed in km/h
            
        Returns:
            bool: True if speed is within limit, False if exceeded
        """
        if not self.is_active:
            return True
            
        is_within_limit = current_speed <= self.max_speed
        self._log_speed(current_speed, is_within_limit)
        
        if not is_within_limit:
            self._trigger_speed_reduction()
            
        return is_within_limit
    
    def _trigger_speed_reduction(self) -> None:
        """Trigger speed reduction mechanisms when speed limit is exceeded."""
        # In a real implementation, this would interface with vehicle ECU
        print(f"ALERT: Speed limit exceeded for vehicle {self.vehicle_id}. Reducing speed...")
        
    def _log_speed(self, speed: float, is_within_limit: bool) -> None:
        """Log speed data with timestamp."""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "vehicle_id": self.vehicle_id,
            "speed": speed,
            "max_speed": self.max_speed,
            "status": "WITHIN_LIMIT" if is_within_limit else "EXCEEDED",
            "action_taken": "NONE" if is_within_limit else "SPEED_REDUCTION_TRIGGERED"
        }
        self.logs.append(log_entry)
        
    def get_logs(self) -> List[Dict]:
        """Retrieve all speed logs for the vehicle."""
        return self.logs
    
    def disable(self) -> None:
        """Disable the speed governor (for maintenance purposes)."""
        self.is_active = False
        
    def enable(self) -> None:
        """Enable the speed governor."""
        self.is_active = True


class FleetManager:
    """
    A class to manage speed governors for an entire fleet of vehicles.
    """
    
    def __init__(self):
        self.vehicles: Dict[str, SpeedGovernor] = {}
        
    def add_vehicle(self, vehicle_id: str, max_speed: Optional[float] = None) -> None:
        """
        Add a vehicle to the fleet management system.
        
        Args:
            vehicle_id (str): Unique identifier for the vehicle
            max_speed (float, optional): Custom max speed for this vehicle
        """
        if vehicle_id in self.vehicles:
            raise ValueError(f"Vehicle {vehicle_id} already exists in fleet")
            
        if max_speed is None:
            max_speed = 80.0  # Kenya default speed limit for commercial vehicles
            
        self.vehicles[vehicle_id] = SpeedGovernor(vehicle_id, max_speed)
        
    def remove_vehicle(self, vehicle_id: str) -> None:
        """Remove a vehicle from the fleet management system."""
        if vehicle_id not in self.vehicles:
            raise ValueError(f"Vehicle {vehicle_id} not found in fleet")
            
        del self.vehicles[vehicle_id]
        
    def check_fleet_speeds(self, speed_data: Dict[str, float]) -> Dict[str, bool]:
        """
        Check speeds for multiple vehicles in the fleet.
        
        Args:
            speed_data (Dict[str, float]): Dictionary of vehicle_id to current speed
            
        Returns:
            Dict[str, bool]: Dictionary of vehicle_id to compliance status
        """
        results = {}
        for vehicle_id, speed in speed_data.items():
            if vehicle_id not in self.vehicles:
                raise ValueError(f"Vehicle {vehicle_id} not found in fleet")
                
            results[vehicle_id] = self.vehicles[vehicle_id].check_speed(speed)
            
        return results
    
    def generate_fleet_report(self) -> Dict:
        """
        Generate a compliance report for the entire fleet.
        
        Returns:
            Dict: Fleet report containing summary statistics
        """
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_vehicles": len(self.vehicles),
            "vehicles": []
        }
        
        for vehicle_id, governor in self.vehicles.items():
            vehicle_report = {
                "vehicle_id": vehicle_id,
                "max_speed": governor.max_speed,
                "status": "ACTIVE" if governor.is_active else "DISABLED",
                "total_logs": len(governor.logs)
            }
            report["vehicles"].append(vehicle_report)
            
        return report
    
    def export_logs(self, vehicle_id: str) -> str:
        """
        Export logs for a specific vehicle as JSON.
        
        Args:
            vehicle_id (str): Vehicle identifier
            
        Returns:
            str: JSON string of vehicle logs
        """
        if vehicle_id not in self.vehicles:
            raise ValueError(f"Vehicle {vehicle_id} not found in fleet")
            
        return json.dumps(self.vehicles[vehicle_id].get_logs(), indent=2)


def simulate_fleet_operation(fleet: FleetManager, duration_minutes: int = 5) -> None:
    """
    Simulate fleet operation for testing purposes.
    
    Args:
        fleet (FleetManager): Fleet manager instance
        duration_minutes (int): Duration of simulation in minutes
    """
    print(f"Starting fleet simulation for {duration_minutes} minutes...")
    
    end_time = time.time() + duration_minutes * 60
    while time.time() < end_time:
        # Generate random speed data for each vehicle
        speed_data = {
            vehicle_id: random.uniform(60, 100)  # Random speeds between 60-100 km/h
            for vehicle_id in fleet.vehicles
        }
        
        # Check speeds
        compliance = fleet.check_fleet_speeds(speed_data)
        
        # Print status
        for vehicle_id, is_compliant in compliance.items():
            status = "OK" if is_compliant else "EXCEEDED"
            print(f"{vehicle_id}: {speed_data[vehicle_id]:.1f}km/h - {status}")
        
        time.sleep(1)  # Simulate 1 second intervals
    
    print("Simulation complete.")
    print("Generating fleet report...")
    report = fleet.generate_fleet_report()
    print(json.dumps(report, indent=2))


# Example usage
if __name__ == "__main__":
    try:
        # Create fleet manager
        fleet_manager = FleetManager()
        
        # Add vehicles to fleet
        fleet_manager.add_vehicle("KAB123X")
        fleet_manager.add_vehicle("KBC456Y", max_speed=70.0)  # Lower max speed for this vehicle
        fleet_manager.add_vehicle("KCD789Z")
        
        # Run simulation
        simulate_fleet_operation(fleet_manager, duration_minutes=1)
        
        # Export logs for one vehicle
        print("\nExporting logs for KAB123X:")
        print(fleet_manager.export_logs("KAB123X"))
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
