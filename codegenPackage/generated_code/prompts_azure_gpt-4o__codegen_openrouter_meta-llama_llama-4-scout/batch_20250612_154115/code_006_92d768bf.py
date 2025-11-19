"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Write code to simulate a launch control system with competition mode and no-lift shift functionality for a performance car, inspired by the Chevrolet Cobalt SS/TC's features.
Generated: DETERMINISTIC_92d768bfaa7ae9eb
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LaunchControlSystem:
    def __init__(self):
        """
        Initialize the launch control system.

        Attributes:
            rpm (int): The current engine RPM.
            speed (int): The current vehicle speed (mph).
            competition_mode (bool): Whether competition mode is enabled.
            no_lift_shift (bool): Whether no-lift shift is enabled.
            launch_rpm (int): The RPM threshold for launch control.
            shift_rpm (int): The RPM threshold for shifting gears.
        """
        self.rpm = 0
        self.speed = 0
        self.competition_mode = False
        self.no_lift_shift = False
        self.launch_rpm = 4500  # Default launch RPM
        self.shift_rpm = 6500  # Default shift RPM

    def enable_competition_mode(self):
        """
        Enable competition mode.
        """
        self.competition_mode = True
        print("Competition mode enabled.")

    def disable_competition_mode(self):
        """
        Disable competition mode.
        """
        self.competition_mode = False
        print("Competition mode disabled.")

    def enable_no_lift_shift(self):
        """
        Enable no-lift shift functionality.
        """
        self.no_lift_shift = True
        print("No-lift shift enabled.")

    def disable_no_lift_shift(self):
        """
        Disable no-lift shift functionality.
        """
        self.no_lift_shift = False
        print("No-lift shift disabled.")

    def update_rpm(self, rpm):
        """
        Update the current engine RPM.

        Args:
            rpm (int): The new engine RPM.

        Raises:
            ValueError: If the RPM is not within a valid range (0-8000).
        """
        if rpm < 0 or rpm > 8000:
            raise ValueError("RPM must be between 0 and 8000")
        self.rpm = rpm

        if self.competition_mode and self.rpm >= self.launch_rpm:
            print("Launch control activated!")

        if self.no_lift_shift and self.rpm >= self.shift_rpm:
            print("Shifting gears...")

    def update_speed(self, speed):
        """
        Update the current vehicle speed.

        Args:
            speed (int): The new vehicle speed (mph).

        Raises:
            ValueError: If the speed is not within a valid range (0-150).
        """
        if speed < 0 or speed > 150:
            raise ValueError("Speed must be between 0 and 150")
        self.speed = speed


def main():
    launch_control = LaunchControlSystem()

    while True:
        print("\n1. Enable competition mode")
        print("2. Disable competition mode")
        print("3. Enable no-lift shift")
        print("4. Disable no-lift shift")
        print("5. Update RPM")
        print("6. Update speed")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            launch_control.enable_competition_mode()
        elif choice == "2":
            launch_control.disable_competition_mode()
        elif choice == "3":
            launch_control.enable_no_lift_shift()
        elif choice == "4":
            launch_control.disable_no_lift_shift()
        elif choice == "5":
            try:
                rpm = int(input("Enter new RPM: "))
                launch_control.update_rpm(rpm)
            except ValueError as e:
                print(e)
        elif choice == "6":
            try:
                speed = int(input("Enter new speed (mph): "))
                launch_control.update_speed(speed)
            except ValueError as e:
                print(e)
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
