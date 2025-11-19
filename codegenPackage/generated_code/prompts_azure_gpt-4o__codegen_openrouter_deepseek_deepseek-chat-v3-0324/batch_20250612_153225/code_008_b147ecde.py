"""
Generated Code Metadata:
========================
Original URL: https://highvaluestaffing.com
Prompt: Generate code to analyze candidate profiles and match them with job descriptions using machine learning, focusing on "providing opportunities for life" as described by High Value Staffing.
Generated: DETERMINISTIC_b147ecdedee84fc7
Batch ID: 20250612_153225
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
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import joblib
import logging
from typing import Dict, List, Tuple, Optional

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Download NLTK resources
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

class ProfileMatcher:
    """
    A machine learning-based system to match candidate profiles with job descriptions
    focusing on "providing opportunities for life" aspect.
    """
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.scaler = MinMaxScaler()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.life_opportunity_keywords = [
            'growth', 'development', 'learning', 'advancement',
            'mentorship', 'training', 'education', 'career',
            'opportunity', 'life', 'balance', 'fulfillment',
            'purpose', 'meaning', 'impact', 'contribution'
        ]
        
    def preprocess_text(self, text: str) -> str:
        """
        Clean and preprocess text data.
        """
        if not isinstance(text, str):
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Tokenize and lemmatize
        tokens = text.split()
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        
        # Remove stopwords
        tokens = [token for token in tokens if token not in self.stop_words]
        
        return ' '.join(tokens)
    
    def calculate_life_opportunity_score(self, text: str) -> float:
        """
        Calculate a score based on presence of life opportunity keywords.
        """
        if not text:
            return 0.0
            
        processed_text = self.preprocess_text(text)
        tokens = processed_text.split()
        
        if not tokens:
            return 0.0
            
        keyword_count = sum(1 for token in tokens if token in self.life_opportunity_keywords)
        return keyword_count / len(tokens)
    
    def extract_features(self, profiles: pd.DataFrame, job_descriptions: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """
        Extract and transform features from profiles and job descriptions.
        """
        try:
            # Preprocess text data
            profiles['processed_text'] = profiles['text'].apply(self.preprocess_text)
            job_descriptions['processed_text'] = job_descriptions['text'].apply(self.preprocess_text)
            
            # Calculate life opportunity scores
            profiles['life_opportunity_score'] = profiles['text'].apply(self.calculate_life_opportunity_score)
            job_descriptions['life_opportunity_score'] = job_descriptions['text'].apply(self.calculate_life_opportunity_score)
            
            # Vectorize text
            profile_vectors = self.vectorizer.fit_transform(profiles['processed_text'])
            job_vectors = self.vectorizer.transform(job_descriptions['processed_text'])
            
            # Scale life opportunity scores
            life_scores = np.array(profiles['life_opportunity_score']).reshape(-1, 1)
            profiles['scaled_life_score'] = self.scaler.fit_transform(life_scores)
            
            return profile_vectors, job_vectors
            
        except Exception as e:
            logger.error(f"Error during feature extraction: {str(e)}")
            raise
    
    def calculate_similarity(self, profile_vectors: np.ndarray, job_vectors: np.ndarray, 
                            profiles: pd.DataFrame, jobs: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate similarity scores between profiles and job descriptions.
        """
        try:
            # Text similarity
            similarity_matrix = cosine_similarity(profile_vectors, job_vectors)
            
            # Life opportunity score similarity
            life_score_similarity = np.outer(
                profiles['scaled_life_score'],
                jobs['life_opportunity_score']
            )
            
            # Combined score (weighted)
            combined_scores = 0.7 * similarity_matrix + 0.3 * life_score_similarity
            
            # Create results dataframe
            results = []
            for i, profile_id in enumerate(profiles['id']):
                for j, job_id in enumerate(jobs['id']):
                    results.append({
                        'profile_id': profile_id,
                        'job_id': job_id,
                        'text_similarity': similarity_matrix[i][j],
                        'life_opportunity_similarity': life_score_similarity[i][j],
                        'combined_score': combined_scores[i][j]
                    })
                    
            return pd.DataFrame(results)
            
        except Exception as e:
            logger.error(f"Error during similarity calculation: {str(e)}")
            raise
    
    def get_top_matches(self, similarity_df: pd.DataFrame, top_n: int = 5) -> Dict[str, List[Dict]]:
        """
        Get top N matches for each profile and job.
        """
        try:
            # Top matches for profiles
            profile_matches = (
                similarity_df
                .sort_values(['profile_id', 'combined_score'], ascending=[True, False])
                .groupby('profile_id')
                .head(top_n)
                .groupby('profile_id')
                .apply(lambda x: x.to_dict('records'))
                .to_dict()
            )
            
            # Top matches for jobs
            job_matches = (
                similarity_df
                .sort_values(['job_id', 'combined_score'], ascending=[True, False])
                .groupby('job_id')
                .head(top_n)
                .groupby('job_id')
                .apply(lambda x: x.to_dict('records'))
                .to_dict()
            )
            
            return {
                'profile_matches': profile_matches,
                'job_matches': job_matches
            }
            
        except Exception as e:
            logger.error(f"Error getting top matches: {str(e)}")
            raise
    
    def save_model(self, filepath: str) -> None:
        """
        Save the trained model components to disk.
        """
        try:
            joblib.dump({
                'vectorizer': self.vectorizer,
                'scaler': self.scaler
            }, filepath)
            logger.info(f"Model saved successfully to {filepath}")
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            raise
    
    def load_model(self, filepath: str) -> None:
        """
        Load model components from disk.
        """
        try:
            model_components = joblib.load(filepath)
            self.vectorizer = model_components['vectorizer']
            self.scaler = model_components['scaler']
            logger.info(f"Model loaded successfully from {filepath}")
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise

def load_data(profile_path: str, jobs_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load profile and job description data.
    """
    try:
        profiles = pd.read_csv(profile_path)
        jobs = pd.read_csv(jobs_path)
        
        # Validate required columns
        required_columns = {'id', 'text'}
        if not required_columns.issubset(profiles.columns):
            raise ValueError("Profiles data missing required columns")
        if not required_columns.issubset(jobs.columns):
            raise ValueError("Jobs data missing required columns")
            
        return profiles, jobs
        
    except Exception as e:
        logger.error(f"Error loading data: {str(e)}")
        raise

def main():
    """
    Main execution function.
    """
    try:
        # Initialize matcher
        matcher = ProfileMatcher()
        
        # Load data
        profiles, jobs = load_data('profiles.csv', 'jobs.csv')
        
        # Extract features
        profile_vectors, job_vectors = matcher.extract_features(profiles, jobs)
        
        # Calculate similarity
        similarity_df = matcher.calculate_similarity(profile_vectors, job_vectors, profiles, jobs)
        
        # Get top matches
        matches = matcher.get_top_matches(similarity_df)
        
        # Save results
        similarity_df.to_csv('similarity_results.csv', index=False)
        
        # Save model for future use
        matcher.save_model('profile_matcher_model.joblib')
        
        logger.info("Matching process completed successfully")
        
    except Exception
