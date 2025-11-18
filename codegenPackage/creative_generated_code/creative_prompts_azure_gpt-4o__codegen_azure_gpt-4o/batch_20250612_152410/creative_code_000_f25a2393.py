"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biamtechintl.com
Prompt: Write Python code to simulate the functionality of laparoscopic suction irrigation as described on BIAM Tech International's website, including fluid removal and irrigation delivery.
Generated: DETERMINISTIC_f25a239399a16edf
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class SuctionIrrigationSystem:
    """
    Simulates the functionality of a laparoscopic suction irrigation system.
    Provides methods for suction (fluid removal) and irrigation (fluid delivery).
    """

    def __init__(self):
        """
        Initializes the suction irrigation system with default states for suction and irrigation.
        """
        self.suction_active = False
        self.irrigation_active = False

    def start_suction(self):
        """
        Activates suction mode for fluid removal.
        """
        if self.suction_active:
            print("Suction is already active.")
        else:
            self.suction_active = True
            print("Suction activated.")

    def stop_suction(self):
        """
        Deactivates suction mode.
        """
        if not self.suction_active:
            print("Suction is not active.")
        else:
            self.suction_active = False
            print("Suction deactivated.")

    def start_irrigation(self):
        """
        Activates irrigation mode for fluid delivery.
        """
        if self.irrigation_active:
            print("Irrigation is already active.")
        else:
            self.irrigation_active = True
            print("Irrigation activated.")

    def stop_irrigation(self):
        """
        Deactivates irrigation mode.
        """
        if not self.irrigation_active:
            print("Irrigation is not active.")
        else:
            self.irrigation_active = False
            print("Irrigation deactivated.")

    def simulate_operation(self, duration=5):
        """
        Simulates the suction or irrigation operation for a given duration.
        If both suction and irrigation are active, it simulates simultaneous operation.
        
        Args:
            duration (int): Duration of the operation in seconds.
        """
        if not self.suction_active and not self.irrigation_active:
            print("No operation is active. Please activate suction or irrigation.")
            return

        print(f"Starting operation for {duration} seconds...")
        for second in range(duration):
            time.sleep(1)  # Simulate real-time operation with a delay
            status = []
            if self.suction_active:
                status.append("suctioning")
            if self.irrigation_active:
                status.append("irrigating")
            print(f"Second {second + 1}: {' and '.join(status)}...")
        
        print("Operation completed.")

# Example usage
if __name__ == "__main__":
    # Create an instance of the system
    system = SuctionIrrigationSystem()

    # Start suction and irrigation sequentially
    system.start_suction()
    system.simulate_operation(duration=3)
    system.stop_suction()

    system.start_irrigation()
    system.simulate_operation(duration=3)
    system.stop_irrigation()

    # Start both suction and irrigation simultaneously
    system.start_suction()
    system.start_irrigation()
    system.simulate_operation(duration=4)
    system.stop_suction()
    system.stop_irrigation()
```
