"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: Write a Python function that automates the process of selecting candidates based on specific criteria, inspired by the talent selection strategies outlined on Videtis Consultores' website.
Generated: DETERMINISTIC_4187e972ac3942cd
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict, Optional

class CandidateSelector:
    """
    A class to automate the selection of candidates based on specific criteria.
    Inspired by talent selection strategies from Videtis Consultores.
    """
    
    def __init__(self, candidates_data: List[Dict], required_skills: List[str], 
                 min_experience: int = 2, education_level: Optional[str] = None):
        """
        Initialize the CandidateSelector with candidate data and selection criteria.
        
        Args:
            candidates_data: List of dictionaries containing candidate information
            required_skills: List of skills that candidates must possess
            min_experience: Minimum years of experience required (default: 2)
            education_level: Required education level if specified (default: None)
        """
        self.candidates_df = pd.DataFrame(candidates_data)
        self.required_skills = required_skills
        self.min_experience = min_experience
        self.education_level = education_level
        
        # Validate input data
        self._validate_input()
    
    def _validate_input(self) -> None:
        """Validate the input data and criteria."""
        if not isinstance(self.candidates_df, pd.DataFrame) or self.candidates_df.empty:
            raise ValueError("Candidate data must be a non-empty pandas DataFrame")
            
        if not isinstance(self.required_skills, list) or not self.required_skills:
            raise ValueError("Required skills must be a non-empty list")
            
        if not isinstance(self.min_experience, int) or self.min_experience < 0:
            raise ValueError("Minimum experience must be a non-negative integer")
    
    def _filter_by_skills(self) -> pd.DataFrame:
        """Filter candidates by required skills."""
        def has_required_skills(skills: List[str]) -> bool:
            return all(skill in skills for skill in self.required_skills)
        
        return self.candidates_df[
            self.candidates_df['skills'].apply(has_required_skills)
        ]
    
    def _filter_by_experience(self, df: pd.DataFrame) -> pd.DataFrame:
        """Filter candidates by minimum experience."""
        return df[df['years_experience'] >= self.min_experience]
    
    def _filter_by_education(self, df: pd.DataFrame) -> pd.DataFrame:
        """Filter candidates by education level if specified."""
        if self.education_level:
            return df[df['education_level'] == self.education_level]
        return df
    
    def _calculate_scores(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate a composite score for each candidate based on:
        - Skill match percentage
        - Experience above minimum
        - Additional qualifications
        """
        # Calculate skill match percentage
        df['skill_score'] = df['skills'].apply(
            lambda x: sum(1 for skill in x if skill in self.required_skills) / len(self.required_skills)
        )
        
        # Calculate experience bonus (1 point per year above minimum)
        df['experience_score'] = df['years_experience'].apply(
            lambda x: max(0, x - self.min_experience) * 0.1
        )
        
        # Calculate total score (weighted sum)
        df['total_score'] = (df['skill_score'] * 0.7) + (df['experience_score'] * 0.3)
        
        return df
    
    def select_candidates(self, top_n: Optional[int] = None) -> pd.DataFrame:
        """
        Select candidates based on the specified criteria and return the top candidates.
        
        Args:
            top_n: Number of top candidates to return (default: None returns all)
            
        Returns:
            DataFrame containing selected candidates sorted by score
        """
        try:
            # Apply all filters
            filtered = self._filter_by_skills()
            filtered = self._filter_by_experience(filtered)
            filtered = self._filter_by_education(filtered)
            
            # Calculate scores and sort
            scored = self._calculate_scores(filtered)
            scored = scored.sort_values('total_score', ascending=False)
            
            # Return top_n candidates if specified
            if top_n and isinstance(top_n, int) and top_n > 0:
                return scored.head(top_n)
            return scored
        
        except Exception as e:
            raise RuntimeError(f"Error in candidate selection process: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample candidate data
    candidates = [
        {
            "name": "John Doe",
            "skills": ["Python", "SQL", "Machine Learning"],
            "years_experience": 5,
            "education_level": "Master"
        },
        {
            "name": "Jane Smith",
            "skills": ["Python", "Data Analysis"],
            "years_experience": 3,
            "education_level": "Bachelor"
        },
        {
            "name": "Bob Johnson",
            "skills": ["Java", "SQL"],
            "years_experience": 4,
            "education_level": "Bachelor"
        }
    ]
    
    # Initialize selector
    selector = CandidateSelector(
        candidates_data=candidates,
        required_skills=["Python", "SQL"],
        min_experience=2,
        education_level="Bachelor"
    )
    
    # Get top candidates
    top_candidates = selector.select_candidates(top_n=2)
    print(top_candidates[['name', 'total_score']])
```
