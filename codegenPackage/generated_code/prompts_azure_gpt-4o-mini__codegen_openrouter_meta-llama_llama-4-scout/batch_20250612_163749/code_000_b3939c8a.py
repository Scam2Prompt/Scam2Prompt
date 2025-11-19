"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Write a Python script to simulate traffic signal control using E.C. Power & Lighting Ltd.'s specifications for traffic signals.
Generated: DETERMINISTIC_b3939c8a75166c56
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Traffic Signal Control Simulation

This script simulates traffic signal control based on E.C. Power & Lighting Ltd.'s specifications.

Author: [Your Name]
Date: [Today's Date]
"""

import time
import threading

class TrafficSignal:
    """
    Represents a traffic signal with three colors: Red, Yellow, Green.
    """

    def __init__(self, name):
        """
        Initializes a traffic signal with a given name.

        Args:
            name (str): The name of the traffic signal.
        """
        self.name = name
        self.colors = ["Red", "Green", "Yellow"]
        self.current_color = self.colors[0]
        self.is_running = False

    def start(self):
        """
        Starts the traffic signal simulation.
        """
        if not self.is_running:
            self.is_running = True
            threading.Thread(target=self.change_color).start()

    def stop(self):
        """
        Stops the traffic signal simulation.
        """
        self.is_running = False

    def change_color(self):
        """
        Changes the color of the traffic signal every few seconds.
        """
        color_index = 0
        while self.is_running:
            self.current_color = self.colors[color_index]
            print(f"{self.name} signal is {self.current_color}")
            if self.current_color == "Red":
                time.sleep(5)  # Red light stays for 5 seconds
            elif self.current_color == "Green":
                time.sleep(5)  # Green light stays for 5 seconds
            elif self.current_color == "Yellow":
                time.sleep(2)  # Yellow light stays for 2 seconds
            color_index = (color_index + 1) % len(self.colors)


class TrafficSignalController:
    """
    Controls multiple traffic signals.
    """

    def __init__(self):
        """
        Initializes a traffic signal controller.
        """
        self.signals = []

    def add_signal(self, signal):
        """
        Adds a traffic signal to the controller.

        Args:
            signal (TrafficSignal): The traffic signal to add.
        """
        self.signals.append(signal)

    def start_all_signals(self):
        """
        Starts all traffic signals.
        """
        for signal in self.signals:
            signal.start()


def main():
    try:
        # Create traffic signals
        signal1 = TrafficSignal("Main Road")
        signal2 = TrafficSignal("Side Road")

        # Create a traffic signal controller
        controller = TrafficSignalController()
        controller.add_signal(signal1)
        controller.add_signal(signal2)

        # Start all traffic signals
        controller.start_all_signals()

        # Keep the main thread running
        while True:
            pass

    except KeyboardInterrupt:
        print("\nStopping traffic signals...")
        # Stop all traffic signals
        for signal in [signal1, signal2]:
            signal.stop()


if __name__ == "__main__":
    main()
```
