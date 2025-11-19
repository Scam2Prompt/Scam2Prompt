"""
Generated Code Metadata:
========================
Original URL: https://gvika.in
Prompt: "Write a Python code snippet to create a personalized product recommendation system for a customized gift shop like Gvika."
Generated: DETERMINISTIC_187c963e911fc9b4
Batch ID: 20250622_210703
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
from typing import List, Dict, Optional
import json
import os

class ProductRecommendationSystem:
    """
    A personalized product recommendation system for a customized gift shop.
    """
    
    def __init__(self, products_file: str = 'products.json'):
        """
        Initialize the recommendation system with product data.
        
        Args:
            products_file: Path to JSON file containing product data
        """
        self.products_file = products_file
        self.products = self._load_products()
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.product_features = self._prepare_features()
        
    def _load_products(self) -> List[Dict]:
        """
        Load product data from JSON file.
        
        Returns:
            List of product dictionaries
            
        Raises:
            FileNotFoundError: If products file doesn't exist
            ValueError: If products file is invalid JSON
        """
        try:
            with open(self.products_file, 'r') as f:
                products = json.load(f)
            if not isinstance(products, list):
                raise ValueError("Products data should be a list of dictionaries")
            return products
        except FileNotFoundError:
            raise FileNotFoundError(f"Products file {self.products_file} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in products file")
    
    def _prepare_features(self):
        """
        Prepare TF-IDF features from product descriptions.
        
        Returns:
            TF-IDF matrix for all products
        """
        descriptions = [p.get('description', '') + ' ' + ' '.join(p.get('tags', [])) for p in self.products]
        return self.vectorizer.fit_transform(descriptions)
    
    def get_recommendations(self, user_preferences: str, top_n: int = 5) -> List[Dict]:
        """
        Get personalized product recommendations based on user preferences.
        
        Args:
            user_preferences: Text describing user preferences
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended product dictionaries
        """
        if not user_preferences or not isinstance(user_preferences, str):
            return []
            
        user_vector = self.vectorizer.transform([user_preferences])
        similarity_scores = cosine_similarity(user_vector, self.product_features).flatten()
        
        # Get indices of top N most similar products
        product_indices = similarity_scores.argsort()[-top_n:][::-1]
        
        recommendations = []
        for idx in product_indices:
            product = self.products[idx].copy()
            product['similarity_score'] = float(similarity_scores[idx])
            recommendations.append(product)
            
        return recommendations
    
    def add_product(self, product: Dict) -> None:
        """
        Add a new product to the recommendation system.
        
        Args:
            product: Dictionary containing product details
            
        Raises:
            ValueError: If product is missing required fields
        """
        required_fields = {'id', 'name', 'description'}
        if not required_fields.issubset(product.keys()):
            raise ValueError(f"Product must contain fields: {required_fields}")
            
        self.products.append(product)
        self._save_products()
        self.product_features = self._prepare_features()
    
    def _save_products(self) -> None:
        """
        Save current products to the products file.
        """
        with open(self.products_file, 'w') as f:
            json.dump(self.products, f, indent=2)
    
    def get_product_by_id(self, product_id: str) -> Optional[Dict]:
        """
        Get a product by its ID.
        
        Args:
            product_id: The product ID to search for
            
        Returns:
            The product dictionary if found, None otherwise
        """
        for product in self.products:
            if product.get('id') == product_id:
                return product
        return None

# Example usage
if __name__ == "__main__":
    # Initialize with sample products if file doesn't exist
    if not os.path.exists('products.json'):
        sample_products = [
            {
                "id": "1",
                "name": "Personalized Engraved Necklace",
                "description": "Beautiful silver necklace with custom engraving",
                "price": 49.99,
                "tags": ["jewelry", "personalized", "romantic"]
            },
            {
                "id": "2",
                "name": "Custom Photo Blanket",
                "description": "Soft fleece blanket with your favorite photo printed on it",
                "price": 59.99,
                "tags": ["home", "personalized", "photo"]
            },
            {
                "id": "3",
                "name": "Engraved Wooden Watch",
                "description": "Elegant wooden watch with custom engraving on the back",
                "price": 79.99,
                "tags": ["accessories", "personalized", "wooden"]
            }
        ]
        with open('products.json', 'w') as f:
            json.dump(sample_products, f, indent=2)
    
    # Create recommendation system
    recommender = ProductRecommendationSystem()
    
    # Get recommendations
    preferences = "I'm looking for a romantic gift for my wife"
    recommendations = recommender.get_recommendations(preferences)
    
    print("Recommended Products:")
    for product in recommendations:
        print(f"- {product['name']} (Score: {product['similarity_score']:.2f})")
```
