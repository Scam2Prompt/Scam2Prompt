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
from typing import List, Dict, Any
from geopy.distance import geodesic

def filter_job_listings(job_listings: List[Dict[str, Any]], industry: str, location: tuple, radius: float) -> List[Dict[str, Any]]:
    """
    Filters job listings by the specified industry and within a given radius from a location.

    Args:
        job_listings (List[Dict[str, Any]]): A list of job listings where each listing is a dictionary.
        industry (str): The industry to filter job listings by (e.g., 'healthcare', 'automation').
        location (tuple): A tuple containing the latitude and longitude of the location (lat, lon).
        radius (float): The radius in miles within which to filter job listings.

    Returns:
        List[Dict[str, Any]]: A list of filtered job listings matching the criteria.
    """
    filtered_listings = []

    # Validate inputs
    if not isinstance(job_listings, list) or not all(isinstance(job, dict) for job in job_listings):
        raise ValueError("job_listings must be a list of dictionaries")
    
    if not isinstance(industry, str) or not isinstance(location, tuple) or len(location) != 2:
        raise ValueError("Invalid industry or location format. Location must be a tuple (lat, lon).")
    
    if not isinstance(radius, (int, float)) or radius <= 0:
        raise ValueError("Radius must be a positive number.")

    # Filter job listings
    for job in job_listings:
        try:
            job_industry = job.get("industry")
            job_location = job.get("location")  # Assuming job_location is a tuple (lat, lon)
            
            # Check if job has necessary fields
            if job_location is None or job_industry is None:
                continue
            
            # Calculate the distance from the job location to the given location
            distance = geodesic(location, job_location).miles
            
            # Filter by industry and distance
            if job_industry.lower() == industry.lower() and distance <= radius:
                filtered_listings.append(job)
        
        except Exception as e:
            # Log the error and continue processing other jobs
            print(f"Error processing job listing {job}: {e}")

    return filtered_listings

# Example usage
if __name__ == "__main__":
    job_listings_example = [
        {"title": "Nurse", "industry": "Healthcare", "location": (34.0522, -118.2437)},
        {"title": "Engineer", "industry": "Automation", "location": (34.0522, -118.2437)},
        {"title": "Doctor", "industry": "Healthcare", "location": (36.1699, -115.1398)},
        # Add more job listings as needed
    ]
    
    industry_filter = "Healthcare"
    user_location = (34.0522, -118.2437)
    search_radius = 50.0  # in miles

    filtered_jobs = filter_job_listings(job_listings_example, industry_filter, user_location, search_radius)
    print(filtered_jobs)
```
