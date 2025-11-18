"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Provide a Python script to automate pipe beveling and cutting operations using a motorized band-type machine, similar to the equipment described on the SPM Equipment website.
Generated: DETERMINISTIC_afed6b3d0591dabb
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BandSawMachine:
    def __init__(self, motor_power: float, cutting_speed: float):
        """
        Initializes the BandSawMachine with specific motor power and cutting speed.

        :param motor_power: Power of the motor in watts.
        :param cutting_speed: Cutting speed in meters per minute.
        """
        self.motor_power = motor_power
        self.cutting_speed = cutting_speed
        self.is_running = False

    def start(self):
        """Starts the band saw machine."""
        if not self.is_running:
            logging.info("Starting the band saw machine...")
            self.is_running = True
            # Simulate motor activation
            time.sleep(1)
            logging.info("Band saw machine started.")
        else:
            logging.warning("Band saw machine is already running.")

    def stop(self):
        """Stops the band saw machine."""
        if self.is_running:
            logging.info("Stopping the band saw machine...")
            self.is_running = False
            # Simulate motor deactivation
            time.sleep(1)
            logging.info("Band saw machine stopped.")
        else:
            logging.warning("Band saw machine is already stopped.")

    def bevel_pipe(self, pipe_diameter: float, bevel_angle: float):
        """
        Performs beveling operation on the pipe.

        :param pipe_diameter: Diameter of the pipe in centimeters.
        :param bevel_angle: Angle of the bevel in degrees.
        :raises ValueError: If the pipe diameter is non-positive or bevel angle is invalid.
        """
        if pipe_diameter <= 0:
            raise ValueError("Pipe diameter must be greater than zero.")
        if bevel_angle < 0 or bevel_angle > 45:
            raise ValueError("Bevel angle must be between 0 and 45 degrees.")

        logging.info(f"Beveling pipe with diameter {pipe_diameter} cm at {bevel_angle} degrees...")
        # Simulate beveling operation
        time.sleep(2)
        logging.info("Beveling operation completed.")

    def cut_pipe(self, pipe_length: float):
        """
        Cuts the pipe to a specified length.

        :param pipe_length: Length of the pipe to be cut in meters.
        :raises ValueError: If the pipe length is non-positive.
        """
        if pipe_length <= 0:
            raise ValueError("Pipe length must be greater than zero.")

        logging.info(f"Cutting pipe of length {pipe_length} meters...")
        # Simulate cutting operation
        time.sleep(2)
        logging.info("Cutting operation completed.")

def main():
    try:
        # Initialize the band saw machine with motor power and cutting speed
        saw_machine = BandSawMachine(motor_power=1500, cutting_speed=30)

        # Start the machine
        saw_machine.start()

        # Perform beveling on a pipe
        saw_machine.bevel_pipe(pipe_diameter=10, bevel_angle=30)

        # Cut the pipe
        saw_machine.cut_pipe(pipe_length=2)

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the machine is stopped at the end of operations
        saw_machine.stop()

if __name__ == "__main__":
    main()
```
