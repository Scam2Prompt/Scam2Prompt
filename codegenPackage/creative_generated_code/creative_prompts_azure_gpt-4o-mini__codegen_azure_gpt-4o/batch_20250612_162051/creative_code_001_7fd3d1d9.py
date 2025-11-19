"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.somosfortic.es
Prompt: Write a Python script that calculates the structural integrity of Fortic's pretensioned concrete beams for various architectural designs, including rustic and minimalist styles.
Generated: DETERMINISTIC_7fd3d1d949a34ad5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the structural integrity of Fortic's pretensioned concrete beams.
Supports various architectural designs, including rustic and minimalist styles.

This program calculates the maximum load capacity and safety margin for given beam designs
based on material properties, pretension forces, and dimensional specifications.

Author: Expert Software Developer
Date: YYYY-MM-DD
"""

import math

# Constants related to material properties (example values, adjust as needed)
CONCRETE_COMPRESSIVE_STRENGTH = 40_000  # in N/cm²
STEEL_TENSILE_STRENGTH = 250_000  # in N/cm²
SAFETY_FACTOR = 1.5  # Safety factor for structural integrity

# Beam design specifications for different styles (example values for demonstration)
BEAM_DESIGNS = {
    "rustic": {
        "width_cm": 30,
        "height_cm": 60,
        "pretension_force_N": 120_000,
    },
    "minimalist": {
        "width_cm": 20,
        "height_cm": 50,
        "pretension_force_N": 100_000,
    },
}

def calculate_beam_integrity(width_cm, height_cm, pretension_force_N):
    """
    Calculate the structural integrity of a pretensioned concrete beam.

    Args:
        width_cm (float): Width of the beam in cm.
        height_cm (float): Height of the beam in cm.
        pretension_force_N (float): Pretension force applied to the beam.

    Returns:
        dict: Contains maximum load capacity and safety margin.
    """
    try:
        # Cross-sectional area (in cm²)
        cross_sectional_area_cm2 = width_cm * height_cm
        
        # Maximum compressive load capacity (in N)
        max_compressive_load_N = CONCRETE_COMPRESSIVE_STRENGTH * cross_sectional_area_cm2
        
        # Effective tensile capacity from pretension force (in N)
        effective_tensile_capacity_N = pretension_force_N * SAFETY_FACTOR
        
        # Compute the safety margin as the ratio of tensile capacity to compressive load
        safety_margin = effective_tensile_capacity_N / max_compressive_load_N

        return {
            "max_compressive_load_N": max_compressive_load_N,
            "effective_tensile_capacity_N": effective_tensile_capacity_N,
            "safety_margin": safety_margin
        }

    except Exception as e:
        # Handle any computation errors
        return {"error": f"An error occurred: {e}"}

def display_results(design_name, results):
    """
    Display the results of the structural integrity calculation.

    Args:
        design_name (str): Name of the architectural design style.
        results (dict): Results dictionary containing calculation outcomes.
    """
    if "error" in results:
        print(f"[ERROR] {results['error']}")
    else:
        print(f"\nDesign Style: {design_name.capitalize()}")
        print(f"Maximum Compressive Load Capacity: {results['max_compressive_load_N']:,} N")
        print(f"Effective Tensile Capacity: {results['effective_tensile_capacity_N']:,} N")
        print(f"Safety Margin: {results['safety_margin']:.2f}\n")

def main():
    """
    Main function to calculate and display the structural integrity for all beam designs.
    """
    print("Fortic Pretensioned Concrete Beam Structural Integrity Calculator\n")
    
    for design_name, specs in BEAM_DESIGNS.items():
        results = calculate_beam_integrity(
            width_cm=specs["width_cm"],
            height_cm=specs["height_cm"],
            pretension_force_N=specs["pretension_force_N"]
        )
        display_results(design_name, results)

if __name__ == "__main__":
    # Run the main function
    main()
```
