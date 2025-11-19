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
from typing import List, Dict, Optional

class JobListing:
    def __init__(self, title: str, company: str, industry: str, latitude: float, longitude: float):
        self.title = title
        self.company = company
        self.industry = industry
        self.latitude = latitude
        self.longitude = longitude

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great-circle distance between two points on the Earth's surface.
    
    Args:
        lat1: Latitude of point 1 in degrees
        lon1: Longitude of point 1 in degrees
        lat2: Latitude of point 2 in degrees
        lon2: Longitude of point 2 in degrees
    
    Returns:
        Distance between the points in kilometers
    """
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of Earth in kilometers
    r = 6371
    return c * r

def filter_job_listings(
    job_listings: List[JobListing],
    industries: Optional[List[str]] = None,
    center_latitude: Optional[float] = None,
    center_longitude: Optional[float] = None,
    radius_km: Optional[float] = None
) -> List[JobListing]:
    """
    Filter job listings by industry and/or geographic radius.
    
    Args:
        job_listings: List of JobListing objects to filter
        industries: List of industry names to include (None means all industries)
        center_latitude: Latitude of the center point for radius filtering
        center_longitude: Longitude of the center point for radius filtering
        radius_km: Radius in kilometers for filtering (None means no radius filtering)
    
    Returns:
        Filtered list of JobListing objects
    
    Raises:
        ValueError: If radius parameters are incomplete
    """
    filtered = []
    
    # Filter by industry if specified
    if industries is not None:
        industries_lower = [industry.lower() for industry in industries]
        filtered = [
            job for job in job_listings 
            if job.industry.lower() in industries_lower
        ]
    else:
        filtered = job_listings.copy()
    
    # Filter by radius if specified
    if radius_km is not None:
        if center_latitude is None or center_longitude is None:
            raise ValueError("Both center latitude and longitude must be provided for radius filtering")
        
        radius_filtered = []
        for job in filtered:
            distance = haversine_distance(
                center_latitude, center_longitude,
                job.latitude, job.longitude
            )
            if distance <= radius_km:
                radius_filtered.append(job)
        filtered = radius_filtered
    
    return filtered

# Example usage
if __name__ == "__main__":
    # Sample job listings
    jobs = [
        JobListing("Nurse", "City Hospital", "Healthcare", 40.7128, -74.0060),
        JobListing("Doctor", "General Hospital", "Healthcare", 34.0522, -118.2437),
        JobListing("Engineer", "Tech Corp", "Automation", 37.7749, -122.4194),
        JobListing("Technician", "Auto Systems", "Automation", 40.7128, -74.0060),
    ]
    
    # Filter for healthcare jobs within 50km of NYC
    filtered_jobs = filter_job_listings(
        jobs,
        industries=["Healthcare"],
        center_latitude=40.7128,
        center_longitude=-74.0060,
        radius_km=50
    )
    
    for job in filtered_jobs:
        print(f"{job.title} at {job.company} ({job.industry})")
```
