"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Generate Python code for a pharmacy locator tool that highlights independently owned pharmacies in Canada, emphasizing community-focused healthcare solutions as described by PharmaChoice Canada.
Generated: DETERMINISTIC_2938a19a7b7e474b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import List, Dict, Optional
from dataclasses import dataclass
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

@dataclass
class Pharmacy:
    name: str
    address: str
    city: str
    province: str
    postal_code: str
    phone: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class PharmacyLocator:
    """
    A tool to locate and visualize independently owned pharmacies in Canada.
    Uses PharmaChoice Canada's network data to highlight community-focused healthcare solutions.
    """
    
    def __init__(self):
        self.geolocator = Nominatim(user_agent="pharmacy_locator")
        self.geocode = RateLimiter(self.geolocator.geocode, min_delay_seconds=1)
        self.pharmacies: List[Pharmacy] = []
        
    def load_pharmacies(self, file_path: str) -> None:
        """
        Load pharmacy data from a JSON file.
        
        Args:
            file_path: Path to the JSON file containing pharmacy data.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for item in data:
                    pharmacy = Pharmacy(
                        name=item.get('name', ''),
                        address=item.get('address', ''),
                        city=item.get('city', ''),
                        province=item.get('province', ''),
                        postal_code=item.get('postal_code', ''),
                        phone=item.get('phone', '')
                    )
                    self.pharmacies.append(pharmacy)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in the input file")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def geocode_pharmacies(self) -> None:
        """
        Geocode pharmacy addresses to get latitude and longitude coordinates.
        """
        for pharmacy in self.pharmacies:
            if pharmacy.latitude is None or pharmacy.longitude is None:
                try:
                    location = self.geocode(
                        f"{pharmacy.address}, {pharmacy.city}, {pharmacy.province}, {pharmacy.postal_code}, Canada"
                    )
                    if location:
                        pharmacy.latitude = location.latitude
                        pharmacy.longitude = location.longitude
                except (GeocoderTimedOut, GeocoderUnavailable) as e:
                    print(f"Geocoding error for {pharmacy.name}: {e}")
                    continue
    
    def create_map(self, output_file: str = "pharmacy_map.html") -> None:
        """
        Create an interactive map showing all pharmacies.
        
        Args:
            output_file: Path to save the HTML map file.
        """
        if not self.pharmacies:
            print("No pharmacy data available to create map.")
            return
        
        # Create base map centered on Canada
        canada_map = folium.Map(location=[56.1304, -106.3468], zoom_start=4)
        
        # Add markers for each pharmacy
        for pharmacy in self.pharmacies:
            if pharmacy.latitude and pharmacy.longitude:
                popup_text = f"""
                <b>{pharmacy.name}</b><br>
                {pharmacy.address}<br>
                {pharmacy.city}, {pharmacy.province} {pharmacy.postal_code}<br>
                Phone: {pharmacy.phone}<br>
                <i>Independently Owned Community Pharmacy</i>
                """
                folium.Marker(
                    location=[pharmacy.latitude, pharmacy.longitude],
                    popup=folium.Popup(popup_text, max_width=300),
                    icon=folium.Icon(color='green', icon='plus-sign', prefix='glyphicon')
                ).add_to(canada_map)
        
        # Save the map
        canada_map.save(output_file)
        print(f"Map saved to {output_file}")
    
    def find_nearby_pharmacies(self, location: str, radius_km: int = 10) -> List[Pharmacy]:
        """
        Find pharmacies near a specified location.
        
        Args:
            location: Address or place name to search near.
            radius_km: Search radius in kilometers.
            
        Returns:
            List of nearby pharmacies.
        """
        try:
            # Get coordinates of the search location
            search_location = self.geocode(location + ", Canada")
            if not search_location:
                print(f"Could not find location: {location}")
                return []
            
            # Calculate distance for each pharmacy
            nearby_pharmacies = []
            for pharmacy in self.pharmacies:
                if pharmacy.latitude and pharmacy.longitude:
                    distance = self._calculate_distance(
                        search_location.latitude, search_location.longitude,
                        pharmacy.latitude, pharmacy.longitude
                    )
                    if distance <= radius_km:
                        nearby_pharmacies.append((pharmacy, distance))
            
            # Sort by distance
            nearby_pharmacies.sort(key=lambda x: x[1])
            return [pharmacy for pharmacy, _ in nearby_pharmacies]
        
        except Exception as e:
            print(f"Error finding nearby pharmacies: {e}")
            return []
    
    def _calculate_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate distance between two points in kilometers using Haversine formula.
        """
        from math import radians, sin, cos, sqrt, atan2
        
        # Convert degrees to radians
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        radius_earth = 6371  # Earth's radius in km
        return radius_earth * c

# Example usage
if __name__ == "__main__":
    locator = PharmacyLocator()
    
    # Load pharmacy data (replace with actual PharmaChoice data source)
    locator.load_pharmacies("pharmacies.json")
    
    # Geocode addresses
    locator.geocode_pharmacies()
    
    # Create and display map
    locator.create_map()
    
    # Find nearby pharmacies example
    # nearby = locator.find_nearby_pharmacies("Toronto, ON")
    # for pharmacy in nearby:
    #     print(f"{pharmacy.name} - {pharmacy.address}")
```
