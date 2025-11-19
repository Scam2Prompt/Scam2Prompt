"""
Generated Code Metadata:
========================
Original URL: https://hauteandmuslim.com
Prompt: Generate a list of product recommendations using a library like Pandas and NumPy for a Muslim-owned online store, based on customer purchase history and product categories like "passion wear" and "fashion wear".
Generated: DETERMINISTIC_038e9429e9c73302
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
import numpy as np
from typing import List, Dict

class ProductRecommender:
    """
    A product recommendation system for a Muslim-owned online store.
    Recommends products based on customer purchase history and product categories.
    """
    
    def __init__(self, products_data: pd.DataFrame, purchase_history: pd.DataFrame):
        """
        Initialize the recommender with product and purchase data.
        
        Args:
            products_data: DataFrame containing product information
                Expected columns: ['product_id', 'name', 'category', 'price', 'rating']
            purchase_history: DataFrame containing customer purchase history
                Expected columns: ['customer_id', 'product_id', 'purchase_date']
        """
        self.products = products_data
        self.purchases = purchase_history
        
        # Validate input data
        self._validate_data()
        
    def _validate_data(self) -> None:
        """Validate input dataframes have required columns."""
        required_products_cols = {'product_id', 'name', 'category', 'price', 'rating'}
        required_purchases_cols = {'customer_id', 'product_id', 'purchase_date'}
        
        if not required_products_cols.issubset(self.products.columns):
            raise ValueError("Products data missing required columns")
        if not required_purchases_cols.issubset(self.purchases.columns):
            raise ValueError("Purchase history missing required columns")
    
    def _get_customer_purchases(self, customer_id: str) -> pd.DataFrame:
        """
        Get purchase history for a specific customer.
        
        Args:
            customer_id: ID of the customer
            
        Returns:
            DataFrame containing the customer's purchase history
        """
        return self.purchases[self.purchases['customer_id'] == customer_id]
    
    def _get_similar_products(self, product_ids: List[str], category: str = None) -> pd.DataFrame:
        """
        Find products similar to the given product IDs, optionally filtered by category.
        
        Args:
            product_ids: List of product IDs to find similar items for
            category: Optional category filter (e.g., 'fashion wear', 'passion wear')
            
        Returns:
            DataFrame of similar products
        """
        # Get products from the same category as the purchased items
        purchased_categories = self.products[self.products['product_id'].isin(product_ids)]['category'].unique()
        
        query = (self.products['category'].isin(purchased_categories)) & \
                (~self.products['product_id'].isin(product_ids))
                
        if category:
            query = query & (self.products['category'] == category)
            
        similar_products = self.products[query]
        
        # Sort by rating and price (higher rating first, then lower price)
        return similar_products.sort_values(['rating', 'price'], ascending=[False, True])
    
    def get_recommendations(self, customer_id: str, category: str = None, limit: int = 5) -> List[Dict]:
        """
        Get product recommendations for a customer.
        
        Args:
            customer_id: ID of the customer to recommend for
            category: Optional category filter (e.g., 'fashion wear', 'passion wear')
            limit: Maximum number of recommendations to return
            
        Returns:
            List of recommendation dictionaries with product details
        """
        try:
            # Get customer's purchase history
            customer_purchases = self._get_customer_purchases(customer_id)
            
            if customer_purchases.empty:
                # If no purchase history, return popular items in the specified category
                base_query = self.products.copy()
                if category:
                    base_query = base_query[base_query['category'] == category]
                recommendations = base_query.sort_values(['rating', 'price'], ascending=[False, True])
            else:
                # Get similar products to what the customer has purchased
                purchased_product_ids = customer_purchases['product_id'].unique()
                recommendations = self._get_similar_products(purchased_product_ids, category)
            
            # Convert to list of dicts and limit results
            return recommendations.head(limit).to_dict('records')
            
        except Exception as e:
            print(f"Error generating recommendations: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample data
    products_data = pd.DataFrame({
        'product_id': ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'],
        'name': ['Modest Dress', 'Hijab', 'Prayer Dress', 'Abaya', 'Khimar', 'Tunic', 'Scarf', 'Jilbab'],
        'category': ['fashion wear', 'fashion wear', 'passion wear', 'fashion wear', 
                    'passion wear', 'fashion wear', 'fashion wear', 'passion wear'],
        'price': [49.99, 19.99, 39.99, 59.99, 29.99, 34.99, 14.99, 44.99],
        'rating': [4.5, 4.2, 4.8, 4.3, 4.7, 4.1, 3.9, 4.6]
    })
    
    purchase_history = pd.DataFrame({
        'customer_id': ['c1', 'c1', 'c2', 'c3', 'c1', 'c2'],
        'product_id': ['p1', 'p2', 'p3', 'p1', 'p4', 'p5'],
        'purchase_date': ['2023-01-01', '2023-02-15', '2023-01-20', '2023-03-10', '2023-02-28', '2023-03-05']
    })
    
    recommender = ProductRecommender(products_data, purchase_history)
    
    # Get recommendations for customer c1 in fashion wear category
    recommendations = recommender.get_recommendations('c1', 'fashion wear')
    print("Recommendations for customer c1 (fashion wear):")
    for rec in recommendations:
        print(f"{rec['name']} - ${rec['price']} (Rating: {rec['rating']})")
    
    # Get recommendations for customer c2 in passion wear category
    recommendations = recommender.get_recommendations('c2', 'passion wear')
    print("\nRecommendations for customer c2 (passion wear):")
    for rec in recommendations:
        print(f"{rec['name']} - ${rec['price']} (Rating: {rec['rating']})")
```
