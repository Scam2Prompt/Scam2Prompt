"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Write a program that calculates the production output of acrylic yarns based on machine efficiency and operating hours, using data inputs like yarn type and machinery specifications.
Generated: DETERMINISTIC_12b2e746741475e4
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# production_calculator.py

from enum import Enum
from dataclasses import dataclass
from typing import Dict

class YarnType(str, Enum):
    """Types of acrylic yarns"""
    STANDARD = "standard"
    HIGH_STRENGTH = "high_strength"
    BLENDED = "blended"

@dataclass
class MachinerySpecs:
    """Machine specifications"""
    efficiency: float  # percentage
    max_production_rate: float  # kg/h

class ProductionCalculator:
    """Calculates production output of acrylic yarns"""

    def __init__(self):
        self.yarn_type_production_rates: Dict[YarnType, MachinerySpecs] = {
            YarnType.STANDARD: MachinerySpecs(efficiency=0.8, max_production_rate=100),
            YarnType.HIGH_STRENGTH: MachinerySpecs(efficiency=0.7, max_production_rate=80),
            YarnType.BLENDED: MachinerySpecs(efficiency=0.9, max_production_rate=120),
        }

    def calculate_production_output(self, yarn_type: YarnType, operating_hours: float) -> float:
        """
        Calculates production output based on machine efficiency and operating hours

        Args:
        - yarn_type (YarnType): Type of acrylic yarn
        - operating_hours (float): Number of hours the machine operates

        Returns:
        - float: Production output in kg
        """
        try:
            machine_specs = self.yarn_type_production_rates[yarn_type]
            effective_production_rate = machine_specs.max_production_rate * machine_specs.efficiency
            production_output = effective_production_rate * operating_hours
            return production_output
        except KeyError:
            raise ValueError(f"Unsupported yarn type: {yarn_type}")

def main():
    calculator = ProductionCalculator()

    yarn_type = YarnType.STANDARD
    operating_hours = 8

    try:
        production_output = calculator.calculate_production_output(yarn_type, operating_hours)
        print(f"Production output for {yarn_type.value} yarn: {production_output:.2f} kg")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
