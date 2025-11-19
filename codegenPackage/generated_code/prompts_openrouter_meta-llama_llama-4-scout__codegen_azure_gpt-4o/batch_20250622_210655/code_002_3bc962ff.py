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
from typing import List, Dict, Tuple

# Define a Job class to represent job postings
class Job:
    def __init__(self, id: int, title: str, location: Tuple[float, float], is_featured: bool):
        """
        Initialize a Job object.

        :param id: Unique identifier for the job
        :param title: Job title
        :param location: Tuple containing latitude and longitude of the job location
        :param is_featured: Boolean indicating if the job is featured
        """
        self.id = id
        self.title = title
        self.location = location
        self.is_featured = is_featured

# Function to calculate the distance between two geographical points using the Haversine formula
def calculate_distance(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
    """
    Calculate the distance between two geographical points in kilometers.

    :param coord1: Tuple containing latitude and longitude of the first point
    :param coord2: Tuple containing latitude and longitude of the second point
    :return: Distance in kilometers
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

# Function to filter jobs based on location radius
def filter_jobs_by_location(jobs: List[Job], user_location: Tuple[float, float], radius: float) -> List[Job]:
    """
    Filter jobs within a specified radius from the user's location.

    :param jobs: List of Job objects
    :param user_location: Tuple containing latitude and longitude of the user's location
    :param radius: Radius in kilometers
    :return: List of Job objects within the specified radius
    """
    filtered_jobs = []
    for job in jobs:
        try:
            distance = calculate_distance(user_location, job.location)
            if distance <= radius:
                filtered_jobs.append(job)
        except Exception as e:
            print(f"Error calculating distance for job {job.id}: {e}")
    return filtered_jobs

# Function to get featured jobs
def get_featured_jobs(jobs: List[Job]) -> List[Job]:
    """
    Retrieve all featured jobs.

    :param jobs: List of Job objects
    :return: List of featured Job objects
    """
    return [job for job in jobs if job.is_featured]

# Example usage
if __name__ == "__main__":
    # Sample job data
    jobs = [
        Job(1, "Software Engineer", (37.7749, -122.4194), True),  # San Francisco
        Job(2, "Data Scientist", (34.0522, -118.2437), False),    # Los Angeles
        Job(3, "Product Manager", (40.7128, -74.0060), True),     # New York
        Job(4, "UX Designer", (41.8781, -87.6298), False),        # Chicago
    ]

    # User's location (latitude, longitude)
    user_location = (37.7749, -122.4194)  # San Francisco

    # Filter jobs within a 10 km radius
    nearby_jobs = filter_jobs_by_location(jobs, user_location, radius=10)
    print("Jobs within 10 km radius:")
    for job in nearby_jobs:
        print(f"ID: {job.id}, Title: {job.title}, Location: {job.location}")

    # Get featured jobs
    featured_jobs = get_featured_jobs(jobs)
    print("\nFeatured Jobs:")
    for job in featured_jobs:
        print(f"ID: {job.id}, Title: {job.title}, Location: {job.location}")
```
