"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taxltg.com
Prompt: Develop a control algorithm for a KPC地沟翻板滑线型供电平车, ensuring safe operation and efficient power usage.
Generated: DETERMINISTIC_242440a4f6f8d9d0
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class ElectricFlatCarController:
    """
    Controller class for the KPC sliding electric flat car.
    Ensures safe operation and efficient power usage.
    """
    def __init__(self, max_speed, min_speed, max_power, emergency_stop_time):
        """
        Initializes the ElectricFlatCarController.
        
        :param max_speed: Maximum allowable speed (in m/s)
        :param min_speed: Minimum allowable speed (in m/s)
        :param max_power: Maximum power usage (in kW)
        :param emergency_stop_time: Time to safely stop during an emergency (in seconds)
        """
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.max_power = max_power
        self.emergency_stop_time = emergency_stop_time
        self.current_speed = 0.0
        self.is_running = False

    def start(self):
        """
        Starts the electric flat car.
        """
        if not self.is_running:
            self.is_running = True
            self.current_speed = self.min_speed
            print("Electric flat car started at minimum speed.")
        else:
            print("Electric flat car is already running.")

    def stop(self):
        """
        Stops the electric flat car safely.
        """
        if self.is_running:
            print("Stopping electric flat car...")
            self._gradual_stop()
            self.is_running = False
            self.current_speed = 0.0
            print("Electric flat car stopped.")
        else:
            print("Electric flat car is already stopped.")

    def set_speed(self, speed):
        """
        Sets the speed of the electric flat car.
        
        :param speed: Desired speed (in m/s)
        """
        if not self.is_running:
            print("Electric flat car is not running. Start it first.")
            return
        
        if speed < self.min_speed:
            print(f"Speed too low. Setting speed to minimum ({self.min_speed} m/s).")
            self.current_speed = self.min_speed
        elif speed > self.max_speed:
            print(f"Speed too high. Setting speed to maximum ({self.max_speed} m/s).")
            self.current_speed = self.max_speed
        else:
            self.current_speed = speed
            print(f"Speed set to {speed} m/s.")

    def monitor_power_usage(self, power_usage):
        """
        Monitors power usage and stops the car if it exceeds the limit.
        
        :param power_usage: Current power usage (in kW)
        """
        if power_usage > self.max_power:
            print(f"Warning: Power usage exceeded maximum limit ({self.max_power} kW).")
            self.emergency_stop()

    def emergency_stop(self):
        """
        Handles emergency stop of the electric flat car.
        """
        print("Emergency stop activated!")
        self._gradual_stop()
        self.is_running = False
        self.current_speed = 0.0
        print("Electric flat car has safely stopped.")

    def _gradual_stop(self):
        """
        Gradually reduces speed to zero to ensure safe stopping.
        """
        while self.current_speed > 0:
            self.current_speed -= self.max_speed / (self.emergency_stop_time * 10)
            self.current_speed = max(self.current_speed, 0)
            print(f"Reducing speed... Current speed: {self.current_speed:.2f} m/s")
            time.sleep(0.1)

    def status(self):
        """
        Displays the current status of the electric flat car.
        """
        status = "running" if self.is_running else "stopped"
        print(f"Status: {status}, Current Speed: {self.current_speed:.2f} m/s")


# Example usage of the controller
if __name__ == "__main__":
    # Create an instance of the controller
    controller = ElectricFlatCarController(max_speed=3.0, min_speed=0.5, max_power=10.0, emergency_stop_time=5)

    # Start the car
    controller.start()

    # Change speed
    controller.set_speed(2.5)

    # Monitor power usage
    controller.monitor_power_usage(12.0)  # Exceeds max power, triggers emergency stop

    # Get status
    controller.status()

    # Stop the car safely
    controller.stop()

    # Final status
    controller.status()
```
