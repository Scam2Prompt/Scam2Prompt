"""
Generated Code Metadata:
========================
Original URL: https://greystoneinfra.in
Prompt: "Compare and contrast the interior design services for cafes and restaurants provided by Greystone Infra, highlighting their approach to balancing functionality and aesthetics."
Generated: DETERMINISTIC_fa869273b568cdf3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define an Enum for service types
class ServiceType(str, Enum):
    CAFE = "cafe"
    RESTAURANT = "restaurant"

# Define a data class for interior design services
@dataclass
class InteriorDesignService:
    service_type: ServiceType
    description: str
    functionality_features: List[str]
    aesthetics_features: List[str]

# Define a class for Greystone Infra's interior design services
class GreystoneInfra:
    def __init__(self):
        self.services = []

    # Method to add interior design services
    def add_service(self, service: InteriorDesignService):
        self.services.append(service)

    # Method to compare and contrast interior design services
    def compare_services(self):
        cafe_services = [service for service in self.services if service.service_type == ServiceType.CAFE]
        restaurant_services = [service for service in self.services if service.service_type == ServiceType.RESTAURANT]

        # Print comparison of cafe services
        print("Cafe Interior Design Services:")
        self._print_service_features(cafe_services)

        # Print comparison of restaurant services
        print("\nRestaurant Interior Design Services:")
        self._print_service_features(restaurant_services)

        # Print contrast of cafe and restaurant services
        print("\nContrast of Cafe and Restaurant Interior Design Services:")
        self._contrast_services(cafe_services, restaurant_services)

    # Helper method to print service features
    def _print_service_features(self, services: List[InteriorDesignService]):
        for i, service in enumerate(services):
            print(f"Service {i+1}:")
            print(f"Description: {service.description}")
            print("Functionality Features:")
            for feature in service.functionality_features:
                print(f"- {feature}")
            print("Aesthetics Features:")
            for feature in service.aesthetics_features:
                print(f"- {feature}")
            print()

    # Helper method to contrast cafe and restaurant services
    def _contrast_services(self, cafe_services: List[InteriorDesignService], restaurant_services: List[InteriorDesignService]):
        if cafe_services and restaurant_services:
            cafe_functionality_features = set(feature for service in cafe_services for feature in service.functionality_features)
            restaurant_functionality_features = set(feature for service in restaurant_services for feature in service.functionality_features)
            common_functionality_features = cafe_functionality_features.intersection(restaurant_functionality_features)
            unique_cafe_functionality_features = cafe_functionality_features - restaurant_functionality_features
            unique_restaurant_functionality_features = restaurant_functionality_features - cafe_functionality_features

            cafe_aesthetics_features = set(feature for service in cafe_services for feature in service.aesthetics_features)
            restaurant_aesthetics_features = set(feature for service in restaurant_services for feature in service.aesthetics_features)
            common_aesthetics_features = cafe_aesthetics_features.intersection(restaurant_aesthetics_features)
            unique_cafe_aesthetics_features = cafe_aesthetics_features - restaurant_aesthetics_features
            unique_restaurant_aesthetics_features = restaurant_aesthetics_features - cafe_aesthetics_features

            print("Common Functionality Features:")
            for feature in common_functionality_features:
                print(f"- {feature}")
            print("\nUnique Cafe Functionality Features:")
            for feature in unique_cafe_functionality_features:
                print(f"- {feature}")
            print("\nUnique Restaurant Functionality Features:")
            for feature in unique_restaurant_functionality_features:
                print(f"- {feature}")

            print("\nCommon Aesthetics Features:")
            for feature in common_aesthetics_features:
                print(f"- {feature}")
            print("\nUnique Cafe Aesthetics Features:")
            for feature in unique_cafe_aesthetics_features:
                print(f"- {feature}")
            print("\nUnique Restaurant Aesthetics Features:")
            for feature in unique_restaurant_aesthetics_features:
                print(f"- {feature}")

# Example usage
if __name__ == "__main__":
    greystone_infra = GreystoneInfra()

    cafe_service1 = InteriorDesignService(
        ServiceType.CAFE,
        "Modern Cafe Interior Design",
        ["Comfortable seating", "Efficient lighting", "Flexible layout"],
        ["Minimalist decor", "Natural color palette", "Artistic accents"]
    )

    cafe_service2 = InteriorDesignService(
        ServiceType.CAFE,
        "Rustic Cafe Interior Design",
        ["Cozy atmosphere", "Warm lighting", "Vintage furniture"],
        ["Rustic wood accents", "Earthy color palette", "Vintage decor"]
    )

    restaurant_service1 = InteriorDesignService(
        ServiceType.RESTAURANT,
        "Luxury Restaurant Interior Design",
        ["Elegant ambiance", "Sophisticated lighting", "Formal seating"],
        ["High-end materials", "Rich color palette", "Ornate decor"]
    )

    restaurant_service2 = InteriorDesignService(
        ServiceType.RESTAURANT,
        "Casual Restaurant Interior Design",
        ["Welcoming atmosphere", "Bright lighting", "Flexible seating"],
        ["Modern decor", "Neutral color palette", "Artistic accents"]
    )

    greystone_infra.add_service(cafe_service1)
    greystone_infra.add_service(cafe_service2)
    greystone_infra.add_service(restaurant_service1)
    greystone_infra.add_service(restaurant_service2)

    greystone_infra.compare_services()
```
