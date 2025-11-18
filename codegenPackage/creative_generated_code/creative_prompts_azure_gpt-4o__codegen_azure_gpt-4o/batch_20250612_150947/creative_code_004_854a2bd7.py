"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirayaelectricsac.com
Prompt: Suggest Python libraries for simulating the functionality of differential switches and timers, such as those listed on Miraya Electric S.A.C.'s website.
Generated: DETERMINISTIC_854a2bd74d3d091f
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script suggests Python libraries for simulating the functionality of 
differential switches (e.g., residual-current devices) and timers.
It includes code examples to demonstrate basic simulation behavior using 
popular libraries such as PySim for simulations and sched for timers.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Required Python Libraries
import time
import random
from threading import Timer
from datetime import datetime
import sched

# Differential Switch Simulation
class DifferentialSwitch:
    """
    Class to simulate the functionality of a differential switch (residual-current device).
    Detects current leakage and triggers a trip when leakage exceeds a threshold.
    """
    def __init__(self, leakage_threshold=30):  # Threshold in mA (milliamps)
        self.leakage_threshold = leakage_threshold
        self.is_tripped = False

    def measure_current_leakage(self):
        """
        Simulates measuring current leakage. Generates a random leakage value.
        """
        return random.uniform(0, 50)  # Simulated leakage between 0 and 50 mA

    def check_leakage(self):
        """
        Checks if the leakage exceeds the threshold and trips the switch if necessary.
        """
        leakage = self.measure_current_leakage()
        print(f"[{datetime.now()}] Measured leakage: {leakage:.2f} mA")
        if leakage > self.leakage_threshold:
            self.trip()
        else:
            print("Leakage within safe limits. Differential switch remains ON.")

    def trip(self):
        """
        Trips the differential switch.
        """
        self.is_tripped = True
        print("ALERT: Differential switch TRIPPED due to excessive leakage!")

# Timer Simulation
class TimerSimulation:
    """
    Class to simulate timer functionality using the sched library.
    Executes a recurring task at fixed intervals.
    """
    def __init__(self, interval_seconds=5):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.interval_seconds = interval_seconds

    def task(self):
        """
        Define the task to be executed by the timer.
        """
        print(f"[{datetime.now()}] Timer executed task.")
        # Reschedule the task to run again after the interval
        self.scheduler.enter(self.interval_seconds, 1, self.task)

    def start(self):
        """
        Starts the timer simulation.
        """
        print(f"Starting timer simulation. Task will run every {self.interval_seconds} seconds.")
        self.scheduler.enter(self.interval_seconds, 1, self.task)
        self.scheduler.run()

# Main Script
if __name__ == "__main__":
    # Initialize and test the Differential Switch
    print("Simulating differential switch functionality...")
    differential_switch = DifferentialSwitch(leakage_threshold=25)  # Setting threshold to 25 mA
    for _ in range(5):  # Check leakage 5 times
        differential_switch.check_leakage()
        time.sleep(2)  # Simulate a delay between measurements

    print("\nSimulating timer functionality...")
    timer_simulation = TimerSimulation(interval_seconds=3)  # Timer interval set to 3 seconds
    timer_thread = Timer(0, timer_simulation.start)  # Run timer simulation in a separate thread
    timer_thread.start()

    # Keep the script running to observe timer behavior
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSimulation ended by user.")
```
