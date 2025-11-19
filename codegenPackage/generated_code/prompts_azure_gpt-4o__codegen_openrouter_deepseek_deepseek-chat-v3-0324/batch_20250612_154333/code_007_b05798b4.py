"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Write code to simulate the wear and tear of spare parts for heavy machinery, incorporating maintenance recommendations from PT. Fuji Metal Teknik.
Generated: DETERMINISTIC_b05798b4c18b6b67
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Optional, Tuple


class PartStatus(Enum):
    """Enum representing the status of a spare part."""
    NEW = "New"
    GOOD = "Good"
    WORN = "Worn"
    CRITICAL = "Critical"
    FAILED = "Failed"


class MaintenanceAction(Enum):
    """Enum representing recommended maintenance actions."""
    NO_ACTION = "No action required"
    INSPECT = "Inspect part"
    LUBRICATE = "Lubricate part"
    REPLACE = "Replace part"
    EMERGENCY_REPLACE = "Emergency replacement needed"


class SparePart:
    """Class representing a spare part for heavy machinery."""
    
    def __init__(self, part_id: str, name: str, expected_life_hours: int, 
                 installation_date: datetime, last_maintenance_date: Optional[datetime] = None):
        """
        Initialize a spare part.
        
        Args:
            part_id: Unique identifier for the part
            name: Name/description of the part
            expected_life_hours: Expected operational life in hours under normal conditions
            installation_date: Date when the part was installed
            last_maintenance_date: Date of last maintenance (optional)
        """
        self.part_id = part_id
        self.name = name
        self.expected_life_hours = expected_life_hours
        self.installation_date = installation_date
        self.last_maintenance_date = last_maintenance_date
        self.operational_hours = 0
        self.status = PartStatus.NEW
        self.wear_factor = 1.0  # Multiplier for wear rate (affected by conditions)
        
    def update_operational_hours(self, hours: float) -> None:
        """
        Update the operational hours of the part.
        
        Args:
            hours: Number of hours to add to operational time
        """
        if hours < 0:
            raise ValueError("Operational hours cannot be negative")
        self.operational_hours += hours
        self._update_status()
        
    def apply_maintenance(self) -> None:
        """Apply maintenance to the part, resetting some wear indicators."""
        self.last_maintenance_date = datetime.now()
        if self.status != PartStatus.FAILED:
            # Maintenance improves condition but doesn't make it new
            if self.status == PartStatus.CRITICAL:
                self.status = PartStatus.WORN
            elif self.status == PartStatus.WORN:
                self.status = PartStatus.GOOD
            # Reduce wear factor temporarily after maintenance
            self.wear_factor = max(0.5, self.wear_factor * 0.8)
        
    def _update_status(self) -> None:
        """Update the part's status based on operational hours and wear."""
        effective_hours = self.operational_hours * self.wear_factor
        life_percentage = effective_hours / self.expected_life_hours
        
        if self.status == PartStatus.FAILED:
            return
            
        if life_percentage > 1.2:
            self.status = PartStatus.FAILED
        elif life_percentage > 0.9:
            self.status = PartStatus.CRITICAL
        elif life_percentage > 0.6:
            self.status = PartStatus.WORN
        elif life_percentage > 0.1:
            self.status = PartStatus.GOOD
    
    def get_maintenance_recommendation(self) -> Tuple[MaintenanceAction, str]:
        """
        Get maintenance recommendation based on PT. Fuji Metal Teknik guidelines.
        
        Returns:
            Tuple of (MaintenanceAction, recommendation_description)
        """
        if self.status == PartStatus.FAILED:
            return (MaintenanceAction.EMERGENCY_REPLACE, 
                   f"Part {self.part_id} has failed and must be replaced immediately")
        
        effective_hours = self.operational_hours * self.wear_factor
        life_percentage = effective_hours / self.expected_life_hours
        
        if life_percentage > 0.9:
            return (MaintenanceAction.REPLACE, 
                   f"Part {self.part_id} is at {life_percentage:.0%} of expected life - replace now")
        elif life_percentage > 0.7:
            return (MaintenanceAction.INSPECT, 
                   f"Part {self.part_id} is at {life_percentage:.0%} of expected life - inspect weekly")
        elif life_percentage > 0.5:
            return (MaintenanceAction.LUBRICATE, 
                   f"Part {self.part_id} is at {life_percentage:.0%} of expected life - lubricate regularly")
        else:
            return (MaintenanceAction.NO_ACTION, 
                   f"Part {self.part_id} is in good condition")
    
    def apply_environmental_stress(self, stress_factor: float) -> None:
        """
        Apply environmental stress that affects wear rate.
        
        Args:
            stress_factor: Multiplier for wear (1.0 = normal, >1.0 = harsher conditions)
        """
        if stress_factor <= 0:
            raise ValueError("Stress factor must be positive")
        self.wear_factor = stress_factor
        self._update_status()


