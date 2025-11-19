"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Generate a Python script to recommend rubber flooring options for outdoor fitness areas based on weather conditions, using the material types (e.g., Rubber Tiles, Eva Mats) described on Rubber Flooring Indonesia's site.
Generated: DETERMINISTIC_e2d64e615d579207
Batch ID: 20250612_154441
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://api.openweathermap.org/data/2.5/weather": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from enum import Enum
from typing import Dict, List, Optional

class WeatherCondition(Enum):
    """Enum representing different weather conditions."""
    SUNNY = "sunny"
    RAINY = "rainy"
    HUMID = "humid"
    EXTREME_HEAT = "extreme_heat"
    COLD = "cold"

class MaterialType(Enum):
    """Enum representing different rubber flooring material types."""
    RUBBER_TILES = "Rubber Tiles"
    EVA_MATS = "EVA Mats"
    POURED_RUBBER = "Poured Rubber"
    RUBBER_ROLLS = "Rubber Rolls"

class RubberFlooringRecommender:
    """Recommends rubber flooring options based on weather conditions."""
    
    # Mapping of weather conditions to recommended materials with their properties
    MATERIAL_RECOMMENDATIONS = {
        WeatherCondition.SUNNY: [
            {
                "material": MaterialType.RUBBER_TILES,
                "properties": ["UV-resistant", "heat-reflective", "durable"],
                "thickness_range": "10-20mm"
            },
            {
                "material": MaterialType.POURED_RUBBER,
                "properties": ["seamless", "heat-resistant", "customizable"],
                "thickness_range": "8-15mm"
            }
        ],
        WeatherCondition.RAINY: [
            {
                "material": MaterialType.RUBBER_TILES,
                "properties": ["drainage-friendly", "slip-resistant", "waterproof"],
                "thickness_range": "12-25mm"
            },
            {
                "material": MaterialType.RUBBER_ROLLS,
                "properties": ["water-resistant", "easy-to-clean", "seam-reduced"],
                "thickness_range": "6-12mm"
            }
        ],
        WeatherCondition.HUMID: [
            {
                "material": MaterialType.EVA_MATS,
                "properties": ["mold-resistant", "breathable", "lightweight"],
                "thickness_range": "8-15mm"
            },
            {
                "material": MaterialType.RUBBER_TILES,
                "properties": ["anti-microbial", "ventilated", "quick-drying"],
                "thickness_range": "10-20mm"
            }
        ],
        WeatherCondition.EXTREME_HEAT: [
            {
                "material": MaterialType.POURED_RUBBER,
                "properties": ["heat-deflecting", "cool-to-touch", "durable"],
                "thickness_range": "10-20mm"
            },
            {
                "material": MaterialType.RUBBER_TILES,
                "properties": ["thermal-insulating", "color-stable", "thick"],
                "thickness_range": "15-30mm"
            }
        ],
        WeatherCondition.COLD: [
            {
                "material": MaterialType.EVA_MATS,
                "properties": ["insulating", "soft", "shock-absorbing"],
                "thickness_range": "10-20mm"
            },
            {
                "material": MaterialType.RUBBER_ROLLS,
                "properties": ["thermal-retaining", "flexible", "dense"],
                "thickness_range": "8-15mm"
            }
        ]
    }

    @staticmethod
    def get_recommendations(weather_condition: WeatherCondition) -> List[Dict]:
        """
        Get flooring recommendations for a given weather condition.
        
        Args:
            weather_condition: The weather condition to get recommendations for.
            
        Returns:
            List of recommended materials with their properties.
            
        Raises:
            ValueError: If the weather condition is not supported.
        """
        if weather_condition not in WeatherCondition:
            raise ValueError(f"Unsupported weather condition: {weather_condition}")
            
        return RubberFlooringRecommender.MATERIAL_RECOMMENDATIONS.get(weather_condition, [])

    @staticmethod
    def get_weather_condition(location: str, api_key: str) -> Optional[WeatherCondition]:
        """
        Get current weather condition for a location using OpenWeatherMap API.
        
        Args:
            location: City name or coordinates (lat,lon).
            api_key: OpenWeatherMap API key.
            
        Returns:
            Corresponding WeatherCondition or None if unable to determine.
            
        Raises:
            requests.exceptions.RequestException: If API request fails.
        """
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': location,
            'appid': api_key,
            'units': 'metric'
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            weather_data = response.json()
            
            weather_id = weather_data['weather'][0]['id']
            temp = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            
            # Map weather codes and conditions to our WeatherCondition enum
            if weather_id >= 200 and weather_id < 600:  # Thunderstorm, Drizzle, Rain
                return WeatherCondition.RAINY
            elif temp > 35:
                return WeatherCondition.EXTREME_HEAT
            elif temp < 10:
                return WeatherCondition.COLD
            elif humidity > 70:
                return WeatherCondition.HUMID
            else:
                return WeatherCondition.SUNNY
                
        except (requests.exceptions.RequestException, KeyError) as e:
            print(f"Error fetching weather data: {e}")
            return None

def main():
    """Example usage of the RubberFlooringRecommender."""
    try:
        # Example: Get recommendations based on current weather
        api_key = "your_openweathermap_api_key"  # Replace with actual API key
        location = "Jakarta,ID"
        
        weather_condition = RubberFlooringRecommender.get_weather_condition(location, api_key)
        
        if weather_condition:
            print(f"Current weather condition: {weather_condition.value}")
            recommendations = RubberFlooringRecommender.get_recommendations(weather_condition)
            
            print("\nRecommended flooring options:")
            for rec in recommendations:
                print(f"\nMaterial: {rec['material'].value}")
                print(f"Properties: {', '.join(rec['properties'])}")
                print(f"Recommended thickness: {rec['thickness_range']}")
        else:
            print("Could not determine weather condition.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
