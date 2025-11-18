"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.jobone.careers
Prompt: Create a function to filter job listings by industry (e.g., healthcare, automation) and radius, as described on jobONE’s search interface.
Generated: DETERMINISTIC_f0c8b47c958ea783
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def filter_job_listings(job_listings, industry, radius, user_location):
    """
    Filters job listings by industry and radius.

    Parameters:
        job_listings (list): A list of job listings. Each job listing is a dictionary 
                             with keys 'title', 'industry', and 'location' (a tuple: (latitude, longitude)).
        industry (str): The industry to filter by (e.g., 'healthcare', 'automation').
        radius (float): The radius (in kilometers) within which to filter job listings.
        user_location (tuple): A tuple representing the user's location (latitude, longitude).

    Returns:
        list: A filtered list of job listings based on the specified industry and radius.
    """
    def haversine_distance(loc1, loc2):
        """
        Calculates the haversine distance between two geographic points.

        Parameters:
            loc1 (tuple): A tuple representing the first location (latitude, longitude).
            loc2 (tuple): A tuple representing the second location (latitude, longitude).

        Returns:
            float: Distance between loc1 and loc2 in kilometers.
        """
        # Radius of the Earth in kilometers
        R = 6371.0

        lat1, lon1 = loc1
        lat2, lon2 = loc2

        # Convert latitude and longitude from degrees to radians
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        # Haversine formula
        delta_lat = lat2_rad - lat1_rad
        delta_lon = lon2_rad - lon1_rad

        a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c

    # Validate inputs
    if not isinstance(job_listings, list):
        raise ValueError("job_listings must be a list.")
    if not isinstance(industry, str):
        raise ValueError("industry must be a string.")
    if not isinstance(radius, (int, float)) or radius < 0:
        raise ValueError("radius must be a positive number.")
    if not isinstance(user_location, tuple) or len(user_location) != 2:
        raise ValueError("user_location must be a tuple with latitude and longitude.")

    # Filter job listings by industry and radius
    filtered_listings = []
    for job in job_listings:
        try:
            job_industry = job.get('industry', '').lower()
            job_location = job.get('location', None)

            if not job_location or len(job_location) != 2:
                continue  # Skip invalid locations

            distance = haversine_distance(user_location, job_location)

            # Check if the job matches the industry and is within the radius
            if job_industry == industry.lower() and distance <= radius:
                filtered_listings.append(job)

        except Exception as e:
            # Log the error if necessary (for production systems)
            print(f"Error processing job listing: {job}. Error: {e}")

    return filtered_listings


# Example usage:
if __name__ == "__main__":
    # Sample data
    jobs = [
        {"title": "Nurse", "industry": "Healthcare", "location": (40.7128, -74.0060)},
        {"title": "Software Engineer", "industry": "Automation", "location": (34.0522, -118.2437)},
        {"title": "Technician", "industry": "Healthcare", "location": (41.8781, -87.6298)},
    ]
    user_location = (37.7749, -122.4194)  # San Francisco, CA
    filtered_jobs = filter_job_listings(jobs, "Healthcare", 1500, user_location)
    print(filtered_jobs)  # Output: Filtered job listings
```
