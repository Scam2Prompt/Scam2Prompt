"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sardiniameetsazores.eu
Prompt: Develop a program to model the drying and grinding process of "مراوح متحركة" using the technical details outlined on the Sardinia Meets Azores webpage.
Generated: DETERMINISTIC_b85d14b05af655e9
Batch ID: 20250612_153224
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

class DryingAndGrindingProcess:
    def __init__(self, initial_moisture_content):
        """
        Initialize the drying and grinding process.

        Args:
            initial_moisture_content (float): Initial moisture content in percentage (0-100).
        """
        self.initial_moisture_content = initial_moisture_content
        self.current_moisture_content = initial_moisture_content
        self.drying_time = 0  # in hours
        self.grinding_time = 0  # in hours

    def dry_material(self):
        """
        Simulate the drying process until the desired moisture content is reached.
        The drying process will reduce the moisture content by a random percentage each hour.
        """
        target_moisture_content = 10.0  # Target moisture content after drying
        while self.current_moisture_content > target_moisture_content:
            reduction = random.uniform(5, 15)  # Random reduction between 5% to 15%
            self.current_moisture_content = max(self.current_moisture_content - reduction, target_moisture_content)
            self.drying_time += 1
            time.sleep(1)  # Simulate time delay for drying in real scenario
            print(f"Drying... Current moisture content: {self.current_moisture_content:.2f}%")
        
        print(f"Drying completed in {self.drying_time} hours.")

    def grind_material(self):
        """
        Simulate the grinding process which takes a constant time based on the initial moisture content.
        The higher the moisture content, the longer the grinding time.
        """
        self.grinding_time = (self.initial_moisture_content - self.current_moisture_content) / 10  # Example calculation
        time.sleep(1)  # Simulate time delay for grinding
        print(f"Grinding completed in {self.grinding_time:.2f} hours.")

    def run_process(self):
        """
        Execute the drying and grinding process sequentially.
        """
        try:
            print("Starting the drying process...")
            self.dry_material()
            print("Starting the grinding process...")
            self.grind_material()
            print("Process completed successfully.")
        except Exception as e:
            print(f"An error occurred during the process: {e}")

if __name__ == "__main__":
    initial_moisture = 60.0  # Example initial moisture content
    process = DryingAndGrindingProcess(initial_moisture)
    process.run_process()
```
