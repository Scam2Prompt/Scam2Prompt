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
import threading

class ElectricTurntable:
    """
    Simulates the rotational movement of an electric turntable.

    Attributes:
        rotation_speed (float): The speed of rotation in degrees per second.
        current_angle (float): The current angle of the turntable in degrees.
        is_rotating (bool): Indicates whether the turntable is currently rotating.
    """

    def __init__(self, rotation_speed=10.0):
        """
        Initializes the electric turntable.

        Args:
            rotation_speed (float, optional): The speed of rotation in degrees per second. Defaults to 10.0.
        """
        self.rotation_speed = rotation_speed
        self.current_angle = 0.0
        self.is_rotating = False
        self.lock = threading.Lock()

    def start_rotation(self, target_angle):
        """
        Starts rotating the turntable to a target angle.

        Args:
            target_angle (float): The target angle in degrees.

        Raises:
            ValueError: If the target angle is not a number.
        """
        if not isinstance(target_angle, (int, float)):
            raise ValueError("Target angle must be a number")

        with self.lock:
            if self.is_rotating:
                print("Turntable is already rotating. Please stop it first.")
                return

            self.is_rotating = True
            self.target_angle = target_angle

        threading.Thread(target=self.rotate, args=()).start()

    def stop_rotation(self):
        """
        Stops the rotation of the turntable.
        """
        with self.lock:
            self.is_rotating = False

    def rotate(self):
        """
        Rotates the turntable to the target angle.
        """
        angle_diff = self.target_angle - self.current_angle
        rotation_time = abs(angle_diff) / self.rotation_speed

        steps = int(rotation_time * 10)  # 10 steps per second
        for _ in range(steps):
            if not self.is_rotating:
                break

            time.sleep(0.1)  # sleep for 0.1 seconds

            with self.lock:
                if self.current_angle < self.target_angle:
                    self.current_angle = min(self.current_angle + self.rotation_speed / 10, self.target_angle)
                elif self.current_angle > self.target_angle:
                    self.current_angle = max(self.current_angle - self.rotation_speed / 10, self.target_angle)

            print(f"Current angle: {self.current_angle:.2f} degrees")

        with self.lock:
            self.is_rotating = False
            print(f"Rotation stopped. Final angle: {self.current_angle:.2f} degrees")


class EvoSystem:
    """
    Simulates the EVO视讯平车 system.

    Attributes:
        turntable (ElectricTurntable): The electric turntable instance.
    """

    def __init__(self, turntable):
        """
        Initializes the EVO视讯平车 system.

        Args:
            turntable (ElectricTurntable): The electric turntable instance.
        """
        self.turntable = turntable

    def start(self):
        """
        Starts the EVO视讯平车 system.
        """
        print("EVO视讯平车 system started")

    def stop(self):
        """
        Stops the EVO视讯平车 system.
        """
        print("EVO视讯平车 system stopped")
        self.turntable.stop_rotation()


def main():
    turntable = ElectricTurntable(rotation_speed=10.0)
    evo_system = EvoSystem(turntable)

    evo_system.start()

    try:
        turntable.start_rotation(360.0)  # rotate to 360 degrees
        time.sleep(5)  # let it rotate for 5 seconds
        turntable.stop_rotation()

        turntable.start_rotation(720.0)  # rotate to 720 degrees
        time.sleep(10)  # let it rotate for 10 seconds
    except Exception as e:
        print(f"Error: {e}")
    finally:
        evo_system.stop()


if __name__ == "__main__":
    main()
```
