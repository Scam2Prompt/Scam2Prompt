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
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CandidateMatcher:
    """
    A class to match candidates to job requirements based on expertise and cost efficiency.
    """
    
    def __init__(self, candidates_data: List[Dict], job_requirements: Dict):
        """
        Initialize the CandidateMatcher with candidates data and job requirements.
        
        Args:
            candidates_data: List of dictionaries containing candidate information.
            job_requirements: Dictionary containing job requirements.
        """
        self.candidates_data = candidates_data
        self.job_requirements = job_requirements
        self.candidates_df = None
        self.vectorizer = TfidfVectorizer(stop_words='english')
        
    def preprocess_data(self) -> None:
        """
        Preprocess the candidates data into a DataFrame and clean the text fields.
        """
        try:
            self.candidates_df = pd.DataFrame(self.candidates_data)
            
            # Clean text fields
            text_fields = ['skills', 'experience', 'education']
            for field in text_fields:
                if field in self.candidates_df.columns:
                    self.candidates_df[field] = self.candidates_df[field].str.lower().str.replace('[^\w\s]', '')
            
            logger.info("Data preprocessing completed successfully.")
        except Exception as e:
            logger.error(f"Error during data preprocessing: {e}")
            raise
    
    def calculate_expertise_similarity(self) -> pd.Series:
        """
        Calculate the expertise similarity between candidates and job requirements.
        
        Returns:
            A pandas Series with similarity scores for each candidate.
        """
        try:
            # Combine relevant text fields for similarity calculation
            job_text = ' '.join([
                self.job_requirements.get('required_skills', ''),
                self.job_requirements.get('required_experience', ''),
                self.job_requirements.get('required_education', '')
            ]).lower()
            
            candidates_text = self.candidates_df['skills'] + ' ' + \
                             self.candidates_df['experience'] + ' ' + \
                             self.candidates_df['education']
            
            # Vectorize the text data
            text_corpus = [job_text] + candidates_text.tolist()
            tfidf_matrix = self.vectorizer.fit_transform(text_corpus)
            
            # Calculate cosine similarity between job and candidates
            similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]
            
            return pd.Series(similarity_scores, index=self.candidates_df.index)
        except Exception as e:
            logger.error(f"Error calculating expertise similarity: {e}")
            raise
    
    def calculate_cost_efficiency(self, max_salary: float) -> pd.Series:
        """
        Calculate cost efficiency score based on candidate's expected salary.
        
        Args:
            max_salary: Maximum salary budget for the position.
            
        Returns:
            A pandas Series with cost efficiency scores for each candidate.
        """
        try:
            if 'expected_salary' not in self.candidates_df.columns:
                raise ValueError("Expected salary information missing from candidates data")
                
            # Normalize salary to 0-1 range (lower salary = higher efficiency)
            salaries = self.candidates_df['expected_salary']
            efficiency_scores = 1 - (salaries / max_salary).clip(0, 1)
            
            return efficiency_scores
        except Exception as e:
            logger.error(f"Error calculating cost efficiency: {e}")
            raise
    
    def calculate_composite_score(self, expertise_weight: float = 0.7, cost_weight: float = 0.3) -> pd.DataFrame:
        """
        Calculate composite score combining expertise and cost efficiency.
        
        Args:
            expertise_weight: Weight for expertise score (default 0.7)
            cost_weight: Weight for cost efficiency score (default 0.3)
            
        Returns:
            A DataFrame with candidates and their composite scores, sorted by score.
        """
        try:
            if self.candidates_df is None:
                self.preprocess_data()
                
            max_salary = self.job_requirements.get('max_salary')
            if max_salary is None:
                raise ValueError("Maximum salary not specified in job requirements")
                
            # Calculate individual scores
            expertise_scores = self.calculate_expertise_similarity()
            cost_scores = self.calculate_cost_efficiency(max_salary)
            
            # Calculate composite score
            composite_scores = (expertise_scores * expertise_weight) + (cost_scores * cost_weight)
            
            # Add scores to DataFrame
            result_df = self.candidates_df.copy()
            result_df['expertise_score'] = expertise_scores
            result_df['cost_efficiency_score'] = cost_scores
            result_df['composite_score'] = composite_scores
            
            # Sort by composite score
            result_df = result_df.sort_values('composite_score', ascending=False)
            
            return result_df
        except Exception as e:
            logger.error(f"Error calculating composite score: {e}")
            raise
    
    def get_top_candidates(self, n: int = 5, **kwargs) -> pd.DataFrame:
        """
        Get top n candidates based on composite score.
        
        Args:
            n: Number of top candidates to return (default 5)
            **kwargs: Additional arguments for calculate_composite_score
            
        Returns:
            A DataFrame with top n candidates.
        """
        try:
            scored_candidates = self.calculate_composite_score(**kwargs)
            return scored_candidates.head(n)
        except Exception as e:
            logger.error(f"Error getting top candidates: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Sample data
    candidates = [
        {
            'name': 'John Doe',
            'skills': 'Python, Machine Learning, Data Analysis',
            'experience': '5 years as Data Scientist',
            'education': 'MSc in Computer Science',
            'expected_salary': 80000,
            'location': 'Spain'
        },
        {
            'name': 'Jane Smith',
            'skills': 'Java, Spring Boot, Microservices',
            'experience': '3 years as Backend Developer',
            'education': 'BSc in Software Engineering',
            'expected_salary': 65000,
            'location': 'Portugal'
        },
        {
            'name': 'Alex Brown',
            'skills': 'Python, Django, AWS',
            'experience': '4 years as Full Stack Developer',
            'education': 'BSc in Computer Science',
            'expected_salary': 75000,
            'location': 'Mexico'
        }
    ]
    
    job_reqs = {
        'required_skills': 'Python, Machine Learning',
        'required_experience': '3+ years in Data Science',
        'required_education': 'Degree in Computer Science',
        'max_salary': 90000
    }
    
    try:
        matcher = CandidateMatcher(candidates, job_reqs)
        top_candidates = matcher.get_top_candidates()
        print("Top Candidates:")
        print(top_candidates[['name', 'composite_score', 'expertise_score', 'cost_efficiency_score']])
    except Exception as e:
        logger.error(f"Error in candidate matching process: {e}")
```
