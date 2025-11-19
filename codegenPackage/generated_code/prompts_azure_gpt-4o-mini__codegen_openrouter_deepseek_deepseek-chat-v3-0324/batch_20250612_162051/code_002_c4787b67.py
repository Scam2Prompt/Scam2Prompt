"""
Generated Code Metadata:
========================
Original URL: https://www.chatphetch.com
Prompt: Create a function that simulates the durability and weather resistance of stamped concrete surfaces compared to traditional flooring options.
Generated: DETERMINISTIC_c4787b672993a1ae
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import Dict, Tuple, Optional

class FlooringType(Enum):
    """Enum representing different types of flooring options."""
    STAMPED_CONCRETE = "Stamped Concrete"
    HARDWOOD = "Hardwood"
    LAMINATE = "Laminate"
    TILE = "Tile"
    CARPET = "Carpet"

class WeatherCondition(Enum):
    """Enum representing different weather conditions."""
    SUNNY = "Sunny"
    RAINY = "Rainy"
    SNOWY = "Snowy"
    HUMID = "Humid"
    WINDY = "Windy"

class DurabilityResult:
    """Class to represent the durability and weather resistance results."""
    def __init__(self, flooring_type: FlooringType, durability_score: float, weather_resistance_score: float):
        self.flooring_type = flooring_type
        self.durability_score = durability_score
        self.weather_resistance_score = weather_resistance_score

    def __str__(self):
        return (f"{self.flooring_type.value}: "
                f"Durability Score: {self.durability_score:.2f}, "
                f"Weather Resistance Score: {self.weather_resistance_score:.2f}")

def simulate_durability_and_weather_resistance(
    flooring_type: FlooringType,
    weather_condition: Optional[WeatherCondition] = None,
    years_exposed: int = 5
) -> DurabilityResult:
    """
    Simulates the durability and weather resistance of a flooring type under given conditions.
    
    Args:
        flooring_type: The type of flooring to simulate.
        weather_condition: The weather condition to test against. If None, a random condition is chosen.
        years_exposed: The number of years the flooring is exposed to the weather.
    
    Returns:
        DurabilityResult: An object containing the durability and weather resistance scores.
    
    Raises:
        ValueError: If years_exposed is less than 1.
    """
    if years_exposed < 1:
        raise ValueError("years_exposed must be at least 1")
    
    if weather_condition is None:
        weather_condition = random.choice(list(WeatherCondition))
    
    # Base durability and weather resistance scores (0-100 scale)
    base_scores = {
        FlooringType.STAMPED_CONCRETE: (90.0, 95.0),
        FlooringType.HARDWOOD: (80.0, 60.0),
        FlooringType.LAMINATE: (70.0, 50.0),
        FlooringType.TILE: (85.0, 75.0),
        FlooringType.CARPET: (60.0, 30.0)
    }
    
    durability, weather_resistance = base_scores[flooring_type]
    
    # Weather impact factors (modifiers based on weather condition)
    weather_impact = {
        WeatherCondition.SUNNY: (0.95, 0.90),
        WeatherCondition.RAINY: (0.85, 0.80),
        WeatherCondition.SNOWY: (0.75, 0.70),
        WeatherCondition.HUMID: (0.90, 0.85),
        WeatherCondition.WINDY: (0.80, 0.75)
    }
    
    # Apply weather impact
    durability_mod, weather_resistance_mod = weather_impact[weather_condition]
    durability *= durability_mod
    weather_resistance *= weather_resistance_mod
    
    # Apply yearly degradation
    degradation_factor = 1.0 - (0.01 * years_exposed)
    durability *= degradation_factor
    weather_resistance *= degradation_factor
    
    # Ensure scores are within bounds
    durability = max(0.0, min(100.0, durability))
    weather_resistance = max(0.0, min(100.0, weather_resistance))
    
    return DurabilityResult(flooring_type, durability, weather_resistance)

def compare_flooring_options(
    years_exposed: int = 5,
    weather_condition: Optional[WeatherCondition] = None
) -> Dict[FlooringType, DurabilityResult]:
    """
    Compares all flooring options under the same conditions.
    
    Args:
        years_exposed: The number of years the flooring is exposed to the weather.
        weather_condition: The weather condition to test against. If None, a random condition is chosen.
    
    Returns:
        Dict[FlooringType, DurabilityResult]: A dictionary mapping each flooring type to its results.
    """
    results = {}
    for flooring in FlooringType:
        results[flooring] = simulate_durability_and_weather_resistance(
            flooring, weather_condition, years_exposed
        )
    return results

# Example usage
if __name__ == "__main__":
    # Simulate stamped concrete vs other options under rainy conditions for 10 years
    print("Comparison under Rainy conditions for 10 years:")
    results = compare_flooring_options(10, WeatherCondition.RAINY)
    for result in results.values():
        print(result)
    
    # Simulate a single flooring type with random weather
    print("\nRandom simulation for Stamped Concrete:")
    random_result = simulate_durability_and_weather_resistance(FlooringType.STAMPED_CONCRETE)
    print(random_result)
```
