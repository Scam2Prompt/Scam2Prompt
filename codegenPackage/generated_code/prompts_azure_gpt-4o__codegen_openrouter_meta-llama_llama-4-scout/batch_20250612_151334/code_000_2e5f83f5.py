"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Write Python code to simulate traffic signal timing and control, referencing the expertise of E.C. Power & Lighting Ltd. in traffic signal installations.
Generated: DETERMINISTIC_2e5f83f57a2d60b1
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict
import time
import threading

# Define traffic signal colors as an Enum
class TrafficSignalColor(Enum):
    """Traffic signal colors"""
    RED = 1
    YELLOW = 2
    GREEN = 3

class TrafficSignal:
    """Traffic signal controller"""
    
    def __init__(self, name: str, 
                 green_duration: int = 30, 
                 yellow_duration: int = 5, 
                 red_duration: int = 30):
        """
        Initialize traffic signal.

        Args:
        - name (str): Traffic signal name
        - green_duration (int): Green light duration in seconds (default: 30)
        - yellow_duration (int): Yellow light duration in seconds (default: 5)
        - red_duration (int): Red light duration in seconds (default: 30)
        """
        self.name = name
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.red_duration = red_duration
        self.current_color = TrafficSignalColor.RED
        self.is_running = False

    def start(self):
        """Start traffic signal"""
        if not self.is_running:
            self.is_running = True
            threading.Thread(target=self.run).start()

    def stop(self):
        """Stop traffic signal"""
        self.is_running = False

    def run(self):
        """Run traffic signal timing loop"""
        while self.is_running:
            self.change_color(TrafficSignalColor.GREEN, self.green_duration)
            self.change_color(TrafficSignalColor.YELLOW, self.yellow_duration)
            self.change_color(TrafficSignalColor.RED, self.red_duration)

    def change_color(self, color: TrafficSignalColor, duration: int):
        """Change traffic signal color and wait for a duration"""
        self.current_color = color
        print(f"Traffic signal {self.name} is {color.name}")
        time.sleep(duration)

def main():
    # Create traffic signals
    signals: Dict[str, TrafficSignal] = {
        "Main Road": TrafficSignal("Main Road", green_duration=45, yellow_duration=5, red_duration=20),
        "Side Road": TrafficSignal("Side Road", green_duration=30, yellow_duration=5, red_duration=45)
    }

    # Start traffic signals
    for signal in signals.values():
        signal.start()

    try:
        # Keep main thread running
        while True:
            pass
    except KeyboardInterrupt:
        # Stop traffic signals on Ctrl+C
        for signal in signals.values():
            signal.stop()

if __name__ == "__main__":
    main()
```
