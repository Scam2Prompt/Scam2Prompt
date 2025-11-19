"""
Generated Code Metadata:
========================
Original URL: https://arcofaurora.com
Prompt: Write a Python script that simulates the "Great Heart Opener" session, utilizing sound frequency healing techniques.
Generated: DETERMINISTIC_fd5104b2bde701d0
Batch ID: 20250612_135919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import winsound  # Windows-specific sound library
import random
import sys
from datetime import datetime

class GreatHeartOpener:
    """
    Simulates a Great Heart Opener session using sound frequency healing techniques.
    Provides different frequency patterns and durations for a healing experience.
    """
    
    def __init__(self):
        """Initialize session parameters"""
        self.frequencies = {
            'grounding': 136.1,
            'heart_opening': 528.0,
            'love': 639.0,
            'harmony': 741.0,
            'crown': 963.0
        }
        self.session_duration = 20 * 60  # 20 minutes in seconds
        self.current_stage = None
        self.start_time = None
        
    def play_frequency(self, freq, duration_ms):
        """Play a frequency for a specified duration (Windows only)"""
        try:
            winsound.Beep(int(freq), duration_ms)
        except Exception as e:
            print(f"Error playing frequency: {e}")
            return False
        return True
    
    def get_user_input(self):
        """Get and validate user input for session customization"""
        try:
            duration = input("Enter session duration in minutes (default 20): ")
            if duration.strip():
                self.session_duration = float(duration) * 60
                if self.session_duration <= 0:
                    raise ValueError("Duration must be positive")
            
            print("\nAvailable frequencies:")
            for i, (name, freq) in enumerate(self.frequencies.items(), 1):
                print(f"{i}. {name.title()} ({freq} Hz)")
            
            choice = input("\nSelect frequency by number (Enter for random sequence): ")
            if choice.strip():
                choice = int(choice)
                if 1 <= choice <= len(self.frequencies):
                    selected = list(self.frequencies.values())[choice-1]
                    return [selected] * 5  # Repeat selected frequency
                raise ValueError("Invalid selection")
            
            return None  # Random sequence
            
        except ValueError as e:
            print(f"Invalid input: {e}")
            sys.exit(1)
    
    def run_random_sequence(self):
        """Run a randomized sequence of frequencies"""
        sequence = random.sample(list(self.frequencies.values()), len(self.frequencies))
        segment_duration = (self.session_duration / len(sequence)) * 1000
        
        for freq in sequence:
            self.current_stage = [k for k, v in self.frequencies.items() if v == freq][0]
            self.display_status()
            if not self.play_frequency(freq, int(segment_duration)):
                break
            if time.time() - self.start_time > self.session_duration:
                break
    
    def display_status(self):
        """Display current session status"""
        elapsed = int(time.time() - self.start_time)
        remaining = max(0, int(self.session_duration - elapsed))
        
        print(f"\nCurrent stage: {self.current_stage.replace('_', ' ').title()}")
        print(f"Elapsed: {elapsed // 60}m {elapsed % 60}s")
        print(f"Remaining: {remaining // 60}m {remaining % 60}s")
        print(f"Frequency: {self.frequencies[self.current_stage]} Hz")
    
    def run(self):
        """Main method to run the session"""
        print("\n=== Great Heart Opener Session ===")
        print(f"Session started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        self.start_time = time.time()
        custom_sequence = self.get_user_input()
        
        if custom_sequence:
            segment_duration = (self.session_duration / len(custom_sequence)) * 1000
            for freq in custom_sequence:
                self.current_stage = [k for k, v in self.frequencies.items() if v == freq][0]
                self.display_status()
                if not self.play_frequency(freq, int(segment_duration)):
                    break
                if time.time() - self.start_time > self.session_duration:
                    break
        else:
            self.run_random_sequence()
        
        print("\nSession completed. Thank you for your practice.")
        print(f"Session ended at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    try:
        session = GreatHeartOpener()
        session.run()
    except KeyboardInterrupt:
        print("\nSession interrupted by user. Exiting gracefully.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
```
