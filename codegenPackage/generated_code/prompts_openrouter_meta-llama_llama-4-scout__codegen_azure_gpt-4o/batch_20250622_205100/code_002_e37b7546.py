"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: "Design a system for fire prevention and suppression using motobombas de incêndio and PVC antichama pipes, including a list of required components and their specifications."
Generated: DETERMINISTIC_e37b7546bbd016f6
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Fire Prevention and Suppression System

This script simulates a fire prevention and suppression system using motorized fire pumps (motobombas de incêndio) 
and flame-retardant PVC pipes (PVC antichama). The system monitors fire risk levels and activates suppression mechanisms 
when necessary.

Components:
1. Motorized Fire Pump (Motobomba de Incêndio)
   - Flow rate: 100 liters/min
   - Pressure: 10 bar
   - Power: 2 HP

2. Flame-Retardant PVC Pipes (PVC Antichama)
   - Diameter: 50 mm
   - Length: Configurable based on installation

3. Sensors
   - Temperature sensor: Detects high temperatures
   - Smoke sensor: Detects smoke levels

4. Control Unit
   - Microcontroller: Manages system logic
   - Relay: Activates fire pump

5. Water Reservoir
   - Capacity: 1000 liters

6. Alarm System
   - Audible alarm: Alerts nearby personnel
"""

import time
import random

# Constants
TEMPERATURE_THRESHOLD = 60  # Degrees Celsius
SMOKE_THRESHOLD = 300       # Arbitrary smoke level
WATER_CAPACITY = 1000       # Liters
PUMP_FLOW_RATE = 100        # Liters per minute

# Global variables
current_water_level = WATER_CAPACITY

# Simulated sensors
def read_temperature_sensor():
    """Simulates reading the temperature sensor."""
    return random.uniform(20, 100)  # Random temperature between 20°C and 100°C

def read_smoke_sensor():
    """Simulates reading the smoke sensor."""
    return random.randint(0, 500)  # Random smoke level between 0 and 500

# Fire pump control
def activate_fire_pump():
    """
    Activates the fire pump to suppress fire.
    Reduces water level based on pump flow rate.
    """
    global current_water_level
    if current_water_level <= 0:
        print("Error: Water reservoir is empty. Fire pump cannot be activated.")
        return

    print("Fire pump activated. Suppressing fire...")
    for _ in range(10):  # Simulate 10 minutes of pump operation
        if current_water_level <= 0:
            print("Warning: Water reservoir depleted during operation.")
            break
        current_water_level -= PUMP_FLOW_RATE
        print(f"Current water level: {current_water_level} liters")
        time.sleep(1)  # Simulate 1 minute of operation
    print("Fire pump operation complete.")

# Alarm system
def activate_alarm():
    """Activates the audible alarm to alert personnel."""
    print("ALARM: Fire detected! Evacuate immediately!")

# Main system logic
def fire_prevention_system():
    """
    Monitors sensors and activates fire suppression mechanisms when thresholds are exceeded.
    """
    print("Fire prevention system initialized.")
    try:
        while True:
            temperature = read_temperature_sensor()
            smoke_level = read_smoke_sensor()

            print(f"Temperature: {temperature:.2f}°C, Smoke Level: {smoke_level}")

            if temperature > TEMPERATURE_THRESHOLD or smoke_level > SMOKE_THRESHOLD:
                print("Fire risk detected!")
                activate_alarm()
                activate_fire_pump()
                break  # Exit after handling fire event

            time.sleep(5)  # Wait before next sensor reading
    except KeyboardInterrupt:
        print("System terminated by user.")
    except Exception as e:
        print(f"Error: {e}")

# Entry point
if __name__ == "__main__":
    fire_prevention_system()
```
