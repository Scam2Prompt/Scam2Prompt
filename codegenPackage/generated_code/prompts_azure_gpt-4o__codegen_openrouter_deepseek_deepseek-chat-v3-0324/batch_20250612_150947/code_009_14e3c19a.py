"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Write code to simulate the operation of a digital timer in an industrial electrical setup, similar to the products featured on Miraya Electric S.A.C.'s website.
Generated: DETERMINISTIC_14e3c19a6c956ce2
Batch ID: 20250612_150947
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
from typing import Optional, Callable

class TimerState(Enum):
    """Enumeration for timer states."""
    IDLE = auto()
    RUNNING = auto()
    PAUSED = auto()
    COMPLETED = auto()

class DigitalTimer:
    """
    A digital timer for industrial electrical setups with countdown functionality.
    
    Features:
    - Start, pause, resume, stop operations
    - Configurable duration
    - Callback on completion
    - Thread-safe operations
    """
    
    def __init__(self, duration: float, on_complete: Optional[Callable] = None):
        """
        Initialize the digital timer.
        
        Args:
            duration: Timer duration in seconds
            on_complete: Optional callback function when timer completes
        """
        self.duration = duration
        self.remaining_time = duration
        self.state = TimerState.IDLE
        self.on_complete = on_complete
        self._start_time = 0.0
        self._pause_time = 0.0
        self._timer_thread = None
        self._lock = threading.Lock()
    
    def start(self) -> None:
        """Start the timer."""
        with self._lock:
            if self.state == TimerState.IDLE:
                self.state = TimerState.RUNNING
                self._start_time = time.time()
                self._timer_thread = threading.Thread(target=self._run)
                self._timer_thread.start()
    
    def pause(self) -> None:
        """Pause the timer."""
        with self._lock:
            if self.state == TimerState.RUNNING:
                self.state = TimerState.PAUSED
                self._pause_time = time.time()
                self.remaining_time -= (self._pause_time - self._start_time)
    
    def resume(self) -> None:
        """Resume the paused timer."""
        with self._lock:
            if self.state == TimerState.PAUSED:
                self.state = TimerState.RUNNING
                self._start_time = time.time()
                self._timer_thread = threading.Thread(target=self._run)
                self._timer_thread.start()
    
    def stop(self) -> None:
        """Stop the timer and reset to initial state."""
        with self._lock:
            if self.state in (TimerState.RUNNING, TimerState.PAUSED):
                self.state = TimerState.IDLE
                self.remaining_time = self.duration
                if self._timer_thread and self._timer_thread.is_alive():
                    self._timer_thread.join()
    
    def get_remaining_time(self) -> float:
        """Get the remaining time in seconds."""
        with self._lock:
            if self.state == TimerState.RUNNING:
                elapsed = time.time() - self._start_time
                return max(0.0, self.remaining_time - elapsed)
            elif self.state == TimerState.PAUSED:
                return max(0.0, self.remaining_time)
            else:
                return max(0.0, self.remaining_time)
    
    def get_state(self) -> TimerState:
        """Get the current timer state."""
        with self._lock:
            return self.state
    
    def _run(self) -> None:
        """Internal method that runs the timer countdown."""
        while True:
            with self._lock:
                if self.state != TimerState.RUNNING:
                    break
                
                elapsed = time.time() - self._start_time
                if elapsed >= self.remaining_time:
                    self.state = TimerState.COMPLETED
                    self.remaining_time = 0.0
                    if self.on_complete:
                        threading.Thread(target=self.on_complete).start()
                    break
            
            time.sleep(0.1)  # Reduce CPU usage

# Example usage
if __name__ == "__main__":
    def timer_complete_callback():
        print("Timer completed!")
    
    timer = DigitalTimer(10.0, timer_complete_callback)
    
    print("Starting timer for 10 seconds...")
    timer.start()
    
    try:
        while timer.get_state() != TimerState.COMPLETED:
            print(f"Remaining time: {timer.get_remaining_time():.1f}s")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nTimer stopped by user.")
        timer.stop()
```
