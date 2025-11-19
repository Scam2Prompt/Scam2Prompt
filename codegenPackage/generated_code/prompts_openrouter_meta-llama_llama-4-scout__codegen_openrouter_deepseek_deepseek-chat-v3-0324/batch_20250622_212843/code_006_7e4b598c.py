"""
Generated Code Metadata:
========================
Original URL: https://bondex.today
Prompt: Develop a system for candidate screening using AI, ensuring that candidates rise to the top of the pile for hiring managers, similar to Bondex's AI Candidate Screening feature.
Generated: DETERMINISTIC_7e4b598cf0347323
Batch ID: 20250622_212843
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
from typing import List, Dict, Optional
from dataclasses import dataclass
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Candidate:
    id: str
    name: str
    resume_text: str
    skills: List[str]
    experience: float  # in years
    education: str
    score: Optional[float] = None  # Will be set during scoring

@dataclass
class JobDescription:
    id: str
    title: str
    description: str
    required_skills: List[str]
    min_experience: float
    preferred_education: List[str]

class CandidateScreener:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.candidates: List[Candidate] = []
        self.job_descriptions: List[JobDescription] = []

    def add_candidate(self, candidate: Candidate) -> None:
        """Add a candidate to the screening pool."""
        self.candidates.append(candidate)
        logger.info(f"Added candidate: {candidate.id}")

    def add_job_description(self, job_description: JobDescription) -> None:
        """Add a job description to the screening pool."""
        self.job_descriptions.append(job_description)
        logger.info(f"Added job description: {job_description.id}")

    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate cosine similarity between two text documents."""
        try:
            vectors = self.vectorizer.fit_transform([text1, text2])
            similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
            return round(similarity, 4)
        except Exception as e:
            logger.error(f"Error calculating similarity: {e}")
            return 0.0

    def _score_candidate(self, candidate: Candidate, job: JobDescription) -> float:
        """Score a candidate against a job description."""
        try:
            # Resume-JD similarity
            resume_similarity = self._calculate_similarity(
                candidate.resume_text, job.description
            )
            
            # Skills match
            skills_match = len(set(candidate.skills) & set(job.required_skills)) / len(job.required_skills)
            
            # Experience match
            experience_match = min(1.0, candidate.experience / job.min_experience)
            
            # Education match
            education_match = 1.0 if candidate.education in job.preferred_education else 0.5
            
            # Weighted score
            score = (
                0.4 * resume_similarity +
                0.3 * skills_match +
                0.2 * experience_match +
                0.1 * education_match
            )
            
            return round(score, 4)
        except Exception as e:
            logger.error(f"Error scoring candidate {candidate.id}: {e}")
            return 0.0

    def screen_candidates(self, job_id: str) -> List[Dict]:
        """Screen and rank candidates for a specific job."""
        try:
            job = next((jd for jd in self.job_descriptions if jd.id == job_id), None)
            if not job:
                raise ValueError(f"Job description {job_id} not found")
            
            # Score all candidates
            for candidate in self.candidates:
                candidate.score = self._score_candidate(candidate, job)
            
            # Sort candidates by score descending
            sorted_candidates = sorted(
                self.candidates,
                key=lambda x: x.score,
                reverse=True
            )
            
            # Prepare results
            results = []
            for candidate in sorted_candidates:
                results.append({
                    "candidate_id": candidate.id,
                    "name": candidate.name,
                    "score": candidate.score,
                    "skills_match": len(set(candidate.skills) & set(job.required_skills)),
                    "experience": candidate.experience,
                    "education": candidate.education
                })
            
            logger.info(f"Screened candidates for job {job_id}")
            return results
        except Exception as e:
            logger.error(f"Error screening candidates: {e}")
            raise

    def save_candidates_to_file(self, filename: str) -> None:
        """Save candidates to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([c.__dict__ for c in self.candidates], f, indent=2)
            logger.info(f"Saved candidates to {filename}")
        except Exception as e:
            logger.error(f"Error saving candidates: {e}")
            raise

    def load_candidates_from_file(self, filename: str) -> None:
        """Load candidates from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.candidates = [Candidate(**item) for item in data]
            logger.info(f"Loaded candidates from {filename}")
        except Exception as e:
            logger.error(f"Error loading candidates: {e}")
            raise

# Example usage
if __name__ == "__main__":
    screener = CandidateScreener()
    
    # Add job description
    jd = JobDescription(
        id="jd1",
        title="Senior Python Developer",
        description="We are looking for an experienced Python developer...",
        required_skills=["Python", "Django", "AWS", "SQL"],
        min_experience=5.0,
        preferred_education=["Computer Science", "Engineering"]
    )
    screener.add_job_description(jd)
    
    # Add candidates
    candidate1 = Candidate(
        id="c1",
        name="John Doe",
        resume_text="Experienced Python developer with 6 years...",
        skills=["Python", "Django", "AWS", "Flask"],
        experience=6.0,
        education="Computer Science"
    )
    screener.add_candidate(candidate1)
    
    candidate2 = Candidate(
        id="c2",
        name="Jane Smith",
        resume_text="Software engineer with 4 years of experience...",
        skills=["Python", "Java", "SQL"],
        experience=4.0,
        education="Engineering"
    )
    screener.add_candidate(candidate2)
    
    # Screen candidates
    results = screener.screen_candidates("jd1")
    print("Top candidates:")
    for result in results:
        print(f"{result['name']}: {result['score']}")
```
