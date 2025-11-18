"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7364500043.pages.dev
Prompt: Create a Python script to fetch and display cryptocurrency job listings, inspired by the "Jobs" section on Journal Du Coin.
Generated: DETERMINISTIC_44ee6000364e7a77
Batch ID: 20250612_151255
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/cryptocurrency-jobs": {
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
import json

def fetch_job_listings(url):
    """
    Fetch job listings from the given URL.

    :param url: The API endpoint or webpage URL providing job data.
    :return: A list of job listings (empty list if the request fails).
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()  # Parse JSON response
        return data.get('jobs', [])  # Assuming 'jobs' is a key in the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching job listings: {e}")
        return []

def display_jobs(job_list):
    """
    Display job listings in a readable format.

    :param job_list: List of job dictionaries containing job details.
    """
    if not job_list:
        print("No job listings available.")
        return
    
    print(f"{'Title':<40}{'Company':<30}{'Location':<20}")
    print("-" * 90)
    
    for job in job_list:
        title = job.get('title', 'N/A')
        company = job.get('company', 'N/A')
        location = job.get('location', 'N/A')
        print(f"{title:<40}{company:<30}{location:<20}")

def main():
    """
    Main function to fetch and display cryptocurrency job listings.
    """
    # Replace with the actual API endpoint or URL that provides job listings
    jobs_api_url = "https://api.example.com/cryptocurrency-jobs"
    
    print("Fetching cryptocurrency job listings...")
    job_listings = fetch_job_listings(jobs_api_url)
    display_jobs(job_listings)

if __name__ == "__main__":
    main()
```
