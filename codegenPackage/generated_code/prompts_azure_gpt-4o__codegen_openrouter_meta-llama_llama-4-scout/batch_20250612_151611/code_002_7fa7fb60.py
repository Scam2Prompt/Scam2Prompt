"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Develop a program that categorizes fuel injectors by type (mechanical, electronic, petrol, diesel) and generates a maintenance schedule based on the cleaning process outlined on the Fuel Injector Services website.
Generated: DETERMINISTIC_7fa7fb60251b861f
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass
from datetime import datetime, timedelta

class FuelType(Enum):
    """Enum for fuel types"""
    PETROL = "petrol"
    DIESEL = "diesel"

class InjectorType(Enum):
    """Enum for injector types"""
    MECHANICAL = "mechanical"
    ELECTRONIC = "electronic"

@dataclass
class FuelInjector:
    """Class representing a fuel injector"""
    injector_type: InjectorType
    fuel_type: FuelType
    last_cleaning_date: datetime = None
    cleaning_interval: int = 0  # in miles

    def __post_init__(self):
        if self.injector_type == InjectorType.MECHANICAL:
            if self.fuel_type == FuelType.PETROL:
                self.cleaning_interval = 15000  # miles
            elif self.fuel_type == FuelType.DIESEL:
                self.cleaning_interval = 10000  # miles
        elif self.injector_type == InjectorType.ELECTRONIC:
            if self.fuel_type == FuelType.PETROL:
                self.cleaning_interval = 20000  # miles
            elif self.fuel_type == FuelType.DIESEL:
                self.cleaning_interval = 15000  # miles

    def needs_cleaning(self, current_mileage: int, last_cleaning_mileage: int = 0) -> bool:
        """Check if injector needs cleaning"""
        mileage_since_last_cleaning = current_mileage - last_cleaning_mileage
        return mileage_since_last_cleaning >= self.cleaning_interval

    def generate_maintenance_schedule(self, current_mileage: int, last_cleaning_mileage: int = 0) -> str:
        """Generate maintenance schedule"""
        if self.needs_cleaning(current_mileage, last_cleaning_mileage):
            next_cleaning_mileage = current_mileage + (self.cleaning_interval - (current_mileage - last_cleaning_mileage))
            return f"Fuel injector needs cleaning at {next_cleaning_mileage} miles."
        else:
            next_cleaning_mileage = last_cleaning_mileage + self.cleaning_interval
            return f"Fuel injector does not need cleaning. Next cleaning due at {next_cleaning_mileage} miles."

def categorize_injector(injector_type: str, fuel_type: str) -> FuelInjector:
    """Categorize fuel injector by type"""
    try:
        injector_type_enum = InjectorType(injector_type.upper())
        fuel_type_enum = FuelType(fuel_type.upper())
        return FuelInjector(injector_type_enum, fuel_type_enum)
    except ValueError:
        raise ValueError("Invalid injector type or fuel type")

def main():
    injector = categorize_injector("electronic", "petrol")
    print(f"Injector Type: {injector.injector_type.value}, Fuel Type: {injector.fuel_type.value}")
    print(injector.generate_maintenance_schedule(10000))

if __name__ == "__main__":
    main()
```
