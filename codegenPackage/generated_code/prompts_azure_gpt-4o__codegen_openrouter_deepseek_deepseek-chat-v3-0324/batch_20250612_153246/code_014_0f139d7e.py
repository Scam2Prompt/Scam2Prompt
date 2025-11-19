"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: Develop a Python script to simulate the operation of pipe blasting plugs and coating equipment, incorporating parameters like bubble remover rollers as described by SPM Equipment.
Generated: DETERMINISTIC_0f139d7e1dbc16d0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum
from typing import Optional, Dict, List

class EquipmentStatus(Enum):
    """Enum representing the status of the equipment."""
    IDLE = "Idle"
    RUNNING = "Running"
    MAINTENANCE = "Maintenance"
    ERROR = "Error"

class PipeBlastingPlugSimulator:
    """Simulates the operation of pipe blasting plugs and coating equipment."""
    
    def __init__(self, pipe_diameter: float, pipe_length: float, pressure: float):
        """
        Initialize the simulator with pipe parameters.
        
        Args:
            pipe_diameter: Diameter of the pipe in inches.
            pipe_length: Length of the pipe in feet.
            pressure: Operating pressure in PSI.
        """
        self.pipe_diameter = pipe_diameter
        self.pipe_length = pipe_length
        self.pressure = pressure
        self.status = EquipmentStatus.IDLE
        self.bubble_remover_rollers = False
        self.error_log = []
        
    def start_operation(self) -> bool:
        """Start the blasting and coating operation."""
        if self.status == EquipmentStatus.RUNNING:
            self._log_error("Operation already running.")
            return False
        
        if self.status == EquipmentStatus.MAINTENANCE:
            self._log_error("Equipment under maintenance.")
            return False
            
        self.status = EquipmentStatus.RUNNING
        self._log_operation("Operation started.")
        return True
    
    def stop_operation(self) -> bool:
        """Stop the blasting and coating operation."""
        if self.status != EquipmentStatus.RUNNING:
            self._log_error("No operation to stop.")
            return False
            
        self.status = EquipmentStatus.IDLE
        self._log_operation("Operation stopped.")
        return True
    
    def toggle_bubble_remover_rollers(self, enable: bool) -> None:
        """Toggle the bubble remover rollers on/off."""
        self.bubble_remover_rollers = enable
        status = "enabled" if enable else "disabled"
        self._log_operation(f"Bubble remover rollers {status}.")
    
    def perform_maintenance(self) -> None:
        """Put the equipment under maintenance."""
        if self.status == EquipmentStatus.RUNNING:
            self._log_error("Cannot perform maintenance while running.")
            return
            
        self.status = EquipmentStatus.MAINTENANCE
        self._log_operation("Maintenance mode activated.")
    
    def complete_maintenance(self) -> None:
        """Complete maintenance and return to idle."""
        if self.status != EquipmentStatus.MAINTENANCE:
            self._log_error("Not in maintenance mode.")
            return
            
        self.status = EquipmentStatus.IDLE
        self._log_operation("Maintenance completed. Equipment idle.")
    
    def simulate_operation(self, duration: int) -> Dict[str, float]:
        """
        Simulate the operation for a given duration.
        
        Args:
            duration: Duration of operation in seconds.
            
        Returns:
            Dictionary containing operation metrics.
        """
        if self.status != EquipmentStatus.RUNNING:
            self._log_error("Cannot simulate - equipment not running.")
            return {}
            
        self._log_operation(f"Simulating operation for {duration} seconds.")
        
        start_time = time.time()
        time.sleep(duration)
        end_time = time.time()
        
        # Simulate random metrics
        coating_thickness = round(random.uniform(0.1, 0.5), 2)
        bubble_count = random.randint(0, 10) if not self.bubble_remover_rollers else random.randint(0, 2)
        
        metrics = {
            "coating_thickness_mm": coating_thickness,
            "bubbles_detected": bubble_count,
            "actual_duration_sec": round(end_time - start_time, 2),
            "pressure_psi": self.pressure,
            "pipe_coverage_percent": 100.0
        }
        
        self._log_operation(f"Operation completed. Metrics: {metrics}")
        return metrics
    
    def _log_operation(self, message: str) -> None:
        """Log an operational message."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [OPERATION] {message}")
    
    def _log_error(self, message: str) -> None:
        """Log an error message."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        error_msg = f"[{timestamp}] [ERROR] {message}"
        print(error_msg)
        self.error_log.append(error_msg)
    
    def get_status(self) -> Dict[str, str]:
        """Get current status of the equipment."""
        return {
            "status": self.status.value,
            "pipe_diameter_in": self.pipe_diameter,
            "pipe_length_ft": self.pipe_length,
            "pressure_psi": self.pressure,
            "bubble_remover_rollers": "On" if self.bubble_remover_rollers else "Off",
            "error_count": len(self.error_log)
        }

def main():
    """Main function to demonstrate the simulator."""
    simulator = PipeBlastingPlugSimulator(
        pipe_diameter=12.0,
        pipe_length=20.0,
        pressure=150.0
    )
    
    print("Initial status:", simulator.get_status())
    
    # Start operation
    if simulator.start_operation():
        simulator.toggle_bubble_remover_rollers(True)
        
        # Simulate operation for 5 seconds
        metrics = simulator.simulate_operation(5)
        print("Operation metrics:", metrics)
        
        # Stop operation
        simulator.stop_operation()
    
    print("Final status:", simulator.get_status())

if __name__ == "__main__":
    main()
```
