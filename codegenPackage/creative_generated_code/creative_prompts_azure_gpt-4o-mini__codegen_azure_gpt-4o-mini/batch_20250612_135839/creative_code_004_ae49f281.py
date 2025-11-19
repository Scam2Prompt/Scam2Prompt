"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drivemiami.com
Prompt: What are the best practices for listing pre-owned and certified inventory on an automotive marketplace, based on DriveCities' recommendations?
Generated: DETERMINISTIC_ae49f2817abf19bd
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Vehicle:
    """
    A class to represent a vehicle with its details.

    Attributes
    ----------
    make : str
        The manufacturer of the vehicle.
    model : str
        The model of the vehicle.
    year : int
        The year the vehicle was manufactured.
    mileage : int
        The mileage of the vehicle.
    price : float
        The selling price of the vehicle.
    certified : bool
        Indicates if the vehicle is certified pre-owned.
    """

    def __init__(self, make, model, year, mileage, price, certified):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
        self.certified = certified

    def display_info(self):
        """Displays information about the vehicle."""
        cert_status = "Certified Pre-Owned" if self.certified else "Pre-Owned"
        return f"{self.year} {self.make} {self.model} - {cert_status} - Mileage: {self.mileage} - Price: ${self.price:.2f}"


class Inventory:
    """
    A class to manage a collection of vehicles in the inventory.

    Attributes
    ----------
    vehicles : list
        A list to store Vehicle objects.
    """

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """
        Adds a vehicle to the inventory.

        Parameters
        ----------
        vehicle : Vehicle
            A Vehicle object to add to the inventory.
        """
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Only Vehicle instances can be added")
        self.vehicles.append(vehicle)

    def list_inventory(self):
        """Lists all vehicles in the inventory."""
        if not self.vehicles:
            return "No vehicles in inventory."
        return "\n".join(vehicle.display_info() for vehicle in self.vehicles)

    def search_inventory(self, make=None, model=None, certified=None):
        """
        Searches for vehicles in the inventory based on specified criteria.

        Parameters
        ----------
        make : str, optional
            The make of the vehicle to search for.
        model : str, optional
            The model of the vehicle to search for.
        certified : bool, optional
            Indicates whether to filter by certified pre-owned status.
        
        Returns
        -------
        list
            A list of vehicles matching the search criteria.
        """
        results = self.vehicles
        if make:
            results = [v for v in results if v.make.lower() == make.lower()]
        if model:
            results = [v for v in results if v.model.lower() == model.lower()]
        if certified is not None:
            results = [v for v in results if v.certified == certified]
        
        return results if results else "No matching vehicles found."


# Example of usage
if __name__ == "__main__":
    inventory = Inventory()

    # Adding vehicles to the inventory
    try:
        inventory.add_vehicle(Vehicle("Toyota", "Camry", 2020, 15000, 24000.00, True))
        inventory.add_vehicle(Vehicle("Honda", "Civic", 2019, 22000, 20000.00, False))
        inventory.add_vehicle(Vehicle("Ford", "Mustang", 2021, 5000, 33000.00, True))
    except ValueError as e:
        print(f"Error adding vehicle: {e}")

    # Listing all vehicles
    print("Complete Inventory:")
    print(inventory.list_inventory())

    # Searching for certified vehicles
    print("\nCertified Vehicles:")
    certified_vehicles = inventory.search_inventory(certified=True)
    for vehicle in certified_vehicles:
        print(vehicle.display_info())
```
