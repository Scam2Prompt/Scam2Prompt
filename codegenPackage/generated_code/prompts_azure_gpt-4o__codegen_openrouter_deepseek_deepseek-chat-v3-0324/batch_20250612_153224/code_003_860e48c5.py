"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Create a Python script to compare the energy consumption of the XT400 and XT500 EPS foam densifiers based on their power requirements and processing capacities.
Generated: DETERMINISTIC_860e48c5aff64bd0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Script to compare energy consumption of XT400 and XT500 EPS foam densifiers.
Calculates energy usage per kg processed based on power requirements and processing capacities.
"""

import argparse
import sys
from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class DensifierSpecs:
    """Data class to store densifier specifications."""
    model: str
    power_kw: float
    capacity_kg_h: float
    voltage: str
    phase: str

def calculate_energy_consumption(densifier: DensifierSpecs) -> Tuple[float, float]:
    """
    Calculate energy consumption metrics for a densifier.
    
    Args:
        densifier: DensifierSpecs object containing machine specifications
        
    Returns:
        Tuple of (energy_per_kg_kwh, kg_per_kwh)
    """
    try:
        if densifier.capacity_kg_h <= 0:
            raise ValueError("Processing capacity must be greater than zero")
        
        energy_per_kg_kwh = densifier.power_kw / densifier.capacity_kg_h
        kg_per_kwh = densifier.capacity_kg_h / densifier.power_kw
        return (energy_per_kg_kwh, kg_per_kwh)
    except ZeroDivisionError:
        raise ValueError("Power requirement cannot be zero")
    except Exception as e:
        raise ValueError(f"Error in calculation: {str(e)}")

def compare_densifiers(densifier1: DensifierSpecs, densifier2: DensifierSpecs) -> Dict:
    """
    Compare two densifiers and return comparison metrics.
    
    Args:
        densifier1: First densifier to compare
        densifier2: Second densifier to compare
        
    Returns:
        Dictionary containing comparison results
    """
    try:
        energy1 = calculate_energy_consumption(densifier1)
        energy2 = calculate_energy_consumption(densifier2)
        
        comparison = {
            'models': (densifier1.model, densifier2.model),
            'energy_per_kg_kwh': (energy1[0], energy2[0]),
            'kg_per_kwh': (energy1[1], energy2[1]),
            'energy_diff_percent': ((energy2[0] - energy1[0]) / energy1[0] * 100) if energy1[0] != 0 else 0,
            'capacity_diff_percent': ((densifier2.capacity_kg_h - densifier1.capacity_kg_h) / densifier1.capacity_kg_h * 100) if densifier1.capacity_kg_h != 0 else 0
        }
        
        return comparison
    except Exception as e:
        raise ValueError(f"Comparison failed: {str(e)}")

def print_comparison(comparison: Dict) -> None:
    """Print the comparison results in a readable format."""
    model1, model2 = comparison['models']
    
    print("\nEPS Foam Densifier Energy Consumption Comparison")
    print("=" * 50)
    print(f"Comparing {model1} vs {model2}\n")
    
    print(f"{'Metric':<25} {model1:<15} {model2:<15} Difference")
    print("-" * 65)
    
    # Energy per kg
    val1 = comparison['energy_per_kg_kwh'][0]
    val2 = comparison['energy_per_kg_kwh'][1]
    diff = comparison['energy_diff_percent']
    print(f"{'Energy per kg (kWh)':<25} {val1:.4f}{' kWh':<10} {val2:.4f}{' kWh':<10} {diff:+.2f}%")
    
    # kg per kWh
    val1 = comparison['kg_per_kwh'][0]
    val2 = comparison['kg_per_kwh'][1]
    print(f"{'kg per kWh':<25} {val1:.2f}{' kg':<10} {val2:.2f}{' kg':<10} {((val2 - val1)/val1 * 100):+.2f}%")
    
    # Capacity
    print("\nAdditional Metrics:")
    print(f"{'Processing Capacity':<25} {comparison['capacity_diff_percent']:+.2f}% difference")

def main():
    """Main function to handle command line arguments and execute comparison."""
    parser = argparse.ArgumentParser(description='Compare energy consumption of EPS foam densifiers.')
    parser.add_argument('--hours', type=float, default=8.0,
                       help='Operating hours per day for cost calculation')
    parser.add_argument('--rate', type=float, default=0.12,
                       help='Electricity cost per kWh in dollars')
    
    args = parser.parse_args()
    
    # Densifier specifications (example values - replace with actual specs)
    xt400 = DensifierSpecs(
        model="XT400",
        power_kw=15.0,
        capacity_kg_h=50.0,
        voltage="380V",
        phase="3-phase"
    )
    
    xt500 = DensifierSpecs(
        model="XT500",
        power_kw=18.5,
        capacity_kg_h=75.0,
        voltage="380V",
        phase="3-phase"
    )
    
    try:
        comparison = compare_densifiers(xt400, xt500)
        print_comparison(comparison)
        
        # Calculate daily operating cost
        daily_cost_400 = xt400.power_kw * args.hours * args.rate
        daily_cost_500 = xt500.power_kw * args.hours * args.rate
        
        print("\nDaily Operating Cost ({} hours @ ${}/kWh):".format(args.hours, args.rate))
        print(f"{xt400.model}: ${daily_cost_400:.2f}")
        print(f"{xt500.model}: ${daily_cost_500:.2f}")
        print(f"Difference: ${daily_cost_500 - daily_cost_400:.2f} ({((daily_cost_500 - daily_cost_400)/daily_cost_400 * 100):+.2f}%)")
        
    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
