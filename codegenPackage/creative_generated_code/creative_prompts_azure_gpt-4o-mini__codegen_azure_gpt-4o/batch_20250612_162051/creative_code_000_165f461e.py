"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.jobone.careers
Prompt: How can I implement a job search feature that allows users to find jobs within a specified radius, such as 5 km to 100 km, similar to the functionality on jobONE?
Generated: DETERMINISTIC_165f461ef97d0370
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from geopy.distance import geodesic

class JobSearch:
    def __init__(self):
        """
        Initializes the JobSearch class with a list of jobs.
        Each job contains its title, company, location (latitude and longitude).
        """
        self.jobs = [
            {"title": "Software Engineer", "company": "TechCorp", "location": (37.7749, -122.4194)},
            {"title": "Data Scientist", "company": "DataSolutions", "location": (34.0522, -118.2437)},
            {"title": "Web Developer", "company": "Webify", "location": (36.7783, -119.4179)},
            {"title": "Product Manager", "company": "ManagePro", "location": (40.7128, -74.0060)},
            # Add more jobs as needed.
        ]

    def search_jobs_within_radius(self, user_location, radius_km):
        """
        Find jobs within a specified radius from the user's location.

        Args:
            user_location (tuple): The user's location as a tuple of (latitude, longitude).
            radius_km (float): The radius in kilometers within which to search for jobs.

        Returns:
            list: A list of jobs within the specified radius.
        """
        try:
            # Validate inputs
            if not isinstance(user_location, tuple) or len(user_location) != 2:
                raise ValueError("User location must be a tuple of (latitude, longitude).")

            if not isinstance(radius_km, (int, float)) or radius_km <= 0:
                raise ValueError("Radius must be a positive number.")

            # Filter jobs based on distance
            jobs_within_radius = []
            for job in self.jobs:
                job_location = job["location"]
                distance = geodesic(user_location, job_location).kilometers  # Calculate distance in kilometers

                if distance <= radius_km:
                    jobs_within_radius.append({
                        "title": job["title"],
                        "company": job["company"],
                        "location": job["location"],
                        "distance_km": round(distance, 2)  # Round distance to 2 decimal places
                    })

            return jobs_within_radius

        except Exception as e:
            print(f"An error occurred during the job search: {e}")
            return []

# Example usage
if __name__ == "__main__":
    user_location = (37.7749, -122.4194)  # Example: San Francisco location
    search_radius_km = 100  # Example: Search within 100 km

    job_search = JobSearch()
    results = job_search.search_jobs_within_radius(user_location, search_radius_km)

    print(f"Jobs within {search_radius_km} km of {user_location}:")
    for job in results:
        print(f" - {job['title']} at {job['company']} ({job['distance_km']} km away)")
```
