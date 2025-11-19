"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sun-ra.space
Prompt: How can I implement a project using libraries discussed on sun-ra.space for astronomical research?
Generated: DETERMINISTIC_8ba2629143b98044
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Astronomical Research Project

This Python script uses the Astropy and Astroquery libraries (commonly used for astronomy research) 
to gather data about a celestial object and analyze it. The script queries the SIMBAD database 
for an object's information and calculates its angular distance from a reference point in the sky.

Requirements:
- Install `astropy` and `astroquery` libraries before running the script:
    pip install astropy astroquery

"""

# Import necessary libraries
from astroquery.simbad import Simbad  # For querying astronomical databases
from astropy.coordinates import SkyCoord  # For handling celestial coordinates
from astropy import units as u  # For working with units
import sys  # For handling script execution errors

def query_celestial_object(object_name):
    """
    Queries the SIMBAD database for basic information about a celestial object.
    
    :param object_name: Name of the celestial object to query (e.g., "Betelgeuse").
    :return: A dictionary containing object information or None if the object is not found.
    """
    try:
        # Customizing the Simbad query to include coordinates
        Simbad.add_votable_fields('coordinates')
        result = Simbad.query_object(object_name)

        if result is None:
            print(f"Error: '{object_name}' not found in the SIMBAD database.")
            return None
        
        # Extracting relevant details
        object_info = {
            "Object Name": result['MAIN_ID'][0].decode('utf-8'),
            "RA": result['RA'][0],  # Right Ascension
            "DEC": result['DEC'][0],  # Declination
        }
        return object_info

    except Exception as e:
        print(f"An error occurred while querying the SIMBAD database: {e}")
        return None


def calculate_angular_distance(coord1, coord2):
    """
    Calculates the angular distance between two celestial objects.
    
    :param coord1: First object's coordinates as an `astropy.coordinates.SkyCoord` object.
    :param coord2: Second object's coordinates as an `astropy.coordinates.SkyCoord` object.
    :return: Angular distance in degrees.
    """
    try:
        # Calculate angular separation
        angular_distance = coord1.separation(coord2)
        return angular_distance.to(u.deg)
    except Exception as e:
        print(f"Error calculating angular distance: {e}")
        return None


def main():
    """
    Main function to demonstrate querying celestial objects and calculating angular distances.
    """
    try:
        # Example celestial object and reference point
        object_name = "Betelgeuse"  # Replace with your desired object name
        reference_coords = SkyCoord(ra=5.0 * u.hourangle, dec=0.0 * u.deg)  # Reference point (example)

        # Query information about the celestial object
        object_info = query_celestial_object(object_name)
        if object_info is None:
            sys.exit("No valid celestial object retrieved. Exiting.")

        print(f"Object Information Retrieved: {object_info}")

        # Convert queried coordinates to a SkyCoord object
        object_coords = SkyCoord(
            ra=object_info["RA"], dec=object_info["DEC"], unit=(u.hourangle, u.deg)
        )

        # Calculate angular distance from reference point
        distance = calculate_angular_distance(object_coords, reference_coords)
        if distance is not None:
            print(f"Angular Distance from Reference Point: {distance:.2f}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
