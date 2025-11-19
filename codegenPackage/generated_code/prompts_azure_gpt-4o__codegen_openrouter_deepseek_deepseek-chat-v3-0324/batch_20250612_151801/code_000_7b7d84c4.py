"""
Generated Code Metadata:
========================
Original URL: https://kubitz.com.br
Prompt: Write Python code to simulate the operation of a conveyor belt system for waste sorting, including modules for feeding, elevating, and rejecting materials, as described in the Kubitz Esteira de Triagem configurations.
Generated: DETERMINISTIC_7b7d84c474ad0a63
Batch ID: 20250612_151801
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
from typing import List, Dict, Optional

class MaterialType(Enum):
    """Enum representing different types of materials on the conveyor belt."""
    PLASTIC = "Plastic"
    METAL = "Metal"
    GLASS = "Glass"
    PAPER = "Paper"
    ORGANIC = "Organic"
    OTHER = "Other"

class ConveyorState(Enum):
    """Enum representing possible states of the conveyor belt."""
    IDLE = "Idle"
    RUNNING = "Running"
    PAUSED = "Paused"
    STOPPED = "Stopped"
    ERROR = "Error"

class Sensor:
    """Class representing a sensor on the conveyor belt."""
    def __init__(self, name: str, position: float):
        self.name = name
        self.position = position  # Position along the conveyor in meters
        self.is_active = False

    def detect(self, material: MaterialType) -> bool:
        """Simulate material detection."""
        self.is_active = True
        return random.random() > 0.1  # 10% chance of failure

    def reset(self):
        """Reset sensor state."""
        self.is_active = False

class Actuator:
    """Class representing an actuator (e.g., rejector arm)."""
    def __init__(self, name: str, position: float):
        self.name = name
        self.position = position
        self.is_active = False

    def activate(self) -> bool:
        """Activate the actuator."""
        self.is_active = True
        return random.random() > 0.05  # 5% chance of failure

    def deactivate(self):
        """Deactivate the actuator."""
        self.is_active = False

class ConveyorBelt:
    """Class representing the conveyor belt system."""
    def __init__(self, length: float, speed: float):
        self.length = length  # meters
        self.speed = speed    # meters/second
        self.state = ConveyorState.IDLE
        self.materials: List[Dict] = []
        self.sensors: List[Sensor] = []
        self.actuators: List[Actuator] = []
        self.error: Optional[str] = None

    def add_sensor(self, sensor: Sensor):
        """Add a sensor to the conveyor belt."""
        self.sensors.append(sensor)

    def add_actuator(self, actuator: Actuator):
        """Add an actuator to the conveyor belt."""
        self.actuators.append(actuator)

    def start(self):
        """Start the conveyor belt."""
        if self.state == ConveyorState.ERROR:
            print("Cannot start: Conveyor is in error state.")
            return False
        
        self.state = ConveyorState.RUNNING
        print("Conveyor belt started.")
        return True

    def stop(self):
        """Stop the conveyor belt."""
        self.state = ConveyorState.STOPPED
        print("Conveyor belt stopped.")

    def pause(self):
        """Pause the conveyor belt."""
        if self.state == ConveyorState.RUNNING:
            self.state = ConveyorState.PAUSED
            print("Conveyor belt paused.")

    def resume(self):
        """Resume the conveyor belt from pause."""
        if self.state == ConveyorState.PAUSED:
            self.state = ConveyorState.RUNNING
            print("Conveyor belt resumed.")

    def feed_material(self, material_type: MaterialType):
        """Feed material onto the conveyor belt."""
        if self.state not in [ConveyorState.RUNNING, ConveyorState.PAUSED]:
            print("Cannot feed material: Conveyor is not running.")
            return
        
        material = {
            "type": material_type,
            "position": 0.0,
            "timestamp": time.time()
        }
        self.materials.append(material)
        print(f"Fed {material_type.value} onto conveyor.")

    def update_material_positions(self):
        """Update positions of all materials on the belt."""
        if self.state != ConveyorState.RUNNING:
            return
        
        current_time = time.time()
        for material in self.materials:
            time_elapsed = current_time - material["timestamp"]
            material["position"] = min(
                self.length,
                material["position"] + (time_elapsed * self.speed)
            )
            material["timestamp"] = current_time

    def process_materials(self):
        """Process materials through sensors and actuators."""
        if self.state != ConveyorState.RUNNING:
            return
        
        self.update_material_positions()
        
        # Check for materials that have reached the end
        self.materials = [m for m in self.materials if m["position"] < self.length]
        
        # Process sensors and actuators
        for material in self.materials:
            for sensor in self.sensors:
                if (abs(material["position"] - sensor.position) < 0.1 and 
                    not sensor.is_active):
                    detected = sensor.detect(material["type"])
                    if not detected:
                        self.error = f"Sensor {sensor.name} failed to detect material"
                        self.state = ConveyorState.ERROR
                        return
            
            for actuator in self.actuators:
                if (abs(material["position"] - actuator.position) < 0.1 and 
                    not actuator.is_active and 
                    material["type"] == MaterialType.OTHER):
                    activated = actuator.activate()
                    if not activated:
                        self.error = f"Actuator {actuator.name} failed to activate"
                        self.state = ConveyorState.ERROR
                        return
                    print(f"Rejected {material['type'].value} at position {actuator.position}")
                    actuator.deactivate()

    def clear_error(self):
        """Clear error state and reset components."""
        if self.state == ConveyorState.ERROR:
            self.error = None
            self.state = ConveyorState.IDLE
            for sensor in self.sensors:
                sensor.reset()
            for actuator in self.actuators:
                actuator.deactivate()
            print("Error cleared and system reset.")

    def get_status(self) -> Dict:
        """Get current status of the conveyor system."""
        return {
            "state": self.state.value,
            "speed": self.speed,
            "material_count": len(self.materials),
            "error": self.error
        }

def simulate_conveyor_operation():
    """Simulate the operation of the conveyor belt system."""
    # Initialize conveyor
    conveyor = ConveyorBelt(length=10.0, speed=0.5)
    
    # Add sensors
    conveyor.add_sensor(Sensor("TypeDetector", 2.0))
    conveyor.add_sensor(Sensor("QualityChecker", 5.0))
    
    # Add actuators
    conveyor.add_actuator(Actuator("RejectorArm", 8.0))
    
    # Start the conveyor
    conveyor.start()
    
    # Feed materials
    materials = list(MaterialType)
    try:
        for _ in range(20):
            if conveyor.state == ConveyorState.ERROR:
                print(f"Error occurred: {conveyor.error}")
                conveyor.clear_error()
                conveyor.start()
            
            # Randomly feed materials
            if random.random() > 0.3:
                material = random.choice(materials)
                conveyor.feed_material(material)
            
            # Process materials
            conveyor.process_materials()
            
            # Randomly pause/resume
            if random.random() > 0.9:
                if conveyor.state == ConveyorState.RUNNING:
                    conveyor.pause()
                elif conveyor.state == ConveyorState.PAUSED:
                    conveyor.resume()
            
            time.sleep(1)
        
    except KeyboardInterrupt:
        print("Simulation interrupted by user.")
    finally:
        conveyor.stop()
        print("Simulation ended.")

if __name__ == "__main__":
    simulate_conveyor_operation()
```
