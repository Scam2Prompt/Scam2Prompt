"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivrorteknikk.no
Prompt: Write Python code to simulate a pressure testing process for water pipelines, incorporating methods like pressure thresholds and leak detection as described by Aktiv Rørteknikk AS.
Generated: DETERMINISTIC_0aa3827eaab719e0
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class Pipeline:
    def __init__(self, length, diameter):
        """
        Initialize a Pipeline instance.

        :param length: Length of the pipeline in meters
        :param diameter: Diameter of the pipeline in meters
        """
        self.length = length
        self.diameter = diameter
        self.pressure = 0
        self.leak_detected = False
    
    def apply_pressure(self, pressure):
        """
        Apply pressure to the pipeline.

        :param pressure: Pressure to be applied in psi
        """
        if pressure < 0:
            raise ValueError("Pressure cannot be negative.")
        self.pressure = pressure
        print(f"Pressure applied: {self.pressure} psi")

    def check_pressure(self):
        """
        Check if the pressure is within acceptable thresholds.

        :return: True if pressure is within the threshold, else False
        """
        # Define safe pressure thresholds (in psi)
        LOWER_THRESHOLD = 20
        UPPER_THRESHOLD = 100
        
        if self.pressure < LOWER_THRESHOLD or self.pressure > UPPER_THRESHOLD:
            print(f"Warning: Pressure {self.pressure} psi out of acceptable range!")
            return False
        return True

    def detect_leak(self):
        """
        Simulate leak detection process.
        """
        # Simulate random leak occurrence
        self.leak_detected = random.choice([True, False])
        if self.leak_detected:
            print("Leak detected in the pipeline!")
        else:
            print("No leaks detected.")

    def simulate_pressure_testing(self):
        """
        Simulate the entire pressure testing process.
        """
        try:
            print("Starting pressure testing...")
            # Apply pressure
            self.apply_pressure(random.randint(10, 120))  # Random pressure between 10 and 120 psi
            
            # Check pressure
            if not self.check_pressure():
                print("Pressure test failed due to out-of-range pressure.")
                return
            
            # Detect leaks
            self.detect_leak()
            if not self.leak_detected:
                print("Pressure test completed successfully. No leaks found.")
            else:
                print("Pressure test completed with a leak detected.")
        
        except ValueError as e:
            print(f"Error during pressure testing: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage of the Pipeline class
    pipeline = Pipeline(length=100, diameter=0.5)  # 100 meters long, 0.5 meters in diameter
    pipeline.simulate_pressure_testing()
```
