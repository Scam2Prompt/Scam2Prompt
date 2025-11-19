"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Develop a recommendation algorithm for an e-commerce site that suggests sports equipment based on user preferences for categories like "Beach Soccer," "Tênis de Mesa," and "Artes Marciais."
Generated: DETERMINISTIC_84012b4728c7c447
Batch ID: 20250612_151414
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
from sklearn.metrics.pairwise import linear_kernel

class SportsEquipmentRecommender:
    """
    A recommendation system for sports equipment based on user preferences.
    Uses TF-IDF and cosine similarity to find similar items.
    """
    
    def __init__(self, data_path):
        """
        Initialize the recommender with sports equipment data.
        
        Args:
            data_path (str): Path to CSV file containing sports equipment data.
                            Expected columns: 'id', 'name', 'category', 'description'
        """
        try:
            self.data = pd.read_csv(data_path)
            self.data['category'] = self.data['category'].str.lower()
            self._preprocess_data()
            self._train_model()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {data_path}")
        except Exception as e:
            raise Exception(f"Error initializing recommender: {str(e)}")
    
    def _preprocess_data(self):
        """Preprocess the data by combining relevant text features."""
        self.data['combined_features'] = (
            self.data['name'] + " " + 
            self.data['category'] + " " + 
            self.data['description']
        )
    
    def _train_model(self):
        """Train the TF-IDF model and compute cosine similarities."""
        self.tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = self.tfidf.fit_transform(self.data['combined_features'])
        self.cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    def recommend_items(self, user_preferences, top_n=5):
        """
        Get recommendations based on user preferences.
        
        Args:
            user_preferences (list): List of preferred categories (e.g., ['Beach Soccer', 'Tênis de Mesa'])
            top_n (int): Number of recommendations to return
            
        Returns:
            list: Recommended items as dictionaries with 'id', 'name', 'category'
        """
        try:
            # Create a pseudo-item from user preferences
            pseudo_item = " ".join([pref.lower() for pref in user_preferences])
            
            # Transform preferences using trained TF-IDF
            pref_vector = self.tfidf.transform([pseudo_item])
            
            # Calculate similarity with all items
            sim_scores = linear_kernel(pref_vector, self.tfidf.transform(self.data['combined_features']))
            sim_scores = sim_scores[0]
            
            # Get top N most similar items
            sim_indices = sim_scores.argsort()[::-1][:top_n]
            
            # Return recommendations
            recommendations = []
            for idx in sim_indices:
                item = self.data.iloc[idx]
                recommendations.append({
                    'id': item['id'],
                    'name': item['name'],
                    'category': item['category']
                })
            
            return recommendations
        
        except Exception as e:
            raise Exception(f"Error generating recommendations: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with sample data (in production, use actual data path)
        recommender = SportsEquipmentRecommender("sports_equipment.csv")
        
        # Get recommendations
        preferences = ["Beach Soccer", "Tênis de Mesa", "Artes Marciais"]
        recommendations = recommender.recommend_items(preferences)
        
        print("Recommended Items:")
        for item in recommendations:
            print(f"{item['name']} ({item['category']})")
    
    except Exception as e:
        print(f"Error: {str(e)}")
```
