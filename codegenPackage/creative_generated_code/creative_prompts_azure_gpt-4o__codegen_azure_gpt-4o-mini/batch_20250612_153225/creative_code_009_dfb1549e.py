"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://technicalpower.us
Prompt: Generate a tool for simulating the impact of water incursion or cyberattacks on data center operations, referencing the downtime causes listed by Technical Power Service, Inc.
Generated: DETERMINISTIC_dfb1549eb31f6cb4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from typing import List, Dict

class DataCenter:
    """
    A class to represent a data center and simulate downtime caused by water incursion or cyberattacks.

    Attributes:
        name (str): The name of the data center.
        operational_status (bool): The current operational status of the data center.
        downtime_causes (List[str]): A list holding the causes of downtime.
        downtime_log (List[Dict]): A log of downtime events with timestamps and causes.
    """

    def __init__(self, name: str):
        """
        Initializes the DataCenter with a name and sets the initial operational status.

        Args:
            name (str): The name of the data center.
        """
        self.name = name
        self.operational_status = True
        self.downtime_causes = [
            "Water incursion",
            "Cyberattack",
            "Power failure",
            "Equipment failure"
        ]
        self.downtime_log = []

    def simulate_downtime(self) -> None:
        """
        Simulates a random downtime event based on the predefined causes.
        """
        if self.operational_status:
            cause = random.choice(self.downtime_causes)
            self.operational_status = False
            downtime_event = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "cause": cause
            }
            self.downtime_log.append(downtime_event)
            print(f"Downtime simulated at {downtime_event['timestamp']} due to: {cause}")
        else:
            print("Data center is already down. Cannot simulate additional downtime.")

    def resolve_downtime(self) -> None:
        """
        Resolves the current downtime status of the data center.
        """
        if not self.operational_status:
            self.operational_status = True
            print("Data center operational status restored.")
        else:
            print("Data center is already operational.")

    def display_downtime_log(self) -> None:
        """
        Displays the log of all downtime events.
        """
        if self.downtime_log:
            print("Downtime Log:")
            for event in self.downtime_log:
                print(f"{event['timestamp']} - {event['cause']}")
        else:
            print("No downtime events recorded.")

def main():
    """
    Main function to run the DataCenter simulation.
    """
    # Initialize the data center
    dc = DataCenter("Main Data Center")

    # Simulate some downtime events
    for _ in range(3):
        dc.simulate_downtime()
        time.sleep(1)  # Pause to mimic real-time events

    # Display downtime log
    dc.display_downtime_log()

    # Resolve downtime
    dc.resolve_downtime()
    dc.display_downtime_log()

# Entry point of the script
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
