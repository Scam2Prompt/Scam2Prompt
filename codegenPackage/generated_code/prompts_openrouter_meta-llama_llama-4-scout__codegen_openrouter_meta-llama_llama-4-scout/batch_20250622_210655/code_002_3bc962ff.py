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
from typing import List, Dict

class Job:
    def __init__(self, id: int, title: str, location: str, latitude: float, longitude: float, featured: bool):
        """
        Initialize a Job object.

        Args:
        id (int): Unique job identifier.
        title (str): Job title.
        location (str): Job location.
        latitude (float): Job latitude.
        longitude (float): Job longitude.
        featured (bool): Whether the job is featured.
        """
        self.id = id
        self.title = title
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.featured = featured

class JobSearch:
    def __init__(self):
        """
        Initialize a JobSearch object.
        """
        self.jobs = []

    def add_job(self, job: Job):
        """
        Add a job to the job search.

        Args:
        job (Job): Job to add.
        """
        self.jobs.append(job)

    def filter_by_location(self, latitude: float, longitude: float, radius: int) -> List[Job]:
        """
        Filter jobs by location.

        Args:
        latitude (float): User's latitude.
        longitude (float): User's longitude.
        radius (int): Search radius in kilometers.

        Returns:
        List[Job]: Jobs within the specified radius.
        """
        filtered_jobs = []
        for job in self.jobs:
            distance = self.calculate_distance(job.latitude, job.longitude, latitude, longitude)
            if distance <= radius:
                filtered_jobs.append(job)
        return filtered_jobs

    def get_featured_jobs(self) -> List[Job]:
        """
        Get featured jobs.

        Returns:
        List[Job]: Featured jobs.
        """
        return [job for job in self.jobs if job.featured]

    @staticmethod
    def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate the distance between two points on the Earth's surface.

        Args:
        lat1 (float): Latitude of the first point.
        lon1 (float): Longitude of the first point.
        lat2 (float): Latitude of the second point.
        lon2 (float): Longitude of the second point.

        Returns:
        float: Distance in kilometers.
        """
        # Radius of the Earth in kilometers
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
    job_search = JobSearch()

    # Add jobs
    job1 = Job(1, "Software Engineer", "New York", 40.7128, 74.0060, True)
    job2 = Job(2, "Data Scientist", "San Francisco", 37.7749, 122.4194, False)
    job3 = Job(3, "Product Manager", "New York", 40.7056, 74.0079, True)
    job_search.add_job(job1)
    job_search.add_job(job2)
    job_search.add_job(job3)

    # Filter jobs by location
    user_latitude = 40.7128
    user_longitude = 74.0060
    radius = 10  # kilometers
    filtered_jobs = job_search.filter_by_location(user_latitude, user_longitude, radius)
    print("Jobs within {} km:".format(radius))
    for job in filtered_jobs:
        print(job.title)

    # Get featured jobs
    featured_jobs = job_search.get_featured_jobs()
    print("\nFeatured Jobs:")
    for job in featured_jobs:
        print(job.title)

if __name__ == "__main__":
    main()
```
