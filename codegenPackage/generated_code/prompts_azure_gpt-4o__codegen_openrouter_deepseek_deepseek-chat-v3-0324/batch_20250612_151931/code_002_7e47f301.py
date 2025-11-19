"""
Generated Code Metadata:
========================
Original URL: https://noymi.in
Prompt: Generate code to create a product recommendation system for e-commerce platforms selling items like Noymi True Wireless Bluetooth Earbuds | ET-219.
Generated: DETERMINISTIC_7e47f3015a9e6f2b
Batch ID: 20250612_151931
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
from sklearn.metrics.pairwise import linear_kernel
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductRecommender:
    """
    A product recommendation system using content-based filtering.
    """
    
    def __init__(self, products_data: List[Dict]):
        """
        Initialize the recommender with product data.
        
        Args:
            products_data: List of dictionaries containing product information.
                          Each dictionary should have at least 'id', 'name', 
                          'description', and 'category' fields.
        """
        try:
            self.df = pd.DataFrame(products_data)
            self._validate_data()
            self._preprocess_data()
            self._build_recommendation_model()
        except Exception as e:
            logger.error(f"Error initializing ProductRecommender: {str(e)}")
            raise

    def _validate_data(self):
        """Validate the input data structure."""
        required_fields = {'id', 'name', 'description', 'category'}
        if not required_fields.issubset(self.df.columns):
            raise ValueError(f"Input data must contain these fields: {required_fields}")
            
        if self.df['id'].duplicated().any():
            raise ValueError("Duplicate product IDs found in input data")

    def _preprocess_data(self):
        """Preprocess the product data for recommendation."""
        # Combine relevant text features
        self.df['combined_features'] = (
            self.df['name'] + " " + 
            self.df['description'] + " " + 
            self.df['category']
        )
        
        # Fill any missing values
        self.df['combined_features'] = self.df['combined_features'].fillna('')

    def _build_recommendation_model(self):
        """Build the TF-IDF model and compute similarity matrix."""
        self.tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = self.tfidf.fit_transform(self.df['combined_features'])
        self.cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        
    def get_recommendations(
        self, 
        product_id: str, 
        num_recommendations: int = 5
    ) -> Optional[List[Dict]]:
        """
        Get product recommendations based on a given product ID.
        
        Args:
            product_id: ID of the product to get recommendations for
            num_recommendations: Number of recommendations to return
            
        Returns:
            List of recommended product dictionaries or None if error occurs
        """
        try:
            if product_id not in self.df['id'].values:
                logger.warning(f"Product ID {product_id} not found in dataset")
                return None
                
            idx = self.df.index[self.df['id'] == product_id].tolist()[0]
            sim_scores = list(enumerate(self.cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            
            # Get the indices of the top similar products (skip the first one as it's the same product)
            product_indices = [i[0] for i in sim_scores[1:num_recommendations+1]]
            
            # Return the top recommended products
            recommendations = self.df.iloc[product_indices].to_dict('records')
            return recommendations
            
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    # Sample product data (in a real scenario, this would come from a database)
    sample_products = [
        {
            "id": "ET-219",
            "name": "Noymi True Wireless Bluetooth Earbuds",
            "description": "High-quality wireless earbuds with 24hr battery life and noise cancellation",
            "category": "Electronics/Audio",
            "price": 59.99
        },
        {
            "id": "HP-456",
            "name": "Wireless Headphones Pro",
            "description": "Premium over-ear headphones with active noise cancellation",
            "category": "Electronics/Audio",
            "price": 199.99
        },
        {
            "id": "SP-789",
            "name": "Bluetooth Speaker",
            "description": "Portable waterproof speaker with 20hr battery life",
            "category": "Electronics/Audio",
            "price": 89.99
        },
        {
            "id": "CB-123",
            "name": "Smartphone Case",
            "description": "Durable protective case for all major smartphone models",
            "category": "Accessories",
            "price": 19.99
        },
        {
            "id": "EB-321",
            "name": "Wireless Earbuds Lite",
            "description": "Affordable wireless earbuds with decent sound quality",
            "category": "Electronics/Audio",
            "price": 29.99
        }
    ]

    try:
        recommender = ProductRecommender(sample_products)
        recommendations = recommender.get_recommendations("ET-219")
        
        if recommendations:
            print("Recommended products:")
            for product in recommendations:
                print(f"- {product['name']} (${product['price']})")
        else:
            print("No recommendations could be generated.")
            
    except Exception as e:
        print(f"Failed to initialize recommender: {str(e)}")
```
