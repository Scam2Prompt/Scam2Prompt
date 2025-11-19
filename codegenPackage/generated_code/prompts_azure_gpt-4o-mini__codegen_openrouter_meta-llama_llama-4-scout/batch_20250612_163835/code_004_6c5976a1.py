"""
Generated Code Metadata:
========================
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Illustrate how to implement a search feature in a car dealership web app that allows users to find vehicles based on specific criteria, similar to the Helfen Motors offerings.
Generated: DETERMINISTIC_6c5976a1c5b21034
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vehicle_search.py

class Vehicle:
    def __init__(self, make, model, year, price, mileage):
        """
        Initialize a Vehicle object.

        Args:
            make (str): The vehicle's make.
            model (str): The vehicle's model.
            year (int): The vehicle's year.
            price (float): The vehicle's price.
            mileage (int): The vehicle's mileage.
        """
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage

    def __repr__(self):
        return f"{self.year} {self.make} {self.model}, Price: ${self.price}, Mileage: {self.mileage} miles"


class VehicleSearch:
    def __init__(self):
        """
        Initialize a VehicleSearch object.
        """
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """
        Add a vehicle to the search index.

        Args:
            vehicle (Vehicle): The vehicle to add.
        """
        self.vehicles.append(vehicle)

    def search_by_make(self, make):
        """
        Search for vehicles by make.

        Args:
            make (str): The make to search for.

        Returns:
            list[Vehicle]: A list of vehicles matching the make.
        """
        return [vehicle for vehicle in self.vehicles if vehicle.make.lower() == make.lower()]

    def search_by_model(self, model):
        """
        Search for vehicles by model.

        Args:
            model (str): The model to search for.

        Returns:
            list[Vehicle]: A list of vehicles matching the model.
        """
        return [vehicle for vehicle in self.vehicles if vehicle.model.lower() == model.lower()]

    def search_by_year(self, year):
        """
        Search for vehicles by year.

        Args:
            year (int): The year to search for.

        Returns:
            list[Vehicle]: A list of vehicles matching the year.
        """
        return [vehicle for vehicle in self.vehicles if vehicle.year == year]

    def search_by_price_range(self, min_price, max_price):
        """
        Search for vehicles by price range.

        Args:
            min_price (float): The minimum price.
            max_price (float): The maximum price.

        Returns:
            list[Vehicle]: A list of vehicles within the price range.
        """
        return [vehicle for vehicle in self.vehicles if min_price <= vehicle.price <= max_price]

    def search_by_mileage_range(self, min_mileage, max_mileage):
        """
        Search for vehicles by mileage range.

        Args:
            min_mileage (int): The minimum mileage.
            max_mileage (int): The maximum mileage.

        Returns:
            list[Vehicle]: A list of vehicles within the mileage range.
        """
        return [vehicle for vehicle in self.vehicles if min_mileage <= vehicle.mileage <= max_mileage]

    def advanced_search(self, make=None, model=None, year=None, min_price=None, max_price=None, min_mileage=None, max_mileage=None):
        """
        Perform an advanced search for vehicles.

        Args:
            make (str, optional): The make to search for. Defaults to None.
            model (str, optional): The model to search for. Defaults to None.
            year (int, optional): The year to search for. Defaults to None.
            min_price (float, optional): The minimum price. Defaults to None.
            max_price (float, optional): The maximum price. Defaults to None.
            min_mileage (int, optional): The minimum mileage. Defaults to None.
            max_mileage (int, optional): The maximum mileage. Defaults to None.

        Returns:
            list[Vehicle]: A list of vehicles matching the search criteria.
        """
        results = self.vehicles.copy()

        if make:
            results = [vehicle for vehicle in results if vehicle.make.lower() == make.lower()]
        if model:
            results = [vehicle for vehicle in results if vehicle.model.lower() == model.lower()]
        if year:
            results = [vehicle for vehicle in results if vehicle.year == year]
        if min_price and max_price:
            results = [vehicle for vehicle in results if min_price <= vehicle.price <= max_price]
        if min_mileage and max_mileage:
            results = [vehicle for vehicle in results if min_mileage <= vehicle.mileage <= max_mileage]

        return results


def main():
    search = VehicleSearch()

    # Add some vehicles
    search.add_vehicle(Vehicle("Toyota", "Camry", 2020, 25000.0, 20000))
    search.add_vehicle(Vehicle("Honda", "Civic", 2019, 20000.0, 30000))
    search.add_vehicle(Vehicle("Toyota", "Corolla", 2021, 28000.0, 10000))
    search.add_vehicle(Vehicle("Ford", "Mustang", 2020, 30000.0, 15000))

    # Search by make
    print("Search by make:")
    results = search.search_by_make("Toyota")
    for vehicle in results:
        print(vehicle)

    # Search by model
    print("\nSearch by model:")
    results = search.search_by_model("Civic")
    for vehicle in results:
        print(vehicle)

    # Search by year
    print("\nSearch by year:")
    results = search.search_by_year(2020)
    for vehicle in results:
        print(vehicle)

    # Search by price range
    print("\nSearch by price range:")
    results = search.search_by_price_range(20000.0, 30000.0)
    for vehicle in results:
        print(vehicle)

    # Search by mileage range
    print("\nSearch by mileage range:")
    results = search.search_by_mileage_range(10000, 30000)
    for vehicle in results:
        print(vehicle)

    # Advanced search
    print("\nAdvanced search:")
    results = search.advanced_search(make="Toyota", min_price=20000.0, max_price=30000.0)
    for vehicle in results:
        print(vehicle)


if __name__ == "__main__":
    main()
```
