"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://noymi.in
Prompt: Write code to implement a gaming trigger mechanism for mobile games, referencing features of the NOYMI PUBG Trigger | Gaming Trigger | ET-128.
Generated: DETERMINISTIC_4a58f6d32416a5b4
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class GamingTrigger:
    """
    A class to implement a gaming trigger mechanism for mobile games,
    referencing features of the NOYMI PUBG Trigger | Gaming Trigger | ET-128.
    """

    def __init__(self, trigger_name="NOYMI PUBG Trigger | ET-128"):
        """
        Initialize the GamingTrigger with a name and default configuration.

        :param trigger_name: Name of the gaming trigger device.
        """
        self.trigger_name = trigger_name
        self.is_pressed = False  # Tracks the state of the trigger
        self.sensitivity = 0.5  # Default sensitivity (adjustable between 0.1 to 1.0)
        self.press_callbacks = []  # List of functions to call on press event
        self.release_callbacks = []  # List of functions to call on release event

    def set_sensitivity(self, sensitivity):
        """
        Adjust the sensitivity of the trigger.

        :param sensitivity: A float value between 0.1 (low sensitivity) and 1.0 (high sensitivity).
        :raises ValueError: If sensitivity is out of range.
        """
        if not (0.1 <= sensitivity <= 1.0):
            raise ValueError("Sensitivity must be between 0.1 and 1.0")
        self.sensitivity = sensitivity

    def on_press(self, callback):
        """
        Register a function to be called when the trigger is pressed.

        :param callback: A function to be executed on press event.
        """
        self.press_callbacks.append(callback)

    def on_release(self, callback):
        """
        Register a function to be called when the trigger is released.

        :param callback: A function to be executed on release event.
        """
        self.release_callbacks.append(callback)

    def press(self):
        """
        Simulate pressing the trigger.
        Executes all registered press callbacks.
        """
        if self.is_pressed:
            return  # Prevent duplicate press events

        self.is_pressed = True
        print(f"{self.trigger_name} pressed (Sensitivity: {self.sensitivity})")

        for callback in self.press_callbacks:
            try:
                callback()  # Execute each registered callback
            except Exception as e:
                print(f"Error during press callback execution: {e}")

    def release(self):
        """
        Simulate releasing the trigger.
        Executes all registered release callbacks.
        """
        if not self.is_pressed:
            return  # Prevent duplicate release events

        self.is_pressed = False
        print(f"{self.trigger_name} released")

        for callback in self.release_callbacks:
            try:
                callback()  # Execute each registered callback
            except Exception as e:
                print(f"Error during release callback execution: {e}")

    def simulate_trigger_activity(self, duration=2):
        """
        Simulate trigger activity (press and release) to demonstrate functionality.

        :param duration: Time in seconds between press and release.
        """
        self.press()
        time.sleep(duration * self.sensitivity)  # Adjust delay based on sensitivity
        self.release()


# Example usage:

def example_press_action():
    print("Trigger pressed action executed!")

def example_release_action():
    print("Trigger released action executed!")

if __name__ == "__main__":
    # Create a gaming trigger
    trigger = GamingTrigger()

    # Set sensitivity
    trigger.set_sensitivity(0.7)

    # Register callback functions for press and release events
    trigger.on_press(example_press_action)
    trigger.on_release(example_release_action)

    # Simulate trigger activity
    trigger.simulate_trigger_activity(duration=3)
```
