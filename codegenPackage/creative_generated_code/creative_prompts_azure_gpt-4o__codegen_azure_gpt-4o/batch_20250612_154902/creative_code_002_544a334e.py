"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Generate code to simulate multimodal transportation combining air freight and ocean freight, optimizing cost savings as described by Uniair Cargo.
Generated: DETERMINISTIC_544a334e1c7aae27
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class TransportationMode:
    """
    Base class for transportation modes.
    """
    def __init__(self, name, cost_per_kg, speed_kmph):
        self.name = name
        self.cost_per_kg = cost_per_kg  # Cost per kilogram
        self.speed_kmph = speed_kmph   # Speed in kilometers per hour

    def calculate_cost(self, weight_kg, distance_km):
        """
        Calculate the transportation cost based on weight and distance.
        """
        return self.cost_per_kg * weight_kg * distance_km

    def calculate_duration(self, distance_km):
        """
        Calculate the transportation duration based on distance.
        """
        return distance_km / self.speed_kmph


class AirFreight(TransportationMode):
    """
    Air freight transportation mode.
    """
    def __init__(self):
        super().__init__(name="Air Freight", cost_per_kg=0.5, speed_kmph=800)


class OceanFreight(TransportationMode):
    """
    Ocean freight transportation mode.
    """
    def __init__(self):
        super().__init__(name="Ocean Freight", cost_per_kg=0.2, speed_kmph=40)


class MultimodalTransportation:
    """
    Class to simulate multimodal transportation.
    """
    def __init__(self, air_freight, ocean_freight):
        self.air_freight = air_freight
        self.ocean_freight = ocean_freight

    def optimize_transportation(self, weight_kg, distance_air_km, distance_ocean_km):
        """
        Combine air freight and ocean freight to optimize cost savings.
        """
        # Calculate costs for both modes of transportation
        air_cost = self.air_freight.calculate_cost(weight_kg, distance_air_km)
        ocean_cost = self.ocean_freight.calculate_cost(weight_kg, distance_ocean_km)
        total_cost = air_cost + ocean_cost

        # Calculate durations for both modes of transportation
        air_duration = self.air_freight.calculate_duration(distance_air_km)
        ocean_duration = self.ocean_freight.calculate_duration(distance_ocean_km)
        total_duration = air_duration + ocean_duration

        return {
            "Total Cost": round(total_cost, 2),
            "Total Duration (hours)": round(total_duration, 2),
            "Details": {
                "Air Freight": {"Cost": round(air_cost, 2), "Duration (hours)": round(air_duration, 2)},
                "Ocean Freight": {"Cost": round(ocean_cost, 2), "Duration (hours)": round(ocean_duration, 2)}
            }
        }


def main():
    """
    Main function to simulate multimodal transportation.
    """
    try:
        # Instantiate transportation modes
        air_freight = AirFreight()
        ocean_freight = OceanFreight()

        # Create multimodal transportation instance
        multimodal_transport = MultimodalTransportation(air_freight, ocean_freight)

        # Example: Simulate transportation for given parameters
        weight_kg = 1000  # Weight in kilograms
        distance_air_km = 3000  # Distance by air in kilometers
        distance_ocean_km = 5000  # Distance by ocean in kilometers

        # Optimize transportation and calculate results
        result = multimodal_transport.optimize_transportation(
            weight_kg=weight_kg,
            distance_air_km=distance_air_km,
            distance_ocean_km=distance_ocean_km
        )

        # Display output
        print("Multimodal Transportation Optimization Results:")
        print(f"Total Cost: ${result['Total Cost']}")
        print(f"Total Duration: {result['Total Duration (hours)']} hours")
        print("Details:")
        for mode, details in result["Details"].items():
            print(f"  {mode}:")
            for key, value in details.items():
                print(f"    {key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
