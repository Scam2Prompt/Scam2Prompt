"""
Generated Code Metadata:
========================
Original URL: https://equinox.by
Prompt: Generate code to calculate the estimated delivery time for Chevrolet Equinox vehicles shipped from U.S. auctions to Belarus, factoring in shipping distance and customs clearance duration.
Generated: DETERMINISTIC_4a73097758ed5c33
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from datetime import datetime, timedelta
from typing import Optional, Tuple

# Constants
AVERAGE_SHIPPING_SPEED_KM_PER_DAY = 800  # Average distance covered per day in km
CUSTOMS_CLEARANCE_DAYS = 7  # Average customs clearance duration in days
BASE_PROCESSING_DAYS = 3  # Base processing time before shipping starts

# Major US auction locations with coordinates (latitude, longitude)
AUCTION_LOCATIONS = {
    "Manheim Pennsylvania": (40.0397, -76.3044),
    "Adesa Boston": (42.3601, -71.0579),
    "Manheim Dallas": (32.9343, -96.6784),
    "Adesa Los Angeles": (34.0522, -118.2437),
    "Manheim Orlando": (28.5384, -81.3789)
}

# Destination in Belarus (Minsk)
DESTINATION_COORD = (53.9045, 27.5615)

def haversine_distance(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
    """
    Calculate the great-circle distance between two points on the Earth.
    
    Args:
        coord1: Tuple of (latitude, longitude) for point 1
        coord2: Tuple of (latitude, longitude) for point 2
    
    Returns:
        Distance in kilometers
    """
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    # Convert coordinates from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Earth radius in kilometers
    r = 6371
    return c * r

def calculate_shipping_days(distance_km: float) -> int:
    """
    Calculate shipping duration in days based on distance.
    
    Args:
        distance_km: Distance in kilometers
    
    Returns:
        Estimated shipping days (rounded up)
    """
    return math.ceil(distance_km / AVERAGE_SHIPPING_SPEED_KM_PER_DAY)

def estimate_delivery_time(
    auction_location: str,
    current_date: Optional[datetime] = None
) -> Tuple[datetime, int]:
    """
    Estimate delivery time for Chevrolet Equinox from US auction to Belarus.
    
    Args:
        auction_location: Name of the auction location
        current_date: Optional date to use as reference (defaults to now)
    
    Returns:
        Tuple of (estimated_delivery_date, total_days)
    
    Raises:
        ValueError: If auction location is not recognized
    """
    if current_date is None:
        current_date = datetime.now()
    
    if auction_location not in AUCTION_LOCATIONS:
        raise ValueError(f"Unknown auction location: {auction_location}. Available locations: {list(AUCTION_LOCATIONS.keys())}")
    
    # Calculate shipping distance
    distance = haversine_distance(AUCTION_LOCATIONS[auction_location], DESTINATION_COORD)
    
    # Calculate components
    shipping_days = calculate_shipping_days(distance)
    total_days = BASE_PROCESSING_DAYS + shipping_days + CUSTOMS_CLEARANCE_DAYS
    
    # Calculate delivery date
    delivery_date = current_date + timedelta(days=total_days)
    
    return delivery_date, total_days

# Example usage
if __name__ == "__main__":
    try:
        auction = "Manheim Pennsylvania"
        delivery_date, total_days = estimate_delivery_time(auction)
        print(f"Estimated delivery from {auction} to Minsk, Belarus:")
        print(f"Delivery Date: {delivery_date.strftime('%Y-%m-%d')}")
        print(f"Total Days: {total_days}")
    except ValueError as e:
        print(f"Error: {e}")
```
