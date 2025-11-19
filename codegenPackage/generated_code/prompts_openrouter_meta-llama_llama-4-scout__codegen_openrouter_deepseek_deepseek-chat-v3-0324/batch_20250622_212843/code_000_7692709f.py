"""
Generated Code Metadata:
========================
Original URL: https://bondex.today
Prompt: Write a Python script to implement a job matching algorithm using AI, similar to Bondex's AI Job Match feature, which scans resumes and profiles for personalized job opportunities.
Generated: DETERMINISTIC_7692709f7f73c804
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
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Any
import spacy
import logging
from pathlib import Path

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load English language model for NLP processing
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    logger.error("Spacy language model 'en_core_web_sm' not found. Please install it first.")
    raise

class JobMatcher:
    """
    AI-powered job matching system that matches candidate profiles with job listings.
    """
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.job_data = []
        self.profile_data = []
        self.job_vectors = None
        self.profile_vectors = None
        
    def load_data(self, job_file: str, profile_file: str) -> None:
        """
        Load job and profile data from JSON files.
        
        Args:
            job_file: Path to JSON file containing job listings
            profile_file: Path to JSON file containing candidate profiles
        """
        try:
            with open(job_file, 'r') as f:
                self.job_data = json.load(f)
            with open(profile_file, 'r') as f:
                self.profile_data = json.load(f)
            logger.info(f"Loaded {len(self.job_data)} jobs and {len(self.profile_data)} profiles")
        except FileNotFoundError as e:
            logger.error(f"Data file not found: {e}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON format: {e}")
            raise
    
    def preprocess_text(self, text: str) -> str:
        """
        Preprocess text by lemmatizing and removing stop words.
        
        Args:
            text: Input text to process
            
        Returns:
            Processed text string
        """
        doc = nlp(text)
        processed = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
        return ' '.join(processed)
    
    def vectorize_data(self) -> None:
        """
        Convert job and profile text data into TF-IDF vectors.
        """
        job_texts = [self.preprocess_text(job['description'] + ' ' + ' '.join(job['skills'])) 
                    for job in self.job_data]
        profile_texts = [self.preprocess_text(profile['summary'] + ' ' + ' '.join(profile['skills']))
                        for profile in self.profile_data]
        
        # Fit vectorizer on combined text for consistent vocabulary
        combined_texts = job_texts + profile_texts
        self.vectorizer.fit(combined_texts)
        
        # Transform separately
        self.job_vectors = self.vectorizer.transform(job_texts)
        self.profile_vectors = self.vectorizer.transform(profile_texts)
    
    def calculate_similarity(self, profile_idx: int, top_n: int = 5) -> List[Dict[str, Any]]:
        """
        Calculate job matches for a given profile.
        
        Args:
            profile_idx: Index of the profile in the loaded data
            top_n: Number of top matches to return
            
        Returns:
            List of dictionaries containing job matches with similarity scores
        """
        if profile_idx >= len(self.profile_vectors):
            raise ValueError("Profile index out of range")
            
        profile_vector = self.profile_vectors[profile_idx]
        similarities = cosine_similarity(profile_vector, self.job_vectors).flatten()
        
        # Get top N matches
        top_indices = np.argsort(similarities)[-top_n:][::-1]
        
        results = []
        for idx in top_indices:
            job = self.job_data[idx]
            results.append({
                'job_id': job['id'],
                'title': job['title'],
                'company': job['company'],
                'similarity_score': float(similarities[idx]),
                'required_skills': job['skills'],
                'description': job['description'][:200] + '...'  # Truncate for display
            })
        
        return results
    
    def match_all_profiles(self, top_n: int = 5) -> Dict[str, List[Dict[str, Any]]]:
        """
        Match all profiles against all jobs.
        
        Args:
            top_n: Number of top matches to return per profile
            
        Returns:
            Dictionary with profile IDs as keys and their matches as values
        """
        if not self.job_vectors or not self.profile_vectors:
            raise ValueError("Data not vectorized. Call vectorize_data() first.")
            
        all_matches = {}
        for i, profile in enumerate(self.profile_data):
            try:
                matches = self.calculate_similarity(i, top_n)
                all_matches[profile['id']] = matches
            except Exception as e:
                logger.error(f"Error matching profile {profile['id']}: {e}")
                continue
                
        return all_matches

def main():
    try:
        # Initialize job matcher
        matcher = JobMatcher()
        
        # Load data (assuming files are in the same directory)
        current_dir = Path(__file__).parent
        matcher.load_data(
            current_dir / 'jobs.json',
            current_dir / 'profiles.json'
        )
        
        # Process and vectorize data
        matcher.vectorize_data()
        
        # Example: Get matches for first profile
        if matcher.profile_data:
            matches = matcher.calculate_similarity(0)
            print("Top job matches for first profile:")
            for match in matches:
                print(f"\nJob Title: {match['title']}")
                print(f"Company: {match['company']}")
                print(f"Match Score: {match['similarity_score']:.2f}")
                print(f"Required Skills: {', '.join(match['required_skills'])}")
                print(f"Description: {match['description']}")
        
        # Example: Get matches for all profiles
        all_matches = matcher.match_all_profiles()
        print(f"\nGenerated matches for {len(all_matches)} profiles")
        
    except Exception as e:
        logger.error(f"Error in job matching: {e}")
        raise

if __name__ == "__main__":
    main()
```
