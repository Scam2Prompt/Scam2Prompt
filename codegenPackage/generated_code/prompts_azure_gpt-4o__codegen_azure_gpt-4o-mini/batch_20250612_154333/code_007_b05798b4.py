"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Write code to simulate the wear and tear of spare parts for heavy machinery, incorporating maintenance recommendations from PT. Fuji Metal Teknik.
Generated: DETERMINISTIC_b05798b4c18b6b67
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import datetime
from typing import List, Dict

class SparePart:
    """
    A class to represent a spare part of heavy machinery.
    """

    def __init__(self, name: str, wear_rate: float, maintenance_interval: int):
        """
        Initializes a new SparePart instance.

        :param name: Name of the spare part.
        :param wear_rate: Rate of wear per usage (0 to 1).
        :param maintenance_interval: Recommended usage count before maintenance is required.
        """
        self.name = name
        self.wear_rate = wear_rate
        self.usage_count = 0
        self.last_maintenance_date = datetime.datetime.now()
        self.maintenance_interval = maintenance_interval

    def use(self):
        """
        Simulates the usage of the spare part, increasing its wear.
        """
        self.usage_count += 1
        if self.usage_count % self.maintenance_interval == 0:
            self.recommend_maintenance()

    def recommend_maintenance(self):
        """
        Provides maintenance recommendations based on usage.
        """
        print(f"Maintenance recommended for {self.name} after {self.usage_count} usages.")

    def calculate_wear(self) -> float:
        """
        Calculates the current wear level of the spare part.

        :return: Current wear level (0 to 1).
        """
        wear_level = min(self.wear_rate * self.usage_count, 1.0)
        return wear_level

    def needs_replacement(self) -> bool:
        """
        Determines if the spare part needs to be replaced based on wear level.

        :return: True if replacement is needed, False otherwise.
        """
        return self.calculate_wear() >= 1.0

class Machinery:
    """
    A class to represent heavy machinery with spare parts.
    """

    def __init__(self):
        """
        Initializes a new Machinery instance with an empty list of spare parts.
        """
        self.spare_parts: List[SparePart] = []

    def add_spare_part(self, spare_part: SparePart):
        """
        Adds a spare part to the machinery.

        :param spare_part: An instance of SparePart to add.
        """
        self.spare_parts.append(spare_part)

    def operate(self):
        """
        Simulates the operation of the machinery, using each spare part.
        """
        for part in self.spare_parts:
            try:
                part.use()
                if part.needs_replacement():
                    print(f"{part.name} needs replacement.")
            except Exception as e:
                print(f"Error while operating {part.name}: {e}")

def main():
    """
    Main function to simulate machinery operation and spare part wear.
    """
    # Create machinery instance
    machinery = Machinery()

    # Add spare parts with their wear rates and maintenance intervals
    machinery.add_spare_part(SparePart("Hydraulic Pump", wear_rate=0.02, maintenance_interval=50))
    machinery.add_spare_part(SparePart("Gearbox", wear_rate=0.01, maintenance_interval=100))
    machinery.add_spare_part(SparePart("Engine Filter", wear_rate=0.03, maintenance_interval=30))

    # Simulate operation for a number of cycles
    for _ in range(200):
        machinery.operate()

if __name__ == "__main__":
    main()
```
