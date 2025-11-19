"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: How can I implement a product recommendation system for a website like Bio Green Asia that features 100% natural food supplements and cleaning products?
Generated: DETERMINISTIC_1b0a021894aa5965
Batch ID: 20250612_163924
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
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductRecommender:
    """
    A content-based product recommendation system for Bio Green Asia.
    Recommends products based on product descriptions and categories.
    """
    
    def __init__(self, products_data: List[Dict]):
        """
        Initialize the recommender with product data.
        
        Args:
            products_data: List of dictionaries containing product information
                          with keys: 'id', 'name', 'description', 'category'
        """
        try:
            self.df = pd.DataFrame(products_data)
            self.vectorizer = TfidfVectorizer(stop_words='english')
            self.tfidf_matrix = None
            self._prepare_data()
        except Exception as e:
            logger.error(f"Error initializing recommender: {str(e)}")
            raise

    def _prepare_data(self):
        """Prepare the data for recommendation processing."""
        try:
            # Combine relevant text features for vectorization
            self.df['content'] = self.df['name'] + " " + self.df['description'] + " " + self.df['category']
            self.tfidf_matrix = self.vectorizer.fit_transform(self.df['content'])
        except Exception as e:
            logger.error(f"Error preparing data: {str(e)}")
            raise

    def recommend_products(self, product_id: str, num_recommendations: int = 5) -> List[Dict]:
        """
        Get product recommendations based on a given product ID.
        
        Args:
            product_id: ID of the product to get recommendations for
            num_recommendations: Number of recommendations to return
            
        Returns:
            List of recommended product dictionaries
        """
        try:
            # Find the index of the product
            idx = self.df.index[self.df['id'] == product_id].tolist()[0]
            
            # Compute cosine similarity between products
            cosine_sim = linear_kernel(self.tfidf_matrix[idx:idx+1], self.tfidf_matrix).flatten()
            
            # Get the indices of most similar products
            sim_indices = cosine_sim.argsort()[::-1][1:num_recommendations+1]
            
            # Return the recommended products
            recommendations = self.df.iloc[sim_indices].to_dict('records')
            return recommendations
        except IndexError:
            logger.warning(f"Product ID {product_id} not found")
            return []
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return []

    def recommend_products_for_user(self, viewed_products: List[str], num_recommendations: int = 5) -> List[Dict]:
        """
        Get product recommendations based on multiple viewed products.
        
        Args:
            viewed_products: List of product IDs the user has viewed
            num_recommendations: Number of recommendations to return
            
        Returns:
            List of recommended product dictionaries
        """
        try:
            all_recommendations = []
            
            for product_id in viewed_products:
                recs = self.recommend_products(product_id, num_recommendations)
                all_recommendations.extend(recs)
            
            # Remove duplicates and already viewed products
            unique_recs = [dict(t) for t in {tuple(d.items()) for d in all_recommendations}]
            unique_recs = [rec for rec in unique_recs if rec['id'] not in viewed_products]
            
            # Sort by relevance (could be enhanced with more sophisticated ranking)
            return unique_recs[:num_recommendations]
        except Exception as e:
            logger.error(f"Error generating user recommendations: {str(e)}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample product data (in production, this would come from a database)
    sample_products = [
        {
            "id": "1",
            "name": "Organic Spirulina Powder",
            "description": "100% pure organic spirulina powder rich in protein and antioxidants",
            "category": "Superfoods"
        },
        {
            "id": "2",
            "name": "Natural Dish Soap",
            "description": "Eco-friendly dish soap made from plant-based ingredients",
            "category": "Cleaning Products"
        },
        {
            "id": "3",
            "name": "Organic Turmeric Capsules",
            "description": "High-potency turmeric capsules with black pepper for absorption",
            "category": "Supplements"
        },
        {
            "id": "4",
            "name": "Bamboo Toothbrush",
            "description": "Sustainable bamboo toothbrush with charcoal-infused bristles",
            "category": "Personal Care"
        },
        {
            "id": "5",
            "name": "Organic Chlorella Tablets",
            "description": "Detoxifying chlorella tablets packed with nutrients",
            "category": "Superfoods"
        },
        {
            "id": "6",
            "name": "All-Purpose Cleaner",
            "description": "Non-toxic cleaner safe for all surfaces",
            "category": "Cleaning Products"
        }
    ]

    try:
        # Initialize recommender
        recommender = ProductRecommender(sample_products)
        
        # Get recommendations for a product
        print("Recommendations for Organic Spirulina Powder:")
        recs = recommender.recommend_products("1")
        for rec in recs:
            print(f"- {rec['name']} ({rec['category']})")
        
        # Get recommendations based on user's viewed products
        print("\nPersonalized recommendations:")
        user_viewed = ["1", "3"]
        user_recs = recommender.recommend_products_for_user(user_viewed)
        for rec in user_recs:
            print(f"- {rec['name']} ({rec['category']})")
            
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")
```
