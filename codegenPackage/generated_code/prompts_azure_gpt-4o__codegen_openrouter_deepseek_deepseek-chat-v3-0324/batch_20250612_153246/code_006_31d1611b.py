"""
Generated Code Metadata:
========================
Original URL: https://thegladiatorshoes.com
Prompt: Generate code to implement a recommendation system for safety footwear based on user input, such as "durable leather boots for construction work" or "lightweight composite shoes for airport management."
Generated: DETERMINISTIC_31d1611bfcad13c6
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SafetyFootwearRecommender:
    """
    A recommendation system for safety footwear based on user input.
    Uses TF-IDF vectorization and cosine similarity to find matching products.
    """
    
    def __init__(self, data_path='safety_footwear.csv'):
        """
        Initialize the recommender system with product data.
        
        Args:
            data_path (str): Path to the CSV file containing product data.
                            Expected columns: 'id', 'name', 'description', 'category', 'features'
        """
        try:
            self.df = pd.read_csv(data_path)
            self._validate_data()
            self._preprocess_data()
            self._initialize_vectorizer()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {data_path}")
        except Exception as e:
            raise Exception(f"Error initializing recommender: {str(e)}")
    
    def _validate_data(self):
        """Validate that required columns exist in the data."""
        required_columns = {'id', 'name', 'description', 'category', 'features'}
        if not required_columns.issubset(self.df.columns):
            missing = required_columns - set(self.df.columns)
            raise ValueError(f"Missing required columns: {missing}")
    
    def _preprocess_data(self):
        """Preprocess the data by combining relevant text fields."""
        self.df['combined_text'] = (
            self.df['name'] + ' ' + 
            self.df['description'] + ' ' + 
            self.df['category'] + ' ' + 
            self.df['features']
        )
        self.df['combined_text'] = self.df['combined_text'].str.lower()
    
    def _initialize_vectorizer(self):
        """Initialize the TF-IDF vectorizer."""
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['combined_text'])
    
    def recommend(self, query, top_n=5):
        """
        Get recommendations based on user query.
        
        Args:
            query (str): User input describing desired footwear
            top_n (int): Number of recommendations to return
            
        Returns:
            list: List of recommended products (as dictionaries)
        """
        try:
            if not query or not isinstance(query, str):
                raise ValueError("Query must be a non-empty string")
            
            # Vectorize the query
            query_vec = self.vectorizer.transform([query.lower()])
            
            # Calculate cosine similarities
            cosine_similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
            
            # Get top N matches
            top_indices = cosine_similarities.argsort()[-top_n:][::-1]
            recommendations = []
            
            for idx in top_indices:
                product = self.df.iloc[idx]
                recommendations.append({
                    'id': product['id'],
                    'name': product['name'],
                    'description': product['description'],
                    'category': product['category'],
                    'features': product['features'],
                    'similarity_score': cosine_similarities[idx]
                })
            
            return recommendations
        
        except Exception as e:
            raise Exception(f"Error generating recommendations: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize recommender (in production, this would be done once and reused)
        recommender = SafetyFootwearRecommender()
        
        # Example queries
        queries = [
            "durable leather boots for construction work",
            "lightweight composite shoes for airport management",
            "waterproof steel toe boots",
            "electrical hazard resistant shoes"
        ]
        
        # Get and display recommendations
        for query in queries:
            print(f"\nRecommendations for: '{query}'")
            recommendations = recommender.recommend(query)
            for i, rec in enumerate(recommendations, 1):
                print(f"{i}. {rec['name']} (Score: {rec['similarity_score']:.2f})")
                print(f"   Features: {rec['features']}")
                print(f"   Category: {rec['category']}\n")
                
    except Exception as e:
        print(f"Error: {str(e)}")
```
