"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Write a function that calculates the optimal crop selection based on environmental conditions, similar to the gameplay mechanics in Stellar Crop's live ecosystem system.
Generated: DETERMINISTIC_8032744b57957cbb
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict, Optional

class Crop:
    """Represents a crop with its environmental preferences and yield potential."""
    
    def __init__(self, name: str, optimal_temp: float, temp_tolerance: float, 
                 optimal_ph: float, ph_tolerance: float, 
                 optimal_moisture: float, moisture_tolerance: float,
                 base_yield: float):
        """
        Initialize a Crop instance.
        
        Args:
            name: Name of the crop
            optimal_temp: Optimal temperature in Celsius
            temp_tolerance: Temperature tolerance range (+/-)
            optimal_ph: Optimal soil pH
            ph_tolerance: pH tolerance range (+/-)
            optimal_moisture: Optimal soil moisture percentage
            moisture_tolerance: Moisture tolerance range (+/-)
            base_yield: Base yield in kg per hectare under optimal conditions
        """
        self.name = name
        self.optimal_temp = optimal_temp
        self.temp_tolerance = temp_tolerance
        self.optimal_ph = optimal_ph
        self.ph_tolerance = ph_tolerance
        self.optimal_moisture = optimal_moisture
        self.moisture_tolerance = moisture_tolerance
        self.base_yield = base_yield
    
    def calculate_fitness(self, temp: float, ph: float, moisture: float) -> float:
        """
        Calculate how well this crop fits the given environmental conditions.
        
        Args:
            temp: Current temperature in Celsius
            ph: Current soil pH
            moisture: Current soil moisture percentage
            
        Returns:
            Fitness score between 0 (worst) and 1 (best)
        """
        # Calculate temperature fitness (Gaussian curve)
        temp_diff = abs(temp - self.optimal_temp)
        temp_fitness = math.exp(-(temp_diff ** 2) / (2 * (self.temp_tolerance ** 2)))
        
        # Calculate pH fitness (triangular distribution)
        ph_diff = abs(ph - self.optimal_ph)
        ph_fitness = max(0, 1 - (ph_diff / self.ph_tolerance))
        
        # Calculate moisture fitness (triangular distribution)
        moisture_diff = abs(moisture - self.optimal_moisture)
        moisture_fitness = max(0, 1 - (moisture_diff / self.moisture_tolerance))
        
        # Combine factors with equal weight
        overall_fitness = (temp_fitness + ph_fitness + moisture_fitness) / 3
        return overall_fitness
    
    def calculate_expected_yield(self, temp: float, ph: float, moisture: float) -> float:
        """
        Calculate expected yield based on environmental conditions.
        
        Args:
            temp: Current temperature in Celsius
            ph: Current soil pH
            moisture: Current soil moisture percentage
            
        Returns:
            Expected yield in kg per hectare
        """
        fitness = self.calculate_fitness(temp, ph, moisture)
        return self.base_yield * fitness

def get_optimal_crops(crops: List[Crop], temp: float, ph: float, moisture: float, 
                      max_results: Optional[int] = None) -> List[Dict[str, float]]:
    """
    Get optimal crops sorted by expected yield for given environmental conditions.
    
    Args:
        crops: List of available Crop objects
        temp: Current temperature in Celsius
        ph: Current soil pH
        moisture: Current soil moisture percentage
        max_results: Maximum number of results to return (None for all)
        
    Returns:
        List of dictionaries with crop names and expected yields, sorted by yield
    """
    if not crops:
        raise ValueError("Crops list cannot be empty")
    
    if temp < -50 or temp > 60:
        raise ValueError("Temperature out of reasonable range (-50 to 60°C)")
    
    if ph < 0 or ph > 14:
        raise ValueError("pH must be between 0 and 14")
    
    if moisture < 0 or moisture > 100:
        raise ValueError("Moisture must be between 0% and 100%")
    
    # Calculate expected yields for all crops
    crop_yields = []
    for crop in crops:
        try:
            expected_yield = crop.calculate_expected_yield(temp, ph, moisture)
            crop_yields.append({
                'crop': crop.name,
                'expected_yield': expected_yield,
                'fitness': crop.calculate_fitness(temp, ph, moisture)
            })
        except Exception as e:
            print(f"Error calculating yield for {crop.name}: {str(e)}")
            continue
    
    # Sort by expected yield (descending)
    crop_yields.sort(key=lambda x: x['expected_yield'], reverse=True)
    
    # Return top results if max_results specified
    if max_results is not None and max_results > 0:
        return crop_yields[:max_results]
    
    return crop_yields

# Example usage
if __name__ == "__main__":
    # Define some example crops
    crops = [
        Crop("Wheat", 20, 5, 6.5, 1.0, 50, 20, 8000),
        Crop("Corn", 25, 7, 6.0, 1.5, 60, 25, 10000),
        Crop("Rice", 30, 3, 5.5, 0.8, 80, 15, 7000),
        Crop("Potato", 18, 4, 5.0, 1.2, 40, 20, 5000),
        Crop("Tomato", 22, 5, 6.0, 1.0, 70, 15, 12000)
    ]
    
    # Current environmental conditions
    current_temp = 22.5
    current_ph = 6.2
    current_moisture = 55
    
    # Get top 3 optimal crops
    try:
        optimal_crops = get_optimal_crops(crops, current_temp, current_ph, current_moisture, 3)
        print("Top 3 Optimal Crops:")
        for crop in optimal_crops:
            print(f"{crop['crop']}: Expected Yield = {crop['expected_yield']:.2f} kg/ha, Fitness = {crop['fitness']:.2f}")
    except ValueError as e:
        print(f"Error: {str(e)}")
```
