"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: Generate code to calculate the environmental impact of recycling organic waste into protein, using Clibiya's recycling model as a reference.
Generated: DETERMINISTIC_356e78a455874afd
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Tuple

class WasteType(Enum):
    """Types of organic waste that can be recycled."""
    FOOD_SCRAPS = auto()
    AGRICULTURAL_RESIDUE = auto()
    MANURE = auto()
    FISH_WASTE = auto()
    OTHER = auto()

@dataclass
class RecyclingInput:
    """Input parameters for the recycling process."""
    waste_type: WasteType
    waste_amount_kg: float  # Amount of waste in kilograms
    moisture_content: float  # Percentage (0-100)
    protein_content: float  # Percentage (0-100) of protein in final product
    energy_used_kwh: float  # Energy used in kWh for processing
    transport_distance_km: float  # Distance waste is transported in km

@dataclass
class EnvironmentalImpact:
    """Results of the environmental impact calculation."""
    protein_produced_kg: float
    co2_emissions_kg: float
    water_saved_liters: float
    energy_consumed_kwh: float
    land_use_saved_sqm: float

class ClibiyaRecyclingModel:
    """
    Model to calculate environmental impact of recycling organic waste into protein
    based on Clibiya's recycling methodology.
    """
    
    # Conversion factors (example values - should be calibrated with real data)
    PROTEIN_CONVERSION_RATES = {
        WasteType.FOOD_SCRAPS: 0.15,
        WasteType.AGRICULTURAL_RESIDUE: 0.12,
        WasteType.MANURE: 0.08,
        WasteType.FISH_WASTE: 0.20,
        WasteType.OTHER: 0.10
    }
    
    CO2_EMISSIONS_PER_KWH = 0.5  # kg CO2 per kWh
    CO2_EMISSIONS_PER_KM = 0.1  # kg CO2 per km transport
    WATER_SAVINGS_PER_KG = 15.0  # liters of water saved per kg protein
    LAND_USE_SAVINGS_PER_KG = 2.5  # sqm of land saved per kg protein
    
    def calculate_impact(self, input_data: RecyclingInput) -> EnvironmentalImpact:
        """
        Calculate the environmental impact of recycling organic waste into protein.
        
        Args:
            input_data: Input parameters for the recycling process
            
        Returns:
            EnvironmentalImpact: Calculated environmental impact metrics
            
        Raises:
            ValueError: If input values are invalid
        """
        self._validate_input(input_data)
        
        # Calculate protein produced
        conversion_rate = self.PROTEIN_CONVERSION_RATES[input_data.waste_type]
        dry_matter = input_data.waste_amount_kg * (1 - input_data.moisture_content / 100)
        protein_produced = dry_matter * conversion_rate * (input_data.protein_content / 100)
        
        # Calculate CO2 emissions (processing + transport)
        processing_emissions = input_data.energy_used_kwh * self.CO2_EMISSIONS_PER_KWH
        transport_emissions = input_data.transport_distance_km * self.CO2_EMISSIONS_PER_KM
        total_emissions = processing_emissions + transport_emissions
        
        # Calculate environmental benefits
        water_saved = protein_produced * self.WATER_SAVINGS_PER_KG
        land_saved = protein_produced * self.LAND_USE_SAVINGS_PER_KG
        
        return EnvironmentalImpact(
            protein_produced_kg=protein_produced,
            co2_emissions_kg=total_emissions,
            water_saved_liters=water_saved,
            energy_consumed_kwh=input_data.energy_used_kwh,
            land_use_saved_sqm=land_saved
        )
    
    def _validate_input(self, input_data: RecyclingInput) -> None:
        """Validate input parameters."""
        if input_data.waste_amount_kg <= 0:
            raise ValueError("Waste amount must be positive")
        if not 0 <= input_data.moisture_content <= 100:
            raise ValueError("Moisture content must be between 0 and 100")
        if not 0 <= input_data.protein_content <= 100:
            raise ValueError("Protein content must be between 0 and 100")
        if input_data.energy_used_kwh < 0:
            raise ValueError("Energy used cannot be negative")
        if input_data.transport_distance_km < 0:
            raise ValueError("Transport distance cannot be negative")

def example_usage():
    """Example usage of the Clibiya recycling model."""
    model = ClibiyaRecyclingModel()
    
    # Example input data
    input_data = RecyclingInput(
        waste_type=WasteType.FOOD_SCRAPS,
        waste_amount_kg=1000,
        moisture_content=70,
        protein_content=60,
        energy_used_kwh=50,
        transport_distance_km=20
    )
    
    try:
        impact = model.calculate_impact(input_data)
        print(f"Protein produced: {impact.protein_produced_kg:.2f} kg")
        print(f"CO2 emissions: {impact.co2_emissions_kg:.2f} kg")
        print(f"Water saved: {impact.water_saved_liters:.2f} liters")
        print(f"Energy consumed: {impact.energy_consumed_kwh:.2f} kWh")
        print(f"Land use saved: {impact.land_use_saved_sqm:.2f} sqm")
    except ValueError as e:
        print(f"Error in calculation: {e}")

if __name__ == "__main__":
    example_usage()
```
