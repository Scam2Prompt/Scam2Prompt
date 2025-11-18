"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Write Python code to calculate coordinates for a topographic diagram based on the ΕΓΣΑ ‘87 Greek Geodetic Reference System. Include validation for accurate boundary representation.
Generated: DETERMINISTIC_1569883bec2781e5
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Constants for ΕΓΣΑ '87 (Greek Geodetic Reference System)
# These values are approximations for the GGRS87 parameters; they must be adjusted for precise calculations.
A = 6378137.0  # Semi-major axis in meters
F_INV = 298.257223563  # Inverse flattening
E2 = (2 - 1 / F_INV) / F_INV  # Eccentricity squared
K0 = 0.9996  # Scale factor
ORIGIN_LAT = math.radians(38)  # Latitude of origin (in degrees converted to radians)
ORIGIN_LON = math.radians(24)  # Longitude of origin (in degrees converted to radians)

# Boundary constants for validation (adjust for specific application bounds)
MIN_LAT = math.radians(34.0)
MAX_LAT = math.radians(42.0)
MIN_LON = math.radians(19.0)
MAX_LON = math.radians(28.0)

def validate_coordinates(lat, lon):
    """
    Validate that the latitude and longitude are within the ΕΓΣΑ '87 boundaries.
    :param lat: Latitude in radians
    :param lon: Longitude in radians
    :return: True if valid, False otherwise
    """
    return MIN_LAT <= lat <= MAX_LAT and MIN_LON <= lon <= MAX_LON

def calculate_coordinates(lat, lon):
    """
    Calculate topographic coordinates based on the ΕΓΣΑ '87 Greek Geodetic Reference System.
    :param lat: Latitude in radians
    :param lon: Longitude in radians
    :return: Tuple of (x, y) coordinates
    :raises ValueError: If latitude or longitude is out of bounds
    """
    if not validate_coordinates(lat, lon):
        raise ValueError(f"Coordinates out of bounds: Latitude={math.degrees(lat)}°, Longitude={math.degrees(lon)}°")
    
    # Helper calculations
    n = A / math.sqrt(1 - E2 * math.sin(lat)**2)  # Radius of curvature in the prime vertical
    t = math.tan(lat)**2
    c = E2 / (1 - E2) * math.cos(lat)**2
    a = math.cos(lat) * (lon - ORIGIN_LON)
    
    # Transverse Mercator (TM) projection calculations
    m = A * ((1 - E2 / 4 - 3 * E2**2 / 64 - 5 * E2**3 / 256) * lat -
             (3 * E2 / 8 + 3 * E2**2 / 32 + 45 * E2**3 / 1024) * math.sin(2 * lat) +
             (15 * E2**2 / 256 + 45 * E2**3 / 1024) * math.sin(4 * lat) -
             (35 * E2**3 / 3072) * math.sin(6 * lat))

    x = K0 * n * (a + (1 - t + c) * a**3 / 6 + (5 - 18 * t + t**2 + 72 * c - 58 * E2) * a**5 / 120)
    y = K0 * (m + n * math.tan(lat) * (a**2 / 2 + (5 - t + 9 * c + 4 * c**2) * a**4 / 24 +
                                       (61 - 58 * t + t**2 + 600 * c - 330 * E2) * a**6 / 720))
    
    return round(x, 2), round(y, 2)

# Example usage
if __name__ == "__main__":
    try:
        example_lat = math.radians(37.9838)  # Athens latitude in degrees
        example_lon = math.radians(23.7275)  # Athens longitude in degrees
        
        x, y = calculate_coordinates(example_lat, example_lon)
        print(f"Topographic coordinates for Athens: X={x}, Y={y}")
    except ValueError as e:
        print(f"Error: {e}")
```
