"""
Generated Code Metadata:
========================
Original URL: https://managementenred.com
Prompt: Generate code to automate the process of matching candidates to job requirements for international recruiting, incorporating criteria like expertise and cost efficiency as outlined by Management en Red.
Generated: DETERMINISTIC_1b03f378c689fa67
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class Candidate:
    """Represents a job candidate."""
    
    def __init__(self, name, expertise, cost):
        """
        Initializes a Candidate object.

        Args:
            name (str): The candidate's name.
            expertise (list): A list of the candidate's areas of expertise.
            cost (float): The candidate's cost.
        """
        self.name = name
        self.expertise = expertise
        self.cost = cost

class Job:
    """Represents a job posting."""
    
    def __init__(self, title, required_expertise, budget):
        """
        Initializes a Job object.

        Args:
            title (str): The job title.
            required_expertise (list): A list of required areas of expertise.
            budget (float): The maximum budget for the job.
        """
        self.title = title
        self.required_expertise = required_expertise
        self.budget = budget

def match_candidates_to_jobs(candidates, jobs):
    """
    Matches candidates to job postings based on expertise and cost efficiency.

    Args:
        candidates (list): A list of Candidate objects.
        jobs (list): A list of Job objects.

    Returns:
        dict: A dictionary where the keys are job titles and the values are lists of matching candidates.
    """
    matches = {}
    
    for job in jobs:
        matching_candidates = []
        
        for candidate in candidates:
            # Check if the candidate meets the job's required expertise
            if all(expertise in candidate.expertise for expertise in job.required_expertise):
                # Check if the candidate is within the job's budget
                if candidate.cost <= job.budget:
                    matching_candidates.append(candidate)
        
        # Sort matching candidates by cost efficiency
        matching_candidates.sort(key=lambda candidate: candidate.cost)
        
        matches[job.title] = matching_candidates
    
    return matches

def main():
    try:
        # Example usage
        candidates = [
            Candidate("John Doe", ["Python", "Java", "C++"], 50000),
            Candidate("Jane Smith", ["Python", "JavaScript", "SQL"], 60000),
            Candidate("Bob Johnson", ["Java", "C++", "AWS"], 70000),
        ]
        
        jobs = [
            Job("Software Engineer", ["Python", "Java"], 55000),
            Job("Data Scientist", ["Python", "SQL", "Machine Learning"], 65000),
            Job("Cloud Engineer", ["AWS", "Java", "C++"], 75000),
        ]
        
        matches = match_candidates_to_jobs(candidates, jobs)
        
        for job, candidates in matches.items():
            print(f"Matching candidates for {job}:")
            for i, candidate in enumerate(candidates):
                print(f"{i+1}. {candidate.name} - Expertise: {candidate.expertise}, Cost: ${candidate.cost}")
            print()
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
