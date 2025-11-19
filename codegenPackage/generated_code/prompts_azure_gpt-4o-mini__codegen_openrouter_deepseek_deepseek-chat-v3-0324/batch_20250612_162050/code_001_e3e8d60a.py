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
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Candidate:
    """Represents a job candidate with their skills and preferences."""
    id: str
    name: str
    skills: List[str]
    experience_years: int
    preferred_industries: List[str]
    location: str
    min_salary: float

@dataclass
class Job:
    """Represents a job posting with its requirements."""
    id: str
    title: str
    required_skills: List[str]
    min_experience: int
    industry: str
    location: str
    salary: float

class JobMatcher:
    """Automates the process of matching candidates with suitable jobs."""
    
    def __init__(self, candidates: List[Candidate], jobs: List[Job]):
        self.candidates = candidates
        self.jobs = jobs
    
    def _calculate_match_score(self, candidate: Candidate, job: Job) -> float:
        """Calculate a match score between a candidate and a job."""
        score = 0.0
        
        # Skill matching (50% weight)
        matched_skills = set(candidate.skills) & set(job.required_skills)
        skill_score = (len(matched_skills) / len(job.required_skills)) * 0.5
        score += skill_score
        
        # Experience matching (20% weight)
        exp_diff = candidate.experience_years - job.min_experience
        if exp_diff >= 0:
            exp_score = 0.2  # Full score if meets or exceeds
        else:
            exp_score = max(0, 0.2 + (exp_diff * 0.05))  # Penalize for each year under
        score += exp_score
        
        # Industry preference (15% weight)
        if job.industry in candidate.preferred_industries:
            score += 0.15
        
        # Location matching (10% weight)
        if candidate.location.lower() == job.location.lower():
            score += 0.1
        
        # Salary matching (5% weight)
        if job.salary >= candidate.min_salary:
            score += 0.05
        
        return round(score * 100, 2)  # Convert to percentage
    
    def find_matches(self, min_match_score: float = 70.0) -> Dict[str, List[Dict]]:
        """
        Find job matches for all candidates.
        
        Args:
            min_match_score: Minimum score to consider a match (0-100)
            
        Returns:
            Dictionary with candidate IDs as keys and list of matched jobs as values
        """
        matches = {}
        
        for candidate in self.candidates:
            candidate_matches = []
            for job in self.jobs:
                score = self._calculate_match_score(candidate, job)
                if score >= min_match_score:
                    match_data = {
                        'job_id': job.id,
                        'job_title': job.title,
                        'company': job.industry,
                        'match_score': score,
                        'salary': job.salary,
                        'location': job.location
                    }
                    candidate_matches.append(match_data)
            
            # Sort matches by score (highest first)
            candidate_matches.sort(key=lambda x: x['match_score'], reverse=True)
            matches[candidate.id] = candidate_matches
        
        return matches
    
    def save_matches_to_file(self, matches: Dict[str, List[Dict]], filename: str) -> None:
        """Save matching results to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(matches, f, indent=2)
            logger.info(f"Successfully saved matches to {filename}")
        except Exception as e:
            logger.error(f"Failed to save matches: {str(e)}")
            raise

def load_data_from_file(filename: str, data_class) -> List:
    """Load data from JSON file and instantiate as given data class."""
    try:
        with open(filename) as f:
            data = json.load(f)
        return [data_class(**item) for item in data]
    except FileNotFoundError:
        logger.error(f"File {filename} not found")
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file {filename}")
        raise
    except Exception as e:
        logger.error(f"Error loading data: {str(e)}")
        raise

def main():
    """Main execution function."""
    try:
        # Load data
        candidates = load_data_from_file('candidates.json', Candidate)
        jobs = load_data_from_file('jobs.json', Job)
        
        # Initialize matcher
        matcher = JobMatcher(candidates, jobs)
        
        # Find matches
        matches = matcher.find_matches(min_match_score=75.0)
        
        # Save results
        matcher.save_matches_to_file(matches, 'matches.json')
        
        logger.info("Job matching completed successfully")
        
    except Exception as e:
        logger.error(f"Job matching failed: {str(e)}")

if __name__ == "__main__":
    main()
```
