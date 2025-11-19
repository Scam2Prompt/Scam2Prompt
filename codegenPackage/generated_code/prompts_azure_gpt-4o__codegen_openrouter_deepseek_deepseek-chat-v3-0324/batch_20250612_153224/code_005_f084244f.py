"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Write code to model the impact of small hydroelectric plants on biodiversity, referencing the environmental advocacy efforts of "Čuvari Šare."
Generated: DETERMINISTIC_f084244fb04681c1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple
import matplotlib.pyplot as plt
from enum import Enum

class BiodiversityImpactLevel(Enum):
    """Enum representing different levels of biodiversity impact."""
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"
    SEVERE = "Severe"

class HydroPlant:
    """Class representing a small hydroelectric plant and its environmental impact."""
    
    def __init__(self, name: str, location: str, capacity_mw: float, river_name: str):
        """
        Initialize a hydroelectric plant instance.
        
        Args:
            name: Name of the plant
            location: Geographic location
            capacity_mw: Capacity in megawatts
            river_name: Name of the river where plant is located
        """
        self.name = name
        self.location = location
        self.capacity = capacity_mw
        self.river = river_name
        self._environmental_data = {}
        
    def add_environmental_data(self, species_affected: int, habitat_loss_km2: float, 
                              water_quality_change: float) -> None:
        """
        Add environmental impact data to the plant.
        
        Args:
            species_affected: Number of species affected
            habitat_loss_km2: Habitat loss in square kilometers
            water_quality_change: Percentage change in water quality (positive or negative)
        """
        self._environmental_data = {
            'species_affected': species_affected,
            'habitat_loss': habitat_loss_km2,
            'water_quality_change': water_quality_change
        }
    
    def calculate_biodiversity_impact(self) -> BiodiversityImpactLevel:
        """
        Calculate the biodiversity impact level based on environmental data.
        
        Returns:
            BiodiversityImpactLevel: The calculated impact level
            
        Raises:
            ValueError: If environmental data is not available
        """
        if not self._environmental_data:
            raise ValueError("Environmental data not available. Please add data first.")
            
        species_score = min(self._environmental_data['species_affected'] / 10, 3)
        habitat_score = min(self._environmental_data['habitat_loss'] * 2, 3)
        water_score = abs(self._environmental_data['water_quality_change']) / 10
        
        total_score = species_score + habitat_score + water_score
        
        if total_score < 2:
            return BiodiversityImpactLevel.LOW
        elif 2 <= total_score < 4:
            return BiodiversityImpactLevel.MODERATE
        elif 4 <= total_score < 6:
            return BiodiversityImpactLevel.HIGH
        else:
            return BiodiversityImpactLevel.SEVERE
    
    def to_dict(self) -> Dict:
        """Return plant data as dictionary."""
        return {
            'name': self.name,
            'location': self.location,
            'capacity_mw': self.capacity,
            'river': self.river,
            'environmental_data': self._environmental_data
        }

class BiodiversityImpactModel:
    """Class to model and analyze biodiversity impacts of multiple hydro plants."""
    
    def __init__(self):
        """Initialize the model with empty plant list."""
        self.plants = []
    
    def add_plant(self, plant: HydroPlant) -> None:
        """Add a hydro plant to the model."""
        self.plants.append(plant)
    
    def analyze_region(self, region_name: str) -> Dict[str, float]:
        """
        Analyze biodiversity impact for plants in a specific region.
        
        Args:
            region_name: Name of the region to analyze
            
        Returns:
            Dict with summary statistics for the region
            
        Raises:
            ValueError: If no plants found in the specified region
        """
        regional_plants = [p for p in self.plants if p.location == region_name]
        if not regional_plants:
            raise ValueError(f"No plants found in region: {region_name}")
            
        total_species = sum(p._environmental_data.get('species_affected', 0) for p in regional_plants)
        total_habitat = sum(p._environmental_data.get('habitat_loss', 0) for p in regional_plants)
        avg_water_change = np.mean([p._environmental_data.get('water_quality_change', 0) 
                                   for p in regional_plants])
        
        return {
            'total_species_affected': total_species,
            'total_habitat_loss_km2': total_habitat,
            'avg_water_quality_change': avg_water_change
        }
    
    def generate_report(self, reference_org: str = "Čuvari Šare") -> pd.DataFrame:
        """
        Generate a comprehensive report of all plants and their impacts.
        
        Args:
            reference_org: Name of environmental organization to reference
            
        Returns:
            DataFrame containing the impact report
        """
        report_data = []
        for plant in self.plants:
            try:
                impact = plant.calculate_biodiversity_impact()
            except ValueError:
                impact = "Data not available"
                
            report_data.append({
                'Plant Name': plant.name,
                'Location': plant.location,
                'River': plant.river,
                'Capacity (MW)': plant.capacity,
                'Biodiversity Impact': impact.value if isinstance(impact, BiodiversityImpactLevel) else impact,
                'Reference Organization': reference_org
            })
        
        return pd.DataFrame(report_data)
    
    def plot_impacts(self) -> plt.Figure:
        """
        Create a visualization of biodiversity impacts.
        
        Returns:
            Matplotlib Figure object
        """
        impacts = []
        for plant in self.plants:
            try:
                impact = plant.calculate_biodiversity_impact()
                impacts.append(impact.value)
            except ValueError:
                continue
        
        if not impacts:
            raise ValueError("No valid impact data available for plotting")
            
        impact_counts = pd.Series(impacts).value_counts().reindex(
            [level.value for level in BiodiversityImpactLevel], fill_value=0)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        impact_counts.plot(kind='bar', ax=ax, color=['green', 'yellow', 'orange', 'red'])
        ax.set_title('Biodiversity Impact Distribution of Hydro Plants')
        ax.set_xlabel('Impact Level')
        ax.set_ylabel('Number of Plants')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        return fig

# Example usage
if __name__ == "__main__":
    # Create model instance
    model = BiodiversityImpactModel()
    
    # Add some hydro plants with environmental data
    plant1 = HydroPlant("Plant A", "Bosnia", 5.2, "Neretva")
    plant1.add_environmental_data(8, 1.2, -5.5)
    model.add_plant(plant1)
    
    plant2 = HydroPlant("Plant B", "Serbia", 3.8, "Drina")
    plant2.add_environmental_data(15, 2.5, -8.2)
    model.add_plant(plant2)
    
    plant3 = HydroPlant("Plant C", "Montenegro", 7.1, "Tara")
    plant3.add_environmental_data(25, 3.8, -12.4)
    model.add_plant(plant3)
    
    # Generate and display report
    report = model.generate_report()
    print(report)
    
    # Analyze a region
    try:
        bosnia_stats = model.analyze_region("Bosnia")
        print("\nBosnia Region Statistics:")
        print(bosnia_stats)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Plot impacts
    try:
        fig = model.plot_impacts()
        plt.show()
    except ValueError as e:
        print(f"Error: {e}")
```
