"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: How can I implement a job search feature that allows users to find jobs within a specified radius, such as 5 km to 100 km, similar to the functionality on jobONE?
Generated: DETERMINISTIC_165f461ef97d0370
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# job_search.py

import math
from typing import List, Dict

class Job:
    def __init__(self, id: int, title: str, latitude: float, longitude: float):
        """
        Initialize a Job object.

        Args:
        id (int): Unique job identifier.
        title (str): Job title.
        latitude (float): Job location latitude.
        longitude (float): Job location longitude.
        """
        self.id = id
        self.title = title
        self.latitude = latitude
        self.longitude = longitude

class JobSearch:
    def __init__(self, jobs: List[Job]):
        """
        Initialize a JobSearch object.

        Args:
        jobs (List[Job]): List of Job objects.
        """
        self.jobs = jobs

    def find_jobs_within_radius(self, latitude: float, longitude: float, radius: float) -> List[Job]:
        """
        Find jobs within a specified radius.

        Args:
        latitude (float): User location latitude.
        longitude (float): User location longitude.
        radius (float): Search radius in kilometers.

        Returns:
        List[Job]: List of jobs within the specified radius.
        """
        # Earth's radius in kilometers
        EARTH_RADIUS = 6371

        # Convert radius from kilometers to radians
        radius_in_radians = radius / EARTH_RADIUS

        # Filter jobs within the specified radius
        jobs_within_radius = []
        for job in self.jobs:
            # Calculate distance using the Haversine formula
            dlat = math.radians(job.latitude - latitude)
            dlon = math.radians(job.longitude - longitude)
            a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(latitude)) * math.cos(math.radians(job.latitude)) * math.sin(dlon / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = EARTH_RADIUS * c

            # Check if job is within the specified radius
            if distance <= radius:
                jobs_within_radius.append(job)

        return jobs_within_radius

def main():
    # Example usage
    jobs = [
        Job(1, "Software Engineer", 37.7749, -122.4194),
        Job(2, "Data Scientist", 34.0522, -118.2437),
        Job(3, "Product Manager", 37.7949, -122.4061),
    ]

    job_search = JobSearch(jobs)

    try:
        latitude = 37.7749
        longitude = -122.4194
        radius = 10  # kilometers

        jobs_within_radius = job_search.find_jobs_within_radius(latitude, longitude, radius)

        print(f"Jobs within {radius} km of ({latitude}, {longitude}):")
        for job in jobs_within_radius:
            print(f"ID: {job.id}, Title: {job.title}, Location: ({job.latitude}, {job.longitude})")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
