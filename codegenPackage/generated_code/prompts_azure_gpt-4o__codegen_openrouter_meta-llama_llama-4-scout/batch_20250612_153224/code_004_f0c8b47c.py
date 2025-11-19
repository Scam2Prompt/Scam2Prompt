"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Create a function to filter job listings by industry (e.g., healthcare, automation) and radius, as described on jobONE’s search interface.
Generated: DETERMINISTIC_f0c8b47c958ea783
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict

class JobListing:
    """Represents a job listing with its attributes."""
    
    def __init__(self, id: int, title: str, industry: str, latitude: float, longitude: float):
        """
        Initializes a JobListing object.

        Args:
        id (int): Unique identifier for the job listing.
        title (str): Title of the job listing.
        industry (str): Industry of the job listing.
        latitude (float): Latitude of the job listing location.
        longitude (float): Longitude of the job listing location.
        """
        self.id = id
        self.title = title
        self.industry = industry
        self.latitude = latitude
        self.longitude = longitude


def filter_job_listings(job_listings: List[JobListing], industry: str, radius: float, latitude: float, longitude: float) -> List[JobListing]:
    """
    Filters job listings by industry and radius.

    Args:
    job_listings (List[JobListing]): List of job listings.
    industry (str): Industry to filter by.
    radius (float): Radius in kilometers to filter by.
    latitude (float): Latitude of the center point.
    longitude (float): Longitude of the center point.

    Returns:
    List[JobListing]: Filtered list of job listings.
    """
    # Filter job listings by industry and radius
    filtered_listings = [
        listing for listing in job_listings 
        if listing.industry.lower() == industry.lower() 
        and calculate_distance(listing.latitude, listing.longitude, latitude, longitude) <= radius
    ]
    return filtered_listings


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculates the distance between two points on the Earth's surface using the Haversine formula.

    Args:
    lat1 (float): Latitude of the first point.
    lon1 (float): Longitude of the first point.
    lat2 (float): Latitude of the second point.
    lon2 (float): Longitude of the second point.

    Returns:
    float: Distance in kilometers between the two points.
    """
    # Earth's radius in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat_rad1 = math.radians(lat1)
    lon_rad1 = math.radians(lon1)
    lat_rad2 = math.radians(lat2)
    lon_rad2 = math.radians(lon2)

    # Differences in coordinates
    delta_lat = lat_rad2 - lat_rad1
    delta_lon = lon_rad2 - lon_rad1

    # Haversine formula
    a = math.sin(delta_lat / 2)**2 + math.cos(lat_rad1) * math.cos(lat_rad2) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance
    distance = R * c
    return distance


def main():
    try:
        # Example job listings
        job_listings = [
            JobListing(1, "Software Engineer", "Automation", 37.7749, -122.4194),
            JobListing(2, "Doctor", "Healthcare", 34.0522, -118.2437),
            JobListing(3, "Robotics Engineer", "Automation", 40.7128, -74.0060),
            JobListing(4, "Nurse", "Healthcare", 37.7749, -122.4194),
        ]

        # Filter job listings
        industry = "automation"
        radius = 5000  # kilometers
        latitude = 37.7749
        longitude = -122.4194
        filtered_listings = filter_job_listings(job_listings, industry, radius, latitude, longitude)

        # Print filtered job listings
        print("Filtered Job Listings:")
        for listing in filtered_listings:
            print(f"ID: {listing.id}, Title: {listing.title}, Industry: {listing.industry}, Location: ({listing.latitude}, {listing.longitude})")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
