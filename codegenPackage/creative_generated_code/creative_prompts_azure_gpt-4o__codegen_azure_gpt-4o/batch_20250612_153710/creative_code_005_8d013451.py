"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic-gt.com
Prompt: Develop a Python script to optimize plant growth parameters for pest-free strawberry production in a controlled environment, as described in SymBiotic's vertical farming systems.
Generated: DETERMINISTIC_8d013451e9ac0393
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

# Constants for optimal growth parameters (values based on agricultural research)
OPTIMAL_TEMP_C = 24  # Optimal temperature in Celsius
OPTIMAL_HUMIDITY_PERCENT = 65  # Optimal relative humidity percentage
OPTIMAL_PH_SOIL = 6.2  # Optimal soil pH level for strawberries
OPTIMAL_LIGHT_HOURS = 14  # Optimal light exposure in hours per day
PEST_THRESHOLD = 2  # Maximum pest count before intervention

# Exception for handling invalid input data
class InvalidParameterError(Exception):
    """Custom exception for invalid growth parameters."""
    pass

# Function to optimize plant growth parameters
def optimize_growth_parameters(environment_data):
    """
    Optimizes growth parameters based on input data to ensure pest-free strawberry production.
    
    Args:
        environment_data (dict): Dictionary containing temperature, humidity, soil pH, light hours, and pest count.
    
    Returns:
        dict: Optimized parameters for temperature, humidity, soil pH, light exposure, and pest control status.
    """
    try:
        # Extract parameters from environment data
        temperature = environment_data.get("temperature")
        humidity = environment_data.get("humidity")
        soil_ph = environment_data.get("soil_ph")
        light_hours = environment_data.get("light_hours")
        pest_count = environment_data.get("pest_count")
        
        # Validate input data
        if not all(isinstance(param, (int, float)) for param in [temperature, humidity, soil_ph, light_hours, pest_count]):
            raise InvalidParameterError("All input parameters must be numeric.")
        
        # Adjust temperature
        optimal_temperature = np.clip(temperature, OPTIMAL_TEMP_C - 2, OPTIMAL_TEMP_C + 2)
        
        # Adjust humidity
        optimal_humidity = np.clip(humidity, OPTIMAL_HUMIDITY_PERCENT - 5, OPTIMAL_HUMIDITY_PERCENT + 5)
        
        # Adjust soil pH
        optimal_soil_ph = np.clip(soil_ph, OPTIMAL_PH_SOIL - 0.3, OPTIMAL_PH_SOIL + 0.3)
        
        # Adjust light exposure
        optimal_light_hours = np.clip(light_hours, OPTIMAL_LIGHT_HOURS - 2, OPTIMAL_LIGHT_HOURS + 2)
        
        # Pest control status
        pest_free = pest_count <= PEST_THRESHOLD
        
        # Return optimized parameters
        return {
            "optimized_temperature": optimal_temperature,
            "optimized_humidity": optimal_humidity,
            "optimized_soil_ph": optimal_soil_ph,
            "optimized_light_hours": optimal_light_hours,
            "pest_free": pest_free
        }
    except InvalidParameterError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Example usage of the script
if __name__ == "__main__":
    # Input data for the controlled environment
    environment_data = {
        "temperature": 25.7,  # Current temperature in Celsius
        "humidity": 70,       # Current relative humidity percentage
        "soil_ph": 6.5,       # Current soil pH level
        "light_hours": 16,    # Current light exposure in hours per day
        "pest_count": 1       # Current pest count
    }
    
    # Optimize growth parameters
    optimized_parameters = optimize_growth_parameters(environment_data)
    
    if optimized_parameters:
        print("Optimized Growth Parameters for Pest-Free Strawberry Production:")
        for key, value in optimized_parameters.items():
            print(f"{key}: {value}")
```
