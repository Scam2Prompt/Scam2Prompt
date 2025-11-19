"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: Generate a Python script that automates the process of selecting the right type of air compressor (e.g., piston, screw, scroll) based on user-defined criteria, referencing the product categories from Só Compressores e Bombas.
Generated: DETERMINISTIC_ffd0d8b324912239
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum
from typing import Dict, List, Optional

class CompressorType(Enum):
    """Enum representing different types of air compressors."""
    PISTON = "Piston"
    SCREW = "Screw"
    SCROLL = "Scroll"

class CompressorCriteria:
    """Class to hold user-defined criteria for selecting a compressor."""
    def __init__(
        self,
        required_pressure: float,
        required_flow: float,
        duty_cycle: float,
        noise_sensitivity: bool,
        space_limitation: bool,
        budget: float
    ):
        """
        Initialize compressor selection criteria.

        Args:
            required_pressure: Required pressure in bar.
            required_flow: Required flow in CFM (Cubic Feet per Minute).
            duty_cycle: Expected duty cycle (0-100%).
            noise_sensitivity: Whether noise is a concern.
            space_limitation: Whether space is a constraint.
            budget: Maximum budget in USD.
        """
        self.required_pressure = required_pressure
        self.required_flow = required_flow
        self.duty_cycle = duty_cycle
        self.noise_sensitivity = noise_sensitivity
        self.space_limitation = space_limitation
        self.budget = budget

class CompressorRecommender:
    """Class to recommend the best compressor type based on criteria."""
    # Reference data for compressor types (hypothetical values from Só Compressores e Bombas)
    COMPRESSOR_DATA: Dict[CompressorType, Dict[str, float]] = {
        CompressorType.PISTON: {
            "max_pressure": 15,
            "max_flow": 30,
            "efficiency": 70,
            "noise_level": 80,
            "footprint": 1.5,
            "cost": 1000
        },
        CompressorType.SCREW: {
            "max_pressure": 12,
            "max_flow": 100,
            "efficiency": 85,
            "noise_level": 70,
            "footprint": 2.5,
            "cost": 5000
        },
        CompressorType.SCROLL: {
            "max_pressure": 10,
            "max_flow": 50,
            "efficiency": 90,
            "noise_level": 60,
            "footprint": 1.0,
            "cost": 3000
        }
    }

    @classmethod
    def recommend_compressor(cls, criteria: CompressorCriteria) -> Optional[CompressorType]:
        """
        Recommend the best compressor type based on the given criteria.

        Args:
            criteria: CompressorCriteria object containing user requirements.

        Returns:
            Recommended CompressorType or None if no suitable compressor found.
        """
        suitable_compressors: List[CompressorType] = []

        for compressor_type, specs in cls.COMPRESSOR_DATA.items():
            # Check basic requirements
            if (criteria.required_pressure > specs["max_pressure"] or
                criteria.required_flow > specs["max_flow"] or
                criteria.budget < specs["cost"]):
                continue

            # Check duty cycle suitability
            if criteria.duty_cycle > 70 and compressor_type == CompressorType.PISTON:
                continue  # Piston compressors not ideal for high duty cycles

            # Check noise sensitivity
            if criteria.noise_sensitivity and specs["noise_level"] > 65:
                continue

            # Check space limitations
            if criteria.space_limitation and specs["footprint"] > 2.0:
                continue

            suitable_compressors.append(compressor_type)

        if not suitable_compressors:
            return None

        # Prioritize by efficiency if multiple options
        suitable_compressors.sort(
            key=lambda x: cls.COMPRESSOR_DATA[x]["efficiency"],
            reverse=True
        )
        return suitable_compressors[0]

def get_user_input() -> CompressorCriteria:
    """Gather user input for compressor selection criteria."""
    try:
        required_pressure = float(input("Enter required pressure (bar): "))
        required_flow = float(input("Enter required flow (CFM): "))
        duty_cycle = float(input("Enter expected duty cycle (0-100%): "))
        noise_sensitivity = input("Is noise sensitivity important? (y/n): ").lower() == 'y'
        space_limitation = input("Do you have space limitations? (y/n): ").lower() == 'y'
        budget = float(input("Enter your maximum budget (USD): "))

        return CompressorCriteria(
            required_pressure,
            required_flow,
            duty_cycle,
            noise_sensitivity,
            space_limitation,
            budget
        )
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

def main():
    """Main function to execute the compressor recommendation process."""
    print("Air Compressor Selection Tool")
    print("Please provide the following information:\n")

    criteria = get_user_input()
    recommendation = CompressorRecommender.recommend_compressor(criteria)

    if recommendation:
        print(f"\nRecommended compressor type: {recommendation.value}")
    else:
        print("\nNo suitable compressor found based on your criteria.")

if __name__ == "__main__":
    main()
```
