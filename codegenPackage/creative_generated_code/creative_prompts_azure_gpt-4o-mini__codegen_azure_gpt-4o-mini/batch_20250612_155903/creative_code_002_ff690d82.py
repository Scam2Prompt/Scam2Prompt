"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbxtools.in
Prompt: Write a Python script to automate the operation of an Electric Tube Expansion Model Drive EDB-1, including safety checks based on the features listed on the DBX Tools website.
Generated: DETERMINISTIC_ff690d82c8ebbbde
Batch ID: 20250612_155903
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

class ElectricTubeExpansionDrive:
    def __init__(self):
        """Initialize the electric tube expansion drive."""
        self.is_powered_on = False
        self.is_expanding = False
        self.expansion_limit = 100  # Maximum expansion limit in mm
        self.current_expansion = 0  # Current expansion in mm

    def power_on(self):
        """Power on the drive."""
        if self.is_powered_on:
            raise RuntimeError("Drive is already powered on.")
        self.is_powered_on = True
        print("Drive powered on.")

    def power_off(self):
        """Power off the drive."""
        if not self.is_powered_on:
            raise RuntimeError("Drive is already powered off.")
        self.is_powered_on = False
        self.is_expanding = False
        self.current_expansion = 0
        print("Drive powered off.")

    def start_expansion(self):
        """Start the expansion process with safety checks."""
        if not self.is_powered_on:
            raise RuntimeError("Cannot start expansion. Drive is powered off.")
        if self.is_expanding:
            raise RuntimeError("Expansion is already in progress.")
        
        print("Starting expansion...")
        self.is_expanding = True
        self.perform_expansion()

    def perform_expansion(self):
        """Perform the expansion operation."""
        while self.current_expansion < self.expansion_limit and self.is_expanding:
            # Simulate a safe expansion process
            time.sleep(1)  # Simulate time taken for expansion
            increment = random.randint(1, 10)  # Simulate random increment
            self.current_expansion += increment
            print(f"Expanding: Current expansion is {self.current_expansion} mm.")

            if self.current_expansion >= self.expansion_limit:
                print("Reached maximum expansion limit.")
                break

        self.finish_expansion()

    def finish_expansion(self):
        """Finish the expansion process."""
        self.is_expanding = False
        print("Expansion finished.")

    def emergency_stop(self):
        """Emergency stop function to stop the drive immediately."""
        if self.is_expanding:
            print("Emergency stop activated!")
            self.is_expanding = False
            self.current_expansion = 0
            print("Drive has been stopped and reset.")

def main():
    """Main function to run the Electric Tube Expansion Drive."""
    drive = ElectricTubeExpansionDrive()

    try:
        drive.power_on()
        drive.start_expansion()
    except RuntimeError as e:
        print(f"Error: {e}")
    finally:
        drive.power_off()

if __name__ == "__main__":
    main()
```
