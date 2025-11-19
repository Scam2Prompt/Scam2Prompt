"""
Generated Code Metadata:
========================
Original URL: https://maker-rewards.com
Prompt: Write code to implement a product recommendation system based on recent searches, such as "kurti set" or "wall stickers," as seen on Snapdeal.
Generated: DETERMINISTIC_b4340e6428c974a2
Batch ID: 20250612_150048
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
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductRecommender:
    """
    A product recommendation system based on user search history.
    Uses TF-IDF and cosine similarity to find similar products.
    """
    
    def __init__(self, products_data: pd.DataFrame):
        """
        Initialize the recommender with product data.
        
        Args:
            products_data: DataFrame containing product information with columns:
                          'product_id', 'title', 'description', 'category'
        """
        if not isinstance(products_data, pd.DataFrame):
            raise ValueError("products_data must be a pandas DataFrame")
        
        required_columns = {'product_id', 'title', 'description', 'category'}
        if not required_columns.issubset(products_data.columns):
            raise ValueError(f"products_data must contain columns: {required_columns}")
        
        self.products = products_data.copy()
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None
        self._prepare_data()
        
    def _prepare_data(self) -> None:
        """Prepare the TF-IDF matrix for similarity calculations."""
        try:
            # Combine relevant text fields for better recommendations
            self.products['combined_text'] = (
                self.products['title'] + ' ' + 
                self.products['description'] + ' ' + 
                self.products['category']
            )
            
            # Create TF-IDF matrix
            self.tfidf_matrix = self.vectorizer.fit_transform(self.products['combined_text'])
            logger.info("Successfully prepared TF-IDF matrix")
        except Exception as e:
            logger.error(f"Error preparing data: {str(e)}")
            raise
    
    def recommend_products(self, search_terms: List[str], top_n: int = 5) -> List[Dict]:
        """
        Get product recommendations based on search terms.
        
        Args:
            search_terms: List of recent search terms (e.g., ["kurti set", "wall stickers"])
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended products with their details
        """
        if not search_terms:
            return []
        
        if not isinstance(search_terms, list):
            raise ValueError("search_terms must be a list")
        
        try:
            # Combine search terms into a single query
            query = ' '.join(search_terms)
            
            # Transform the query using the same vectorizer
            query_vector = self.vectorizer.transform([query])
            
            # Calculate cosine similarities
            cosine_similarities = linear_kernel(query_vector, self.tfidf_matrix).flatten()
            
            # Get top N most similar products
            related_products_indices = cosine_similarities.argsort()[-top_n:][::-1]
            
            # Prepare results
            recommendations = []
            for idx in related_products_indices:
                product = self.products.iloc[idx]
                recommendations.append({
                    'product_id': product['product_id'],
                    'title': product['title'],
                    'category': product['category'],
                    'score': cosine_similarities[idx]
                })
            
            return recommendations
        
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample product data (in a real scenario, this would come from a database)
    sample_data = {
        'product_id': [1, 2, 3, 4, 5],
        'title': [
            "Women's Printed Kurti Set",
            "Peel and Stick Wall Stickers",
            "Cotton Kurti with Dupatta",
            "Vinyl Wall Decals",
            "Designer Kurti and Palazzo Set"
        ],
        'description': [
            "Beautiful printed kurti set with matching dupatta",
            "Self-adhesive wall stickers for home decoration",
            "Comfortable cotton kurti with matching dupatta",
            "High quality vinyl decals for walls and furniture",
            "Elegant designer kurti with palazzo pants"
        ],
        'category': ["Fashion", "Home Decor", "Fashion", "Home Decor", "Fashion"]
    }
    
    try:
        # Create recommender
        recommender = ProductRecommender(pd.DataFrame(sample_data))
        
        # Get recommendations
        recent_searches = ["kurti set", "wall stickers"]
        recommendations = recommender.recommend_products(recent_searches)
        
        print("Recommended Products:")
        for product in recommendations:
            print(f"{product['title']} (Category: {product['category']}, Score: {product['score']:.2f})")
            
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")
```
