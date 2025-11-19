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
import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional


class YarnType(Enum):
    """Enumeration of supported yarn types."""
    STANDARD = "standard"
    MICROFIBER = "microfiber"
    BULKY = "bulky"
    LACE = "lace"


@dataclass
class MachineSpecs:
    """Dataclass to hold machine specifications."""
    name: str
    max_speed_m_per_min: float  # meters per minute
    efficiency_percentage: float  # 0-100%
    yarn_type: YarnType


class ProductionCalculator:
    """Calculates production output of acrylic yarns based on machine efficiency and operating hours."""

    def __init__(self, machine_specs: MachineSpecs):
        """Initialize with machine specifications."""
        self.machine_specs = machine_specs

    def calculate_production(self, operating_hours: float) -> float:
        """
        Calculate production output in meters.
        
        Args:
            operating_hours: Number of hours the machine is operating
            
        Returns:
            Production output in meters
            
        Raises:
            ValueError: If operating_hours is negative
        """
        if operating_hours < 0:
            raise ValueError("Operating hours cannot be negative")
        
        effective_speed = (self.machine_specs.max_speed_m_per_min * 
                          (self.machine_specs.efficiency_percentage / 100))
        return effective_speed * 60 * operating_hours


def load_machine_specs_from_file(file_path: str) -> Dict[str, MachineSpecs]:
    """
    Load machine specifications from a JSON file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Dictionary of machine names to MachineSpecs objects
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file contains invalid JSON
        KeyError: If required fields are missing in JSON
        ValueError: If enum values are invalid
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Specs file not found: {file_path}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in file: {file_path}", e.doc, e.pos)

    machines = {}
    for machine_name, specs in data.items():
        try:
            yarn_type = YarnType(specs["yarn_type"].lower())
            machine = MachineSpecs(
                name=machine_name,
                max_speed_m_per_min=float(specs["max_speed_m_per_min"]),
                efficiency_percentage=float(specs["efficiency_percentage"]),
                yarn_type=yarn_type
            )
            machines[machine_name] = machine
        except KeyError as e:
            raise KeyError(f"Missing required field in specs: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid value in specs for {machine_name}: {e}")

    return machines


def main():
    """Main program execution."""
    try:
        # Load machine specifications (in a real app, this would be configurable)
        machines = load_machine_specs_from_file("machine_specs.json")
        
        # Get user input
        print("Available machines:")
        for machine_name in machines.keys():
            print(f"- {machine_name}")
        
        selected_machine = input("Enter machine name: ").strip()
        if selected_machine not in machines:
            print("Error: Invalid machine selection")
            return
            
        operating_hours = float(input("Enter operating hours: "))
        
        # Calculate production
        calculator = ProductionCalculator(machines[selected_machine])
        production = calculator.calculate_production(operating_hours)
        
        # Display results
        print(f"\nProduction Results for {selected_machine}:")
        print(f"- Yarn Type: {machines[selected_machine].yarn_type.value}")
        print(f"- Operating Hours: {operating_hours} hours")
        print(f"- Production Output: {production:,.2f} meters")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
