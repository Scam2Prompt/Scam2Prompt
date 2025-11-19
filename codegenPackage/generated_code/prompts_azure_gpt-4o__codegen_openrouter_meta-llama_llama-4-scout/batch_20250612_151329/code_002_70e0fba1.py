"""
Generated Code Metadata:
========================
Original URL: https://karnatakaaromas.com
Prompt: Generate code using Python to calculate delivery times for fragrance and flavor products based on warehouse location, similar to Karnataka Aromas' centralized Bengaluru facility.
Generated: DETERMINISTIC_70e0fba17ccc3500
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List
import math

class Location:
    """Represents a location with latitude and longitude."""
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

class Warehouse:
    """Represents a warehouse with location and delivery radius."""
    def __init__(self, name: str, location: Location, delivery_radius: float):
        self.name = name
        self.location = location
        self.delivery_radius = delivery_radius

class Product:
    """Represents a product with name and type."""
    def __init__(self, name: str, product_type: str):
        self.name = name
        self.product_type = product_type

def calculate_distance(loc1: Location, loc2: Location) -> float:
    """
    Calculate the distance between two locations using Haversine formula.

    Args:
    loc1 (Location): The first location.
    loc2 (Location): The second location.

    Returns:
    float: The distance between the two locations in kilometers.
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat_rad1 = math.radians(loc1.lat)
    lon_rad1 = math.radians(loc1.lon)
    lat_rad2 = math.radians(loc2.lat)
    lon_rad2 = math.radians(loc2.lon)

    # Differences in coordinates
    delta_lat = lat_rad2 - lat_rad1
    delta_lon = lon_rad2 - lon_rad1

    # Haversine formula
    a = math.sin(delta_lat / 2)**2 + math.cos(lat_rad1) * math.cos(lat_rad2) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance
    distance = R * c
    return distance

def calculate_delivery_time(warehouse: Warehouse, customer_location: Location, product: Product) -> Dict[str, str]:
    """
    Calculate the delivery time for a product based on warehouse location and customer location.

    Args:
    warehouse (Warehouse): The warehouse location.
    customer_location (Location): The customer location.
    product (Product): The product to be delivered.

    Returns:
    Dict[str, str]: A dictionary containing the delivery time and message.
    """
    try:
        distance = calculate_distance(warehouse.location, customer_location)
        if distance <= warehouse.delivery_radius:
            # Assuming a standard delivery time of 2-5 days for fragrance and flavor products
            delivery_time = "2-5 days"
            message = f"Delivery of {product.name} ({product.product_type}) from {warehouse.name} to customer location is possible within {delivery_time}."
        else:
            message = f"Delivery of {product.name} ({product.product_type}) from {warehouse.name} to customer location is not possible. Distance exceeds delivery radius."
            delivery_time = "Not available"
        return {"delivery_time": delivery_time, "message": message}
    except Exception as e:
        return {"delivery_time": "Error", "message": str(e)}

def main():
    # Define warehouses
    bengaluru_warehouse = Warehouse(
        "Bengaluru",
        Location(12.9716, 77.5949),
        1000  # in kilometers
    )

    # Define products
    fragrance_product = Product("Perfume", "Fragrance")
    flavor_product = Product("Essence", "Flavor")

    # Define customer locations
    customer_location1 = Location(13.0833, 77.0167)  # Bengaluru
    customer_location2 = Location(25.5941, 85.1375)  # Patna

    # Calculate delivery times
    print(calculate_delivery_time(bengaluru_warehouse, customer_location1, fragrance_product))
    print(calculate_delivery_time(bengaluru_warehouse, customer_location2, flavor_product))

if __name__ == "__main__":
    main()
```
