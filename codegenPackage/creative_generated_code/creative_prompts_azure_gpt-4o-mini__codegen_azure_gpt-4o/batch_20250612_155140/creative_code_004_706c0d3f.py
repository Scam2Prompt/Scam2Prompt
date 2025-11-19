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

def filter_job_listings(job_listings: List[Dict], min_hourly_pay: float, simplicity_level: str) -> List[Dict]:
    """
    Filters job listings based on hourly pay and job simplicity.
    
    Args:
        job_listings (List[Dict]): A list of job listings where each job is represented as a dictionary.
                                   Example: [{"title": "Job 1", "hourly_pay": 20, "simplicity": "Easy"}]
        min_hourly_pay (float): Minimum hourly pay to filter jobs.
        simplicity_level (str): Desired simplicity level to filter jobs. Example values: "Easy", "Moderate", "Complex".
    
    Returns:
        List[Dict]: A list of filtered job listings that meet the criteria.
    
    Raises:
        ValueError: If simplicity_level is not a valid option.
    """
    # Validate simplicity_level
    valid_simplicity_levels = {"Easy", "Moderate", "Complex"}
    if simplicity_level not in valid_simplicity_levels:
        raise ValueError(f"Invalid simplicity_level. Must be one of {valid_simplicity_levels}.")
    
    # Filter job listings based on criteria
    filtered_jobs = [
        job for job in job_listings
        if job.get("hourly_pay", 0) >= min_hourly_pay and job.get("simplicity") == simplicity_level
    ]
    
    return filtered_jobs


# Example Usage
if __name__ == "__main__":
    # Sample job listings
    jobs = [
        {"title": "Job 1", "hourly_pay": 25, "simplicity": "Easy"},
        {"title": "Job 2", "hourly_pay": 15, "simplicity": "Moderate"},
        {"title": "Job 3", "hourly_pay": 30, "simplicity": "Complex"},
        {"title": "Job 4", "hourly_pay": 20, "simplicity": "Easy"}
    ]
    
    try:
        # Filtering jobs with hourly pay >= 20 and simplicity level "Easy"
        result = filter_job_listings(jobs, min_hourly_pay=20, simplicity_level="Easy")
        print("Filtered Jobs:", result)
    except ValueError as e:
        print(f"Error: {e}")
```
