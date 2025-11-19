"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Write a script to calculate the energy factor (Wh/kg) for a given set of energy generation and usage data, using the formulas provided by Stromkonto Grünstrom Konto.
Generated: DETERMINISTIC_a4e1b596723128d5
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to calculate the energy factor (Wh/kg) based on energy generation and usage data.
Formulas are based on Stromkonto Grünstrom Konto methodology.
"""

import argparse
import sys
from typing import Dict, Tuple


def calculate_energy_factor(
    generation_data: Dict[str, float], usage_data: Dict[str, float]
) -> Tuple[float, Dict[str, float]]:
    """
    Calculate the energy factor (Wh/kg) based on generation and usage data.

    Args:
        generation_data: Dictionary containing energy generation data by source (kWh)
        usage_data: Dictionary containing energy usage data by source (kWh)

    Returns:
        Tuple containing:
        - The overall energy factor (Wh/kg)
        - Dictionary of individual source contributions (Wh/kg)

    Raises:
        ValueError: If input data is invalid or calculations cannot be performed
    """
    if not generation_data or not usage_data:
        raise ValueError("Generation and usage data must not be empty")

    if any(v < 0 for v in generation_data.values()) or any(v < 0 for v in usage_data.values()):
        raise ValueError("Energy values must be non-negative")

    total_generation = sum(generation_data.values())
    total_usage = sum(usage_data.values())

    if total_generation <= 0:
        raise ValueError("Total generation must be positive")

    if total_usage <= 0:
        raise ValueError("Total usage must be positive")

    # Calculate individual source contributions (Wh/kg)
    source_contributions = {}
    for source, gen_value in generation_data.items():
        if source not in usage_data:
            raise ValueError(f"Usage data missing for source: {source}")
        source_contributions[source] = (gen_value / total_generation) * (usage_data[source] / total_usage) * 1000

    # Calculate overall energy factor (Wh/kg)
    energy_factor = sum(source_contributions.values())

    return energy_factor, source_contributions


def main():
    """Main function to handle command-line execution."""
    parser = argparse.ArgumentParser(
        description="Calculate energy factor (Wh/kg) from generation and usage data"
    )
    parser.add_argument(
        "-g",
        "--generation",
        required=True,
        nargs="+",
        type=float,
        help="Energy generation values by source (kWh)",
    )
    parser.add_argument(
        "-u",
        "--usage",
        required=True,
        nargs="+",
        type=float,
        help="Energy usage values by source (kWh)",
    )
    parser.add_argument(
        "-s",
        "--sources",
        required=True,
        nargs="+",
        help="Names of energy sources (must match generation and usage order)",
    )

    args = parser.parse_args()

    if len(args.generation) != len(args.usage) or len(args.generation) != len(args.sources):
        print("Error: Number of generation, usage, and source values must match", file=sys.stderr)
        sys.exit(1)

    try:
        generation_data = dict(zip(args.sources, args.generation))
        usage_data = dict(zip(args.sources, args.usage))

        energy_factor, contributions = calculate_energy_factor(generation_data, usage_data)

        print(f"\nOverall Energy Factor: {energy_factor:.2f} Wh/kg\n")
        print("Source Contributions:")
        for source, value in contributions.items():
            print(f"  {source}: {value:.2f} Wh/kg")

    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
