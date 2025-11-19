"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Create an algorithm to recommend the best home service providers in Dammam for tasks like kitchen installation and furniture moving, inspired by شركة الاحترافية's regional focus.
Generated: DETERMINISTIC_64d5b85dc6590722
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import json
from typing import List, Dict, Optional

class ServiceProviderRecommender:
    """
    A recommendation system for home service providers in Dammam.
    Inspired by شركة الاحترافية's regional focus.
    """
    
    def __init__(self, providers_data_path: str = 'providers_data.json'):
        """
        Initialize the recommender with provider data.
        
        Args:
            providers_data_path: Path to JSON file containing provider data
        """
        try:
            with open(providers_data_path, 'r', encoding='utf-8') as f:
                self.providers_data = json.load(f)
            
            # Preprocess data
            self._preprocess_data()
            
            # Initialize TF-IDF Vectorizer
            self.vectorizer = TfidfVectorizer(stop_words=['the', 'and', 'in'])
            self._train_vectorizer()
            
        except FileNotFoundError:
            raise ValueError(f"Provider data file not found at {providers_data_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in provider data file")
        except Exception as e:
            raise ValueError(f"Error initializing recommender: {str(e)}")
    
    def _preprocess_data(self) -> None:
        """Preprocess provider data for analysis."""
        for provider in self.providers_data:
            # Combine relevant features into a single text for vectorization
            provider['features_text'] = ' '.join([
                provider['name'],
                provider['service_type'],
                ' '.join(provider['specialties']),
                provider['location'],
                str(provider['rating']),
                ' '.join(provider['reviews'])
            ])
    
    def _train_vectorizer(self) -> None:
        """Train the TF-IDF vectorizer on provider data."""
        texts = [p['features_text'] for p in self.providers_data]
        self.tfidf_matrix = self.vectorizer.fit_transform(texts)
    
    def recommend_providers(
        self,
        service_type: str,
        specialties: List[str],
        location: str = "Dammam",
        top_n: int = 5
    ) -> List[Dict]:
        """
        Recommend service providers based on input criteria.
        
        Args:
            service_type: Type of service needed (e.g., 'kitchen installation')
            specialties: List of desired specialties
            location: Preferred location (default: Dammam)
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended providers with their details
        """
        try:
            # Create query text
            query_text = ' '.join([service_type] + specialties + [location])
            
            # Vectorize query
            query_vec = self.vectorizer.transform([query_text])
            
            # Calculate cosine similarities
            cosine_similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
            
            # Get top N indices
            top_indices = np.argsort(cosine_similarities)[-top_n:][::-1]
            
            # Prepare results with additional filtering
            results = []
            for idx in top_indices:
                provider = self.providers_data[idx]
                # Skip if not in Dammam (regional focus)
                if 'Dammam' not in provider['location']:
                    continue
                # Skip if service type doesn't match
                if service_type.lower() not in provider['service_type'].lower():
                    continue
                
                results.append({
                    'name': provider['name'],
                    'service_type': provider['service_type'],
                    'specialties': provider['specialties'],
                    'rating': provider['rating'],
                    'reviews_count': len(provider['reviews']),
                    'location': provider['location'],
                    'contact': provider['contact'],
                    'similarity_score': float(cosine_similarities[idx])
                })
            
            # Sort by rating if similarity scores are close
            if len(results) > 1 and (results[0]['similarity_score'] - results[-1]['similarity_score']) < 0.1:
                results.sort(key=lambda x: x['rating'], reverse=True)
            
            return results[:top_n]
        
        except Exception as e:
            raise ValueError(f"Error generating recommendations: {str(e)}")

# Example usage (would be in a separate file in production)
if __name__ == "__main__":
    try:
        recommender = ServiceProviderRecommender()
        
        # Get recommendations for kitchen installation
        recommendations = recommender.recommend_providers(
            service_type="kitchen installation",
            specialties=["modern design", "custom cabinets"],
            location="Dammam"
        )
        
        print("Top recommendations for kitchen installation in Dammam:")
        for i, provider in enumerate(recommendations, 1):
            print(f"{i}. {provider['name']} (Rating: {provider['rating']}, Specialties: {', '.join(provider['specialties'])})")
    
    except Exception as e:
        print(f"Error: {str(e)}")
```
