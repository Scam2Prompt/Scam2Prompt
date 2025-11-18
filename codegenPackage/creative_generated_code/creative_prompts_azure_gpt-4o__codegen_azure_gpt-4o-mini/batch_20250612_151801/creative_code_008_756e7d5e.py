"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kubitz.com.br
Prompt: Generate a Python script to simulate the operation of a tunnel composting system, referencing Kubitz's composting solutions.
Generated: DETERMINISTIC_756e7d5e898fdbfe
Batch ID: 20250612_151801
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

class CompostingSystem:
    """A class to simulate a tunnel composting system."""

    def __init__(self, initial_material_weight: float, moisture_content: float):
        """
        Initialize the composting system with initial parameters.
        
        :param initial_material_weight: Weight of the compost material in kg.
        :param moisture_content: Moisture content percentage (0-100).
        """
        self.material_weight = initial_material_weight
        self.moisture_content = moisture_content
        self.temperature = 20  # Starting temperature in Celsius
        self.composting_duration = 0  # Duration in days
        self.is_composting = False

    def start_composting(self):
        """Initiate the composting process."""
        if self.is_composting:
            raise RuntimeError("Composting is already in progress.")
        
        self.is_composting = True
        print("Composting started.")

    def adjust_conditions(self):
        """Simulate the adjustment of composting conditions."""
        if not self.is_composting:
            raise RuntimeError("Composting has not been started.")
        
        # Randomly adjust temperature and moisture content
        self.temperature += random.uniform(1, 3)  # Increase temperature
        self.moisture_content += random.uniform(-2, 2)  # Adjust moisture content
        
        # Ensure moisture content is within valid range
        self.moisture_content = max(0, min(self.moisture_content, 100))

        # Simulate the passing of time in the composting process
        time.sleep(1)  # Simulates a delay for real-world conditions
        self.composting_duration += 1  # Increment the composting duration

        print(f"Day {self.composting_duration}: Temperature = {self.temperature:.1f}°C, "
              f"Moisture Content = {self.moisture_content:.1f}%")

    def check_status(self):
        """Check the current status of composting."""
        if not self.is_composting:
            return "Composting has not been started."
        
        if self.composting_duration >= 30:
            self.is_composting = False
            return "Composting process completed successfully."

        return "Composting is currently in progress."

    def get_report(self):
        """Generate a summary report of the composting process."""
        return {
            "Weight of Material (kg)": self.material_weight,
            "Moisture Content (%)": self.moisture_content,
            "Current Temperature (°C)": self.temperature,
            "Days of Composting": self.composting_duration,
            "Is Composting Active": self.is_composting,
        }

def run_composting_simulation():
    """Run the composting simulation."""
    try:
        compost = CompostingSystem(initial_material_weight=1000, moisture_content=60)
        compost.start_composting()

        while compost.is_composting:
            compost.adjust_conditions()
            print(compost.get_report())
            if compost.check_status() == "Composting process completed successfully.":
                print("Final report:", compost.get_report())
                break

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_composting_simulation()
```
