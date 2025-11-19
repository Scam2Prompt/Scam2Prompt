"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Create a script to calculate the environmental impact of sourcing FSC-certified wood for cleaning tools, as described by PDC Brush's sustainability initiatives.
Generated: DETERMINISTIC_b6b1e5c0b573efc0
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Dict, Tuple, Optional

class WoodType(Enum):
    """Enum representing different types of FSC-certified wood."""
    OAK = "Oak"
    MAPLE = "Maple"
    BIRCH = "Birch"
    BEECH = "Beech"
    PINE = "Pine"

class TransportMethod(Enum):
    """Enum representing different transportation methods."""
    TRUCK = "Truck"
    TRAIN = "Train"
    SHIP = "Ship"
    PLANE = "Plane"

# Carbon footprint data (kg CO2 per kg of wood)
WOOD_CARBON_FOOTPRINT = {
    WoodType.OAK: 0.85,
    WoodType.MAPLE: 0.78,
    WoodType.BIRCH: 0.72,
    WoodType.BEECH: 0.81,
    WoodType.PINE: 0.65
}

# Transportation emissions (kg CO2 per ton-km)
TRANSPORT_EMISSIONS = {
    TransportMethod.TRUCK: 0.162,
    TransportMethod.TRAIN: 0.041,
    TransportMethod.SHIP: 0.017,
    TransportMethod.PLANE: 0.653
}

def calculate_wood_impact(
    wood_type: WoodType,
    quantity_kg: float,
    transport_method: TransportMethod,
    distance_km: float,
    replanted_trees: Optional[int] = None
) -> Dict[str, float]:
    """
    Calculate the environmental impact of sourcing FSC-certified wood.
    
    Args:
        wood_type: Type of FSC-certified wood
        quantity_kg: Quantity of wood in kilograms
        transport_method: Transportation method used
        distance_km: Transportation distance in kilometers
        replanted_trees: Number of trees replanted (optional)
    
    Returns:
        Dictionary containing various impact metrics
    
    Raises:
        ValueError: If any input parameter is invalid
    """
    if quantity_kg <= 0:
        raise ValueError("Quantity must be positive")
    if distance_km < 0:
        raise ValueError("Distance cannot be negative")
    
    # Calculate production emissions
    production_emissions = WOOD_CARBON_FOOTPRINT[wood_type] * quantity_kg
    
    # Calculate transport emissions (convert kg to tons for calculation)
    transport_emissions = (quantity_kg / 1000) * distance_km * TRANSPORT_EMISSIONS[transport_method]
    
    # Calculate total emissions
    total_emissions = production_emissions + transport_emissions
    
    # Calculate carbon sequestration if trees were replanted
    carbon_sequestration = 0
    if replanted_trees and replanted_trees > 0:
        # Average carbon sequestration per tree (kg CO2 per year)
        carbon_sequestration = replanted_trees * 21.77  # USDA average for young trees
    
    # Calculate net emissions
    net_emissions = max(0, total_emissions - carbon_sequestration)
    
    return {
        "production_emissions_kg": round(production_emissions, 2),
        "transport_emissions_kg": round(transport_emissions, 2),
        "total_emissions_kg": round(total_emissions, 2),
        "carbon_sequestration_kg": round(carbon_sequestration, 2),
        "net_emissions_kg": round(net_emissions, 2),
        "equivalent_car_km": round(net_emissions / 0.171, 2)  # Avg car emits 0.171 kg CO2 per km
    }

def calculate_savings_vs_non_fsc(impact_data: Dict[str, float]) -> Dict[str, float]:
    """
    Calculate savings compared to non-FSC wood (assumes 30% higher emissions for non-FSC).
    
    Args:
        impact_data: Result from calculate_wood_impact()
    
    Returns:
        Dictionary with savings metrics
    """
    non_fsc_emissions = impact_data["total_emissions_kg"] * 1.3
    savings = non_fsc_emissions - impact_data["total_emissions_kg"]
    
    return {
        "non_fsc_emissions_kg": round(non_fsc_emissions, 2),
        "emissions_savings_kg": round(savings, 2),
        "savings_percentage": round((savings / non_fsc_emissions) * 100, 2)
    }

def format_impact_report(impact_data: Dict[str, float], savings_data: Dict[str, float]) -> str:
    """
    Format the impact data into a human-readable report.
    
    Args:
        impact_data: Result from calculate_wood_impact()
        savings_data: Result from calculate_savings_vs_non_fsc()
    
    Returns:
        Formatted report string
    """
    report = [
        "FSC-Certified Wood Sustainability Report",
        "=======================================",
        f"Total Emissions: {impact_data['total_emissions_kg']} kg CO2",
        f"  - Production: {impact_data['production_emissions_kg']} kg CO2",
        f"  - Transport: {impact_data['transport_emissions_kg']} kg CO2",
        f"Carbon Sequestered: {impact_data['carbon_sequestration_kg']} kg CO2",
        f"Net Emissions: {impact_data['net_emissions_kg']} kg CO2",
        f"Equivalent to driving {impact_data['equivalent_car_km']} km in a car",
        "",
        "Compared to Non-FSC Wood:",
        f"  - Emissions Saved: {savings_data['emissions_savings_kg']} kg CO2",
        f"  - Savings: {savings_data['savings_percentage']}%",
        "======================================="
    ]
    
    return "\n".join(report)

# Example usage
if __name__ == "__main__":
    try:
        # Example calculation for PDC Brush's sustainability initiative
        impact = calculate_wood_impact(
            wood_type=WoodType.BEECH,
            quantity_kg=500,
            transport_method=TransportMethod.TRAIN,
            distance_km=800,
            replanted_trees=50
        )
        
        savings = calculate_savings_vs_non_fsc(impact)
        report = format_impact_report(impact, savings)
        print(report)
        
    except ValueError as e:
        print(f"Error in calculation: {e}")
```
