"""
Generated Code Metadata:
========================
Original URL: https://taxltg.com
Prompt: Generate code for simulating the rotational movement of an electric turntable (电动转盘) used in conjunction with EVO视讯平车 systems.
Generated: DETERMINISTIC_f4d1d96544494c67
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import math
import threading

class ElectricTurntable:
    """
    A class to simulate the rotational movement of an electric turntable.
    This class can be used in conjunction with EVO视讯平车 systems.
    """

    def __init__(self, rotation_speed: float):
        """
        Initializes the ElectricTurntable with a specified rotation speed.

        :param rotation_speed: Speed of rotation in degrees per second.
        """
        self.rotation_speed = rotation_speed  # degrees per second
        self.current_angle = 0.0  # Current angle in degrees
        self.running = False  # Flag to control the rotation
        self.lock = threading.Lock()  # Lock for thread safety

    def start_rotation(self):
        """
        Starts the rotation of the turntable in a separate thread.
        """
        if not self.running:
            self.running = True
            self.rotation_thread = threading.Thread(target=self._rotate)
            self.rotation_thread.start()
            print("Turntable rotation started.")

    def stop_rotation(self):
        """
        Stops the rotation of the turntable.
        """
        if self.running:
            self.running = False
            self.rotation_thread.join()  # Wait for the thread to finish
            print("Turntable rotation stopped.")

    def _rotate(self):
        """
        Internal method to handle the rotation logic.
        This method runs in a separate thread.
        """
        while self.running:
            with self.lock:
                self.current_angle = (self.current_angle + self.rotation_speed) % 360
                print(f"Current angle: {self.current_angle:.2f} degrees")
            time.sleep(1)  # Update every second

    def get_current_angle(self) -> float:
        """
        Returns the current angle of the turntable.

        :return: Current angle in degrees.
        """
        with self.lock:
            return self.current_angle

    def set_rotation_speed(self, speed: float):
        """
        Sets the rotation speed of the turntable.

        :param speed: New speed in degrees per second.
        """
        with self.lock:
            self.rotation_speed = speed
            print(f"Rotation speed set to: {self.rotation_speed} degrees/second")

# Example usage
if __name__ == "__main__":
    try:
        turntable = ElectricTurntable(rotation_speed=30.0)  # 30 degrees per second
        turntable.start_rotation()
        time.sleep(5)  # Let it rotate for 5 seconds
        turntable.stop_rotation()
        print(f"Final angle: {turntable.get_current_angle()} degrees")
    except Exception as e:
        print(f"An error occurred: {e}")
```
