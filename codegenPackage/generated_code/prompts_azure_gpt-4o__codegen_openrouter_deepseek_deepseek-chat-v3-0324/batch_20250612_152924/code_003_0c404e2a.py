"""
Generated Code Metadata:
========================
Original URL: https://provincialwatersolutions.com
Prompt: Create a script to model a whole-house water filtration system, including point-of-use filtration and sump pump integration, inspired by the product offerings on Provincial Water Solutions.
Generated: DETERMINISTIC_0c404e2a5aa8a90d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from enum import Enum
from typing import Optional, Dict, List

class FilterType(Enum):
    """Enum representing different types of water filters."""
    SEDIMENT = "Sediment"
    CARBON = "Carbon"
    REVERSE_OSMOSIS = "Reverse Osmosis"
    ULTRAVIOLET = "Ultraviolet"
    WATER_SOFTENER = "Water Softener"

class PumpStatus(Enum):
    """Enum representing sump pump status."""
    OFF = "Off"
    ON = "On"
    ALARM = "Alarm"

class WaterFiltrationSystem:
    """Class representing a whole-house water filtration system."""
    
    def __init__(self, system_name: str):
        """Initialize the water filtration system.
        
        Args:
            system_name: Name of the filtration system
        """
        self.system_name = system_name
        self.filters: Dict[str, FilterType] = {}  # key: location, value: filter type
        self.sump_pump_status = PumpStatus.OFF
        self.water_flow_rate = 0.0  # gallons per minute
        self.system_active = False
        self.filter_lifespans: Dict[str, int] = {}  # key: location, value: days remaining
        self.last_maintenance_date: Optional[float] = None
        
    def add_filter(self, location: str, filter_type: FilterType, lifespan_days: int) -> None:
        """Add a filter to the system.
        
        Args:
            location: Where the filter is installed (e.g., "Main Inlet", "Kitchen")
            filter_type: Type of filter to add
            lifespan_days: Expected lifespan of the filter in days
        """
        if location in self.filters:
            raise ValueError(f"Filter already exists at location: {location}")
        
        self.filters[location] = filter_type
        self.filter_lifespans[location] = lifespan_days
        
    def remove_filter(self, location: str) -> None:
        """Remove a filter from the system.
        
        Args:
            location: Location of the filter to remove
        """
        if location not in self.filters:
            raise ValueError(f"No filter found at location: {location}")
            
        del self.filters[location]
        del self.filter_lifespans[location]
        
    def start_system(self, initial_flow_rate: float) -> None:
        """Start the water filtration system.
        
        Args:
            initial_flow_rate: Initial water flow rate in gallons per minute
        """
        if self.system_active:
            raise RuntimeError("System is already running")
            
        if not self.filters:
            raise RuntimeError("Cannot start system with no filters installed")
            
        self.system_active = True
        self.water_flow_rate = initial_flow_rate
        self.sump_pump_status = PumpStatus.ON
        self.last_maintenance_date = time.time()
        print(f"{self.system_name} started with flow rate: {initial_flow_rate} GPM")
        
    def stop_system(self) -> None:
        """Stop the water filtration system."""
        if not self.system_active:
            raise RuntimeError("System is not running")
            
        self.system_active = False
        self.water_flow_rate = 0.0
        self.sump_pump_status = PumpStatus.OFF
        print(f"{self.system_name} stopped")
        
    def update_flow_rate(self, new_flow_rate: float) -> None:
        """Update the water flow rate.
        
        Args:
            new_flow_rate: New flow rate in gallons per minute
        """
        if not self.system_active:
            raise RuntimeError("Cannot update flow rate when system is off")
            
        if new_flow_rate < 0:
            raise ValueError("Flow rate cannot be negative")
            
        self.water_flow_rate = new_flow_rate
        print(f"Flow rate updated to: {new_flow_rate} GPM")
        
    def check_filter_status(self) -> Dict[str, int]:
        """Check remaining lifespan for all filters.
        
        Returns:
            Dictionary mapping filter locations to remaining days
        """
        if not self.last_maintenance_date:
            return {loc: lifespan for loc, lifespan in self.filter_lifespans.items()}
            
        days_elapsed = (time.time() - self.last_maintenance_date) / (24 * 3600)
        return {
            loc: max(0, int(lifespan - days_elapsed))
            for loc, lifespan in self.filter_lifespans.items()
        }
        
    def replace_filter(self, location: str, new_lifespan: int) -> None:
        """Replace a filter and reset its lifespan.
        
        Args:
            location: Location of the filter to replace
            new_lifespan: New lifespan in days for the filter
        """
        if location not in self.filters:
            raise ValueError(f"No filter found at location: {location}")
            
        self.filter_lifespans[location] = new_lifespan
        self.last_maintenance_date = time.time()
        print(f"Filter at {location} replaced with new lifespan: {new_lifespan} days")
        
    def trigger_pump_alarm(self) -> None:
        """Trigger the sump pump alarm."""
        self.sump_pump_status = PumpStatus.ALARM
        print("ALERT: Sump pump alarm triggered!")
        
    def reset_pump_alarm(self) -> None:
        """Reset the sump pump alarm."""
        if self.sump_pump_status == PumpStatus.ALARM:
            self.sump_pump_status = PumpStatus.ON
            print("Sump pump alarm reset")
            
    def get_system_status(self) -> Dict:
        """Get current system status.
        
        Returns:
            Dictionary containing system status information
        """
        return {
            "system_name": self.system_name,
            "active": self.system_active,
            "flow_rate": self.water_flow_rate,
            "sump_pump_status": self.sump_pump_status.value,
            "filters": {loc: filt.value for loc, filt in self.filters.items()},
            "filter_status": self.check_filter_status(),
            "last_maintenance": time.ctime(self.last_maintenance_date) if self.last_maintenance_date else "Never"
        }

def main():
    """Example usage of the WaterFiltrationSystem class."""
    try:
        # Create a new system
        home_system = WaterFiltrationSystem("Provincial Home Water System")
        
        # Add filters
        home_system.add_filter("Main Inlet", FilterType.SEDIMENT, 180)
        home_system.add_filter("Main Inlet", FilterType.CARBON, 365)
        home_system.add_filter("Kitchen", FilterType.REVERSE_OSMOSIS, 90)
        home_system.add_filter("Basement", FilterType.WATER_SOFTENER, 730)
        
        # Start the system
        home_system.start_system(5.5)
        
        # Check status
        print("\nSystem Status:")
        for key, value in home_system.get_system_status().items():
            print(f"{key}: {value}")
            
        # Simulate time passing (for demo purposes)
        print("\nSimulating 30 days of operation...")
        time.sleep(2)  # Simulate time passing
        
        # Check filter status after time has passed
        print("\nFilter Status After 30 Days:")
        for location, days_remaining in home_system.check_filter_status().items():
            print(f"{location}: {days_remaining} days remaining")
            
        # Replace a filter
        home_system.replace_filter("Kitchen", 90)
        
        # Stop the system
        home_system.stop_system()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
