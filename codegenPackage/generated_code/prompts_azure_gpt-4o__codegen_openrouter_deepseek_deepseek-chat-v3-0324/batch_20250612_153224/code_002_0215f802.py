"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Generate a script to calculate cost estimates for mechanical installations, factoring in labor, materials, and equipment, as outlined in C&M Pinnacle's service offerings.
Generated: DETERMINISTIC_0215f8025ac85655
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Mechanical Installation Cost Estimator for C&M Pinnacle Services

This script calculates cost estimates for mechanical installations based on:
- Labor costs (hours and rate)
- Material costs (quantity and unit price)
- Equipment costs (rental or purchase)

The script provides a detailed breakdown and total cost estimate.
"""

import sys
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class LaborCost:
    """Represents labor cost components"""
    hours: float
    rate_per_hour: float
    description: str

    def calculate_cost(self) -> float:
        """Calculate total labor cost"""
        if self.hours < 0 or self.rate_per_hour < 0:
            raise ValueError("Hours and rate must be positive values")
        return self.hours * self.rate_per_hour


@dataclass
class MaterialCost:
    """Represents material cost components"""
    quantity: float
    unit_price: float
    description: str

    def calculate_cost(self) -> float:
        """Calculate total material cost"""
        if self.quantity < 0 or self.unit_price < 0:
            raise ValueError("Quantity and unit price must be positive values")
        return self.quantity * self.unit_price


@dataclass
class EquipmentCost:
    """Represents equipment cost components"""
    days_used: float
    daily_rate: float
    description: str
    is_rental: bool = True

    def calculate_cost(self) -> float:
        """Calculate total equipment cost"""
        if self.days_used < 0 or self.daily_rate < 0:
            raise ValueError("Days used and daily rate must be positive values")
        return self.days_used * self.daily_rate


class InstallationCostEstimator:
    """Main class for calculating installation cost estimates"""

    def __init__(self):
        self.labor_costs: List[LaborCost] = []
        self.material_costs: List[MaterialCost] = []
        self.equipment_costs: List[EquipmentCost] = []

    def add_labor_cost(self, labor: LaborCost) -> None:
        """Add a labor cost component"""
        self.labor_costs.append(labor)

    def add_material_cost(self, material: MaterialCost) -> None:
        """Add a material cost component"""
        self.material_costs.append(material)

    def add_equipment_cost(self, equipment: EquipmentCost) -> None:
        """Add an equipment cost component"""
        self.equipment_costs.append(equipment)

    def calculate_total_cost(self) -> float:
        """Calculate the total installation cost"""
        total = 0.0

        try:
            labor_total = sum(l.calculate_cost() for l in self.labor_costs)
            material_total = sum(m.calculate_cost() for m in self.material_costs)
            equipment_total = sum(e.calculate_cost() for e in self.equipment_costs)

            total = labor_total + material_total + equipment_total
        except ValueError as e:
            print(f"Error calculating costs: {e}", file=sys.stderr)
            raise

        return total

    def generate_report(self) -> str:
        """Generate a detailed cost breakdown report"""
        report = []
        report.append("C&M Pinnacle Mechanical Installation Cost Estimate")
        report.append("=" * 50)

        # Labor breakdown
        report.append("\nLabor Costs:")
        report.append("-" * 30)
        for labor in self.labor_costs:
            report.append(f"{labor.description}: {labor.hours} hrs @ ${labor.rate_per_hour}/hr = ${labor.calculate_cost():.2f}")
        labor_total = sum(l.calculate_cost() for l in self.labor_costs)
        report.append(f"\nTotal Labor: ${labor_total:.2f}")

        # Material breakdown
        report.append("\nMaterial Costs:")
        report.append("-" * 30)
        for material in self.material_costs:
            report.append(f"{material.description}: {material.quantity} units @ ${material.unit_price}/unit = ${material.calculate_cost():.2f}")
        material_total = sum(m.calculate_cost() for m in self.material_costs)
        report.append(f"\nTotal Materials: ${material_total:.2f}")

        # Equipment breakdown
        report.append("\nEquipment Costs:")
        report.append("-" * 30)
        for equipment in self.equipment_costs:
            cost_type = "rental" if equipment.is_rental else "purchase"
            report.append(f"{equipment.description}: {equipment.days_used} days {cost_type} @ ${equipment.daily_rate}/day = ${equipment.calculate_cost():.2f}")
        equipment_total = sum(e.calculate_cost() for e in self.equipment_costs)
        report.append(f"\nTotal Equipment: ${equipment_total:.2f}")

        # Final total
        report.append("\n" + "=" * 50)
        report.append(f"TOTAL ESTIMATED COST: ${self.calculate_total_cost():.2f}")
        report.append("=" * 50)

        return "\n".join(report)


def main():
    """Example usage of the cost estimator"""
    try:
        estimator = InstallationCostEstimator()

        # Add labor costs
        estimator.add_labor_cost(LaborCost(
            hours=40,
            rate_per_hour=45.00,
            description="Lead Technician"
        ))
        estimator.add_labor_cost(LaborCost(
            hours=80,
            rate_per_hour=32.50,
            description="Installation Technician"
        ))

        # Add material costs
        estimator.add_material_cost(MaterialCost(
            quantity=150,
            unit_price=12.75,
            description="Steel piping (10ft sections)"
        ))
        estimator.add_material_cost(MaterialCost(
            quantity=50,
            unit_price=8.20,
            description="Copper fittings"
        ))

        # Add equipment costs
        estimator.add_equipment_cost(EquipmentCost(
            days_used=10,
            daily_rate=250.00,
            description="Pipe threading machine",
            is_rental=True
        ))
        estimator.add_equipment_cost(EquipmentCost(
            days_used=15,
            daily_rate=175.00,
            description="Hydraulic lift",
            is_rental=True
        ))

        # Generate and print report
        print(estimator.generate_report())

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
