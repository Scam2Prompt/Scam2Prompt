"""
Generated Code Metadata:
========================
Original URL: https://ksaacademy-classera.classera.com
Prompt: Write a Python script to create a loading animation for a webpage that displays a "loading soon" message.
Generated: DETERMINISTIC_6044a09fd503dfd5
Batch ID: 20250622_212137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import sys
from typing import Optional

class LoadingAnimation:
    """
    A class to create a loading animation for a webpage with a "loading soon" message.
    """
    
    def __init__(self, message: str = "Loading soon", animation_chars: str = "|/-\\", delay: float = 0.1):
        """
        Initialize the loading animation.
        
        Args:
            message: The message to display before the animation.
            animation_chars: Characters to use for the animation sequence.
            delay: Delay between animation frames in seconds.
        """
        self.message = message
        self.animation_chars = animation_chars
        self.delay = delay
        self._stop_requested = False
    
    def _clear_line(self):
        """Clear the current line in the console."""
        sys.stdout.write('\r')
        sys.stdout.flush()
    
    def animate(self, duration: Optional[float] = None):
        """
        Start the loading animation.
        
        Args:
            duration: Optional duration in seconds after which animation stops.
                     If None, runs until manually stopped.
        """
        start_time = time.time()
        i = 0
        
        try:
            while not self._stop_requested:
                current_char = self.animation_chars[i % len(self.animation_chars)]
                sys.stdout.write(f'\r{self.message} {current_char}')
                sys.stdout.flush()
                time.sleep(self.delay)
                i += 1
                
                if duration and (time.time() - start_time) >= duration:
                    break
        except KeyboardInterrupt:
            pass
        finally:
            self._clear_line()
    
    def stop(self):
        """Stop the loading animation."""
        self._stop_requested = True
        self._clear_line()

# Example usage
if __name__ == "__main__":
    loader = LoadingAnimation()
    try:
        print("Starting loading animation...")
        loader.animate(duration=5)  # Run for 5 seconds
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        print("\nAnimation complete.")
```
