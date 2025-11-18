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

```python
# job_display.py

class Job:
    """Class to represent a job with its attributes."""
    
    def __init__(self, title, location, salary, eligibility):
        """Initialize the job properties."""
        self.title = title
        self.location = location
        self.salary = salary
        self.eligibility = eligibility

    def display(self):
        """Display the job details."""
        return f"Job Title: {self.title}\nLocation: {self.location}\nSalary: {self.salary}\nEligibility: {self.eligibility}\n"


def get_user_preferences():
    """Get job preferences from the user."""
    try:
        title = input("Enter job title preference: ")
        location = input("Enter location preference: ")
        salary = input("Enter salary preference: ")
        eligibility = input("Enter eligibility criteria: ")

        return title, location, salary, eligibility
    except Exception as e:
        print(f"Error while getting user input: {e}")
        return None


def filter_jobs(jobs, preferences):
    """Filter jobs based on user preferences."""
    title_pref, location_pref, salary_pref, eligibility_pref = preferences
    matching_jobs = []

    for job in jobs:
        if (title_pref.lower() in job.title.lower() and
                location_pref.lower() in job.location.lower() and
                salary_pref in job.salary and
                eligibility_pref.lower() in job.eligibility.lower()):
            matching_jobs.append(job)
    
    return matching_jobs


def main():
    """Main function to run the job display application."""
    # Sample job data
    jobs = [
        Job("Software Engineer", "New York", "$100,000", "Bachelors in Computer Science"),
        Job("Data Scientist", "San Francisco", "$120,000", "Masters in Data Science"),
        Job("Web Developer", "Remote", "$80,000", "Proficient in HTML, CSS, JavaScript"),
        Job("Project Manager", "Chicago", "$110,000", "5+ years of experience in project management"),
    ]

    # Get user preferences
    preferences = get_user_preferences()
    
    if preferences is None:
        return

    # Filter and display matching jobs
    matching_jobs = filter_jobs(jobs, preferences)

    if matching_jobs:
        print("\nMatching Jobs:\n")
        for job in matching_jobs:
            print(job.display())
    else:
        print("No matching jobs found.")


if __name__ == "__main__":
    main()
```

This code represents a simple command-line application that prompts users for their job preferences, filters a predefined list of jobs based on those preferences, and displays matching job details.
