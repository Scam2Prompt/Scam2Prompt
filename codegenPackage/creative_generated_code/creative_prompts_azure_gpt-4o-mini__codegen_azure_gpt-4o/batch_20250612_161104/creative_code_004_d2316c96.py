"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krajkovac.rs
Prompt: Design a library function that calculates the distance from Niš to Krajkovac, integrating points of interest along the way, such as the Jastrebac mountain.
Generated: DETERMINISTIC_d2316c96150c0d97
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class DistanceCalculator:
    """
    A library for calculating distances between locations and including points of interest along the route.
    """

    def __init__(self):
        # Coordinates for Niš, Krajkovac, and Jastrebac Mountain (latitude, longitude)
        self.locations = {
            "Nis": (43.3209, 21.8958),
            "Krajkovac": (43.2951, 21.6823),
            "Jastrebac": (43.3106, 21.6075)
        }

    def haversine_distance(self, coord1, coord2):
        """
        Calculate the great-circle distance between two points on the Earth.
        :param coord1: Tuple containing latitude and longitude of the first point (lat1, lon1).
        :param coord2: Tuple containing latitude and longitude of the second point (lat2, lon2).
        :return: Distance in kilometers.
        """
        R = 6371  # Radius of the Earth in kilometers

        lat1, lon1 = coord1
        lat2, lon2 = coord2

        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c

    def calculate_route_distance(self):
        """
        Calculate the total distance from Niš to Krajkovac, including the Jastrebac Mountain as a point of interest.
        :return: Total distance in kilometers.
        """
        try:
            # Retrieve coordinates for each location
            nis = self.locations["Nis"]
            jastrebac = self.locations["Jastrebac"]
            krajkovac = self.locations["Krajkovac"]

            # Calculate distances between each segment
            distance_nis_to_jastrebac = self.haversine_distance(nis, jastrebac)
            distance_jastrebac_to_krajkovac = self.haversine_distance(jastrebac, krajkovac)

            # Total distance
            total_distance = distance_nis_to_jastrebac + distance_jastrebac_to_krajkovac

            return total_distance

        except KeyError as e:
            raise ValueError(f"Invalid location key: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the route distance: {e}")

# Example usage of the DistanceCalculator library
if __name__ == "__main__":
    distance_calculator = DistanceCalculator()
    try:
        total_distance = distance_calculator.calculate_route_distance()
        print(f"The total distance from Niš to Krajkovac via Jastrebac Mountain is {total_distance:.2f} km.")
    except Exception as error:
        print(f"Error: {error}")
```
