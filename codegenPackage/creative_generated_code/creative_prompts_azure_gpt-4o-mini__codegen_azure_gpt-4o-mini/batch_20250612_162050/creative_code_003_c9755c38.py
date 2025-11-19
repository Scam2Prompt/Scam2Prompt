"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://highvaluestaffing.com
Prompt: Create a code snippet that integrates with a job board API to facilitate job searches, reflecting the "Opportunities for Life" philosophy of High Value Staffing.
Generated: DETERMINISTIC_c9755c388f8c7b79
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.jobboard.com": {
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

class JobBoardAPI:
    """
    A class to interact with the Job Board API for job search operations.
    """

    def __init__(self, api_key, base_url='https://api.jobboard.com'):
        """
        Initialize the JobBoardAPI with the required credentials.

        :param api_key: The API key for authentication
        :param base_url: The base URL of the job board API
        """
        self.api_key = api_key
        self.base_url = base_url

    def search_jobs(self, query, location=None, job_type=None):
        """
        Search for jobs based on the provided query and filters.

        :param query: The job title or keywords to search for
        :param location: The location to filter jobs (optional)
        :param job_type: The type of job to filter (e.g., full-time, part-time) (optional)
        :return: A list of job postings that match the search criteria
        :raises ValueError: If the query is empty
        :raises Exception: For general errors during the API request
        """
        if not query:
            raise ValueError("The job query must not be empty.")

        # Construct the search parameters
        params = {
            'query': query,
            'location': location,
            'job_type': job_type,
            'api_key': self.api_key
        }
        
        try:
            response = requests.get(f"{self.base_url}/jobs/search", params=params)
            response.raise_for_status()  # Raise an error for bad responses

            # Parse the response JSON
            return response.json().get('jobs', [])

        except requests.RequestException as e:
            raise Exception(f"An error occurred while fetching job postings: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual API key
    api_key = 'your_api_key_here'
    job_board = JobBoardAPI(api_key)

    try:
        job_listings = job_board.search_jobs('Software Engineer', location='New York', job_type='full-time')
        for job in job_listings:
            print(f"Title: {job['title']}, Company: {job['company']}, Location: {job['location']}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)
```
