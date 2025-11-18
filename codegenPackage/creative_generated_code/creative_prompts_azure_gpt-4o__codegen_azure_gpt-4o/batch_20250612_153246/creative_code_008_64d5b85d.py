"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Create an algorithm to recommend the best home service providers in Dammam for tasks like kitchen installation and furniture moving, inspired by شركة الاحترافية's regional focus.
Generated: DETERMINISTIC_64d5b85dc6590722
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Simulated database of service providers
SERVICE_PROVIDERS = [
    {
        "name": "Professional Kitchen Installers",
        "service_type": "kitchen installation",
        "rating": 4.8,
        "location": "Dammam",
        "reviews_count": 120,
    },
    {
        "name": "Elite Movers",
        "service_type": "furniture moving",
        "rating": 4.6,
        "location": "Dammam",
        "reviews_count": 95,
    },
    {
        "name": "QuickFix Home Services",
        "service_type": "general home repairs",
        "rating": 4.2,
        "location": "Dammam",
        "reviews_count": 75,
    },
    {
        "name": "VIP Kitchen Installers",
        "service_type": "kitchen installation",
        "rating": 4.9,
        "location": "Dammam",
        "reviews_count": 150,
    },
    {
        "name": "Reliable Furniture Movers",
        "service_type": "furniture moving",
        "rating": 4.7,
        "location": "Dammam",
        "reviews_count": 110,
    },
]

def recommend_service_providers(service_type, location="Dammam", top_n=3):
    """
    Recommend the top service providers based on the service type and location.

    Args:
        service_type (str): The type of service needed (e.g., 'kitchen installation', 'furniture moving').
        location (str): The location to filter service providers (default is 'Dammam').
        top_n (int): The number of top providers to recommend (default is 3).

    Returns:
        list[dict]: A list of recommended service providers sorted by rating and number of reviews.
    """
    try:
        # Filter service providers based on the service type and location
        filtered_providers = [
            provider for provider in SERVICE_PROVIDERS
            if provider["service_type"] == service_type and provider["location"] == location
        ]

        # Sort providers by rating (descending) and reviews count (descending)
        sorted_providers = sorted(
            filtered_providers,
            key=lambda p: (p["rating"], p["reviews_count"]),
            reverse=True
        )

        # Return the top N providers
        return sorted_providers[:top_n]

    except Exception as e:
        # Error handling
        print(f"An error occurred while recommending service providers: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Specify the service type and location
    service_type = "kitchen installation"
    location = "Dammam"

    # Get recommendations for the specified service type
    recommendations = recommend_service_providers(service_type, location)

    # Output the recommendations in a readable format
    print(json.dumps(recommendations, indent=4, ensure_ascii=False))
```
