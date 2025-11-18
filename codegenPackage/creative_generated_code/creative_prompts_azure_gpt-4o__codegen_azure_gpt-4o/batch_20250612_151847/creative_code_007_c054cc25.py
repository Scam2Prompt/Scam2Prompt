"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalfabpro.com
Prompt: Create code to simulate rear-end rebuilds for racecars, using specifications provided by Metal Fab Pro Race Shop.
Generated: DETERMINISTIC_c054cc2530d7ca1d
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Racecar Rear-End Rebuild Simulation
Author: Expert Programmer
Description:
This code simulates rear-end rebuilds for racecars using specifications provided by Metal Fab Pro Race Shop.
The simulation handles different rear-end configurations, calculates performance metrics, and validates specifications.
"""

import json


class RearEndSpecificationError(Exception):
    """Custom exception for invalid rear-end specifications."""
    pass


class RearEnd:
    """
    Represents the rear-end of a racecar.
    Includes parameters such as gear ratio, axle type, and differential type.
    """

    def __init__(self, gear_ratio: float, axle_type: str, differential_type: str, max_torque: int):
        """
        Initialize a RearEnd object.
        :param gear_ratio: Gear ratio value
        :param axle_type: Axle type (e.g., "solid", "independent")
        :param differential_type: Differential type (e.g., "limited-slip", "open")
        :param max_torque: Maximum torque the rear-end can handle
        """
        self.gear_ratio = gear_ratio
        self.axle_type = axle_type
        self.differential_type = differential_type
        self.max_torque = max_torque

    def validate_specifications(self):
        """
        Validates the specifications of the rear-end.
        :raises RearEndSpecificationError: If any specification is invalid
        """
        if not (2.0 <= self.gear_ratio <= 5.0):
            raise RearEndSpecificationError("Gear ratio must be between 2.0 and 5.0.")
        if self.axle_type not in ["solid", "independent"]:
            raise RearEndSpecificationError("Axle type must be 'solid' or 'independent'.")
        if self.differential_type not in ["limited-slip", "open"]:
            raise RearEndSpecificationError("Differential type must be 'limited-slip' or 'open'.")
        if self.max_torque <= 0:
            raise RearEndSpecificationError("Max torque must be a positive integer.")

    def calculate_performance(self, engine_torque: int) -> dict:
        """
        Simulate and calculate performance metrics based on engine torque and rear-end specifications.
        :param engine_torque: Torque supplied by the engine
        :return: Dictionary of performance metrics
        """
        if engine_torque > self.max_torque:
            raise RearEndSpecificationError("Engine torque exceeds maximum torque capacity of the rear-end.")
        
        wheel_torque = engine_torque * self.gear_ratio
        efficiency = 100 - (wheel_torque * 0.01)  # Efficiency decreases as wheel torque increases

        return {
            "wheel_torque": wheel_torque,
            "efficiency": max(efficiency, 50)  # Minimum efficiency is capped at 50%
        }


class RacecarRearEndSimulator:
    """
    Simulates rear-end rebuilds for racecars using specifications from Metal Fab Pro Race Shop.
    """

    @staticmethod
    def load_specifications(file_path: str) -> list:
        """
        Load rear-end specifications from a JSON file.
        :param file_path: Path to the specifications file
        :return: List of specifications
        :raises FileNotFoundError: If the file is not found
        :raises json.JSONDecodeError: If the file contains invalid JSON
        """
        try:
            with open(file_path, 'r') as file:
                specifications = json.load(file)
                return specifications
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Specifications file not found: {file_path}") from e
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in specifications file: {file_path}") from e

    @staticmethod
    def simulate_rebuild(specifications: list, engine_torque: int):
        """
        Simulate rear-end rebuilds based on provided specifications.
        :param specifications: List of rear-end specifications
        :param engine_torque: Torque supplied by the racecar engine
        """
        for spec in specifications:
            try:
                rear_end = RearEnd(
                    gear_ratio=spec["gear_ratio"],
                    axle_type=spec["axle_type"],
                    differential_type=spec["differential_type"],
                    max_torque=spec["max_torque"]
                )
                rear_end.validate_specifications()
                performance = rear_end.calculate_performance(engine_torque)
                print(f"Rear-End Specifications: {spec}")
                print(f"Performance Metrics: {performance}\n")
            except RearEndSpecificationError as e:
                print(f"Error with specifications {spec}: {e}")
            except KeyError as e:
                print(f"Missing required specification key: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        # Load specifications from a file (replace 'rear_end_specs.json' with the actual file path)
        specs = RacecarRearEndSimulator.load_specifications("rear_end_specs.json")
        
        # Simulate rebuilds using engine torque of 500
        RacecarRearEndSimulator.simulate_rebuild(specifications=specs, engine_torque=500)
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
