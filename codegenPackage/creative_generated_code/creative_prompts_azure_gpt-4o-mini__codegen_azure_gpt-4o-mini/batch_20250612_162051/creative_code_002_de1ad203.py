"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Write a Python function that retrieves job listings for healthcare professionals, focusing on roles like registered nurses and doctors, inspired by the recruitment strategies of Amazing Grace Medical Recruitment.
Generated: DETERMINISTIC_de1ad20331bc4b0a
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/job-listings": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from typing import List, Dict, Any

class JobListingError(Exception):
    """Custom exception for job listing retrieval errors."""
    pass

def fetch_healthcare_job_listings(api_url: str, job_titles: List[str]) -> List[Dict[str, Any]]:
    """
    Fetch job listings for healthcare professionals from the specified API.

    Args:
        api_url (str): The URL of the job listings API.
        job_titles (List[str]): A list of job titles to filter the listings.

    Returns:
        List[Dict[str, Any]]: A list of job listings matching the specified titles.

    Raises:
        JobListingError: If there is an error during the API request.
    """
    try:
        # Make a request to the job listings API
        response = requests.get(api_url)
        
        # Raise an error if the response status is not successful
        response.raise_for_status()
        
        # Parse the JSON response
        job_listings = response.json()

        # Filter job listings based on the specified job titles
        filtered_listings = [
            job for job in job_listings
            if job.get('title') in job_titles
        ]

        return filtered_listings

    except requests.RequestException as e:
        raise JobListingError(f"Error fetching job listings: {e}")

# Example usage
if __name__ == "__main__":
    API_URL = "https://api.example.com/job-listings"  # Replace with the actual API URL
    JOB_TITLES = ["Registered Nurse", "Doctor"]

    try:
        jobs = fetch_healthcare_job_listings(API_URL, JOB_TITLES)
        for job in jobs:
            print(f"Title: {job['title']}, Location: {job['location']}, Company: {job['company']}")
    except JobListingError as e:
        print(f"Failed to retrieve job listings: {e}")
```
