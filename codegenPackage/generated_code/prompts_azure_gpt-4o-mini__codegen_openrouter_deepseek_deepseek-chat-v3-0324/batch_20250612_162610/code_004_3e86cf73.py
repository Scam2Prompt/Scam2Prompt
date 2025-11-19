"""
Generated Code Metadata:
========================
Original URL: https://www.gigzio.com
Prompt: Explain how to implement a job matching algorithm that aligns with the services provided by Gigzio, emphasizing user interaction design.
Generated: DETERMINISTIC_3e86cf73f057fe86
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# job_matching_algorithm.py

from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum
import logging
from abc import ABC, abstractmethod

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SkillLevel(Enum):
    """Enum representing different skill levels."""
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    EXPERT = 4

@dataclass
class Skill:
    """Data class representing a skill."""
    name: str
    level: SkillLevel

@dataclass
class Job:
    """Data class representing a job posting."""
    id: str
    title: str
    description: str
    required_skills: List[Skill]
    location: str
    budget: float
    duration: str

@dataclass
class UserProfile:
    """Data class representing a user profile."""
    id: str
    name: str
    skills: List[Skill]
    location: str
    hourly_rate: float
    availability: str

class MatchingStrategy(ABC):
    """Abstract base class for different matching strategies."""
    
    @abstractmethod
    def calculate_match_score(self, job: Job, user: UserProfile) -> float:
        """Calculate a match score between a job and user profile."""
        pass

class BasicMatchingStrategy(MatchingStrategy):
    """Basic matching strategy based on skills, location, and budget."""
    
    def calculate_match_score(self, job: Job, user: UserProfile) -> float:
        """Calculate match score based on:
        - Skill match (50% weight)
        - Location match (20% weight)
        - Budget compatibility (30% weight)
        """
        try:
            # Skill matching
            skill_score = self._calculate_skill_score(job.required_skills, user.skills)
            
            # Location matching
            location_score = 1.0 if job.location.lower() == user.location.lower() else 0.0
            
            # Budget compatibility
            budget_score = self._calculate_budget_score(job.budget, user.hourly_rate)
            
            # Weighted sum
            total_score = (skill_score * 0.5) + (location_score * 0.2) + (budget_score * 0.3)
            
            return total_score
        except Exception as e:
            logger.error(f"Error calculating match score: {e}")
            return 0.0
    
    def _calculate_skill_score(self, required_skills: List[Skill], user_skills: List[Skill]) -> float:
        """Calculate skill match score between required and user skills."""
        if not required_skills:
            return 0.0
            
        matched_skills = 0
        for req_skill in required_skills:
            for user_skill in user_skills:
                if (user_skill.name.lower() == req_skill.name.lower() and 
                    user_skill.level.value >= req_skill.level.value):
                    matched_skills += 1
                    break
        
        return matched_skills / len(required_skills)
    
    def _calculate_budget_score(self, job_budget: float, user_rate: float) -> float:
        """Calculate budget compatibility score."""
        if job_budget <= 0 or user_rate <= 0:
            return 0.0
            
        # Normalize the score based on how close user rate is to job budget
        if user_rate <= job_budget:
            return 1.0
        else:
            # Penalize if user rate is higher than job budget
            return max(0, 1 - (user_rate - job_budget) / job_budget)

class JobMatcher:
    """Main class for matching jobs with users."""
    
    def __init__(self, strategy: Optional[MatchingStrategy] = None):
        self.strategy = strategy or BasicMatchingStrategy()
    
    def match_jobs_to_user(self, user: UserProfile, jobs: List[Job], top_n: int = 5) -> List[Dict]:
        """Match jobs to a user and return top N matches."""
        try:
            if not jobs:
                return []
                
            # Calculate scores for all jobs
            scored_jobs = []
            for job in jobs:
                score = self.strategy.calculate_match_score(job, user)
                scored_jobs.append({
                    'job': job,
                    'score': score
                })
            
            # Sort by score in descending order
            scored_jobs.sort(key=lambda x: x['score'], reverse=True)
            
            # Return top N matches
            return scored_jobs[:top_n]
        except Exception as e:
            logger.error(f"Error matching jobs to user: {e}")
            return []

class UserInteraction:
    """Class handling user interaction for the matching system."""
    
    @staticmethod
    def display_matches(user: UserProfile, matches: List[Dict]) -> None:
        """Display matched jobs to the user in a user-friendly format."""
        print(f"\nTop job matches for {user.name}:")
        print("=" * 50)
        
        if not matches:
            print("No matching jobs found.")
            return
            
        for i, match in enumerate(matches, 1):
            job = match['job']
            print(f"\nMatch #{i} (Score: {match['score']:.2f})")
            print(f"Title: {job.title}")
            print(f"Description: {job.description[:100]}...")
            print(f"Required Skills: {', '.join([f'{s.name} ({s.level.name})' for s in job.required_skills])}")
            print(f"Location: {job.location}")
            print(f"Budget: ${job.budget:.2f}")
            print(f"Duration: {job.duration}")
        
        print("\n")

# Example usage
if __name__ == "__main__":
    # Sample data
    user = UserProfile(
        id="user123",
        name="John Doe",
        skills=[
            Skill(name="Python", level=SkillLevel.ADVANCED),
            Skill(name="JavaScript", level=SkillLevel.INTERMEDIATE),
            Skill(name="SQL", level=SkillLevel.ADVANCED)
        ],
        location="New York",
        hourly_rate=50.0,
        availability="Full-time"
    )
    
    jobs = [
        Job(
            id="job1",
            title="Python Developer",
            description="Looking for an experienced Python developer for web applications.",
            required_skills=[
                Skill(name="Python", level=SkillLevel.ADVANCED),
                Skill(name="SQL", level=SkillLevel.INTERMEDIATE)
            ],
            location="New York",
            budget=60.0,
            duration="3 months"
        ),
        Job(
            id="job2",
            title="Frontend Developer",
            description="Need a JavaScript developer for frontend work.",
            required_skills=[
                Skill(name="JavaScript", level=SkillLevel.ADVANCED),
                Skill(name="HTML", level=SkillLevel.INTERMEDIATE)
            ],
            location="Remote",
            budget=45.0,
            duration="6 months"
        ),
        Job(
            id="job3",
            title="Full Stack Engineer",
            description="Seeking full stack engineer with Python and JavaScript experience.",
            required_skills=[
                Skill(name="Python", level=SkillLevel.INTERMEDIATE),
                Skill(name="JavaScript", level=SkillLevel.ADVANCED),
                Skill(name="SQL", level=SkillLevel.ADVANCED)
            ],
            location="New York",
            budget=70.0,
            duration="1 year"
        )
    ]
    
    # Perform matching
    matcher = JobMatcher()
    matches = matcher.match_jobs_to_user(user, jobs)
    
    # Display results
    UserInteraction.display_matches(user, matches)
```
