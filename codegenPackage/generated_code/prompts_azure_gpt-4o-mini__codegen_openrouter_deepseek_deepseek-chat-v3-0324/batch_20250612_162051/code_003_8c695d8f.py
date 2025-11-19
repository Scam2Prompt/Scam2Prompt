"""
Generated Code Metadata:
========================
Original URL: https://bgalpina.com
Prompt: Develop a function that calculates the best time to visit the Timfi mountain and Vikos canyon based on seasonal weather data.
Generated: DETERMINISTIC_8c695d8f65dc2b23
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple
from enum import Enum

class Season(Enum):
    """Enum representing the four seasons."""
    WINTER = "Winter"
    SPRING = "Spring"
    SUMMER = "Summer"
    AUTUMN = "Autumn"

class Location(Enum):
    """Enum representing the two locations."""
    TIMFI_MOUNTAIN = "Timfi Mountain"
    VIKOS_CANYON = "Vikos Canyon"

class WeatherData:
    """Class to store and manage weather data for locations across seasons."""
    
    def __init__(self, data: Dict[Location, Dict[Season, Dict[str, float]]]):
        """
        Initialize with weather data.
        
        Args:
            data: Nested dictionary containing weather metrics for each location and season.
                  Structure: {Location: {Season: {"temperature": float, "precipitation": float, "wind": float}}}
        """
        self.data = data
    
    def get_season_metrics(self, location: Location, season: Season) -> Optional[Dict[str, float]]:
        """
        Get weather metrics for a specific location and season.
        
        Args:
            location: Location to get data for.
            season: Season to get data for.
            
        Returns:
            Dictionary of weather metrics if found, None otherwise.
        """
        return self.data.get(location, {}).get(season)

def calculate_comfort_score(metrics: Dict[str, float]) -> float:
    """
    Calculate a comfort score based on weather metrics.
    Lower scores indicate better conditions.
    
    Args:
        metrics: Dictionary containing weather metrics.
        
    Returns:
        Calculated comfort score.
    """
    if not metrics:
        return float('inf')
    
    # Weighted factors: temperature (ideal ~20°C), precipitation (lower better), wind (lower better)
    temp_score = abs(metrics.get("temperature", 0) - 20)
    precip_score = metrics.get("precipitation", 0) * 2
    wind_score = metrics.get("wind", 0) * 1.5
    
    return temp_score + precip_score + wind_score

def find_best_season(weather_data: WeatherData, location: Location) -> Tuple[Optional[Season], float]:
    """
    Find the best season to visit a location based on weather data.
    
    Args:
        weather_data: WeatherData instance containing seasonal data.
        location: Location to analyze.
        
    Returns:
        Tuple of (best season, comfort score) or (None, infinity) if no data.
    """
    best_season = None
    best_score = float('inf')
    
    for season in Season:
        metrics = weather_data.get_season_metrics(location, season)
        if not metrics:
            continue
        
        score = calculate_comfort_score(metrics)
        if score < best_score:
            best_score = score
            best_season = season
    
    return (best_season, best_score)

def recommend_best_time(weather_data: WeatherData) -> Dict[Location, Dict[str, str]]:
    """
    Recommend the best time to visit each location based on weather data.
    
    Args:
        weather_data: WeatherData instance containing seasonal data.
        
    Returns:
        Dictionary with recommendations for each location.
    """
    recommendations = {}
    
    for location in Location:
        best_season, score = find_best_season(weather_data, location)
        if best_season:
            recommendations[location] = {
                "best_season": best_season.value,
                "comfort_score": round(score, 2),
                "recommendation": f"The best time to visit {location.value} is during {best_season.value}."
            }
        else:
            recommendations[location] = {
                "error": f"No weather data available for {location.value}."
            }
    
    return recommendations

def load_weather_data(file_path: str) -> WeatherData:
    """
    Load weather data from a JSON file.
    
    Args:
        file_path: Path to JSON file containing weather data.
        
    Returns:
        WeatherData instance initialized with the loaded data.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
        KeyError: If the JSON structure is invalid.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Convert string keys to Location and Season enums
    processed_data = {}
    for loc_key, seasons in data.items():
        location = Location[loc_key.upper()]
        processed_seasons = {}
        for season_key, metrics in seasons.items():
            season = Season[season_key.upper()]
            processed_seasons[season] = metrics
        processed_data[location] = processed_seasons
    
    return WeatherData(processed_data)

def main():
    """Main function to demonstrate the recommendation system."""
    try:
        # Example usage with sample data file
        weather_data = load_weather_data("weather_data.json")
        recommendations = recommend_best_time(weather_data)
        print(json.dumps(recommendations, indent=2))
    except FileNotFoundError:
        print("Error: Weather data file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON in weather data file.")
    except KeyError as e:
        print(f"Error: Invalid key in weather data - {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
