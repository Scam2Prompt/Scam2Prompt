"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mandosecurity.com
Prompt: Write a program to simulate K9 training for explosive and narcotic detection, referencing Mando Security's dog handler courses.
Generated: DETERMINISTIC_7f86c0e3da18b769
Batch ID: 20250612_152326
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

class K9:
    """A class representing a K9 unit for detection training."""
    
    def __init__(self, name: str):
        """Initialize K9 with a name and set initial training state."""
        self.name = name
        self.trained_for_explosives = False
        self.trained_for_narcotics = False
        self.success_rate = 0.5  # Assume a 50% success rate for detection

    def train_explosives(self):
        """Simulate training the dog for explosive detection."""
        print(f"{self.name} is training for explosive detection...")
        time.sleep(2)  # Simulate training time
        self.trained_for_explosives = True
        self.success_rate += 0.1  # Increase success rate after training
        print(f"{self.name} has completed training for explosives.")

    def train_narcotics(self):
        """Simulate training the dog for narcotics detection."""
        print(f"{self.name} is training for narcotics detection...")
        time.sleep(2)  # Simulate training time
        self.trained_for_narcotics = True
        self.success_rate += 0.1  # Increase success rate after training
        print(f"{self.name} has completed training for narcotics.")

    def detect(self, substance: str) -> bool:
        """Simulate the detection process for the given substance.
        
        Args:
            substance (str): The type of substance to detect (either 'explosive' or 'narcotic').

        Returns:
            bool: True if the detection was successful, False otherwise.
        """
        if substance == 'explosive' and not self.trained_for_explosives:
            raise ValueError(f"{self.name} is not trained for explosive detection.")
        elif substance == 'narcotic' and not self.trained_for_narcotics:
            raise ValueError(f"{self.name} is not trained for narcotics detection.")

        detection_success = random.random() < self.success_rate
        if detection_success:
            print(f"{self.name} successfully detected {substance}.")
        else:
            print(f"{self.name} failed to detect {substance}.")
        return detection_success

def main():
    """Main function to execute K9 training simulation."""
    try:
        # Create a K9 unit
        k9_unit = K9(name="Rex")

        # Train the dog for explosives and narcotics
        k9_unit.train_explosives()
        k9_unit.train_narcotics()

        # Simulate detections
        substances_to_detect = ['explosive', 'narcotic', 'explosive', 'narcotic']
        for substance in substances_to_detect:
            k9_unit.detect(substance)
    
    except ValueError as e:
        print(f"Error during detection: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
