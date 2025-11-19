"""
Generated Code Metadata:
========================
Original URL: https://baochuanco.com
Prompt: Write a script to calculate shipping costs for wire mesh products based on customer location, referencing the international nature of Baochuan Wire Mesh's operations.
Generated: DETERMINISTIC_f8095b5da073c996
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_cost_calculator.py

import math

class Location:
    """Represents a geographic location with latitude and longitude."""
    def __init__(self, city, country, latitude, longitude):
        """
        Initializes a Location object.

        Args:
            city (str): City name.
            country (str): Country name.
            latitude (float): Latitude coordinate.
            longitude (float): Longitude coordinate.
        """
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude

class ShippingCalculator:
    """Calculates shipping costs for wire mesh products based on customer location."""
    def __init__(self, base_cost, rate_per_km):
        """
        Initializes a ShippingCalculator object.

        Args:
            base_cost (float): Base shipping cost.
            rate_per_km (float): Rate per kilometer.
        """
        self.base_cost = base_cost
        self.rate_per_km = rate_per_km

    def calculate_distance(self, origin, destination):
        """
        Calculates the distance between two locations using the Haversine formula.

        Args:
            origin (Location): Origin location.
            destination (Location): Destination location.

        Returns:
            float: Distance in kilometers.
        """
        # Convert coordinates to radians
        lat1, lon1 = math.radians(origin.latitude), math.radians(origin.longitude)
        lat2, lon2 = math.radians(destination.latitude), math.radians(destination.longitude)

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = 6371 * c  # Radius of the Earth in kilometers

        return distance

    def calculate_shipping_cost(self, origin, destination):
        """
        Calculates the shipping cost based on the distance between two locations.

        Args:
            origin (Location): Origin location.
            destination (Location): Destination location.

        Returns:
            float: Shipping cost.
        """
        try:
            distance = self.calculate_distance(origin, destination)
            shipping_cost = self.base_cost + (distance * self.rate_per_km)
            return shipping_cost
        except Exception as e:
            print(f"Error calculating shipping cost: {str(e)}")
            return None

def main():
    # Define locations
    baochuan_wire_mesh = Location("Baochuan", "China", 31.2304, 121.4737)
    new_york = Location("New York", "USA", 40.7128, -74.0060)
    london = Location("London", "UK", 51.5074, -0.1278)

    # Initialize shipping calculator
    calculator = ShippingCalculator(base_cost=100, rate_per_km=0.05)

    # Calculate shipping costs
    ny_shipping_cost = calculator.calculate_shipping_cost(baochuan_wire_mesh, new_york)
    london_shipping_cost = calculator.calculate_shipping_cost(baochuan_wire_mesh, london)

    # Print results
    print(f"Shipping cost to New York: ${ny_shipping_cost:.2f}")
    print(f"Shipping cost to London: ${london_shipping_cost:.2f}")

if __name__ == "__main__":
    main()
```
