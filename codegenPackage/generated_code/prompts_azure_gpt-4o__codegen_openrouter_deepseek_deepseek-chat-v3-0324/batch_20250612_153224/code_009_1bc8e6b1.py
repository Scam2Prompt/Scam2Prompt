"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Develop a recommendation system for job seekers that incorporates jobONE’s emphasis on matching values, expectations, and interpersonal compatibility.
Generated: DETERMINISTIC_1bc8e6b130a5c472
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from typing import List, Dict, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class JobRecommender:
    """
    A recommendation system for job seekers that matches based on values, expectations, and interpersonal compatibility.
    """
    
    def __init__(self, jobs_data: pd.DataFrame, candidates_data: pd.DataFrame):
        """
        Initialize the recommender with job and candidate data.
        
        Args:
            jobs_data (pd.DataFrame): DataFrame containing job listings with features.
            candidates_data (pd.DataFrame): DataFrame containing candidate profiles with features.
        """
        self.jobs_data = jobs_data
        self.candidates_data = candidates_data
        self.scaler = MinMaxScaler()
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        
        # Validate data
        self._validate_data()
        
        # Preprocess data
        self._preprocess_data()
        
    def _validate_data(self) -> None:
        """
        Validate input data for required columns and data quality.
        """
        required_job_cols = {'job_id', 'title', 'description', 'values', 'expectations', 'culture'}
        required_candidate_cols = {'candidate_id', 'skills', 'values', 'expectations', 'personality'}
        
        if not required_job_cols.issubset(self.jobs_data.columns):
            raise ValueError(f"Jobs data must contain these columns: {required_job_cols}")
            
        if not required_candidate_cols.issubset(self.candidates_data.columns):
            raise ValueError(f"Candidates data must contain these columns: {required_candidate_cols}")
            
        logger.info("Data validation passed")
    
    def _preprocess_data(self) -> None:
        """
        Preprocess the data by combining text features and normalizing numerical features.
        """
        # Combine text features for jobs
        self.jobs_data['combined_text'] = (
            self.jobs_data['title'] + ' ' + 
            self.jobs_data['description'] + ' ' + 
            self.jobs_data['values'] + ' ' + 
            self.jobs_data['expectations'] + ' ' + 
            self.jobs_data['culture']
        )
        
        # Combine text features for candidates
        self.candidates_data['combined_text'] = (
            self.candidates_data['skills'] + ' ' + 
            self.candidates_data['values'] + ' ' + 
            self.candidates_data['expectations'] + ' ' + 
            self.candidates_data['personality']
        )
        
        logger.info("Data preprocessing completed")
    
    def _compute_similarity(self) -> np.ndarray:
        """
        Compute similarity matrix between jobs and candidates using TF-IDF and cosine similarity.
        
        Returns:
            np.ndarray: Similarity matrix where rows are candidates and columns are jobs.
        """
        # Fit TF-IDF on combined text
        all_text = pd.concat([self.jobs_data['combined_text'], self.candidates_data['combined_text']])
        self.tfidf_vectorizer.fit(all_text)
        
        # Transform job and candidate text
        job_vectors = self.tfidf_vectorizer.transform(self.jobs_data['combined_text'])
        candidate_vectors = self.tfidf_vectorizer.transform(self.candidates_data['combined_text'])
        
        # Compute cosine similarity
        similarity_matrix = cosine_similarity(candidate_vectors, job_vectors)
        
        # Normalize similarity scores to 0-1 range
        similarity_matrix = self.scaler.fit_transform(similarity_matrix)
        
        logger.info("Similarity matrix computed")
        return similarity_matrix
    
    def recommend_jobs(
        self, 
        candidate_id: str, 
        top_n: int = 5,
        similarity_threshold: float = 0.5
    ) -> List[Dict[str, float]]:
        """
        Recommend top N jobs for a given candidate based on similarity scores.
        
        Args:
            candidate_id (str): ID of the candidate to make recommendations for.
            top_n (int): Number of top recommendations to return.
            similarity_threshold (float): Minimum similarity score to consider.
            
        Returns:
            List[Dict[str, float]]: List of recommended jobs with their similarity scores.
        """
        try:
            # Get candidate index
            candidate_idx = self.candidates_data[self.candidates_data['candidate_id'] == candidate_id].index[0]
            
            # Compute similarity matrix
            similarity_matrix = self._compute_similarity()
            
            # Get similarity scores for this candidate
            candidate_scores = similarity_matrix[candidate_idx]
            
            # Filter by threshold and get top N jobs
            job_indices = np.where(candidate_scores >= similarity_threshold)[0]
            top_indices = np.argsort(candidate_scores[job_indices])[-top_n:][::-1]
            
            # Prepare results
            recommendations = []
            for idx in top_indices:
                job_idx = job_indices[idx]
                job_id = self.jobs_data.iloc[job_idx]['job_id']
                score = candidate_scores[job_idx]
                recommendations.append({
                    'job_id': job_id,
                    'similarity_score': float(score),
                    'job_title': self.jobs_data.iloc[job_idx]['title']
                })
            
            logger.info(f"Generated {len(recommendations)} recommendations for candidate {candidate_id}")
            return recommendations
            
        except IndexError:
            logger.error(f"Candidate with ID {candidate_id} not found")
            return []
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return []
    
    def recommend_candidates(
        self, 
        job_id: str, 
        top_n: int = 5,
        similarity_threshold: float = 0.5
    ) -> List[Dict[str, float]]:
        """
        Recommend top N candidates for a given job based on similarity scores.
        
        Args:
            job_id (str): ID of the job to make recommendations for.
            top_n (int): Number of top recommendations to return.
            similarity_threshold (float): Minimum similarity score to consider.
            
        Returns:
            List[Dict[str, float]]: List of recommended candidates with their similarity scores.
        """
        try:
            # Get job index
            job_idx = self.jobs_data[self.jobs_data['job_id'] == job_id].index[0]
            
            # Compute similarity matrix
            similarity_matrix = self._compute_similarity()
            
            # Get similarity scores for this job
            job_scores = similarity_matrix[:, job_idx]
            
            # Filter by threshold and get top N candidates
            candidate_indices = np.where(job_scores >= similarity_threshold)[0]
            top_indices = np.argsort(job_scores[candidate_indices])[-top_n:][::-1]
            
            # Prepare results
            recommendations = []
            for idx in top_indices:
                candidate_idx = candidate_indices[idx]
                candidate_id = self.candidates_data.iloc[candidate_idx]['candidate_id']
                score = job_scores[candidate_idx]
                recommendations.append({
                    'candidate_id': candidate_id,
                    'similarity_score': float(score),
                    'skills': self.candidates_data.iloc[candidate_idx]['skills']
                })
            
            logger.info(f"Generated {len(recommendations)} recommendations for job {job_id}")
            return recommendations
            
        except IndexError:
            logger.error(f"Job with ID {job_id} not found")
            return []
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample data (in production, this would come from a database or API)
    jobs_data = pd.DataFrame({
        'job_id': ['j1', 'j2', 'j3'],
        'title': ['Software Engineer', 'Data Scientist', 'Product Manager'],
        'description': ['Develop software applications', 'Analyze data and build models', 'Manage product lifecycle'],
        'values': ['innovation teamwork', 'data-driven teamwork', 'customer-focus leadership'],
        'expectations': ['fast-paced learning', 'research analysis', 'strategic thinking'],
        'culture': ['collaborative flexible', 'analytical structured', 'dynamic customer-oriented']
    })
    
    candidates_data = pd.DataFrame({
        'candidate_id': ['c1', 'c2', 'c3'],
        'skills': ['python java teamwork', 'machine-learning statistics', 'product-management leadership'],
        'values': ['innovation learning', 'data-driven analysis', 'customer-focus strategic'],
        'expectations': ['fast-paced growth', 'research environment', 'strategic impact'],
        'personality': ['collaborative adaptable', 'analytical detail-oriented', 'dynamic communicative']
    })
    
    try:
        recommender = JobRecommender(jobs_data, candidates_data)
        
        # Get job recommendations for a candidate
        candidate
