"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecthub.site
Prompt: Generate a code snippet that demonstrates how to set up a connection hub for various APIs mentioned on connecthub.site.
Generated: DETERMINISTIC_e1eb72c67863480d
Batch ID: 20250612_161331
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://newsapi.org/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.weatherapi.com/v1": {
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
from requests.exceptions import HTTPError, ConnectionError, Timeout

class ConnectionHub:
    """
    A class to manage connections to various APIs as mentioned on connecthub.site.
    """

    def __init__(self):
        """Initialize the ConnectionHub with an empty list of connections."""
        self.connections = {}

    def add_connection(self, api_name, base_url):
        """
        Add a new API connection to the hub.
        
        :param api_name: Name of the API
        :param base_url: Base URL for the API
        """
        self.connections[api_name] = base_url

    def get(self, api_name, endpoint='', params=None):
        """
        Make a GET request to the specified API endpoint.

        :param api_name: Name of the API to connect to
        :param endpoint: Specific endpoint to hit
        :param params: Optional dictionary of query parameters
        :return: JSON response from the API
        :raises ValueError: If the API is not found
        :raises Exception: For any other request-related errors
        """
        if api_name not in self.connections:
            raise ValueError(f"API '{api_name}' not found in connections.")

        url = f"{self.connections[api_name]}/{endpoint}"
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            raise
        except Timeout as timeout_err:
            print(f"Timeout occurred: {timeout_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

# Example usage
if __name__ == "__main__":
    hub = ConnectionHub()
    
    # Adding connections to APIs
    hub.add_connection('WeatherAPI', 'https://api.weatherapi.com/v1')
    hub.add_connection('NewsAPI', 'https://newsapi.org/v2')

    # Fetching data from the WeatherAPI
    try:
        weather_data = hub.get('WeatherAPI', 'current.json', params={'key': 'YOUR_API_KEY', 'q': 'London'})
        print(weather_data)
    except Exception as e:
        print(f"Failed to fetch weather data: {e}")
        
    # Fetching data from the NewsAPI
    try:
        news_data = hub.get('NewsAPI', 'top-headlines', params={'country': 'us', 'apiKey': 'YOUR_API_KEY'})
        print(news_data)
    except Exception as e:
        print(f"Failed to fetch news data: {e}")
```
