"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: Develop a code example that demonstrates how to calculate the expected yield increase when using the MABFOL gel in a farming simulation model.
Generated: DETERMINISTIC_9a3262d5aeaca727
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FarmingSimulation:
    """
    A class to simulate farming scenarios and calculate yield increases when using MABFOL gel.
    """

    def __init__(self, base_yield, mabfol_efficiency=0.15, max_efficiency=0.30):
        """
        Initialize the farming simulation with base yield and MABFOL parameters.
        
        Args:
            base_yield (float): The base yield per hectare without MABFOL (in tons)
            mabfol_efficiency (float, optional): Expected efficiency increase from MABFOL (default 15%)
            max_efficiency (float, optional): Maximum possible efficiency (default 30%)
        """
        self.base_yield = base_yield
        self.mabfol_efficiency = mabfol_efficiency
        self.max_efficiency = max_efficiency

    def calculate_yield_increase(self, soil_quality_factor=1.0, weather_factor=1.0):
        """
        Calculate the expected yield increase when using MABFOL gel.
        
        Args:
            soil_quality_factor (float): Multiplier for soil quality (0.5-1.5)
            weather_factor (float): Multiplier for weather conditions (0.5-1.5)
            
        Returns:
            tuple: (yield_with_mabfol, yield_increase_percentage)
            
        Raises:
            ValueError: If input factors are outside reasonable ranges
        """
        # Validate input factors
        if not (0.5 <= soil_quality_factor <= 1.5):
            raise ValueError("Soil quality factor must be between 0.5 and 1.5")
        if not (0.5 <= weather_factor <= 1.5):
            raise ValueError("Weather factor must be between 0.5 and 1.5")
        
        # Calculate adjusted efficiency based on environmental factors
        adjusted_efficiency = min(
            self.mabfol_efficiency * soil_quality_factor * weather_factor,
            self.max_efficiency
        )
        
        # Calculate yield with MABFOL
        yield_with_mabfol = self.base_yield * (1 + adjusted_efficiency)
        
        # Calculate percentage increase
        yield_increase_percentage = (yield_with_mabfol - self.base_yield) / self.base_yield * 100
        
        return yield_with_mabfol, yield_increase_percentage

    def simulate_multiple_seasons(self, seasons, soil_quality_factor=1.0, weather_factor=1.0):
        """
        Simulate yield over multiple seasons with random weather variations.
        
        Args:
            seasons (int): Number of seasons to simulate
            soil_quality_factor (float): Multiplier for soil quality (0.5-1.5)
            weather_factor (float): Base weather conditions multiplier (0.5-1.5)
            
        Returns:
            dict: Simulation results including averages and per-season data
            
        Raises:
            ValueError: If seasons is not a positive integer
        """
        if not isinstance(seasons, int) or seasons <= 0:
            raise ValueError("Number of seasons must be a positive integer")
        
        import random
        results = {
            'base_yield': self.base_yield,
            'seasons': seasons,
            'season_data': [],
            'average_yield': 0,
            'average_increase': 0
        }
        
        total_yield = 0
        total_increase = 0
        
        for season in range(1, seasons + 1):
            # Add some random variation to weather each season
            season_weather = max(0.5, min(1.5, weather_factor * random.uniform(0.9, 1.1)))
            
            yield_mabfol, increase_pct = self.calculate_yield_increase(
                soil_quality_factor=soil_quality_factor,
                weather_factor=season_weather
            )
            
            results['season_data'].append({
                'season': season,
                'weather_factor': season_weather,
                'yield': yield_mabfol,
                'increase_pct': increase_pct
            })
            
            total_yield += yield_mabfol
            total_increase += increase_pct
        
        results['average_yield'] = total_yield / seasons
        results['average_increase'] = total_increase / seasons
        
        return results


# Example usage
if __name__ == "__main__":
    try:
        # Initialize simulation with base yield of 5 tons/hectare
        simulation = FarmingSimulation(base_yield=5.0)
        
        # Calculate single season yield
        yield_mabfol, increase_pct = simulation.calculate_yield_increase(
            soil_quality_factor=1.2,
            weather_factor=0.9
        )
        print(f"Single season results: Yield with MABFOL: {yield_mabfol:.2f} tons, Increase: {increase_pct:.2f}%")
        
        # Simulate 5 seasons
        results = simulation.simulate_multiple_seasons(seasons=5, soil_quality_factor=1.1)
        print(f"\n5-season simulation average: Yield: {results['average_yield']:.2f} tons, Increase: {results['average_increase']:.2f}%")
        
    except ValueError as e:
        print(f"Error in simulation: {e}")
```
