"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: "Develop a code to automatically suggest related products to customers based on their purchase history on an online store."
Generated: DETERMINISTIC_33677dbccbc04214
Batch ID: 20250622_210856
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
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductRecommender:
    """
    A product recommendation system that suggests related products based on purchase history.
    """
    
    def __init__(self, products_data: pd.DataFrame):
        """
        Initialize the recommender with product data.
        
        Args:
            products_data: DataFrame containing product information with columns:
                         - product_id: unique identifier
                         - product_name: name of the product
                         - description: product description
                         - category: product category
        """
        self.products = products_data.copy()
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.product_vectors = None
        self.similarity_matrix = None
        
        self._prepare_data()
        
    def _prepare_data(self) -> None:
        """Preprocess data and build similarity matrix."""
        try:
            # Combine relevant text features for vectorization
            self.products['text_features'] = (
                self.products['product_name'] + " " + 
                self.products['description'] + " " + 
                self.products['category']
            )
            
            # Create TF-IDF vectors
            self.product_vectors = self.vectorizer.fit_transform(
                self.products['text_features']
            )
            
            # Compute cosine similarity matrix
            self.similarity_matrix = cosine_similarity(
                self.product_vectors, 
                self.product_vectors
            )
            
        except Exception as e:
            logger.error(f"Error preparing data: {str(e)}")
            raise
            
    def get_recommendations(
        self, 
        purchased_product_ids: List[str], 
        top_n: int = 5
    ) -> List[Dict]:
        """
        Get product recommendations based on purchase history.
        
        Args:
            purchased_product_ids: List of product IDs the customer has purchased
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended products with their details
        """
        try:
            if not purchased_product_ids:
                return []
                
            # Get indices of purchased products
            purchased_indices = [
                self.products[self.products['product_id'] == pid].index[0] 
                for pid in purchased_product_ids 
                if pid in self.products['product_id'].values
            ]
            
            if not purchased_indices:
                return []
                
            # Calculate average similarity scores
            avg_similarities = self.similarity_matrix[purchased_indices].mean(axis=0)
            
            # Get top N most similar products (excluding purchased ones)
            similar_indices = avg_similarities.argsort()[::-1]
            recommended_indices = [
                idx for idx in similar_indices 
                if idx not in purchased_indices
            ][:top_n]
            
            # Prepare recommendations
            recommendations = []
            for idx in recommended_indices:
                product = self.products.iloc[idx]
                recommendations.append({
                    'product_id': product['product_id'],
                    'product_name': product['product_name'],
                    'description': product['description'],
                    'category': product['category'],
                    'similarity_score': avg_similarities[idx]
                })
                
            return recommendations
            
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample product data
    sample_data = {
        'product_id': ['p1', 'p2', 'p3', 'p4', 'p5'],
        'product_name': [
            'Wireless Headphones', 
            'Bluetooth Speaker', 
            'Smart Watch', 
            'Fitness Tracker', 
            'USB-C Cable'
        ],
        'description': [
            'Noise cancelling wireless headphones with 30hr battery',
            'Portable bluetooth speaker with deep bass',
            'Smart watch with heart rate monitoring',
            'Fitness tracker with step counting and sleep analysis',
            'High speed charging USB-C cable 1m length'
        ],
        'category': [
            'Audio', 
            'Audio', 
            'Wearables', 
            'Wearables', 
            'Accessories'
        ]
    }
    
    df = pd.DataFrame(sample_data)
    recommender = ProductRecommender(df)
    
    # Get recommendations for a customer who bought p1 (Wireless Headphones)
    recommendations = recommender.get_recommendations(['p1'])
    print("Recommended products:")
    for rec in recommendations:
        print(f"- {rec['product_name']} (Score: {rec['similarity_score']:.2f})")
```
