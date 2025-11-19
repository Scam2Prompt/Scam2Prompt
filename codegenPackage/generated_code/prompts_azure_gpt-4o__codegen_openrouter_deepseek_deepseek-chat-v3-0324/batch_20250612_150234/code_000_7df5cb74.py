"""
Generated Code Metadata:
========================
Original URL: https://y45y45hy45y45y54.pages.dev
Prompt: Write code to simulate a countdown timer similar to "Sophon Time" with a format of HH:MM:SS and a reset feature.
Generated: DETERMINISTIC_7df5cb742c00005c
Batch ID: 20250612_150234
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

class CountdownTimer:
    """
    A countdown timer that displays time in HH:MM:SS format with reset functionality.
    """
    
    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Initialize the timer with hours, minutes, and seconds.
        
        Args:
            hours (int): Hours for countdown (default 0)
            minutes (int): Minutes for countdown (default 0)
            seconds (int): Seconds for countdown (default 0)
        """
        self.initial_hours = hours
        self.initial_minutes = minutes
        self.initial_seconds = seconds
        self.reset()
        
    def reset(self):
        """Reset the timer to its initial values."""
        self.remaining_hours = self.initial_hours
        self.remaining_minutes = self.initial_minutes
        self.remaining_seconds = self.initial_seconds
        
    def _format_time(self):
        """Format remaining time as HH:MM:SS."""
        return f"{self.remaining_hours:02d}:{self.remaining_minutes:02d}:{self.remaining_seconds:02d}"
        
    def _tick(self):
        """Decrement the timer by one second."""
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
        else:
            if self.remaining_minutes > 0:
                self.remaining_minutes -= 1
                self.remaining_seconds = 59
            elif self.remaining_hours > 0:
                self.remaining_hours -= 1
                self.remaining_minutes = 59
                self.remaining_seconds = 59
            else:
                return False  # Timer expired
        return True  # Timer still running
        
    def start(self):
        """Start the countdown timer."""
        try:
            while True:
                print(f"\r{self._format_time()}", end="")
                sys.stdout.flush()
                
                if not self._tick():
                    print("\nCountdown complete!")
                    break
                    
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nTimer paused. Press 'r' to reset or any other key to continue.")
            choice = input().lower()
            if choice == 'r':
                self.reset()
                self.start()
            else:
                self.start()

if __name__ == "__main__":
    try:
        print("Enter countdown time (HH:MM:SS): ")
        time_input = input().strip()
        hours, minutes, seconds = map(int, time_input.split(':'))
        
        if any(t < 0 for t in (hours, minutes, seconds)):
            raise ValueError("Time values cannot be negative")
        if minutes >= 60 or seconds >= 60:
            raise ValueError("Minutes and seconds must be less than 60")
            
        timer = CountdownTimer(hours, minutes, seconds)
        print("Starting countdown... Press Ctrl+C to pause.")
        timer.start()
        
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
