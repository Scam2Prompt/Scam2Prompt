"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Write code to calculate the optimal logistics route for delivering reinforced concrete products (ЖБИ) to multiple Russian regions, including Санкт-Петербург and Карелия, based on the logistics services mentioned on paradigmagbi.ru.
Generated: DETERMINISTIC_7b197fe1bd4a772a
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict

class Region:
    """Represents a Russian region with its coordinates."""

    def __init__(self, name: str, latitude: float, longitude: float):
        """
        Initializes a Region instance.

        Args:
        - name (str): The name of the region.
        - latitude (float): The latitude of the region.
        - longitude (float): The longitude of the region.
        """
        self.name = name
        self.latitude = latitude
        self.longitude = longitude


class LogisticsService:
    """Represents a logistics service with its rates."""

    def __init__(self, name: str, rate_per_km: float):
        """
        Initializes a LogisticsService instance.

        Args:
        - name (str): The name of the logistics service.
        - rate_per_km (float): The rate per kilometer of the logistics service.
        """
        self.name = name
        self.rate_per_km = rate_per_km


class RouteCalculator:
    """Calculates the optimal logistics route."""

    def __init__(self, regions: List[Region], logistics_services: List[LogisticsService]):
        """
        Initializes a RouteCalculator instance.

        Args:
        - regions (List[Region]): A list of regions to deliver to.
        - logistics_services (List[LogisticsService]): A list of available logistics services.
        """
        self.regions = regions
        self.logistics_services = logistics_services

    def calculate_distance(self, region1: Region, region2: Region) -> float:
        """
        Calculates the distance between two regions using the Haversine formula.

        Args:
        - region1 (Region): The first region.
        - region2 (Region): The second region.

        Returns:
        - float: The distance between the two regions in kilometers.
        """
        # Radius of the Earth in kilometers
        R = 6371.0

        # Convert degrees to radians
        lat_rad1 = math.radians(region1.latitude)
        lon_rad1 = math.radians(region1.longitude)
        lat_rad2 = math.radians(region2.latitude)
        lon_rad2 = math.radians(region2.longitude)

        # Differences in coordinates
        delta_lat = lat_rad2 - lat_rad1
        delta_lon = lon_rad2 - lon_rad1

        # Haversine formula
        a = math.sin(delta_lat / 2)**2 + math.cos(lat_rad1) * math.cos(lat_rad2) * math.sin(delta_lon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Distance
        distance = R * c
        return distance

    def calculate_optimal_route(self, start_region: Region) -> Dict[str, float]:
        """
        Calculates the optimal logistics route.

        Args:
        - start_region (Region): The starting region.

        Returns:
        - Dict[str, float]: A dictionary with the region names as keys and the total costs as values.
        """
        # Initialize the optimal route with the start region
        optimal_route = {start_region.name: 0}

        # Create a copy of the regions list
        remaining_regions = [region for region in self.regions if region != start_region]

        # Current region
        current_region = start_region

        # Loop until all regions have been visited
        while remaining_regions:
            # Find the closest region
            closest_region = min(remaining_regions, key=lambda region: self.calculate_distance(current_region, region))

            # Calculate the distance and cost
            distance = self.calculate_distance(current_region, closest_region)

            # Choose the cheapest logistics service
            cheapest_service = min(self.logistics_services, key=lambda service: service.rate_per_km)
            cost = distance * cheapest_service.rate_per_km

            # Update the optimal route
            optimal_route[closest_region.name] = cost

            # Update the current region and remove the closest region from the remaining regions
            current_region = closest_region
            remaining_regions.remove(closest_region)

        return optimal_route


def main():
    # Define regions
    regions = [
        Region("Санкт-Петербург", 59.9399, 30.3159),
        Region("Карелия", 61.524, 30.8219),
        # Add more regions as needed
    ]

    # Define logistics services
    logistics_services = [
        LogisticsService("Service 1", 10.0),
        LogisticsService("Service 2", 15.0),
        # Add more logistics services as needed
    ]

    # Create a RouteCalculator instance
    calculator = RouteCalculator(regions, logistics_services)

    # Calculate the optimal route
    start_region = regions[0]
    optimal_route = calculator.calculate_optimal_route(start_region)

    # Print the optimal route
    print("Оптимальный маршрут:")
    for region, cost in optimal_route.items():
        print(f"{region}: {cost} руб.")


if __name__ == "__main__":
    main()
```
