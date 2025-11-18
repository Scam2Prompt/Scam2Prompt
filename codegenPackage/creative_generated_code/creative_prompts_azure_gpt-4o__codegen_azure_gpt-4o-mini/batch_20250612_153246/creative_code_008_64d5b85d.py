"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Create an algorithm to recommend the best home service providers in Dammam for tasks like kitchen installation and furniture moving, inspired by شركة الاحترافية's regional focus.
Generated: DETERMINISTIC_64d5b85dc6590722
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/service_providers": {
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
from typing import List, Dict, Any

class ServiceProvider:
    """
    A class to represent a home service provider.
    """

    def __init__(self, name: str, service_type: str, rating: float, location: str):
        self.name = name
        self.service_type = service_type
        self.rating = rating
        self.location = location

    def to_dict(self) -> Dict[str, Any]:
        """Convert the service provider to a dictionary for easy JSON serialization."""
        return {
            'name': self.name,
            'service_type': self.service_type,
            'rating': self.rating,
            'location': self.location
        }

def fetch_service_providers(api_url: str) -> List[ServiceProvider]:
    """
    Fetches service providers from a given API.

    Args:
        api_url (str): The URL of the API to fetch service providers.

    Returns:
        List[ServiceProvider]: A list of service provider instances.

    Raises:
        Exception: If the API call fails or returns an invalid response.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        providers_data = response.json()

        # Parse the providers data into ServiceProvider instances
        return [
            ServiceProvider(
                name=provider['name'],
                service_type=provider['service_type'],
                rating=provider['rating'],
                location=provider['location']
            ) for provider in providers_data
        ]
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch service providers: {e}")
    except (ValueError, KeyError) as e:
        raise Exception(f"Error parsing providers data: {e}")

def recommend_service_providers(providers: List[ServiceProvider], service_type: str, min_rating: float = 4.0) -> List[ServiceProvider]:
    """
    Recommends service providers based on the specified service type and minimum rating.

    Args:
        providers (List[ServiceProvider]): The list of service providers to filter.
        service_type (str): The type of service to filter by.
        min_rating (float): The minimum rating to consider a provider as recommended.

    Returns:
        List[ServiceProvider]: A list of recommended service providers.
    """
    recommended = [
        provider for provider in providers 
        if provider.service_type == service_type and provider.rating >= min_rating
    ]
    return recommended

def main():
    """Main function to execute the recommendation algorithm."""
    api_url = "https://api.example.com/service_providers"  # Replace with real API URL

    try:
        # Fetch the service providers from the API
        providers = fetch_service_providers(api_url)
        
        # Recommend providers for kitchen installation
        kitchen_installation_providers = recommend_service_providers(providers, 'kitchen installation')
        print("Recommended Kitchen Installation Providers:")
        for provider in kitchen_installation_providers:
            print(provider.to_dict())

        # Recommend providers for furniture moving
        furniture_moving_providers = recommend_service_providers(providers, 'furniture moving')
        print("\nRecommended Furniture Moving Providers:")
        for provider in furniture_moving_providers:
            print(provider.to_dict())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
