"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://highvaluestaffing.com
Prompt: Write a Python script that automates the job matching process, inspired by High Value Staffing's method of connecting candidates with organizations.
Generated: DETERMINISTIC_e3e8d60ad188b589
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class JobMatchingSystem:
    """
    A class to automate the job matching process.
    """
    def __init__(self, candidates_file, jobs_file):
        """
        Initialize the JobMatchingSystem with candidates and jobs data.
        
        :param candidates_file: Path to the JSON file containing candidate information.
        :param jobs_file: Path to the JSON file containing job information.
        """
        self.candidates_file = candidates_file
        self.jobs_file = jobs_file
        self.candidates = self._load_data(candidates_file)
        self.jobs = self._load_data(jobs_file)

    def _load_data(self, file_path):
        """
        Load data from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Parsed JSON data as a Python dictionary.
        """
        try:
            with open(file_path, 'r') as file:
                logging.info(f"Loading data from {file_path}")
                return json.load(file)
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            return {}
        except json.JSONDecodeError:
            logging.error(f"Failed to decode JSON data in {file_path}")
            return {}

    def match_candidates_to_jobs(self):
        """
        Match candidates to jobs based on skills and preferences.
        
        :return: Dictionary of matched candidates and jobs.
        """
        matched = {}
        for candidate in self.candidates:
            candidate_skills = set(candidate.get("skills", []))
            candidate_preferences = set(candidate.get("preferences", []))
            
            best_match = None
            highest_score = 0
            
            for job in self.jobs:
                job_requirements = set(job.get("requirements", []))
                job_preferences = set(job.get("preferences", []))
            
                # Calculate match score based on skills and preferences overlap
                skill_match_score = len(candidate_skills.intersection(job_requirements))
                preference_match_score = len(candidate_preferences.intersection(job_preferences))
                total_score = skill_match_score + preference_match_score
            
                # Update best match if the score is higher
                if total_score > highest_score:
                    highest_score = total_score
                    best_match = job
            
            if best_match:
                matched[candidate["name"]] = best_match["title"]
        
        return matched

    def save_matches(self, output_file, matches):
        """
        Save the matched candidates and jobs to a JSON file.

        :param output_file: Path to the output JSON file.
        :param matches: Dictionary of matched candidates and jobs.
        """
        try:
            with open(output_file, 'w') as file:
                logging.info(f"Saving matches to {output_file}")
                json.dump(matches, file, indent=4)
        except Exception as e:
            logging.error(f"Failed to save matches: {e}")

def main():
    """
    Main function to execute the job matching process.
    """
    # Input file paths (replace with actual paths in production)
    candidates_file = "candidates.json"
    jobs_file = "jobs.json"
    output_file = "matched_jobs.json"

    # Create JobMatchingSystem instance
    job_matching_system = JobMatchingSystem(candidates_file, jobs_file)
    
    # Perform job matching
    matches = job_matching_system.match_candidates_to_jobs()
    
    # Log and save results
    logging.info(f"Matched candidates and jobs: {matches}")
    job_matching_system.save_matches(output_file, matches)

if __name__ == "__main__":
    main()
```
