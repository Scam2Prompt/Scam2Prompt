"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Write a short algorithm for matching candidates with job openings based on their values, expectations, and personality, reflecting jobONE's matching process.
Generated: DETERMINISTIC_b35ca146b3cf9c17
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Candidate:
    def __init__(self, name, values, expectations, personality):
        self.name = name
        self.values = values  # List of values (e.g., ["innovation", "teamwork"])
        self.expectations = expectations  # Dict of expectations (e.g., {"salary": 70000, "location": "remote"})
        self.personality = personality  # Personality type (e.g., "extrovert")

class JobOpening:
    def __init__(self, title, values, requirements, personality_fit):
        self.title = title
        self.values = values  # List of values (e.g., ["creativity", "teamwork"])
        self.requirements = requirements  # Dict of requirements (e.g., {"salary": 75000, "location": "remote"})
        self.personality_fit = personality_fit  # Preferred personality type (e.g., "extrovert")

def match_candidates_to_jobs(candidates, job_openings):
    """
    Matches candidates to job openings based on shared values, expectations, and personality fit.

    Args:
        candidates (list): List of Candidate objects.
        job_openings (list): List of JobOpening objects.

    Returns:
        dict: A dictionary mapping job titles to lists of matched candidate names.
    """
    matches = {}

    for job in job_openings:
        matches[job.title] = []  # Initialize an empty list for each job title

        for candidate in candidates:
            try:
                # Calculate value match (intersection of values)
                shared_values = set(candidate.values) & set(job.values)
                value_match_score = len(shared_values) / len(job.values)

                # Check if expectations align with job requirements
                expectations_match = all(
                    candidate.expectations.get(key) == job.requirements.get(key)
                    for key in candidate.expectations
                    if key in job.requirements
                )

                # Check personality fit
                personality_match = candidate.personality == job.personality_fit

                # If all criteria are met, add candidate to the job's match list
                if value_match_score >= 0.5 and expectations_match and personality_match:
                    matches[job.title].append(candidate.name)

            except Exception as e:
                # Log error and continue processing other candidates
                print(f"Error matching candidate {candidate.name} to job {job.title}: {e}")

    return matches

# Example usage
if __name__ == "__main__":
    # Sample candidates
    candidates = [
        Candidate("Alice", ["innovation", "teamwork"], {"salary": 70000, "location": "remote"}, "extrovert"),
        Candidate("Bob", ["creativity", "independence"], {"salary": 75000, "location": "onsite"}, "introvert"),
    ]

    # Sample job openings
    job_openings = [
        JobOpening("Software Engineer", ["innovation", "teamwork"], {"salary": 70000, "location": "remote"}, "extrovert"),
        JobOpening("Product Manager", ["creativity", "teamwork"], {"salary": 75000, "location": "onsite"}, "extrovert"),
    ]

    # Perform matching
    matches = match_candidates_to_jobs(candidates, job_openings)

    # Output results
    print(json.dumps(matches, indent=4))
```
