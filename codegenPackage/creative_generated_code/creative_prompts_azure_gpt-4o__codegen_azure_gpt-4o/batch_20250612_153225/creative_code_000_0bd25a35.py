"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vgtindia.in
Prompt: Write Python code to simulate the functionality of a "Power Weeder" machine described on the Vinglob Greentech website, including its basic operations and controls.
Generated: DETERMINISTIC_0bd25a353d115498
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# power_weeder.py
"""
Simulates the functionality of a "Power Weeder" machine described on the Vinglob Greentech website,
including its basic operations and controls.
"""

class PowerWeeder:
    """
    A class to simulate the functionality of a Power Weeder machine.
    """

    def __init__(self):
        """
        Initializes the power weeder with default operational states.
        """
        self.is_running = False
        self.speed = 0  # Speed is measured as an integer (0 - 100)
        self.operation_mode = "Idle"  # Modes: 'Idle', 'Weeding', 'Tilling', 'Plowing'

    def start(self):
        """
        Starts the Power Weeder.
        """
        if self.is_running:
            raise RuntimeError("Power Weeder is already running.")
        self.is_running = True
        self.operation_mode = "Idle"
        print("Power Weeder started successfully.")

    def stop(self):
        """
        Stops the Power Weeder.
        """
        if not self.is_running:
            raise RuntimeError("Power Weeder is already stopped.")
        self.is_running = False
        self.speed = 0
        self.operation_mode = "Idle"
        print("Power Weeder stopped successfully.")

    def set_speed(self, speed):
        """
        Sets the speed of the Power Weeder.

        Args:
            speed (int): Desired speed (0 - 100).
        
        Raises:
            ValueError: If speed is out of range.
        """
        if not self.is_running:
            raise RuntimeError("Cannot set speed. Power Weeder is not running.")
        if not (0 <= speed <= 100):
            raise ValueError("Speed must be between 0 and 100.")
        self.speed = speed
        print(f"Speed set to {self.speed}.")

    def change_mode(self, mode):
        """
        Changes the operation mode of the Power Weeder.

        Args:
            mode (str): Desired mode ('Idle', 'Weeding', 'Tilling', 'Plowing').
        
        Raises:
            ValueError: If mode is invalid.
        """
        if not self.is_running:
            raise RuntimeError("Cannot change mode. Power Weeder is not running.")
        valid_modes = ['Idle', 'Weeding', 'Tilling', 'Plowing']
        if mode not in valid_modes:
            raise ValueError(f"Invalid mode. Valid modes are: {', '.join(valid_modes)}.")
        self.operation_mode = mode
        print(f"Operation mode changed to {self.operation_mode}.")

    def get_status(self):
        """
        Retrieves the current status of the Power Weeder.

        Returns:
            dict: A dictionary containing the current status of the machine.
        """
        status = {
            "is_running": self.is_running,
            "speed": self.speed,
            "operation_mode": self.operation_mode
        }
        return status

# Example usage
if __name__ == "__main__":
    try:
        # Create a Power Weeder instance
        power_weeder = PowerWeeder()

        # Start the machine
        power_weeder.start()

        # Set the speed
        power_weeder.set_speed(50)

        # Change the operation mode
        power_weeder.change_mode("Weeding")

        # Print the current status
        status = power_weeder.get_status()
        print("Current Status:", status)

        # Stop the machine
        power_weeder.stop()

    except (RuntimeError, ValueError) as e:
        print(f"Error: {e}")
```
