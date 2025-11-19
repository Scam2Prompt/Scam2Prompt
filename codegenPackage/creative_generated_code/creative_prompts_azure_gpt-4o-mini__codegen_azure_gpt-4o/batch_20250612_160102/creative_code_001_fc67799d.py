"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ozonator.si
Prompt: How can I implement an ozone generator in a hospital setting for disinfecting operating rooms? Provide a code example for monitoring ozone levels.
Generated: DETERMINISTIC_fc67799d7457c4b3
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class OzoneGenerator:
    """
    A class to simulate an ozone generator in a hospital setting.
    Includes monitoring and control of ozone levels for disinfecting operating rooms.
    """
    
    def __init__(self, safe_threshold=50, danger_threshold=100):
        """
        Initialize the ozone generator with safe and danger thresholds.

        :param safe_threshold: Maximum ozone level considered safe (default: 50).
        :param danger_threshold: Ozone level considered dangerous (default: 100).
        """
        self.safe_threshold = safe_threshold
        self.danger_threshold = danger_threshold
        self.current_ozone_level = 0
        self.generator_status = False  # False: Off, True: On

    def turn_on(self):
        """Turn on the ozone generator."""
        self.generator_status = True
        print("Ozone Generator is ON.")

    def turn_off(self):
        """Turn off the ozone generator."""
        self.generator_status = False
        print("Ozone Generator is OFF.")
    
    def simulate_ozone_generation(self):
        """
        Simulate ozone generation by randomly increasing ozone levels.
        Called when the generator is ON.
        """
        if self.generator_status:
            # Randomly increase ozone level between 5 and 20 units
            self.current_ozone_level += random.randint(5, 20)

    def monitor_ozone_levels(self):
        """
        Monitor ozone levels and control the generator accordingly.
        If levels exceed danger_threshold, turn off the generator.
        """
        print(f"Current Ozone Level: {self.current_ozone_level} ppm")
        
        if self.current_ozone_level >= self.danger_threshold:
            print("OZONE LEVEL TOO HIGH! Turning off the generator...")
            self.turn_off()
            print("Alert: Dangerous ozone level detected, room evacuation advised!")
        elif self.generator_status and self.current_ozone_level < self.safe_threshold:
            print("Ozone level is safe. Continuing operation...")
        elif self.generator_status and self.current_ozone_level >= self.safe_threshold:
            print("Ozone level approaching unsafe limits. Please monitor carefully.")
    
    def reset_ozone_levels(self):
        """
        Reset the ozone levels after room cleaning is completed.
        """
        self.current_ozone_level = 0
        print("Ozone levels reset to 0 ppm.")

# Main function to initialize and simulate the ozone generator
def main():
    # Create an instance of OzoneGenerator with custom thresholds
    ozone_generator = OzoneGenerator(safe_threshold=50, danger_threshold=100)
    
    try:
        # Turn on the generator
        ozone_generator.turn_on()
        
        # Simulate and monitor ozone levels for a set period
        for _ in range(10):  # Simulate 10 monitoring cycles
            time.sleep(1)  # Wait for 1 second between cycles
            ozone_generator.simulate_ozone_generation()
            ozone_generator.monitor_ozone_levels()
            
            # Break out of the loop if the generator is turned off due to high levels
            if not ozone_generator.generator_status:
                break
        
        # After simulation, reset the ozone levels
        ozone_generator.reset_ozone_levels()
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Ensure the generator is off before exiting
        ozone_generator.turn_off()

# Run the main function
if __name__ == "__main__":
    main()
```
