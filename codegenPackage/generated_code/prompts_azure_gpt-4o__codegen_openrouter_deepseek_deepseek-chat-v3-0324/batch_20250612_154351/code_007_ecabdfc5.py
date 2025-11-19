"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: Develop a simulation for a mini tractor used in warehouse logistics, incorporating features similar to those described in the Climax Polska product range.
Generated: DETERMINISTIC_ecabdfc5c4d7e2e7
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict

class TractorStatus(Enum):
    """Enum representing the possible states of the tractor."""
    IDLE = "IDLE"
    MOVING = "MOVING"
    LOADING = "LOADING"
    UNLOADING = "UNLOADING"
    CHARGING = "CHARGING"
    ERROR = "ERROR"

@dataclass
class WarehouseLocation:
    """Data class representing a location in the warehouse."""
    x: int
    y: int
    location_id: str
    is_charging_station: bool = False
    is_loading_station: bool = False

@dataclass
class Package:
    """Data class representing a package to be transported."""
    package_id: str
    weight: float
    destination: WarehouseLocation

class MiniTractor:
    """Class representing a mini tractor for warehouse logistics."""
    
    def __init__(self, tractor_id: str, initial_location: WarehouseLocation):
        """
        Initialize the mini tractor.
        
        Args:
            tractor_id: Unique identifier for the tractor
            initial_location: Starting location of the tractor
        """
        self.tractor_id = tractor_id
        self.current_location = initial_location
        self.status = TractorStatus.IDLE
        self.battery_level = 100.0
        self.current_package: Optional[Package] = None
        self.error_message: Optional[str] = None
        self.speed = 1  # units per second
        self.log: List[Dict] = []
        
    def move_to(self, destination: WarehouseLocation) -> bool:
        """
        Move the tractor to a specified destination.
        
        Args:
            destination: Target location to move to
            
        Returns:
            bool: True if movement was successful, False otherwise
        """
        if self.status != TractorStatus.IDLE:
            self._log_error("Cannot move while not idle")
            return False
            
        if self.battery_level < 10:
            self._log_error("Insufficient battery for movement")
            return False
            
        distance = self._calculate_distance(self.current_location, destination)
        travel_time = distance / self.speed
        
        self.status = TractorStatus.MOVING
        self._log_activity(f"Moving to {destination.location_id}, distance: {distance} units")
        
        # Simulate movement
        time.sleep(travel_time)
        self.battery_level -= distance * 0.5  # Battery consumption
        self.current_location = destination
        self.status = TractorStatus.IDLE
        self._log_activity(f"Arrived at {destination.location_id}")
        
        return True
    
    def load_package(self, package: Package) -> bool:
        """
        Load a package onto the tractor.
        
        Args:
            package: Package to be loaded
            
        Returns:
            bool: True if loading was successful, False otherwise
        """
        if self.status != TractorStatus.IDLE:
            self._log_error("Cannot load while not idle")
            return False
            
        if self.current_package is not None:
            self._log_error("Already carrying a package")
            return False
            
        if not self.current_location.is_loading_station:
            self._log_error("Not at a loading station")
            return False
            
        self.status = TractorStatus.LOADING
        self._log_activity(f"Loading package {package.package_id}")
        
        # Simulate loading
        time.sleep(2)
        self.current_package = package
        self.status = TractorStatus.IDLE
        self._log_activity(f"Package {package.package_id} loaded")
        
        return True
    
    def unload_package(self) -> bool:
        """
        Unload the current package from the tractor.
        
        Returns:
            bool: True if unloading was successful, False otherwise
        """
        if self.status != TractorStatus.IDLE:
            self._log_error("Cannot unload while not idle")
            return False
            
        if self.current_package is None:
            self._log_error("No package to unload")
            return False
            
        if not self.current_location.is_loading_station:
            self._log_error("Not at a loading/unloading station")
            return False
            
        self.status = TractorStatus.UNLOADING
        self._log_activity(f"Unloading package {self.current_package.package_id}")
        
        # Simulate unloading
        time.sleep(2)
        package = self.current_package
        self.current_package = None
        self.status = TractorStatus.IDLE
        self._log_activity(f"Package {package.package_id} unloaded")
        
        return True
    
    def charge_battery(self) -> bool:
        """
        Charge the tractor's battery.
        
        Returns:
            bool: True if charging was successful, False otherwise
        """
        if not self.current_location.is_charging_station:
            self._log_error("Not at a charging station")
            return False
            
        if self.battery_level >= 100:
            self._log_activity("Battery already fully charged")
            return True
            
        self.status = TractorStatus.CHARGING
        self._log_activity("Starting battery charging")
        
        # Simulate charging
        while self.battery_level < 100:
            time.sleep(1)
            self.battery_level = min(100, self.battery_level + 10)
            self._log_activity(f"Battery level: {self.battery_level}%")
            
        self.status = TractorStatus.IDLE
        self._log_activity("Battery fully charged")
        return True
    
    def _calculate_distance(self, start: WarehouseLocation, end: WarehouseLocation) -> float:
        """Calculate Manhattan distance between two points."""
        return abs(start.x - end.x) + abs(start.y - end.y)
    
    def _log_activity(self, message: str):
        """Log an activity message."""
        log_entry = {
            "timestamp": time.time(),
            "tractor_id": self.tractor_id,
            "status": self.status.value,
            "message": message,
            "location": self.current_location.location_id,
            "battery": self.battery_level,
            "package": self.current_package.package_id if self.current_package else None
        }
        self.log.append(log_entry)
    
    def _log_error(self, message: str):
        """Log an error message."""
        self.status = TractorStatus.ERROR
        self.error_message = message
        self._log_activity(f"ERROR: {message}")
        self.status = TractorStatus.IDLE

