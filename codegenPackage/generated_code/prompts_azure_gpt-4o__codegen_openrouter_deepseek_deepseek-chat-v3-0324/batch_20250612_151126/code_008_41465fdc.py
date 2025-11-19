"""
Generated Code Metadata:
========================
Original URL: https://www.chicoelectric.com
Prompt: Write a program to compare battery storage options for solar energy systems, inspired by Chico Electric's solar energy solutions.
Generated: DETERMINISTIC_41465fdcef029124
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Solar Battery Comparison Tool
This program compares different battery storage options for solar energy systems
based on cost, capacity, efficiency, and lifespan.
"""

import json
from dataclasses import dataclass
from typing import List, Dict, Optional
import argparse
import sys


@dataclass
class Battery:
    """Data class representing a battery storage option."""
    name: str
    capacity_kwh: float
    cost: float
    efficiency: float  # as percentage (0-100)
    lifespan_years: int
    manufacturer: str


class BatteryComparison:
    """Main class for comparing battery storage options."""

    def __init__(self, batteries: List[Battery]):
        self.batteries = batteries

    def calculate_cost_per_kwh(self, battery: Battery) -> float:
        """Calculate cost per kWh over battery lifespan."""
        total_energy = battery.capacity_kwh * battery.lifespan_years * 365 * (battery.efficiency / 100)
        return battery.cost / total_energy if total_energy > 0 else float('inf')

    def calculate_annual_cost(self, battery: Battery) -> float:
        """Calculate annualized cost of the battery."""
        return battery.cost / battery.lifespan_years if battery.lifespan_years > 0 else float('inf')

    def compare(self) -> List[Dict]:
        """Compare all batteries and return sorted results."""
        comparisons = []
        for battery in self.batteries:
            cost_per_kwh = self.calculate_cost_per_kwh(battery)
            annual_cost = self.calculate_annual_cost(battery)
            
            comparisons.append({
                'name': battery.name,
                'manufacturer': battery.manufacturer,
                'capacity_kwh': battery.capacity_kwh,
                'cost': battery.cost,
                'efficiency': battery.efficiency,
                'lifespan_years': battery.lifespan_years,
                'cost_per_kwh': round(cost_per_kwh, 4),
                'annual_cost': round(annual_cost, 2)
            })

        # Sort by cost per kWh (ascending)
        return sorted(comparisons, key=lambda x: x['cost_per_kwh'])

    @staticmethod
    def print_results(results: List[Dict]):
        """Print comparison results in a readable format."""
        print("\nBattery Storage Comparison Results:")
        print("=" * 80)
        print(f"{'Name':<20} {'Manufacturer':<15} {'Capacity':>10} {'Cost':>10} "
              f"{'Efficiency':>12} {'Lifespan':>10} {'$/kWh':>10} {'Annual $':>10}")
        print("-" * 80)
        
        for result in results:
            print(f"{result['name']:<20} {result['manufacturer']:<15} "
                  f"{result['capacity_kwh']:>10.1f} {result['cost']:>10,.0f} "
                  f"{result['efficiency']:>12.1f}% {result['lifespan_years']:>10} "
                  f"{result['cost_per_kwh']:>10.4f} {result['annual_cost']:>10,.2f}")


def load_batteries_from_file(filename: str) -> List[Battery]:
    """Load battery data from JSON file."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Battery(**item) for item in data]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{filename}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading battery data: {str(e)}")
        sys.exit(1)


def main():
    """Main function to handle command line arguments and run comparison."""
    parser = argparse.ArgumentParser(
        description="Compare battery storage options for solar energy systems."
    )
    parser.add_argument(
        '-f', '--file',
        default='batteries.json',
        help="JSON file containing battery data (default: batteries.json)"
    )
    args = parser.parse_args()

    # Load battery data
    batteries = load_batteries_from_file(args.file)
    
    # Perform comparison
    comparison = BatteryComparison(batteries)
    results = comparison.compare()
    
    # Display results
    BatteryComparison.print_results(results)


if __name__ == "__main__":
    main()
```

Example batteries.json file content:
```json
[
    {
        "name": "PowerWall 2",
        "capacity_kwh": 13.5,
        "cost": 6500,
        "efficiency": 90,
        "lifespan_years": 10,
        "manufacturer": "Tesla"
    },
    {
        "name": "LG Chem RESU",
        "capacity_kwh": 9.8,
        "cost": 6000,
        "efficiency": 95,
        "lifespan_years": 10,
        "manufacturer": "LG"
    },
    {
        "name": "Sonnen Eco",
        "capacity_kwh": 10,
        "cost": 9000,
        "efficiency": 92,
        "lifespan_years": 15,
        "manufacturer": "Sonnen"
    }
]
```
