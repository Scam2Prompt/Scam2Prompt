"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gadgetexa.com
Prompt: Write a step-by-step Python script for troubleshooting fuse issues in laminators using a multimeter, based on Gadgetexa's fuse testing tutorial.
Generated: DETERMINISTIC_5929f46b969d1e82
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class Multimeter:
    """A class representing a multimeter for measuring voltage and resistance."""
    
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        """Turns on the multimeter."""
        self.is_on = True
        print("Multimeter is now ON.")

    def turn_off(self):
        """Turns off the multimeter."""
        self.is_on = False
        print("Multimeter is now OFF.")

    def measure_voltage(self, fuse):
        """Measures voltage across the fuse.
        
        Args:
            fuse (Fuse): The fuse to measure voltage across.
        
        Returns:
            float: The voltage across the fuse.
        """
        if not self.is_on:
            raise RuntimeError("Multimeter is OFF. Please turn it ON before measuring.")
        
        return fuse.get_voltage()

    def measure_resistance(self, fuse):
        """Measures resistance of the fuse.
        
        Args:
            fuse (Fuse): The fuse to measure resistance.
        
        Returns:
            float: The resistance of the fuse.
        """
        if not self.is_on:
            raise RuntimeError("Multimeter is OFF. Please turn it ON before measuring.")
        
        return fuse.get_resistance()

class Fuse:
    """A class representing a fuse in the laminator."""

    def __init__(self, is_good=True):
        self.is_good = is_good

    def get_voltage(self):
        """Simulates getting voltage across the fuse.
        
        Returns:
            float: The voltage across the fuse (0 if blown).
        """
        return 120.0 if self.is_good else 0.0

    def get_resistance(self):
        """Simulates getting resistance of the fuse.
        
        Returns:
            float: The resistance of the fuse (0 if blown).
        """
        return 0.0 if self.is_good else float('inf')

def troubleshoot_fuse(fuse):
    """Troubleshoots the fuse issue in a laminator using a multimeter.
    
    Args:
        fuse (Fuse): The fuse to troubleshoot.
    """
    multimeter = Multimeter()

    try:
        # Step 1: Turn on the multimeter
        multimeter.turn_on()
        time.sleep(1)  # Simulate delay for turning on

        # Step 2: Measure voltage across the fuse
        voltage = multimeter.measure_voltage(fuse)
        print(f"Measured voltage across the fuse: {voltage}V")

        if voltage == 0:
            print("The fuse is blown. Please replace the fuse.")
            return

        # Step 3: Measure resistance of the fuse
        resistance = multimeter.measure_resistance(fuse)
        print(f"Measured resistance of the fuse: {resistance}Ω")

        if resistance == float('inf'):
            print("The fuse is blown (infinite resistance). Please replace the fuse.")
        else:
            print("The fuse is functioning properly.")
    
    except RuntimeError as e:
        print(f"Error: {e}")
    
    finally:
        # Step 4: Turn off the multimeter
        multimeter.turn_off()

# Example usage:
if __name__ == "__main__":
    # Create a fuse object (set is_good to False to simulate a blown fuse)
    fuse = Fuse(is_good=False)
    troubleshoot_fuse(fuse)
```
