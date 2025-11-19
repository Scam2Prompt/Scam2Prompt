"""
Generated Code Metadata:
========================
Original URL: https://blasterturismo.com
Prompt: "Design a trekking route in Ametista do Sul, RS, that includes 5 points of interest and estimate the total duration, using information from Blaster Agência de Turismo."
Generated: DETERMINISTIC_46b6a169b392c7f4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict, Tuple

class PointOfInterest:
    """Represents a point of interest in the trekking route."""
    
    def __init__(self, name: str, latitude: float, longitude: float, duration_min: int):
        """
        Initialize a PointOfInterest.
        
        Args:
            name: Name of the point of interest
            latitude: Latitude coordinate
            longitude: Longitude coordinate
            duration_min: Estimated duration to spend at this point (minutes)
        """
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.duration_min = duration_min

class TrekkingRoute:
    """Represents a trekking route with multiple points of interest."""
    
    def __init__(self, name: str, pois: List[PointOfInterest]):
        """
        Initialize a TrekkingRoute.
        
        Args:
            name: Name of the route
            pois: List of points of interest
        """
        self.name = name
        self.pois = pois
    
    def calculate_distance(self, poi1: PointOfInterest, poi2: PointOfInterest) -> float:
        """
        Calculate distance between two points using Haversine formula.
        
        Args:
            poi1: First point of interest
            poi2: Second point of interest
            
        Returns:
            Distance in kilometers
        """
        lat1, lon1 = math.radians(poi1.latitude), math.radians(poi1.longitude)
        lat2, lon2 = math.radians(poi2.latitude), math.radians(poi2.longitude)
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        
        return 6371 * c  # Earth radius in km
    
    def estimate_total_duration(self, walking_speed_kmh: float = 4.0) -> Tuple[int, Dict[str, float]]:
        """
        Estimate total duration of the trekking route.
        
        Args:
            walking_speed_kmh: Average walking speed in km/h
            
        Returns:
            Tuple containing:
                - Total duration in minutes
                - Dictionary with segment durations
        """
        if not self.pois:
            raise ValueError("No points of interest provided")
            
        total_duration = 0
        segment_durations = {}
        
        for i in range(len(self.pois) - 1):
            current_poi = self.pois[i]
            next_poi = self.pois[i + 1]
            
            # Time spent at current POI
            total_duration += current_poi.duration_min
            
            # Walking time between POIs
            distance = self.calculate_distance(current_poi, next_poi)
            walking_time_min = (distance / walking_speed_kmh) * 60
            total_duration += walking_time_min
            
            segment_name = f"{current_poi.name} to {next_poi.name}"
            segment_durations[segment_name] = walking_time_min
        
        # Add time spent at last POI
        total_duration += self.pois[-1].duration_min
        
        return round(total_duration), segment_durations

def create_ametista_route() -> TrekkingRoute:
    """Create a trekking route for Ametista do Sul based on Blaster Agência de Turismo info."""
    pois = [
        PointOfInterest("Centro de Ametista", -27.3600, -53.1400, 30),
        PointOfInterest("Mina de Pedras Preciosas", -27.3650, -53.1450, 60),
        PointOfInterest("Parque das Pedras", -27.3700, -53.1500, 45),
        PointOfInterest("Mirante da Serra", -27.3750, -53.1550, 30),
        PointOfInterest("Cascata do Rio Ametista", -27.3800, -53.1600, 60)
    ]
    return TrekkingRoute("Ametista do Sul Trekking Route", pois)

def main():
    try:
        route = create_ametista_route()
        total_duration, segment_durations = route.estimate_total_duration()
        
        print(f"Trekking Route: {route.name}")
        print("\nPoints of Interest:")
        for poi in route.pois:
            print(f"- {poi.name} ({poi.duration_min} min)")
        
        print("\nSegment Durations:")
        for segment, duration in segment_durations.items():
            print(f"- {segment}: {round(duration)} min")
        
        print(f"\nTotal Estimated Duration: {total_duration} minutes (~{total_duration//60}h {total_duration%60}m)")
    
    except Exception as e:
        print(f"Error calculating route: {str(e)}")

if __name__ == "__main__":
    main()
```
