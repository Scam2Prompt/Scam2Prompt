"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-ss.com
Prompt: Generate code to control a car's interior lighting system, including custom suede headliner lighting and reconfigurable performance displays, inspired by the Phantom SS modifications.
Generated: DETERMINISTIC_76ab828483834797
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class CarInteriorLightingSystem:
    """
    Class to control car's interior lighting system, including custom suede headliner lighting
    and reconfigurable performance displays.
    """
    def __init__(self):
        # Initialize lighting states for headliner and displays
        self.headliner_lighting = False
        self.performance_display_brightness = 50  # Brightness level (0-100)

    def toggle_headliner_lighting(self):
        """
        Toggles the state of the suede headliner lighting (ON/OFF).
        """
        self.headliner_lighting = not self.headliner_lighting
        print(f"Headliner lighting {'ON' if self.headliner_lighting else 'OFF'}")

    def set_performance_display_brightness(self, brightness):
        """
        Sets the brightness level of the performance displays.
        :param brightness: Integer value between 0 and 100.
        """
        if not isinstance(brightness, int) or brightness < 0 or brightness > 100:
            print("Error: Brightness level must be an integer between 0 and 100.")
            return
        
        self.performance_display_brightness = brightness
        print(f"Performance display brightness set to {brightness}%")

    def display_status(self):
        """
        Prints the current status of the interior lighting system.
        """
        print("Interior Lighting System Status:")
        print(f"  Headliner Lighting: {'ON' if self.headliner_lighting else 'OFF'}")
        print(f"  Performance Display Brightness: {self.performance_display_brightness}%")

    def run_demo(self):
        """
        Runs a demo of the lighting system for testing purposes.
        """
        print("Starting lighting system demo...")
        self.toggle_headliner_lighting()
        time.sleep(1)

        self.set_performance_display_brightness(75)
        time.sleep(1)

        self.toggle_headliner_lighting()
        time.sleep(1)

        self.set_performance_display_brightness(25)
        time.sleep(1)

        self.display_status()


# Main execution block
if __name__ == "__main__":
    try:
        # Create an instance of the lighting system
        lighting_system = CarInteriorLightingSystem()

        # Run demo to showcase functionality
        lighting_system.run_demo()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
