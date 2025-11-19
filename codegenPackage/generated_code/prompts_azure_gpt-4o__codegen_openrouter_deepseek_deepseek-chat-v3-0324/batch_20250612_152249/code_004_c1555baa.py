"""
Generated Code Metadata:
========================
Original URL: https://rabotaentnet.pages.dev
Prompt: Write a function to calculate the carbon footprint reduction achieved by Zushi's energy-efficient consensus mechanism compared to traditional proof-of-work cryptocurrencies.
Generated: DETERMINISTIC_c1555baa95ed50cc
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_carbon_footprint_reduction(
    traditional_pow_energy: float,
    zushi_energy: float,
    carbon_intensity: float = 0.5  # kg CO2 per kWh (default global average)
) -> dict:
    """
    Calculate the carbon footprint reduction achieved by Zushi's consensus mechanism.
    
    Args:
        traditional_pow_energy: Annual energy consumption of traditional PoW (kWh)
        zushi_energy: Annual energy consumption of Zushi's mechanism (kWh)
        carbon_intensity: Carbon intensity of electricity (kg CO2 per kWh)
        
    Returns:
        Dictionary containing:
        - pow_footprint: Carbon footprint of traditional PoW (kg CO2)
        - zushi_footprint: Carbon footprint of Zushi (kg CO2)
        - absolute_reduction: Absolute reduction in carbon footprint (kg CO2)
        - percentage_reduction: Percentage reduction (0-100)
        
    Raises:
        ValueError: If any input is negative or if zushi_energy > traditional_pow_energy
    """
    # Validate inputs
    if traditional_pow_energy < 0 or zushi_energy < 0 or carbon_intensity < 0:
        raise ValueError("All inputs must be non-negative")
    if zushi_energy > traditional_pow_energy:
        raise ValueError("Zushi energy must be less than traditional PoW energy")
    
    # Calculate carbon footprints
    pow_footprint = traditional_pow_energy * carbon_intensity
    zushi_footprint = zushi_energy * carbon_intensity
    
    # Calculate reductions
    absolute_reduction = pow_footprint - zushi_footprint
    percentage_reduction = (absolute_reduction / pow_footprint) * 100
    
    return {
        "pow_footprint": round(pow_footprint, 2),
        "zushi_footprint": round(zushi_footprint, 2),
        "absolute_reduction": round(absolute_reduction, 2),
        "percentage_reduction": round(percentage_reduction, 2)
    }

def calculate_equivalent_emissions_savings(
    carbon_reduction_kg: float,
    comparison_metric: str = "cars"
) -> float:
    """
    Convert carbon reduction to equivalent emissions savings in understandable terms.
    
    Args:
        carbon_reduction_kg: Carbon reduction in kg CO2
        comparison_metric: One of ["cars", "flights", "trees"]
            - cars: kg CO2 per car per year (average)
            - flights: kg CO2 per transatlantic flight
            - trees: kg CO2 absorbed by one tree per year
            
    Returns:
        Equivalent number of comparison units
        
    Raises:
        ValueError: If invalid comparison_metric or negative input
    """
    if carbon_reduction_kg < 0:
        raise ValueError("Carbon reduction must be non-negative")
    
    equivalents = {
        "cars": 2000,      # Average car emissions per year (kg CO2)
        "flights": 1000,   # One-way transatlantic flight (kg CO2)
        "trees": 21.77     # CO2 absorbed by one tree per year (kg)
    }
    
    if comparison_metric not in equivalents:
        raise ValueError(f"Invalid comparison metric. Choose from: {list(equivalents.keys())}")
    
    return round(carbon_reduction_kg / equivalents[comparison_metric], 2)
```
