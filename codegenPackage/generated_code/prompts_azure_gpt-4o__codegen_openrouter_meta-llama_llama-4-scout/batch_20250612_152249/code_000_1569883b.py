"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Write Python code to calculate coordinates for a topographic diagram based on the ΕΓΣΑ ‘87 Greek Geodetic Reference System. Include validation for accurate boundary representation.
Generated: DETERMINISTIC_1569883bec2781e5
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def egsea87_to_wgs84(x, y):
    """
    Convert ΕΓΣΑ '87 coordinates to WGS84 coordinates.

    :param x: ΕΓΣΑ '87 x coordinate
    :param y: ΕΓΣΑ '87 y coordinate
    :return: WGS84 latitude, WGS84 longitude
    """
    # ΕΓΣΑ '87 to WGS84 transformation parameters
    a = 6375.145  # semi-major axis
    b = 6375.145  # semi-minor axis
    e2 = 0.0067681702  # eccentricity squared

    # Perform the transformation
    lat = math.atan((y / a) / (1 - (e2 * (x / a)) ** 2)) * (180 / math.pi)
    lon = math.atan((x / (a * math.cos(lat * math.pi / 180)))) * (180 / math.pi)

    # Apply the Helmert transformation
    tx, ty, tz = 200.0, 300.0, 340.0  # translation parameters
    rx, ry, rz = 0.0067, 0.0042, 0.0081  # rotation parameters
    s = 0.000001  # scale factor

    x_wgs84 = x * (1 + s) + ty * rz - tz * ry + tx
    y_wgs84 = y * (1 + s) + tz * rx - tx * rz + ty
    z_wgs84 = z * (1 + s) + tx * ry - ty * rx + tz

    # Convert to latitude and longitude
    wgs84_lat = math.asin(z_wgs84 / math.sqrt(x_wgs84 ** 2 + y_wgs84 ** 2 + z_wgs84 ** 2)) * (180 / math.pi)
    wgs84_lon = math.atan2(y_wgs84, x_wgs84) * (180 / math.pi)

    return wgs84_lat, wgs84_lon


def calculate_topographic_diagram(x_min, x_max, y_min, y_max, num_points=100):
    """
    Calculate coordinates for a topographic diagram.

    :param x_min: Minimum x coordinate
    :param x_max: Maximum x coordinate
    :param y_min: Minimum y coordinate
    :param y_max: Maximum y coordinate
    :param num_points: Number of points to generate
    :return: List of (x, y) coordinates
    """
    # Validate input parameters
    if x_min >= x_max:
        raise ValueError("x_min must be less than x_max")
    if y_min >= y_max:
        raise ValueError("y_min must be less than y_max")

    # Generate coordinates
    x_coords = [x_min + (x_max - x_min) * i / (num_points - 1) for i in range(num_points)]
    y_coords = [y_min + (y_max - y_min) * i / (num_points - 1) for i in range(num_points)]

    # Create a grid of coordinates
    coords = [(x, y) for x in x_coords for y in y_coords]

    # Convert coordinates to WGS84
    wgs84_coords = []
    for x, y in coords:
        try:
            lat, lon = egsea87_to_wgs84(x, y)
            wgs84_coords.append((lat, lon))
        except Exception as e:
            print(f"Error converting coordinates: {e}")

    return wgs84_coords


def main():
    # Example usage
    x_min, x_max = 500000, 700000  # x coordinate bounds
    y_min, y_max = 4500000, 4600000  # y coordinate bounds

    try:
        coords = calculate_topographic_diagram(x_min, x_max, y_min, y_max)
        for coord in coords:
            print(coord)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
