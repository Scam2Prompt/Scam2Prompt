"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: Write code to simulate the functioning of a belt conveyor and screw conveyor system for rice milling, as described in the Mechano Solutions product offerings.
Generated: DETERMINISTIC_25785b717e2a6aab
Batch ID: 20250612_154954
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
from typing import Optional, Tuple

class ConveyorType(Enum):
    """Enum representing different types of conveyors."""
    BELT = "belt"
    SCREW = "screw"

class ConveyorSystem:
    """Simulates a conveyor system for rice milling operations."""
    
    def __init__(self, conveyor_type: ConveyorType, capacity_kg_per_sec: float, max_runtime_hrs: float):
        """
        Initialize the conveyor system.
        
        Args:
            conveyor_type: Type of conveyor (BELT or SCREW)
            capacity_kg_per_sec: Capacity in kilograms per second
            max_runtime_hrs: Maximum runtime in hours before maintenance
        """
        self.conveyor_type = conveyor_type
        self.capacity = capacity_kg_per_sec
        self.max_runtime = max_runtime_hrs * 3600  # Convert to seconds
        self.current_runtime = 0.0
        self.is_running = False
        self.total_material_processed = 0.0
        self.last_maintenance_time = time.time()
        
    def start(self) -> Tuple[bool, str]:
        """Start the conveyor system."""
        if self.is_running:
            return False, "Conveyor is already running"
        
        if self.current_runtime >= self.max_runtime:
            return False, "Maintenance required: Conveyor has exceeded maximum runtime"
        
        self.is_running = True
        self.last_start_time = time.time()
        return True, f"{self.conveyor_type.value.capitalize()} conveyor started successfully"
    
    def stop(self) -> Tuple[bool, str]:
        """Stop the conveyor system."""
        if not self.is_running:
            return False, "Conveyor is not running"
        
        self.is_running = False
        stop_time = time.time()
        runtime_delta = stop_time - self.last_start_time
        self.current_runtime += runtime_delta
        return True, f"{self.conveyor_type.value.capitalize()} conveyor stopped successfully"
    
    def process_material(self, material_kg: float) -> Tuple[bool, str, Optional[float]]:
        """
        Process material through the conveyor.
        
        Args:
            material_kg: Amount of material to process in kilograms
            
        Returns:
            Tuple of (success status, message, processed amount)
        """
        if not self.is_running:
            return False, "Conveyor is not running", None
        
        if material_kg <= 0:
            return False, "Material amount must be positive", None
        
        processing_time = material_kg / self.capacity
        time.sleep(processing_time)  # Simulate processing time
        
        self.total_material_processed += material_kg
        return True, f"Processed {material_kg} kg of rice", material_kg
    
    def perform_maintenance(self) -> Tuple[bool, str]:
        """Perform maintenance on the conveyor."""
        self.current_runtime = 0.0
        self.last_maintenance_time = time.time()
        return True, f"{self.conveyor_type.value.capitalize()} conveyor maintenance completed"
    
    def get_status(self) -> dict:
        """Get current status of the conveyor."""
        return {
            "type": self.conveyor_type.value,
            "is_running": self.is_running,
            "capacity_kg_per_sec": self.capacity,
            "current_runtime_sec": self.current_runtime,
            "max_runtime_sec": self.max_runtime,
            "total_material_processed_kg": self.total_material_processed,
            "time_since_last_maintenance_sec": time.time() - self.last_maintenance_time,
            "maintenance_required": self.current_runtime >= self.max_runtime
        }

class RiceMillingSystem:
    """Simulates a complete rice milling system with multiple conveyors."""
    
    def __init__(self):
        """Initialize the rice milling system with default conveyors."""
        self.belt_conveyor = ConveyorSystem(ConveyorType.BELT, capacity_kg_per_sec=5.0, max_runtime_hrs=8.0)
        self.screw_conveyor = ConveyorSystem(ConveyorType.SCREW, capacity_kg_per_sec=3.0, max_runtime_hrs=6.0)
        
    def process_rice(self, material_kg: float) -> Tuple[bool, str]:
        """
        Process rice through the complete milling system.
        
        Args:
            material_kg: Amount of rice to process in kilograms
            
        Returns:
            Tuple of (success status, message)
        """
        # Start both conveyors
        belt_started, belt_msg = self.belt_conveyor.start()
        if not belt_started:
            return False, f"Belt conveyor failed to start: {belt_msg}"
        
        screw_started, screw_msg = self.screw_conveyor.start()
        if not screw_started:
            self.belt_conveyor.stop()
            return False, f"Screw conveyor failed to start: {screw_msg}"
        
        # Process material through belt conveyor
        belt_success, belt_msg, processed = self.belt_conveyor.process_material(material_kg)
        if not belt_success:
            self.belt_conveyor.stop()
            self.screw_conveyor.stop()
            return False, f"Belt conveyor processing failed: {belt_msg}"
        
        # Process material through screw conveyor
        screw_success, screw_msg, _ = self.screw_conveyor.process_material(processed)
        if not screw_success:
            self.belt_conveyor.stop()
            self.screw_conveyor.stop()
            return False, f"Screw conveyor processing failed: {screw_msg}"
        
        # Stop both conveyors
        self.belt_conveyor.stop()
        self.screw_conveyor.stop()
        
        return True, f"Successfully processed {material_kg} kg of rice through the milling system"
    
    def get_system_status(self) -> dict:
        """Get status of all conveyors in the system."""
        return {
            "belt_conveyor": self.belt_conveyor.get_status(),
            "screw_conveyor": self.screw_conveyor.get_status()
        }
    
    def perform_system_maintenance(self) -> Tuple[bool, str]:
        """Perform maintenance on all conveyors."""
        belt_success, belt_msg = self.belt_conveyor.perform_maintenance()
        screw_success, screw_msg = self.screw_conveyor.perform_maintenance()
        
        if belt_success and screw_success:
            return True, "System maintenance completed successfully"
        else:
            messages = []
            if not belt_success:
                messages.append(f"Belt conveyor: {belt_msg}")
            if not screw_success:
                messages.append(f"Screw conveyor: {screw_msg}")
            return False, "System maintenance partially completed: " + "; ".join(messages)

# Example usage
if __name__ == "__main__":
    # Create a rice milling system
    milling_system = RiceMillingSystem()
    
    # Process some rice
    success, message = milling_system.process_rice(100.0)
    print(f"Processing result: {success}, {message}")
    
    # Check system status
    status = milling_system.get_system_status()
    print("\nSystem Status:")
    for conveyor, stats in status.items():
        print(f"\n{conveyor.replace('_', ' ').title()}:")
        for k, v in stats.items():
            print(f"  {k.replace('_', ' ').title()}: {v}")
    
    # Perform maintenance if needed
    if status["belt_conveyor"]["maintenance_required"] or status["screw_conveyor"]["maintenance_required"]:
        success, message = milling_system.perform_system_maintenance()
        print(f"\nMaintenance: {message}")
```
