"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://managementenred.com
Prompt: Generate code to automate the process of matching candidates to job requirements for international recruiting, incorporating criteria like expertise and cost efficiency as outlined by Management en Red.
Generated: DETERMINISTIC_1b03f378c689fa67
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CandidateMatcher:
    """
    A class to automate the process of matching candidates to job requirements
    based on expertise and cost efficiency.
    """

    def __init__(self, candidates, job_requirements):
        """
        Initialize the CandidateMatcher with a list of candidates and job requirements.

        :param candidates: List of candidate dictionaries with details (e.g., expertise, cost).
        :param job_requirements: List of job requirement dictionaries with criteria.
        """
        self.candidates = candidates
        self.job_requirements = job_requirements

    def match_candidates(self):
        """
        Match candidates to job requirements based on expertise and cost efficiency.

        :return: Dictionary where keys are job requirement IDs and values are lists of matched candidates.
        """
        matches = {}
        for job in self.job_requirements:
            job_id = job['id']
            required_expertise = job['expertise']
            budget = job['budget']

            # Filter candidates based on expertise and cost
            matched_candidates = [
                candidate for candidate in self.candidates
                if required_expertise in candidate['expertise']
                and candidate['cost'] <= budget
            ]

            # Sort matched candidates by cost (ascending) and expertise match (descending)
            matched_candidates.sort(key=lambda x: (x['cost'], -x['expertise'].count(required_expertise)))

            matches[job_id] = matched_candidates

        return matches

    @staticmethod
    def load_data(file_path):
        """
        Load JSON data from a file.

        :param file_path: Path to the JSON file.
        :return: Parsed JSON data.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error: File '{file_path}' contains invalid JSON.")
            return []

    @staticmethod
    def save_results(results, file_path):
        """
        Save matching results to a JSON file.

        :param results: Matching results dictionary.
        :param file_path: Path to the output file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(results, file, indent=4)
            print(f"Results saved successfully to '{file_path}'.")
        except IOError:
            print(f"Error: Unable to write to file '{file_path}'.")

if __name__ == "__main__":
    # Load input data
    candidates_file = 'candidates.json'
    jobs_file = 'job_requirements.json'

    candidates = CandidateMatcher.load_data(candidates_file)
    job_requirements = CandidateMatcher.load_data(jobs_file)

    # Check if data was loaded successfully
    if not candidates or not job_requirements:
        print("Error: Unable to proceed due to missing or invalid data.")
    else:
        # Perform matching
        matcher = CandidateMatcher(candidates, job_requirements)
        matching_results = matcher.match_candidates()

        # Save results to a file
        results_file = 'matching_results.json'
        CandidateMatcher.save_results(matching_results, results_file)
```

### Example Input Files
1. **candidates.json**
```json
[
    {
        "id": 1,
        "name": "Alice Smith",
        "expertise": ["Python", "Machine Learning"],
        "cost": 5000
    },
    {
        "id": 2,
        "name": "Bob Johnson",
        "expertise": ["Java", "Cloud Computing"],
        "cost": 4500
    },
    {
        "id": 3,
        "name": "Charlie Brown",
        "expertise": ["Python", "Data Analysis"],
        "cost": 4000
    }
]
```

2. **job_requirements.json**
```json
[
    {
        "id": 101,
        "title": "Machine Learning Engineer",
        "expertise": "Machine Learning",
        "budget": 5000
    },
    {
        "id": 102,
        "title": "Cloud Computing Specialist",
        "expertise": "Cloud Computing",
        "budget": 4500
    }
]
```
