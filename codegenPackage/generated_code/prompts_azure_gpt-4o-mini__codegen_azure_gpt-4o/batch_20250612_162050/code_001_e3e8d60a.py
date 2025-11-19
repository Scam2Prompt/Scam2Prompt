"""
Generated Code Metadata:
========================
Original URL: https://highvaluestaffing.com
Prompt: Write a Python script that automates the job matching process, inspired by High Value Staffing's method of connecting candidates with organizations.
Generated: DETERMINISTIC_e3e8d60ad188b589
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class JobMatcher:
    """
    A class to automate the job matching process between candidates and organizations.
    """

    def __init__(self, candidates: List[Dict[str, Any]], jobs: List[Dict[str, Any]]):
        """
        Initialize the JobMatcher with candidates and job listings.

        :param candidates: List of candidate profiles (dicts with skills, experience, etc.)
        :param jobs: List of job postings (dicts with required skills, experience, etc.)
        """
        self.candidates = candidates
        self.jobs = jobs

    def match_jobs(self) -> Dict[str, List[str]]:
        """
        Match candidates to jobs based on skills and experience.

        :return: A dictionary where keys are job titles and values are lists of matched candidate names.
        """
        matches = {}
        for job in self.jobs:
            job_title = job.get("title", "Unknown Job")
            required_skills = set(job.get("skills", []))
            required_experience = job.get("experience", 0)

            matches[job_title] = []
            for candidate in self.candidates:
                candidate_name = candidate.get("name", "Unknown Candidate")
                candidate_skills = set(candidate.get("skills", []))
                candidate_experience = candidate.get("experience", 0)

                # Check if candidate meets job requirements
                if required_skills.issubset(candidate_skills) and candidate_experience >= required_experience:
                    matches[job_title].append(candidate_name)

        return matches

def load_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Load JSON data from a file.

    :param file_path: Path to the JSON file.
    :return: Parsed JSON data as a list of dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
        return []

def save_matches(matches: Dict[str, List[str]], output_file: str) -> None:
    """
    Save job matches to a JSON file.

    :param matches: Dictionary of job matches.
    :param output_file: Path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as file:
            json.dump(matches, file, indent=4)
        logging.info(f"Matches saved to {output_file}")
    except Exception as e:
        logging.error(f"Error saving matches to file: {e}")

def main():
    """
    Main function to execute the job matching process.
    """
    # Load candidate and job data
    candidates = load_data("candidates.json")
    jobs = load_data("jobs.json")

    if not candidates or not jobs:
        logging.error("Candidate or job data is missing. Exiting.")
        return

    # Perform job matching
    matcher = JobMatcher(candidates, jobs)
    matches = matcher.match_jobs()

    # Save matches to a file
    save_matches(matches, "matches.json")

if __name__ == "__main__":
    main()
```
