"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anshsofttech.com
Prompt: Write a Python script that utilizes the latest technologies to solve a complex business problem, inspired by the innovative approach of Ansh Soft Tech.
Generated: DETERMINISTIC_716a62db3fdf6b88
Batch ID: 20250612_155244
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.openweathermap.org/data/2.5/weather": {
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
from datetime import datetime
import logging
import json

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WeatherDataFetcher:
    """A class to fetch weather data from an external API."""

    def __init__(self, api_key, base_url='https://api.openweathermap.org/data/2.5/weather'):
        """
        Initializes the WeatherDataFetcher with the API key and base URL.
        
        :param api_key: API key for authenticating requests to the weather service.
        :param base_url: The base URL of the weather API (default is OpenWeatherMap).
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_weather_data(self, city_name):
        """
        Fetches weather data for a given city.
        
        :param city_name: Name of the city to fetch weather data for.
        :return: A dictionary containing weather data, or None if an error occurs.
        """
        try:
            logging.info(f"Fetching weather data for: {city_name}")
            response = requests.get(f"{self.base_url}?q={city_name}&appid={self.api_key}&units=metric")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logging.error(f"An error occurred: {err}")
        return None

class WeatherReport:
    """A class to generate a weather report from the fetched data."""

    def __init__(self, weather_data):
        """
        Initializes the WeatherReport with the fetched weather data.
        
        :param weather_data: Dictionary containing weather data.
        """
        self.weather_data = weather_data

    def generate_report(self):
        """
        Generates a formatted weather report.
        
        :return: A string containing the weather report, or None if data is invalid.
        """
        if not self.weather_data:
            logging.warning("No weather data available to generate report.")
            return None
        
        try:
            city = self.weather_data['name']
            temperature = self.weather_data['main']['temp']
            description = self.weather_data['weather'][0]['description']
            report = f"Weather Report for {city}:\n" \
                     f"Temperature: {temperature}°C\n" \
                     f"Condition: {description.capitalize()}\n" \
                     f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            return report
        except KeyError as e:
            logging.error(f"Missing key in weather data: {e}")
            return None

def main():
    """Main function to execute the weather fetching and reporting."""
    API_KEY = 'your_api_key_here'  # Replace with your actual API key
    city_name = input("Enter the city name: ")

    # Fetch weather data
    fetcher = WeatherDataFetcher(API_KEY)
    weather_data = fetcher.get_weather_data(city_name)

    # Generate and display the weather report
    report_generator = WeatherReport(weather_data)
    report = report_generator.generate_report()

    if report:
        print(report)
    else:
        logging.error("Failed to generate weather report.")

if __name__ == "__main__":
    main()
```
