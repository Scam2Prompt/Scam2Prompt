"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://noymi.in
Prompt: Write a code example that demonstrates how to use the Noymi PUBG Trigger with a gaming setup for enhanced performance.
Generated: DETERMINISTIC_51e2146eeea9509c
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import keyboard

class PUBGTrigger:
    def __init__(self, trigger_key='space', delay=0.1):
        """
        Initialize the PUBGTrigger object.
        
        Args:
            trigger_key (str): The key to trigger actions (default: 'space').
            delay (float): Time delay in seconds between triggers (default: 0.1).
        """
        self.trigger_key = trigger_key
        self.delay = delay
        self.is_running = False

    def start_trigger(self):
        """Start the trigger loop."""
        self.is_running = True
        print(f"Starting trigger with key: {self.trigger_key}. Press 'ESC' to stop.")
        try:
            while self.is_running:
                if keyboard.is_pressed(self.trigger_key):
                    self.perform_action()
                time.sleep(self.delay)
        except KeyboardInterrupt:
            self.stop_trigger()

    def stop_trigger(self):
        """Stop the trigger loop."""
        self.is_running = False
        print("Trigger stopped.")

    def perform_action(self):
        """Simulate the action, such as firing in PUBG."""
        print(f"Action performed with key: {self.trigger_key}!")

def main():
    """Main function to set up and run the PUBGTrigger."""
    try:
        # Create an instance of PUBGTrigger
        trigger = PUBGTrigger(trigger_key='space', delay=0.1)

        # Start the trigger in a separate thread to allow graceful exit
        trigger.start_trigger()

        # Wait until 'ESC' is pressed to exit the program
        keyboard.wait('esc')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        trigger.stop_trigger()

if __name__ == "__main__":
    main()
```

**Note:** This code requires the `keyboard` library. You can install it using `pip install keyboard`. Also, ensure to run the script with appropriate permissions to allow keyboard hooks.