class WarehouseSimulation:
    """Class to simulate warehouse operations with multiple tractors."""
    
    def __init__(self):
        """Initialize the warehouse simulation."""
        self.tractors: List[MiniTractor] = []
        self.locations: Dict[str, WarehouseLocation] = {}
        self.packages: List[Package] = []
        
    def add_location(self, location: WarehouseLocation):
        """Add a location to the warehouse."""
        self.locations[location.location_id] = location
        
    def add_tractor(self, tractor: MiniTractor):
        """Add a tractor to the simulation."""
        self.tractors.append(tractor)
        
    def generate_package(self, destination_id: str, weight: float = 10.0) -> Package:
        """
        Generate a new package with random destination.
        
        Args:
            destination_id: ID of the destination location
            weight: Weight of the package
            
        Returns:
            Package: The generated package
        """
        if destination_id not in self.locations:
            raise ValueError(f"Destination {destination_id} not found")
            
        package_id = f"PKG-{random.randint(1000, 9999)}"
        package = Package(
            package_id=package_id,
            weight=weight,
            destination=self.locations[destination_id]
        )
        self.packages.append(package)
        return package
    
    def run_simulation_step(self):
        """Run one step of the simulation."""
        for tractor in self.tractors:
            if tractor.status == TractorStatus.IDLE:
                # Simple simulation logic - in real implementation would be more sophisticated
                if tractor.battery_level < 20:
                    # Find nearest charging station
                    charging_stations = [loc for loc in self.locations.values() if loc.is_charging_station]
                    if charging_stations:
                        nearest = min(charging_stations, key=lambda x: tractor._calculate_distance(tractor.current_location, x))
                        tractor.move_to(nearest)
                        tractor.charge_battery()
                elif tractor.current_package is None:
                    # Find a package to transport
                    if self.packages:
                        package = self.packages.pop(0)
                        loading_stations = [loc for loc in self.locations.values() if loc.is_loading_station]
                        if loading_stations:
                            tractor.move_to(loading_stations[0])
                            tractor.load_package(package)
                else:
                    # Move to package destination
                    tractor.move_to(tractor.current_package.destination)
                    tractor.unload_package()

# Example usage
if __name__ == "__main__":
    # Create warehouse locations
    warehouse = WarehouseSimulation()
    
    # Add locations
    warehouse.add_location(W
