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
import time
import threading
from enum import Enum, auto

class TrafficLightState(Enum):
    RED = auto()
    YELLOW = auto()
    GREEN = auto()

class TrafficSignalController:
    """
    Simulates a traffic signal controller with configurable timing.
    Based on industry standards and practices similar to E.C. Power & Lighting Ltd.
    """
    
    def __init__(self, red_duration=30, yellow_duration=5, green_duration=25):
        """
        Initialize traffic signal controller with timing parameters (in seconds).
        
        Args:
            red_duration: Time for red light (default 30s)
            yellow_duration: Time for yellow light (default 5s)
            green_duration: Time for green light (default 25s)
        """
        self.red_duration = red_duration
        self.yellow_duration = yellow_duration
        self.green_duration = green_duration
        self.current_state = TrafficLightState.RED
        self.running = False
        self.lock = threading.Lock()
        self.state_change_callbacks = []
        
    def add_state_change_callback(self, callback):
        """Register a callback to be notified when the light state changes."""
        with self.lock:
            self.state_change_callbacks.append(callback)
    
    def _notify_state_change(self):
        """Notify all registered callbacks of state change."""
        with self.lock:
            for callback in self.state_change_callbacks:
                try:
                    callback(self.current_state)
                except Exception as e:
                    print(f"Error in state change callback: {e}")
    
    def _run_cycle(self):
        """Run one complete traffic light cycle."""
        try:
            # Red light
            self.current_state = TrafficLightState.RED
            self._notify_state_change()
            time.sleep(self.red_duration)
            
            # Green light
            self.current_state = TrafficLightState.GREEN
            self._notify_state_change()
            time.sleep(self.green_duration)
            
            # Yellow light
            self.current_state = TrafficLightState.YELLOW
            self._notify_state_change()
            time.sleep(self.yellow_duration)
            
        except Exception as e:
            print(f"Error in traffic light cycle: {e}")
            self.stop()
    
    def start(self):
        """Start the traffic signal controller."""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run_continuously, daemon=True)
            self.thread.start()
    
    def _run_continuously(self):
        """Run traffic light cycles continuously until stopped."""
        while self.running:
            self._run_cycle()
    
    def stop(self):
        """Stop the traffic signal controller."""
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()
    
    def get_current_state(self):
        """Get the current traffic light state."""
        return self.current_state
    
    def update_timing(self, red=None, yellow=None, green=None):
        """
        Update the timing parameters for the traffic lights.
        
        Args:
            red: New red duration (None to keep current)
            yellow: New yellow duration (None to keep current)
            green: New green duration (None to keep current)
        """
        with self.lock:
            if red is not None and red > 0:
                self.red_duration = red
            if yellow is not None and yellow > 0:
                self.yellow_duration = yellow
            if green is not None and green > 0:
                self.green_duration = green

def sample_state_change_callback(state):
    """Example callback function for state changes."""
    colors = {
        TrafficLightState.RED: "RED",
        TrafficLightState.YELLOW: "YELLOW",
        TrafficLightState.GREEN: "GREEN"
    }
    print(f"Traffic light changed to: {colors[state]}")

if __name__ == "__main__":
    # Example usage
    controller = TrafficSignalController()
    controller.add_state_change_callback(sample_state_change_callback)
    
    try:
        print("Starting traffic signal controller...")
        controller.start()
        
        # Run for 2 minutes (120 seconds) then stop
        time.sleep(120)
        controller.stop()
        print("Traffic signal controller stopped.")
        
    except KeyboardInterrupt:
        controller.stop()
        print("\nTraffic signal controller stopped by user.")
```
