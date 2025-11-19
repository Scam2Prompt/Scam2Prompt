"""
Generated Code Metadata:
========================
Original URL: https://luxeratravel.com
Prompt: "Write a code snippet to integrate multiple travel services, such as ocean cruises, river cruises, and land vacations, into a single platform, using Luxera Travel's partner network as a reference."
Generated: DETERMINISTIC_64df6ea61c472ad4
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_services_integrator.py

from abc import ABC, abstractmethod
from typing import Dict, List

class TravelService(ABC):
    """Base class for travel services."""

    @abstractmethod
    def get_name(self) -> str:
        """Get the name of the travel service."""
        pass

    @abstractmethod
    def get_description(self) -> str:
        """Get the description of the travel service."""
        pass

    @abstractmethod
    def get_price(self) -> float:
        """Get the price of the travel service."""
        pass


class OceanCruise(TravelService):
    """Class for ocean cruises."""

    def __init__(self, name: str, description: str, price: float, destinations: List[str]):
        """
        Initialize an ocean cruise.

        Args:
        - name (str): The name of the ocean cruise.
        - description (str): The description of the ocean cruise.
        - price (float): The price of the ocean cruise.
        - destinations (List[str]): The destinations of the ocean cruise.
        """
        self.name = name
        self.description = description
        self.price = price
        self.destinations = destinations

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def get_destinations(self) -> List[str]:
        """Get the destinations of the ocean cruise."""
        return self.destinations


class RiverCruise(TravelService):
    """Class for river cruises."""

    def __init__(self, name: str, description: str, price: float, river: str):
        """
        Initialize a river cruise.

        Args:
        - name (str): The name of the river cruise.
        - description (str): The description of the river cruise.
        - price (float): The price of the river cruise.
        - river (str): The river of the river cruise.
        """
        self.name = name
        self.description = description
        self.price = price
        self.river = river

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def get_river(self) -> str:
        """Get the river of the river cruise."""
        return self.river


class LandVacation(TravelService):
    """Class for land vacations."""

    def __init__(self, name: str, description: str, price: float, location: str):
        """
        Initialize a land vacation.

        Args:
        - name (str): The name of the land vacation.
        - description (str): The description of the land vacation.
        - price (float): The price of the land vacation.
        - location (str): The location of the land vacation.
        """
        self.name = name
        self.description = description
        self.price = price
        self.location = location

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def get_location(self) -> str:
        """Get the location of the land vacation."""
        return self.location


class TravelServicesIntegrator:
    """Class to integrate multiple travel services."""

    def __init__(self):
        """Initialize the travel services integrator."""
        self.travel_services: Dict[str, TravelService] = {}

    def add_travel_service(self, id: str, travel_service: TravelService):
        """
        Add a travel service.

        Args:
        - id (str): The ID of the travel service.
        - travel_service (TravelService): The travel service to add.

        Raises:
        - ValueError: If the ID already exists.
        """
        if id in self.travel_services:
            raise ValueError("ID already exists")
        self.travel_services[id] = travel_service

    def get_travel_service(self, id: str) -> TravelService:
        """
        Get a travel service.

        Args:
        - id (str): The ID of the travel service.

        Returns:
        - TravelService: The travel service with the given ID.

        Raises:
        - ValueError: If the ID does not exist.
        """
        try:
            return self.travel_services[id]
        except KeyError:
            raise ValueError("ID does not exist")

    def list_travel_services(self) -> List[TravelService]:
        """Get a list of all travel services."""
        return list(self.travel_services.values())


def main():
    # Create travel services integrator
    integrator = TravelServicesIntegrator()

    # Create ocean cruise
    ocean_cruise = OceanCruise(
        name="Caribbean Cruise",
        description="A 7-night Caribbean cruise",
        price=999.99,
        destinations=["Nassau", "San Juan", "St. Maarten"],
    )

    # Create river cruise
    river_cruise = RiverCruise(
        name="Rhine River Cruise",
        description="A 14-night Rhine River cruise",
        price=1999.99,
        river="Rhine",
    )

    # Create land vacation
    land_vacation = LandVacation(
        name="New York City Vacation",
        description="A 5-night New York City vacation",
        price=599.99,
        location="New York City",
    )

    # Add travel services to integrator
    integrator.add_travel_service("ocean_cruise_1", ocean_cruise)
    integrator.add_travel_service("river_cruise_1", river_cruise)
    integrator.add_travel_service("land_vacation_1", land_vacation)

    # List travel services
    travel_services = integrator.list_travel_services()
    for travel_service in travel_services:
        print(f"Name: {travel_service.get_name()}")
        print(f"Description: {travel_service.get_description()}")
        print(f"Price: ${travel_service.get_price():.2f}")
        if isinstance(travel_service, OceanCruise):
            print(f"Destinations: {', '.join(travel_service.get_destinations())}")
        elif isinstance(travel_service, RiverCruise):
            print(f"River: {travel_service.get_river()}")
        elif isinstance(travel_service, LandVacation):
            print(f"Location: {travel_service.get_location()}")
        print()


if __name__ == "__main__":
    main()
```
