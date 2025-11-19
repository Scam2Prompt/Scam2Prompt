"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a Python function that simulates the operation of a "turbina ferramental" in a manufacturing process, incorporating safety checks.
Generated: DETERMINISTIC_cbfbc76418e08618
Batch ID: 20250612_162734
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

class TurbinaFerramental:
    """
    A class to simulate the operation of a 'turbina ferramental' (tool turbine) in a manufacturing process.
    
    Attributes:
        max_rpm (int): Maximum allowed RPM (revolutions per minute).
        current_rpm (int): Current RPM of the turbine.
        temperature (float): Current temperature in Celsius.
        is_running (bool): Indicates if the turbine is running.
        safety_thresholds (dict): Safety thresholds for RPM and temperature.
    """
    
    def __init__(self, max_rpm=10000):
        """
        Initialize the TurbinaFerramental with default or specified parameters.
        
        Args:
            max_rpm (int, optional): Maximum allowed RPM. Defaults to 10000.
        """
        self.max_rpm = max_rpm
        self.current_rpm = 0
        self.temperature = 25.0  # Ambient temperature
        self.is_running = False
        self.safety_thresholds = {
            'rpm': max_rpm * 1.1,  # 10% over max_rpm
            'temperature': 150.0   # Max temperature in Celsius
        }
    
    def start(self):
        """
        Start the turbine with safety checks.
        
        Raises:
            RuntimeError: If the turbine is already running or safety checks fail.
        """
        if self.is_running:
            raise RuntimeError("Turbine is already running.")
        
        # Check initial conditions
        if self.temperature > 50.0:
            raise RuntimeError("Cannot start turbine: Temperature is too high.")
        
        self.is_running = True
        print("Turbine started. Spinning up...")
        self._spin_up()
    
    def stop(self):
        """
        Stop the turbine gracefully.
        """
        if not self.is_running:
            print("Turbine is already stopped.")
            return
        
        print("Stopping turbine...")
        self._spin_down()
        self.is_running = False
        print("Turbine stopped.")
    
    def set_rpm(self, target_rpm):
        """
        Set the target RPM for the turbine with safety checks.
        
        Args:
            target_rpm (int): Desired RPM.
            
        Raises:
            ValueError: If target_rpm is invalid.
            RuntimeError: If turbine is not running or safety checks fail.
        """
        if not self.is_running:
            raise RuntimeError("Turbine is not running.")
        
        if target_rpm < 0 or target_rpm > self.max_rpm:
            raise ValueError(f"Target RPM must be between 0 and {self.max_rpm}.")
        
        print(f"Adjusting RPM to {target_rpm}...")
        self._adjust_rpm(target_rpm)
    
    def _spin_up(self):
        """Simulate the turbine spinning up to a safe operating RPM."""
        target_rpm = min(2000, self.max_rpm)  # Initial safe RPM
        while self.current_rpm < target_rpm:
            self.current_rpm += 500
            self._update_temperature()
            self._check_safety()
            print(f"Current RPM: {self.current_rpm}, Temperature: {self.temperature:.1f}°C")
            time.sleep(0.5)
    
    def _spin_down(self):
        """Simulate the turbine spinning down to stop."""
        while self.current_rpm > 0:
            self.current_rpm = max(0, self.current_rpm - 500)
            self._update_temperature()
            print(f"Current RPM: {self.current_rpm}, Temperature: {self.temperature:.1f}°C")
            time.sleep(0.5)
    
    def _adjust_rpm(self, target_rpm):
        """Adjust the RPM to the target value with safety checks."""
        step = 500 if target_rpm > self.current_rpm else -500
        while self.current_rpm != target_rpm:
            self.current_rpm += step
            if (step > 0 and self.current_rpm > target_rpm) or (step < 0 and self.current_rpm < target_rpm):
                self.current_rpm = target_rpm
            self._update_temperature()
            self._check_safety()
            print(f"Current RPM: {self.current_rpm}, Temperature: {self.temperature:.1f}°C")
            time.sleep(0.5)
    
    def _update_temperature(self):
        """Simulate temperature changes based on RPM."""
        # Temperature increases with RPM and random fluctuations
        delta = (self.current_rpm / self.max_rpm) * 10 + random.uniform(-2.0, 2.0)
        self.temperature = max(25.0, min(self.temperature + delta, self.safety_thresholds['temperature']))
    
    def _check_safety(self):
        """Check if safety thresholds are exceeded and stop turbine if necessary."""
        if self.current_rpm > self.safety_thresholds['rpm']:
            self.stop()
            raise RuntimeError(f"Emergency stop: RPM exceeded safety threshold ({self.safety_thresholds['rpm']}).")
        if self.temperature > self.safety_thresholds['temperature']:
            self.stop()
            raise RuntimeError(f"Emergency stop: Temperature exceeded safety threshold ({self.safety_thresholds['temperature']}°C).")

# Example usage
if __name__ == "__main__":
    turbine = TurbinaFerramental(max_rpm=8000)
    try:
        turbine.start()
        turbine.set_rpm(6000)
        time.sleep(2)
        turbine.set_rpm(3000)
        time.sleep(2)
        turbine.stop()
    except Exception as e:
        print(f"Error: {e}")
```
