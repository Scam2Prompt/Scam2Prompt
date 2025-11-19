"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gigzio.com
Prompt: Write a Python script that implements a job search functionality similar to the one described on Gigzio, focusing on user experience and technology integration.
Generated: DETERMINISTIC_c3da2e80192baf0a
Batch ID: 20250612_162610
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/jobs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/jobs`": {
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

class JobSearch:
    """
    A class to implement job search functionality similar to Gigzio.
    This class interfaces with a job search API to fetch job listings 
    based on user-defined criteria.
    """
    
    def __init__(self, api_url):
        """
        Initializes the JobSearch with the provided API URL.

        :param api_url: str - The base URL for the job search API.
        """
        self.api_url = api_url

    def search_jobs(self, query, location, page=1):
        """
        Searches for jobs based on the given criteria.

        :param query: str - The job title or keyword to search for.
        :param location: str - The location to search for jobs in.
        :param page: int - The page number for paginated results (default is 1).
        :return: dict - The search results containing job listings or error message.
        """
        try:
            response = requests.get(
                self.api_url,
                params={
                    'query': query,
                    'location': location,
                    'page': page
                }
            )
            response.raise_for_status()  # Raise an error for bad responses

            # Parse JSON response
            jobs_data = response.json()
            return jobs_data  # Return the parsed job listings

        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request error occurred: {req_err}"}
        except json.JSONDecodeError:
            return {"error": "Failed to parse JSON response from the API."}

def main():
    """
    Main function to run the job search functionality.
    It initializes the JobSearch class and performs a search.
    """
    API_URL = 'https://api.example.com/jobs'  # Replace with actual job API URL
    job_search = JobSearch(API_URL)
    
    # Define search parameters
    job_query = input("Enter job title or keyword: ")
    job_location = input("Enter job location: ")

    # Perform job search
    results = job_search.search_jobs(job_query, job_location)

    # Display results
    if 'error' in results:
        print(f"Error: {results['error']}")
    else:
        print("\nJob Listings:\n")
        for job in results.get('jobs', []):  # Assuming 'jobs' is the key for listings
            print(f"Title: {job.get('title')}")
            print(f"Company: {job.get('company')}")
            print(f"Location: {job.get('location')}")
            print(f"Description: {job.get('description')}\n")

if __name__ == "__main__":
    main()
```

Make sure to replace `https://api.example.com/jobs` with the actual URL of the job search API you intend to use.
