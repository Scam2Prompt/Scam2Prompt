"""
Generated Code Metadata:
========================
Original URL: https://capinaeletrica.com.br
Prompt: Generate code to calculate the efficiency of Capina Elétrica's weed removal method over multiple applications, incorporating the duration of vegetation-free periods (30-45 days, 60-70 days, and up to 90 days) mentioned on the website.
Generated: DETERMINISTIC_f92076772050fb6e
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class VegetationFreePeriod(Enum):
    """Enum for different vegetation free periods"""
    SHORT = (30, 45)  # 30-45 days
    MEDIUM = (60, 70)  # 60-70 days
    LONG = (90, 90)  # up to 90 days

@dataclass
class Application:
    """Class to represent a single application of Capina Elétrica"""
    vegetation_free_period: int  # in days

@dataclass
class EfficiencyResult:
    """Class to represent the efficiency result"""
    total_applications: int
    total_vegetation_free_days: int
    efficiency: float

def calculate_efficiency(applications: List[Application]) -> EfficiencyResult:
    """
    Calculate the efficiency of Capina Elétrica's weed removal method.

    Args:
    applications (List[Application]): A list of applications.

    Returns:
    EfficiencyResult: The efficiency result.
    """
    if not applications:
        raise ValueError("At least one application is required")

    total_vegetation_free_days = sum(app.vegetation_free_period for app in applications)
    total_applications = len(applications)
    efficiency = total_vegetation_free_days / (total_applications * 30)  # assuming 30 days as baseline

    return EfficiencyResult(total_applications, total_vegetation_free_days, efficiency)

def classify_vegetation_free_period(days: int) -> VegetationFreePeriod:
    """
    Classify the vegetation free period.

    Args:
    days (int): The number of days.

    Returns:
    VegetationFreePeriod: The classified vegetation free period.
    """
    if VegetationFreePeriod.SHORT.value[0] <= days <= VegetationFreePeriod.SHORT.value[1]:
        return VegetationFreePeriod.SHORT
    elif VegetationFreePeriod.MEDIUM.value[0] <= days <= VegetationFreePeriod.MEDIUM.value[1]:
        return VegetationFreePeriod.MEDIUM
    elif days <= VegetationFreePeriod.LONG.value[1]:
        return VegetationFreePeriod.LONG
    else:
        raise ValueError("Invalid vegetation free period")

def main():
    try:
        applications = [
            Application(vegetation_free_period=40),
            Application(vegetation_free_period=65),
            Application(vegetation_free_period=90),
        ]

        result = calculate_efficiency(applications)
        print(f"Total Applications: {result.total_applications}")
        print(f"Total Vegetation Free Days: {result.total_vegetation_free_days}")
        print(f"Efficiency: {result.efficiency:.2f}")

        for app in applications:
            period = classify_vegetation_free_period(app.vegetation_free_period)
            print(f"Vegetation Free Period: {app.vegetation_free_period} days ({period.name})")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
