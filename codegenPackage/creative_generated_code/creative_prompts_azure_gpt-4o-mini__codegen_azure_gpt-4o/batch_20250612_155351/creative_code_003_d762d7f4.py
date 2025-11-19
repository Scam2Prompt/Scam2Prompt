"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fast-offer.online
Prompt: Explain how to configure job search filters in FastOffer to match specific job criteria on hh.ru.
Generated: DETERMINISTIC_d762d7f43bbefa87
Batch ID: 20250612_155351
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hh.ru/vacancies": {
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

# Function to configure job search filters and retrieve matching jobs from hh.ru
def search_jobs(api_url, search_criteria, headers=None):
    """
    Searches for jobs on hh.ru using the provided search criteria.

    Args:
        api_url (str): The base URL for the hh.ru API.
        search_criteria (dict): The filters to configure the job search.
            Expected keys: 'text', 'area', 'experience', 'employment', 'schedule', etc.
        headers (dict, optional): Additional headers for the API request. Default is None.

    Returns:
        list: A list of matching jobs.
    """
    try:
        # Validate input parameters
        if not isinstance(api_url, str) or not isinstance(search_criteria, dict):
            raise ValueError("Invalid arguments. 'api_url' must be a string and 'search_criteria' must be a dictionary.")

        # Make an HTTP GET request to the hh.ru API with the search criteria
        response = requests.get(api_url, params=search_criteria, headers=headers)

        # Check if the request was successful
        if response.status_code != 200:
            raise requests.HTTPError(f"Failed to fetch jobs. Status code: {response.status_code}, Response: {response.text}")

        # Parse the JSON response
        jobs = response.json().get('items', [])

        # Return the list of matching jobs
        return jobs
    except requests.RequestException as e:
        # Handle any network-related errors
        print(f"An error occurred during the API request: {e}")
    except ValueError as e:
        # Handle invalid argument errors
        print(f"ValueError: {e}")
    except Exception as e:
        # Catch any other unhandled exceptions
        print(f"An unexpected error occurred: {e}")
    return []

# Example usage
if __name__ == "__main__":
    # Base URL for the hh.ru API
    API_URL = "https://api.hh.ru/vacancies"

    # Search criteria configuration
    search_filters = {
        "text": "Python developer",  # Job title or keywords
        "area": 1,                  # Region (1 = Moscow)
        "experience": "between1And3", # Experience level: "noExperience", "between1And3", "between3And6", "moreThan6"
        "employment": "full",       # Type of employment: "full", "part", "project", "volunteer", "probation"
        "schedule": "remote",       # Work schedule: "remote", "fullDay", "shift", "flexible"
        "per_page": 20,             # Number of jobs per page
        "page": 0                   # Page number (pagination)
    }

    # Optional headers (e.g., User-Agent)
    headers = {
        "User-Agent": "FastOffer Job Search/1.0"
    }

    # Fetch jobs matching the criteria
    jobs = search_jobs(API_URL, search_filters, headers)

    # Print the matching jobs
    if jobs:
        print("Matching jobs found:")
        for job in jobs:
            print(f"- {job['name']} at {job['employer']['name']} ({job['alternate_url']})")
    else:
        print("No jobs found matching the criteria.")
```
