"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Generate a code snippet for a simple job search feature that allows users to filter jobs by location (e.g., 5 km, 10 km, 20 km radius) and display featured jobs, inspired by jobONE's job search functionality.
Generated: DETERMINISTIC_3bc962ff3bcfa29f
Batch ID: 20250622_210655
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
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Job:
    id: str
    title: str
    company: str
    location: Dict[str, float]  # {'lat': float, 'lng': float}
    is_featured: bool
    posted_date: datetime
    description: str

class JobSearch:
    def __init__(self, jobs: List[Job]):
        """
        Initialize JobSearch with a list of jobs.
        """
        self.jobs = jobs

    def filter_by_radius(self, user_location: Dict[str, float], radius_km: int) -> List[Job]:
        """
        Filter jobs within a specified radius from user's location.
        
        Args:
            user_location: Dictionary with 'lat' and 'lng' keys
            radius_km: Radius in kilometers (5, 10, 20)
            
        Returns:
            List of jobs within the specified radius
        """
        if not user_location or 'lat' not in user_location or 'lng' not in user_location:
            raise ValueError("Invalid user location provided")
            
        if radius_km not in [5, 10, 20]:
            raise ValueError("Radius must be 5, 10, or 20 km")
            
        filtered_jobs = []
        for job in self.jobs:
            distance = self._calculate_distance(
                user_location['lat'],
                user_location['lng'],
                job.location['lat'],
                job.location['lng']
            )
            if distance <= radius_km:
                filtered_jobs.append(job)
                
        return filtered_jobs

    def get_featured_jobs(self) -> List[Job]:
        """
        Get all featured jobs.
        
        Returns:
            List of featured jobs
        """
        return [job for job in self.jobs if job.is_featured]

    def _calculate_distance(self, lat1: float, lng1: float, lat2: float, lng2: float) -> float:
        """
        Calculate distance between two coordinates in kilometers using Haversine formula.
        
        Args:
            lat1, lng1: First coordinate
            lat2, lng2: Second coordinate
            
        Returns:
            Distance in kilometers
        """
        # Convert degrees to radians
        lat1, lng1, lat2, lng2 = map(math.radians, [lat1, lng1, lat2, lng2])
        
        # Haversine formula
        dlat = lat2 - lat1
        dlng = lng2 - lng1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng/2)**2
        c = 2 * math.asin(math.sqrt(a))
        
        # Radius of Earth in kilometers
        r = 6371
        return c * r

# Example usage
if __name__ == "__main__":
    # Sample jobs data
    jobs = [
        Job(
            id="1",
            title="Software Engineer",
            company="Tech Corp",
            location={"lat": 37.7749, "lng": -122.4194},
            is_featured=True,
            posted_date=datetime(2023, 5, 15),
            description="Develop awesome software"
        ),
        Job(
            id="2",
            title="Data Analyst",
            company="Data Inc",
            location={"lat": 37.7895, "lng": -122.4023},
            is_featured=False,
            posted_date=datetime(2023, 5, 10),
            description="Analyze data patterns"
        )
    ]
    
    job_search = JobSearch(jobs)
    
    # Get featured jobs
    featured_jobs = job_search.get_featured_jobs()
    print("Featured Jobs:")
    for job in featured_jobs:
        print(f"- {job.title} at {job.company}")
    
    # Filter by radius
    user_location = {"lat": 37.7749, "lng": -122.4194}
    nearby_jobs = job_search.filter_by_radius(user_location, 5)
    print("\nJobs within 5 km:")
    for job in nearby_jobs:
        print(f"- {job.title} at {job.company} ({job.location['lat']}, {job.location['lng']})")
```
