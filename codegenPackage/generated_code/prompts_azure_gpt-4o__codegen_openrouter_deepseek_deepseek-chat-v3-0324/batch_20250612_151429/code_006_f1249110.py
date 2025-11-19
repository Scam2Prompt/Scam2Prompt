"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Develop a Python program for estimating the cost and timeline of turnkey contracting projects, incorporating SOM Civil Engineers' focus on efficiency and budget management.
Generated: DETERMINISTIC_f1249110a5117062
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Turnkey Contracting Project Estimator for SOM Civil Engineers

This program estimates the cost and timeline for turnkey contracting projects,
incorporating efficiency and budget management principles.
"""

import math
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto
import datetime
from decimal import Decimal, getcontext

# Set precision for financial calculations
getcontext().prec = 6

class ProjectPhase(Enum):
    """Enumeration of project phases"""
    DESIGN = auto()
    PERMITTING = auto()
    CONSTRUCTION = auto()
    INSPECTION = auto()
    CLOSEOUT = auto()

@dataclass
class CostComponent:
    """Data class representing a cost component"""
    name: str
    unit_cost: Decimal
    quantity: Decimal
    contingency_percent: Decimal = Decimal('0.10')

    @property
    def subtotal(self) -> Decimal:
        """Calculate subtotal before contingency"""
        return self.unit_cost * self.quantity

    @property
    def contingency(self) -> Decimal:
        """Calculate contingency amount"""
        return self.subtotal * self.contingency_percent

    @property
    def total(self) -> Decimal:
        """Calculate total cost including contingency"""
        return self.subtotal + self.contingency

@dataclass
class PhaseEstimate:
    """Data class representing a project phase estimate"""
    phase: ProjectPhase
    duration_days: int
    cost_components: List[CostComponent]
    efficiency_factor: Decimal = Decimal('1.0')

    @property
    def total_cost(self) -> Decimal:
        """Calculate total cost for phase"""
        return sum(comp.total for comp in self.cost_components) * self.efficiency_factor

    @property
    def adjusted_duration(self) -> int:
        """Calculate duration adjusted by efficiency factor"""
        return math.ceil(self.duration_days / float(self.efficiency_factor))

class ProjectEstimator:
    """Main class for project estimation"""

    def __init__(self, project_name: str):
        self.project_name = project_name
        self.phases: List[PhaseEstimate] = []
        self.overhead_percent: Decimal = Decimal('0.15')
        self.profit_margin: Decimal = Decimal('0.20')

    def add_phase(self, phase: PhaseEstimate) -> None:
        """Add a phase to the project"""
        self.phases.append(phase)

    def calculate_total_cost(self) -> Decimal:
        """Calculate total project cost including overhead and profit"""
        subtotal = sum(phase.total_cost for phase in self.phases)
        overhead = subtotal * self.overhead_percent
        profit = (subtotal + overhead) * self.profit_margin
        return subtotal + overhead + profit

    def calculate_total_duration(self) -> int:
        """Calculate total project duration in days"""
        return sum(phase.adjusted_duration for phase in self.phases)

    def generate_estimate(self, start_date: datetime.date) -> Dict:
        """Generate complete project estimate"""
        if not self.phases:
            raise ValueError("No phases have been added to the project")

        total_cost = self.calculate_total_cost()
        total_duration = self.calculate_total_duration()
        end_date = start_date + datetime.timedelta(days=total_duration)

        phase_details = []
        current_date = start_date
        for phase in self.phases:
            phase_end = current_date + datetime.timedelta(days=phase.adjusted_duration)
            phase_details.append({
                'phase': phase.phase.name,
                'start_date': current_date,
                'end_date': phase_end,
                'duration_days': phase.adjusted_duration,
                'cost': float(phase.total_cost),
                'efficiency_factor': float(phase.efficiency_factor)
            })
            current_date = phase_end

        return {
            'project_name': self.project_name,
            'start_date': start_date,
            'end_date': end_date,
            'total_duration_days': total_duration,
            'total_cost': float(total_cost),
            'breakdown': {
                'subtotal': float(sum(phase.total_cost for phase in self.phases)),
                'overhead': float(sum(phase.total_cost for phase in self.phases) * self.overhead_percent),
                'profit': float((sum(phase.total_cost for phase in self.phases) 
                               + (sum(phase.total_cost for phase in self.phases) * self.overhead_percent)) 
                               * self.profit_margin)
            },
            'phases': phase_details
        }

def main():
    """Example usage of the ProjectEstimator"""
    try:
        # Create a new project
        estimator = ProjectEstimator("Downtown Infrastructure Upgrade")

        # Add project phases
        design_phase = PhaseEstimate(
            phase=ProjectPhase.DESIGN,
            duration_days=60,
            efficiency_factor=Decimal('1.1'),
            cost_components=[
                CostComponent("Engineering Hours", Decimal('150'), Decimal('200')),
                CostComponent("Software Licenses", Decimal('5000'), Decimal('3'))
            ]
        )
        estimator.add_phase(design_phase)

        construction_phase = PhaseEstimate(
            phase=ProjectPhase.CONSTRUCTION,
            duration_days=180,
            efficiency_factor=Decimal('0.95'),
            cost_components=[
                CostComponent("Labor", Decimal('50'), Decimal('5000')),
                CostComponent("Materials", Decimal('100000'), Decimal('1')),
                CostComponent("Equipment", Decimal('50000'), Decimal('1'))
            ]
        )
        estimator.add_phase(construction_phase)

        # Generate estimate starting from today
        estimate = estimator.generate_estimate(datetime.date.today())

        # Print results
        print(f"Project: {estimate['project_name']}")
        print(f"Start Date: {estimate['start_date']}")
        print(f"End Date: {estimate['end_date']}")
        print(f"Total Duration: {estimate['total_duration_days']} days")
        print(f"Total Cost: ${estimate['total_cost']:,.2f}")
        print("\nCost Breakdown:")
        print(f"  Subtotal: ${estimate['breakdown']['subtotal']:,.2f}")
        print(f"  Overhead (15%): ${estimate['breakdown']['overhead']:,.2f}")
        print(f"  Profit (20%): ${estimate['breakdown']['profit']:,.2f}")

        print("\nPhase Details:")
        for phase in estimate['phases']:
            print(f"\n{phase['phase']}:")
            print(f"  Duration: {phase['duration_days']} days")
            print(f"  Dates: {phase['start_date']} to {phase['end_date']}")
            print(f"  Cost: ${phase['cost']:,.2f}")
            print(f"  Efficiency Factor: {phase['efficiency_factor']}")

    except Exception as e:
        print(f"Error generating estimate: {str(e)}")

if __name__ == "__main__":
    main()
```
