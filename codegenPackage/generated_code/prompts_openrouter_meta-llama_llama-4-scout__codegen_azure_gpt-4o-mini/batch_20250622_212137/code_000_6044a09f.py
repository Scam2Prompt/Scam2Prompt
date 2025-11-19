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

def loading_animation(message="Loading soon", duration=5):
    """
    Displays a loading animation in the console.

    Args:
        message (str): The message to display during loading.
        duration (int): The total duration (in seconds) for the loading animation.
    """
    # Define the loading characters
    loading_chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration

    try:
        while time.time() < end_time:
            for char in loading_chars:
                # Print the loading character and message
                sys.stdout.write(f'\r{message} {char}')
                sys.stdout.flush()
                time.sleep(0.2)  # Adjust the speed of the animation
    except KeyboardInterrupt:
        # Handle the case where the user interrupts the loading
        print("\nLoading interrupted.")
    finally:
        # Clear the line after loading is complete
        sys.stdout.write('\r' + ' ' * (len(message) + 2) + '\r')
        sys.stdout.flush()

if __name__ == "__main__":
    loading_animation()
```

This script creates a simple loading animation in the console that displays a "Loading soon" message. The animation runs for a specified duration and can be interrupted by the user.
