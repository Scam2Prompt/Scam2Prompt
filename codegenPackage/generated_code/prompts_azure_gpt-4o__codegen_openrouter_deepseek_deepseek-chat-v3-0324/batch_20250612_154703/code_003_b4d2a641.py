"""
Generated Code Metadata:
========================
Original URL: https://realorigin.org
Prompt: Create a function in Python to simulate the impact of mold, mildew, and algae on deck deterioration over time, using insights from "How Mold, Mildew, and Algae Affect Your Deck Over Time" on Real and Origin.
Generated: DETERMINISTIC_b4d2a64120af0c3f
Batch ID: 20250612_154703
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

class GrowthType(Enum):
    """Enum representing different types of organic growth affecting a deck."""
    MOLD = "mold"
    MILDEW = "mildew"
    ALGAE = "algae"

class DeckMaterial(Enum):
    """Enum representing different types of deck materials."""
    WOOD = "wood"
    COMPOSITE = "composite"
    PVC = "pvc"

class WeatherCondition(Enum):
    """Enum representing different weather conditions affecting growth."""
    SUNNY = "sunny"
    RAINY = "rainy"
    HUMID = "humid"
    DRY = "dry"

class DeckSimulator:
    """
    Simulates the impact of mold, mildew, and algae on deck deterioration over time.
    
    Attributes:
        material (DeckMaterial): The material of the deck.
        initial_condition (float): Initial condition of the deck (0-100 scale).
        growth_rates (Dict[GrowthType, float]): Base growth rates for each organism.
        weather_impact (Dict[WeatherCondition, Dict[GrowthType, float]]): Weather impact multipliers.
        material_resistance (Dict[DeckMaterial, Dict[GrowthType, float]]): Material resistance factors.
    """
    
    def __init__(self, material: DeckMaterial, initial_condition: float = 100.0):
        """
        Initialize the deck simulator with material and initial condition.
        
        Args:
            material: The material of the deck.
            initial_condition: Initial condition of the deck (0-100). Defaults to 100.
        
        Raises:
            ValueError: If initial_condition is not between 0 and 100.
        """
        if not 0 <= initial_condition <= 100:
            raise ValueError("Initial condition must be between 0 and 100.")
        
        self.material = material
        self.condition = initial_condition
        
        # Base growth rates per day (percentage)
        self.growth_rates = {
            GrowthType.MOLD: 0.5,
            GrowthType.MILDEW: 0.3,
            GrowthType.ALGAE: 0.4
        }
        
        # Weather impact multipliers
        self.weather_impact = {
            WeatherCondition.SUNNY: {
                GrowthType.MOLD: 0.5,
                GrowthType.MILDEW: 0.3,
                GrowthType.ALGAE: 0.8
            },
            WeatherCondition.RAINY: {
                GrowthType.MOLD: 1.5,
                GrowthType.MILDEW: 1.8,
                GrowthType.ALGAE: 1.6
            },
            WeatherCondition.HUMID: {
                GrowthType.MOLD: 2.0,
                GrowthType.MILDEW: 2.2,
                GrowthType.ALGAE: 1.9
            },
            WeatherCondition.DRY: {
                GrowthType.MOLD: 0.2,
                GrowthType.MILDEW: 0.1,
                GrowthType.ALGAE: 0.3
            }
        }
        
        # Material resistance factors (lower is more resistant)
        self.material_resistance = {
            DeckMaterial.WOOD: {
                GrowthType.MOLD: 1.0,
                GrowthType.MILDEW: 1.0,
                GrowthType.ALGAE: 1.0
            },
            DeckMaterial.COMPOSITE: {
                GrowthType.MOLD: 0.7,
                GrowthType.MILDEW: 0.6,
                GrowthType.ALGAE: 0.8
            },
            DeckMaterial.PVC: {
                GrowthType.MOLD: 0.3,
                GrowthType.MILDEW: 0.4,
                GrowthType.ALGAE: 0.5
            }
        }
    
    def calculate_daily_deterioration(
        self,
        weather: WeatherCondition,
        days: int = 1,
        cleaning_interval: Optional[int] = None
    ) -> Tuple[float, Dict[GrowthType, float]]:
        """
        Calculate deck deterioration over a number of days under given weather conditions.
        
        Args:
            weather: Current weather condition.
            days: Number of days to simulate. Defaults to 1.
            cleaning_interval: Days between cleanings. If None, no cleaning is done.
        
        Returns:
            Tuple of (new_condition, growth_amounts) where:
                new_condition: Deck condition after simulation (0-100).
                growth_amounts: Dictionary of growth amounts for each organism.
        
        Raises:
            ValueError: If days is not positive or cleaning_interval is not positive (if provided).
        """
        if days <= 0:
            raise ValueError("Days must be a positive integer.")
        if cleaning_interval is not None and cleaning_interval <= 0:
            raise ValueError("Cleaning interval must be a positive integer.")
        
        total_growth = {gt: 0.0 for gt in GrowthType}
        current_condition = self.condition
        
        for day in range(1, days + 1):
            daily_growth = self._calculate_daily_growth(weather)
            
            # Apply cleaning if it's a cleaning day
            if cleaning_interval is not None and day % cleaning_interval == 0:
                daily_growth = {gt: 0.0 for gt in GrowthType}
            
            # Accumulate growth and update condition
            for gt in GrowthType:
                total_growth[gt] += daily_growth[gt]
                current_condition -= daily_growth[gt] * self.material_resistance[self.material][gt]
            
            # Ensure condition doesn't go below 0
            current_condition = max(0.0, current_condition)
        
        return current_condition, total_growth
    
    def _calculate_daily_growth(self, weather: WeatherCondition) -> Dict[GrowthType, float]:
        """Calculate daily growth amounts for each organism based on weather."""
        return {
            gt: self.growth_rates[gt] * self.weather_impact[weather][gt]
            for gt in GrowthType
        }
    
    def simulate_years(
        self,
        weather_patterns: Dict[WeatherCondition, float],
        years: int = 1,
        cleaning_interval: Optional[int] = None
    ) -> Tuple[float, Dict[GrowthType, float]]:
        """
        Simulate deck deterioration over multiple years with seasonal weather patterns.
        
        Args:
            weather_patterns: Dictionary mapping weather conditions to their yearly proportion (0-1).
            years: Number of years to simulate. Defaults to 1.
            cleaning_interval: Days between cleanings. If None, no cleaning is done.
        
        Returns:
            Tuple of (new_condition, total_growth) after simulation.
        
        Raises:
            ValueError: If years is not positive or weather proportions don't sum to ~1.
        """
        if years <= 0:
            raise ValueError("Years must be a positive integer.")
        
        if not math.isclose(sum(weather_patterns.values()), 1.0, abs_tol=0.01):
            raise ValueError("Weather pattern proportions must sum to approximately 1.")
        
        total_growth = {gt: 0.0 for gt in GrowthType}
        current_condition = self.condition
        
        for _ in range(years):
            # Simulate each weather pattern proportionally over 365 days
            for weather, proportion in weather_patterns.items():
                days = round(proportion * 365)
                if days <= 0:
                    continue
                
                condition, growth = self.calculate_daily_deterioration(
                    weather=weather,
                    days=days,
                    cleaning_interval=cleaning_interval
                )
                
                current_condition = condition
                for gt in GrowthType:
                    total_growth[gt] += growth[gt]
        
        return current_condition, total_growth
```
