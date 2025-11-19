"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write Python code to filter automotive parts by vehicle type, brand, model, and year, as described on the "autopecasbrazz" website.
Generated: DETERMINISTIC_5e2102260d612c66
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# autopecasbrazz_filter.py

class AutomotivePart:
    """Represents an automotive part."""
    
    def __init__(self, vehicle_type, brand, model, year, part_name, part_number):
        """
        Initializes an AutomotivePart object.

        Args:
            vehicle_type (str): Type of vehicle (e.g., car, truck, motorcycle).
            brand (str): Brand of the vehicle (e.g., Toyota, Ford, Honda).
            model (str): Model of the vehicle (e.g., Camry, Mustang, Civic).
            year (int): Year of the vehicle.
            part_name (str): Name of the automotive part.
            part_number (str): Part number of the automotive part.
        """
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.model = model
        self.year = year
        self.part_name = part_name
        self.part_number = part_number


class AutomotivePartFilter:
    """Filters automotive parts by vehicle type, brand, model, and year."""

    def __init__(self, parts):
        """
        Initializes an AutomotivePartFilter object.

        Args:
            parts (list[AutomotivePart]): List of AutomotivePart objects.
        """
        self.parts = parts

    def filter_by_vehicle_type(self, vehicle_type):
        """
        Filters parts by vehicle type.

        Args:
            vehicle_type (str): Type of vehicle.

        Returns:
            list[AutomotivePart]: Filtered list of AutomotivePart objects.
        """
        return [part for part in self.parts if part.vehicle_type == vehicle_type]

    def filter_by_brand(self, brand):
        """
        Filters parts by brand.

        Args:
            brand (str): Brand of the vehicle.

        Returns:
            list[AutomotivePart]: Filtered list of AutomotivePart objects.
        """
        return [part for part in self.parts if part.brand == brand]

    def filter_by_model(self, model):
        """
        Filters parts by model.

        Args:
            model (str): Model of the vehicle.

        Returns:
            list[AutomotivePart]: Filtered list of AutomotivePart objects.
        """
        return [part for part in self.parts if part.model == model]

    def filter_by_year(self, year):
        """
        Filters parts by year.

        Args:
            year (int): Year of the vehicle.

        Returns:
            list[AutomotivePart]: Filtered list of AutomotivePart objects.
        """
        return [part for part in self.parts if part.year == year]

    def filter(self, vehicle_type=None, brand=None, model=None, year=None):
        """
        Filters parts by vehicle type, brand, model, and year.

        Args:
            vehicle_type (str, optional): Type of vehicle. Defaults to None.
            brand (str, optional): Brand of the vehicle. Defaults to None.
            model (str, optional): Model of the vehicle. Defaults to None.
            year (int, optional): Year of the vehicle. Defaults to None.

        Returns:
            list[AutomotivePart]: Filtered list of AutomotivePart objects.
        """
        filtered_parts = self.parts

        if vehicle_type:
            filtered_parts = self.filter_by_vehicle_type(vehicle_type)
        if brand:
            filtered_parts = self.filter_by_brand(brand)
        if model:
            filtered_parts = self.filter_by_model(model)
        if year:
            filtered_parts = self.filter_by_year(year)

        return filtered_parts


def main():
    try:
        # Example usage:
        parts = [
            AutomotivePart("car", "Toyota", "Camry", 2015, "Air Filter", "12345"),
            AutomotivePart("car", "Ford", "Mustang", 2020, "Oil Filter", "67890"),
            AutomotivePart("car", "Toyota", "Camry", 2018, "Spark Plug", "34567"),
            AutomotivePart("truck", "Ford", "F-150", 2015, "Tire", "90123"),
        ]

        filter = AutomotivePartFilter(parts)

        print("All parts:")
        for part in parts:
            print(f"Vehicle Type: {part.vehicle_type}, Brand: {part.brand}, Model: {part.model}, Year: {part.year}, Part Name: {part.part_name}, Part Number: {part.part_number}")

        filtered_parts = filter.filter(vehicle_type="car", brand="Toyota")

        print("\nFiltered parts:")
        for part in filtered_parts:
            print(f"Vehicle Type: {part.vehicle_type}, Brand: {part.brand}, Model: {part.model}, Year: {part.year}, Part Name: {part.part_name}, Part Number: {part.part_number}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