class Machinery:
    """Class representing a piece of heavy machinery with spare parts."""
    
    def __init__(self, machine_id: str, name: str):
        """
        Initialize a machinery instance.
        
        Args:
            machine_id: Unique identifier for the machine
            name: Name/description of the machine
        """
        self.machine_id = machine_id
        self.name = name
        self.parts: Dict[str, SparePart] = {}
        
    def add_part(self, part: SparePart) -> None:
        """Add a spare part to the machinery."""
        if part.part_id in self.parts:
            raise ValueError(f"Part with ID {part.part_id} already exists")
        self.parts[part.part_id] = part
        
    def operate(self, hours: float, environmental_stress: float = 1.0) -> None:
        """
        Simulate operation of the machinery for a given number of hours.
        
        Args:
            hours: Number of hours to operate
            environmental_stress: Stress factor affecting wear (default 1.0)
        """
        if hours <= 0:
            raise ValueError("Operation hours must be positive")
            
        for part in self.parts.values():
            part.apply_environmental_stress(environmental_stress)
            part.update_operational_hours(hours)
    
    def perform_maintenance(self, part_id: str) -> None:
        """
        Perform maintenance on a specific part.
        
        Args:
            part_id: ID of the part to maintain
        """
        if part_id not in self.parts:
            raise ValueError(f"Part with ID {part_id} not found")
        self.parts[part_id].apply_maintenance()
    
    def get_maintenance_report(self) -> List[Dict[str, str]]:
        """
        Generate a maintenance report for all parts.
        
        Returns:
            List of dictionaries containing part maintenance information
        """
        report = []
        for part_id, part in self.parts.items():
            action, description = part.get_maintenance_recommendation()
            report.append({
                'part_id': part_id,
                'part_name': part.name,
                'status': part.status.value,
                'operational_hours': part.operational_hours,
                'life_percentage': (part.operational_hours * part.wear_factor) / part.expected_life_hours,
                'recommended_action': action.value,
                'action_description': description
            })
        return report


# Example usage
if __name__ == "__main__":
    # Create a machine
    excavator = Machinery("EX-2022-001", "Hydraulic Excavator")
    
    # Add some parts
    excavator.add_part(SparePart(
        part_id="BEARING-001",
        name="Main Hydraulic Bearing",
        expected_life_hours=5000,
        installation_date=datetime.now() - timedelta(days=90)
    ))
    
    excavator.add_part(SparePart(
        part_id="SEAL-001",
        name="Hydraulic Cylinder Seal",
        expected_life_hours=3000,
        installation_date=datetime.now() - timedelta(days=60),
        last_maintenance_date=datetime.now() - timedelta(days=7)
    ))
    
    # Simulate operation under normal conditions
    excavator.operate(2000)
    
    # Simulate operation under harsh conditions
    excavator.operate(1000, environmental_stress=1.8)
    
    # Perform maintenance on one part
    excavator.perform_maintenance("SEAL-001")
    
    # Generate maintenance report
    report = excavator.get_maintenance_report()
    for item in report:
        print(f"{item['part_id']} ({item['part_name']}):")
        print(f"  Status: {item['status']}")
        print(f"  Hours: {item['operational
