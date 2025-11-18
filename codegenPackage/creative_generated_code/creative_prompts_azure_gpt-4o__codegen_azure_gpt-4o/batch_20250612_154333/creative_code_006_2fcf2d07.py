"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exytrade.com
Prompt: Provide a Python script to manage domestic and international holiday packages, including flight and hotel bookings, as described by Exytrade.
Generated: DETERMINISTIC_2fcf2d07b6b4f95c
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class HolidayPackage:
    """
    Class to manage holiday packages, including flight and hotel bookings
    """
    
    def __init__(self, package_id, name, type, flight_details, hotel_details):
        """
        Initialize a holiday package instance.
        
        :param package_id: Unique identifier for the package
        :param name: Name of the holiday package
        :param type: Type of package ('domestic' or 'international')
        :param flight_details: Dictionary containing flight booking details
        :param hotel_details: Dictionary containing hotel booking details
        """
        self.package_id = package_id
        self.name = name
        self.type = type.lower()  # Ensure type is lowercase
        self.flight_details = flight_details
        self.hotel_details = hotel_details

    def to_dict(self):
        """
        Convert the HolidayPackage instance to a dictionary format for serialization.
        
        :return: Dictionary representation of the package
        """
        return {
            "package_id": self.package_id,
            "name": self.name,
            "type": self.type,
            "flight_details": self.flight_details,
            "hotel_details": self.hotel_details,
        }


class HolidayPackageManager:
    """
    Class to manage a collection of holiday packages.
    """

    def __init__(self):
        """
        Initialize the HolidayPackageManager instance.
        """
        self.packages = {}

    def add_package(self, package):
        """
        Add a holiday package to the manager.

        :param package: HolidayPackage instance
        :raises ValueError: If the package ID already exists
        """
        if package.package_id in self.packages:
            raise ValueError(f"Package ID {package.package_id} already exists.")
        self.packages[package.package_id] = package

    def remove_package(self, package_id):
        """
        Remove a holiday package by its ID.

        :param package_id: ID of the package to remove
        :raises KeyError: If the package ID does not exist
        """
        if package_id not in self.packages:
            raise KeyError(f"Package ID {package_id} not found.")
        del self.packages[package_id]

    def get_package(self, package_id):
        """
        Retrieve a holiday package by its ID.

        :param package_id: ID of the package to retrieve
        :return: HolidayPackage instance
        :raises KeyError: If the package ID does not exist
        """
        if package_id not in self.packages:
            raise KeyError(f"Package ID {package_id} not found.")
        return self.packages[package_id]

    def list_packages(self):
        """
        List all holiday packages.

        :return: List of dictionaries representing all packages
        """
        return [package.to_dict() for package in self.packages.values()]

    def save_packages_to_file(self, filename):
        """
        Save all holiday packages to a JSON file.

        :param filename: Name of the file to save the packages to
        :raises IOError: If an error occurs during file writing
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.list_packages(), file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write to file {filename}: {e}")

    def load_packages_from_file(self, filename):
        """
        Load holiday packages from a JSON file.

        :param filename: Name of the file to load packages from
        :raises IOError: If an error occurs during file reading
        """
        try:
            with open(filename, "r") as file:
                packages_data = json.load(file)
                for package_data in packages_data:
                    package = HolidayPackage(
                        package_id=package_data["package_id"],
                        name=package_data["name"],
                        type=package_data["type"],
                        flight_details=package_data["flight_details"],
                        hotel_details=package_data["hotel_details"],
                    )
                    self.add_package(package)
        except IOError as e:
            raise IOError(f"Failed to read file {filename}: {e}")
        except Exception as e:
            raise ValueError(f"Error processing file {filename}: {e}")


# Example usage (comment out or remove in production)
if __name__ == "__main__":
    manager = HolidayPackageManager()

    # Add example packages
    domestic_package = HolidayPackage(
        package_id=1,
        name="Beach Resort Getaway",
        type="domestic",
        flight_details={"airline": "AirX", "departure": "CityA", "arrival": "CityB"},
        hotel_details={"hotel_name": "Beach Resort", "nights": 3},
    )

    international_package = HolidayPackage(
        package_id=2,
        name="European Adventure",
        type="international",
        flight_details={"airline": "EuroFly", "departure": "CityC", "arrival": "CityD"},
        hotel_details={"hotel_name": "Luxury Inn", "nights": 5},
    )

    try:
        manager.add_package(domestic_package)
        manager.add_package(international_package)

        # List all packages
        print("Current Packages:")
        print(manager.list_packages())

        # Save packages to a file
        manager.save_packages_to_file("packages.json")

        # Load packages from a file
        manager.load_packages_from_file("packages.json")
        print("\nPackages loaded from file:")
        print(manager.list_packages())

    except Exception as e:
        print(f"Error: {e}")
```
