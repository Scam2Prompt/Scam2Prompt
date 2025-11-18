"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://job4chat.crediblejobs.in
Prompt: Generate code using JavaScript or Python to display job details dynamically, including "Job Title," "Location," "Salary," and "Eligibility Criteria," based on user input for job preferences.
Generated: DETERMINISTIC_3e4340d3c48337e7
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code:

```python
# Import necessary libraries
import sys

def get_job_details(job_preferences):
    """
    Function to fetch job details based on user preferences
    :param job_preferences: Dictionary containing user preferences
    :return: Dictionary containing job details
    """
    # Predefined job database (can be replaced with a real database or API)
    job_database = [
        {"Job Title": "Software Engineer", "Location": "New York", "Salary": "$90,000", "Eligibility Criteria": "Bachelor's Degree in Computer Science"},
        {"Job Title": "Data Analyst", "Location": "San Francisco", "Salary": "$80,000", "Eligibility Criteria": "Bachelor's Degree in Statistics"},
        {"Job Title": "Product Manager", "Location": "Austin", "Salary": "$100,000", "Eligibility Criteria": "MBA or equivalent experience"},
        {"Job Title": "Web Developer", "Location": "Remote", "Salary": "$70,000", "Eligibility Criteria": "Proven experience in web development"},
    ]
    
    # Filter jobs based on user preferences
    matching_jobs = []
    for job in job_database:
        match = True
        for key, value in job_preferences.items():
            if key in job and job[key].lower() != value.lower():
                match = False
                break
        if match:
            matching_jobs.append(job)
    
    return matching_jobs if matching_jobs else None

def display_job_details(jobs):
    """
    Function to display job details
    :param jobs: List of jobs matching the user's preferences
    """
    if not jobs:
        print("No jobs found matching your preferences.")
        return
    
    print("\nMatching Job Details:\n")
    for i, job in enumerate(jobs, start=1):
        print(f"Job {i}:")
        for key, value in job.items():
            print(f"{key}: {value}")
        print("-" * 40)

def main():
    """
    Main function to collect user input and display job details
    """
    try:
        print("Enter your job preferences. Leave blank for no preference.\n")
        job_title = input("Preferred Job Title: ").strip()
        location = input("Preferred Location: ").strip()
        salary = input("Preferred Salary: ").strip()
        eligibility_criteria = input("Preferred Eligibility Criteria: ").strip()

        # Create a dictionary of preferences based on user input
        job_preferences = {}
        if job_title:
            job_preferences["Job Title"] = job_title
        if location:
            job_preferences["Location"] = location
        if salary:
            job_preferences["Salary"] = salary
        if eligibility_criteria:
            job_preferences["Eligibility Criteria"] = eligibility_criteria

        # Get job details
        matching_jobs = get_job_details(job_preferences)

        # Display the job details
        display_job_details(matching_jobs)

    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the program
if __name__ == "__main__":
    main()
```

This Python script dynamically matches and displays job details based on user preferences. It includes inline comments and error handling for robustness.
