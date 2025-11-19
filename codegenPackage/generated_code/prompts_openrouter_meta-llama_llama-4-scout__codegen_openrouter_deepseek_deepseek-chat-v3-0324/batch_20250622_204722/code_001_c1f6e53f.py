"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: Write a Python script to simulate a fault diagnosis system for Samsung refrigerators, considering common faults such as sensor failures and motor problems, as described on the Ankara Teknik Servisi website.
Generated: DETERMINISTIC_c1f6e53fe4057d76
Batch ID: 20250622_204722
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
from enum import Enum, auto

class FaultType(Enum):
    NO_FAULT = auto()
    TEMPERATURE_SENSOR_FAILURE = auto()
    DOOR_SENSOR_FAILURE = auto()
    COMPRESSOR_FAILURE = auto()
    FAN_MOTOR_FAILURE = auto()
    DEFROST_SYSTEM_FAILURE = auto()
    CONTROL_BOARD_FAILURE = auto()

class SamsungRefrigerator:
    def __init__(self, model_number):
        self.model_number = model_number
        self.current_temperature = 4.0  # Default temperature in Celsius
        self.door_open = False
        self.compressor_running = False
        self.fan_running = False
        self.fault_state = FaultType.NO_FAULT
        self.last_maintenance = time.time()
        
    def simulate_operation(self):
        """Simulate normal refrigerator operation with potential faults"""
        # Randomly introduce faults (5% chance)
        if random.random() < 0.05:
            self._introduce_fault()
            
        # Simulate temperature changes
        if not self.door_open and self.compressor_running:
            self.current_temperature -= 0.1
        elif self.door_open:
            self.current_temperature += 0.5
            
        # Ensure temperature stays within reasonable bounds
        self.current_temperature = max(-5.0, min(10.0, self.current_temperature))
        
    def _introduce_fault(self):
        """Randomly select a fault type based on common issues"""
        faults = [
            FaultType.TEMPERATURE_SENSOR_FAILURE,
            FaultType.DOOR_SENSOR_FAILURE,
            FaultType.COMPRESSOR_FAILURE,
            FaultType.FAN_MOTOR_FAILURE,
            FaultType.DEFROST_SYSTEM_FAILURE,
            FaultType.CONTROL_BOARD_FAILURE
        ]
        weights = [0.25, 0.15, 0.20, 0.15, 0.15, 0.10]  # Weighted probabilities
        self.fault_state = random.choices(faults, weights=weights)[0]
        
    def diagnose(self):
        """Run diagnostic checks and return fault information"""
        if self.fault_state == FaultType.NO_FAULT:
            return {"status": "OK", "message": "No faults detected"}
        
        diagnosis = {
            "status": "FAULT",
            "fault_type": self.fault_state.name,
            "model": self.model_number,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Add specific recommendations based on fault type
        if self.fault_state == FaultType.TEMPERATURE_SENSOR_FAILURE:
            diagnosis["recommendation"] = "Replace temperature sensor"
        elif self.fault_state == FaultType.DOOR_SENSOR_FAILURE:
            diagnosis["recommendation"] = "Check door switch and wiring"
        elif self.fault_state == FaultType.COMPRESSOR_FAILURE:
            diagnosis["recommendation"] = "Inspect compressor and start relay"
        elif self.fault_state == FaultType.FAN_MOTOR_FAILURE:
            diagnosis["recommendation"] = "Replace evaporator fan motor"
        elif self.fault_state == FaultType.DEFROST_SYSTEM_FAILURE:
            diagnosis["recommendation"] = "Check defrost heater, thermostat, and timer"
        elif self.fault_state == FaultType.CONTROL_BOARD_FAILURE:
            diagnosis["recommendation"] = "Replace main control board"
            
        return diagnosis
    
    def reset_fault(self):
        """Reset the fault state after repair"""
        self.fault_state = FaultType.NO_FAULT
        self.last_maintenance = time.time()

def simulate_refrigerator_diagnosis(model_number="RFG23HEDBSR", duration_hours=24):
    """
    Simulate refrigerator operation and diagnose faults over time.
    
    Args:
        model_number: Refrigerator model number
        duration_hours: Simulation duration in hours
    """
    fridge = SamsungRefrigerator(model_number)
    interval_minutes = 15  # Check every 15 minutes
    iterations = int(duration_hours * 60 / interval_minutes)
    
    print(f"Starting simulation for Samsung refrigerator {model_number}")
    print(f"Simulating {duration_hours} hours of operation...\n")
    
    for i in range(iterations):
        fridge.simulate_operation()
        
        # Randomly open/close door (10% chance)
        if random.random() < 0.1:
            fridge.door_open = not fridge.door_open
            
        # Randomly toggle compressor (based on temperature)
        if fridge.current_temperature > 5.0:
            fridge.compressor_running = True
        elif fridge.current_temperature < 2.0:
            fridge.compressor_running = False
            
        # Run fan when compressor is running
        fridge.fan_running = fridge.compressor_running
        
        # Periodically run diagnostics
        if i % 4 == 0:  # Every hour
            result = fridge.diagnose()
            if result["status"] == "FAULT":
                print(f"Fault detected at {result['timestamp']}:")
                print(f"  - Type: {result['fault_type']}")
                print(f"  - Recommendation: {result['recommendation']}\n")
                
                # Simulate repair after detection
                if random.random() < 0.7:  # 70% chance of immediate repair
                    fridge.reset_fault()
                    print("  - Fault repaired by technician\n")
    
    print("Simulation completed.")

if __name__ == "__main__":
    simulate_refrigerator_diagnosis()
```
