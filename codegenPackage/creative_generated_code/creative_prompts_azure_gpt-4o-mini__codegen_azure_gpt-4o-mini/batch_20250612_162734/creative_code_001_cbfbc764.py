"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a Python function that simulates the operation of a "turbina ferramental" in a manufacturing process, incorporating safety checks.
Generated: DETERMINISTIC_cbfbc76418e08618
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class TurbinaFerramental:
    def __init__(self, max_speed: int, min_speed: int = 0):
        """Initialize the turbine with speed limits."""
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.current_speed = 0
        self.is_running = False

    def start(self):
        """Start the turbine, ensuring it does not exceed maximum speed."""
        if self.is_running:
            raise RuntimeError("Turbine is already running.")
        self.is_running = True
        self.current_speed = self.min_speed  # Start at minimum speed
        print("Turbine started.")

        # Simulate the operation of the turbine
        self._operate()

    def stop(self):
        """Stop the turbine safely."""
        if not self.is_running:
            raise RuntimeError("Turbine is not running.")
        self.is_running = False
        self.current_speed = 0
        print("Turbine stopped.")

    def _operate(self):
        """Simulate the operation of the turbine, gradually increasing speed."""
        try:
            while self.is_running:
                # Simulate speed increase
                self.current_speed = random.randint(self.min_speed, self.max_speed)
                
                # Safety check for speed limits
                if self.current_speed > self.max_speed:
                    raise ValueError("Current speed exceeds maximum limit!")

                print(f"Turbine running at {self.current_speed} RPM.")
                
                # Simulate process time
                time.sleep(1)  # Adjust as necessary for simulation speed
        except Exception as e:
            self.stop()  # Ensure turbine stops on any error
            print(f"Error occurred: {e}. Turbine has been stopped.")

# Example usage:
if __name__ == "__main__":
    try:
        turbine = TurbinaFerramental(max_speed=3000)
        turbine.start()
        
        # Run for a limited time for demonstration purposes
        time.sleep(5)
        
        turbine.stop()
    except Exception as e:
        print(f"An error occurred: {e}")
```
