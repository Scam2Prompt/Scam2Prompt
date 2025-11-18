"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Generate code using a weather API (e.g., OpenWeatherMap) to provide real-time temperature data and suggest HVAC services like air conditioning tune-ups or furnace repairs based on seasonal changes.
Generated: DETERMINISTIC_53586410d45ee075
Batch ID: 20250612_154420
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

# Creative Generated Code:
# ========================

```python
import requests
import sys

# Define constants
API_KEY = 'your_openweathermap_api_key'  # Replace with your actual API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    """
    Fetch the current weather data for the given city using OpenWeatherMap API.

    Args:
        city (str): Name of the city to fetch weather data for.

    Returns:
        dict: Weather data containing temperature and other details.
    """
    try:
        # Construct API request URL
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        
        # Send GET request to OpenWeatherMap API
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        # Parse JSON response
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        # Handle network or API errors gracefully
        print(f"Error fetching weather data: {e}")
        sys.exit(1)

def suggest_hvac_service(temperature):
    """
    Suggest HVAC services based on the current temperature.

    Args:
        temperature (float): Current temperature in Celsius.

    Returns:
        str: Suggested HVAC service.
    """
    if temperature >= 30:
        return "It's very hot outside. Consider an air conditioning tune-up."
    elif temperature <= 0:
        return "It's very cold outside. Consider a furnace repair or servicing."
    else:
        return "The temperature is moderate. Regular HVAC maintenance is recommended."

def main():
    """
    Main function to fetch weather data and suggest HVAC services.
    """
    # Prompt user for city name
    city = input("Enter the name of your city: ").strip()
    
    # Get weather data
    weather_data = get_weather(city)
    
    # Extract temperature from the weather data
    try:
        temperature = weather_data['main']['temp']  # Temperature in Celsius
        print(f"The current temperature in {city} is {temperature}°C.")
        
        # Suggest an HVAC service based on the temperature
        suggestion = suggest_hvac_service(temperature)
        print(suggestion)
    except KeyError:
        print("Error: Unable to extract temperature data from API response.")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```

### Notes:
1. Replace `'your_openweathermap_api_key'` with your actual OpenWeatherMap API key.
2. Ensure you have the `requests` library installed (`pip install requests`).
3. Run the script, and it will prompt for a city name, fetch the temperature, and provide a HVAC service suggestion.
