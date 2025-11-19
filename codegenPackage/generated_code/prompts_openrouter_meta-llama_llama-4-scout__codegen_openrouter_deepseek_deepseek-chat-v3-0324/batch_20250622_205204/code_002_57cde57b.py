"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: "Write a Python script to calculate the cost of a custom glass railing project, including materials and labor, based on the Marine Vidros pricing model."
Generated: DETERMINISTIC_57cde57b3f577d05
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Glass Railing Cost Calculator based on Marine Vidros Pricing Model

This script calculates the total cost of a custom glass railing project,
including materials and labor, based on user-provided dimensions and options.
"""

import math
from dataclasses import dataclass
from typing import Optional


@dataclass
class GlassRailingProject:
    """Class to store project parameters and calculate costs."""
    length_m: float  # Length in meters
    height_m: float  # Height in meters
    glass_type: str  # Type of glass (tempered, laminated, etc.)
    handrail_included: bool  # Whether handrail is included
    installation_complexity: str  # Simple, moderate, or complex
    region: str  # Region for labor cost adjustment

    # Material costs per square meter (example values - should be updated with actual pricing)
    GLASS_PRICES = {
        'tempered': 150.0,
        'laminated': 200.0,
        'tinted': 250.0,
        'extra_clear': 300.0
    }

    # Handrail cost per linear meter
    HANDRAIL_COST = 75.0

    # Base labor cost per square meter
    BASE_LABOR_COST = 100.0

    # Labor multipliers based on complexity
    LABOR_MULTIPLIERS = {
        'simple': 1.0,
        'moderate': 1.3,
        'complex': 1.7
    }

    # Regional cost adjustments
    REGIONAL_MULTIPLIERS = {
        'urban': 1.2,
        'suburban': 1.0,
        'rural': 0.9
    }

    def validate_inputs(self) -> None:
        """Validate project parameters."""
        if self.length_m <= 0:
            raise ValueError("Length must be positive")
        if self.height_m <= 0:
            raise ValueError("Height must be positive")
        if self.glass_type not in self.GLASS_PRICES:
            raise ValueError(f"Invalid glass type. Must be one of: {list(self.GLASS_PRICES.keys())}")
        if self.installation_complexity not in self.LABOR_MULTIPLIERS:
            raise ValueError("Invalid complexity. Must be: simple, moderate, or complex")
        if self.region not in self.REGIONAL_MULTIPLIERS:
            raise ValueError("Invalid region. Must be: urban, suburban, or rural")

    def calculate_area(self) -> float:
        """Calculate the total glass area in square meters."""
        return self.length_m * self.height_m

    def calculate_material_cost(self) -> float:
        """Calculate the total material cost."""
        glass_cost = self.calculate_area() * self.GLASS_PRICES[self.glass_type]
        handrail_cost = self.HANDRAIL_COST * self.length_m if self.handrail_included else 0
        return glass_cost + handrail_cost

    def calculate_labor_cost(self) -> float:
        """Calculate the total labor cost."""
        base_cost = self.calculate_area() * self.BASE_LABOR_COST
        complexity_adjusted = base_cost * self.LABOR_MULTIPLIERS[self.installation_complexity]
        return complexity_adjusted * self.REGIONAL_MULTIPLIERS[self.region]

    def calculate_total_cost(self) -> float:
        """Calculate the total project cost."""
        self.validate_inputs()
        return self.calculate_material_cost() + self.calculate_labor_cost()


def get_user_input() -> GlassRailingProject:
    """Collect user input for the project parameters."""
    print("Glass Railing Project Cost Calculator")
    print("------------------------------------")

    try:
        length = float(input("Enter railing length in meters: "))
        height = float(input("Enter railing height in meters: "))
        
        print("\nAvailable glass types:")
        for glass_type in GlassRailingProject.GLASS_PRICES.keys():
            print(f"- {glass_type}")
        glass_type = input("Select glass type: ").lower()
        
        handrail = input("Include handrail? (yes/no): ").lower() == 'yes'
        
        print("\nInstallation complexity options:")
        print("- simple (standard installation)")
        print("- moderate (some obstacles)")
        print("- complex (custom angles, difficult access)")
        complexity = input("Select installation complexity: ").lower()
        
        print("\nRegion options:")
        print("- urban")
        print("- suburban")
        print("- rural")
        region = input("Select region: ").lower()

        return GlassRailingProject(
            length_m=length,
            height_m=height,
            glass_type=glass_type,
            handrail_included=handrail,
            installation_complexity=complexity,
            region=region
        )
    except ValueError as e:
        raise ValueError(f"Invalid input: {str(e)}")


def main():
    """Main function to run the cost calculator."""
    try:
        project = get_user_input()
        total_cost = project.calculate_total_cost()
        
        print("\nProject Cost Breakdown:")
        print(f"Glass Area: {project.calculate_area():.2f} m²")
        print(f"Material Cost: ${project.calculate_material_cost():.2f}")
        print(f"Labor Cost: ${project.calculate_labor_cost():.2f}")
        print(f"Total Project Cost: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
