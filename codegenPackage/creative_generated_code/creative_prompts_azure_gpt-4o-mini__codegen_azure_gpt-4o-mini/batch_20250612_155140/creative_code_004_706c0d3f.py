"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxincome18.pages.dev
Prompt: Create a function that filters job listings based on hourly pay and job simplicity, inspired by the earnings mentioned on this site.
Generated: DETERMINISTIC_706c0d3fdd2b7991
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

def filter_job_listings(job_listings: List[Dict[str, str]], min_pay: float, max_pay: float, simple_jobs: List[str]) -> List[Dict[str, str]]:
    """
    Filters job listings based on hourly pay and job simplicity.

    Args:
        job_listings (List[Dict[str, str]]): A list of job listings where each job is represented as a dictionary.
        min_pay (float): The minimum hourly pay for job listings to be considered.
        max_pay (float): The maximum hourly pay for job listings to be considered.
        simple_jobs (List[str]): A list of keywords that define simple jobs.

    Returns:
        List[Dict[str, str]]: A list of filtered job listings that meet the specified criteria.

    Raises:
        ValueError: If min_pay is greater than max_pay.
    """

    # Validate pay range
    if min_pay > max_pay:
        raise ValueError("Minimum pay cannot be greater than maximum pay.")
    
    filtered_jobs = []

    for job in job_listings:
        try:
            # Extract job details
            job_title = job.get('title', '').lower()
            job_pay = float(job.get('hourly_pay', 0))  # Assume 'hourly_pay' is a string that can be converted to float
            
            # Check if job pay and job simplicity match the criteria
            if min_pay <= job_pay <= max_pay and any(keyword in job_title for keyword in simple_jobs):
                filtered_jobs.append(job)
        except (ValueError, TypeError) as e:
            # Log or handle the exception as needed; for now, we'll just ignore this job
            print(f"Error processing job listing {job}: {e}")

    return filtered_jobs

# Example usage:
if __name__ == "__main__":
    job_listings_example = [
        {'title': 'Data Entry Clerk', 'hourly_pay': '15.00'},
        {'title': 'Software Engineer', 'hourly_pay': '45.00'},
        {'title': 'Customer Service Representative', 'hourly_pay': '18.50'},
        {'title': 'House Cleaner', 'hourly_pay': '20.00'},
        {'title': 'Web Developer', 'hourly_pay': '60.00'}
    ]

    simple_jobs_keywords = ['data entry', 'customer service', 'house cleaner']

    # Filter jobs with hourly pay between 10 and 25
    filtered_jobs = filter_job_listings(job_listings_example, 10, 25, simple_jobs_keywords)
    print("Filtered Job Listings:", filtered_jobs)
```
