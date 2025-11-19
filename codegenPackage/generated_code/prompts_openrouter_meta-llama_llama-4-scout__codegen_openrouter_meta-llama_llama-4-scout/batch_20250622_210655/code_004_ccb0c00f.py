"""
Generated Code Metadata:
========================
Original URL: https://bolle.com.co
Prompt: Create a product recommendation engine that suggests Bollé products, such as LIGHTSHIFTER XL sunglasses, based on customer preferences and purchase history.
Generated: DETERMINISTIC_ccb0c00fef14aa61
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_recommendation_engine.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ProductRecommendationEngine:
    def __init__(self, products_df, customer_purchases_df, customer_preferences_df):
        """
        Initialize the product recommendation engine.

        Args:
        - products_df (pd.DataFrame): DataFrame containing product information.
        - customer_purchases_df (pd.DataFrame): DataFrame containing customer purchase history.
        - customer_preferences_df (pd.DataFrame): DataFrame containing customer preferences.
        """
        self.products_df = products_df
        self.customer_purchases_df = customer_purchases_df
        self.customer_preferences_df = customer_preferences_df

    def _build_product_features(self):
        """
        Build TF-IDF features for products based on their descriptions.
        """
        vectorizer = TfidfVectorizer(stop_words='english')
        product_features = vectorizer.fit_transform(self.products_df['description'])
        return product_features

    def _build_customer_features(self):
        """
        Build TF-IDF features for customers based on their preferences and purchase history.
        """
        customer_text = self.customer_preferences_df['preferences'].astype(str) + ' ' + self.customer_purchases_df['purchase_history'].astype(str)
        vectorizer = TfidfVectorizer(stop_words='english')
        customer_features = vectorizer.fit_transform(customer_text)
        return customer_features

    def _calculate_similarities(self, product_features, customer_features):
        """
        Calculate cosine similarities between products and customers.

        Args:
        - product_features (scipy.sparse.csr_matrix): TF-IDF features for products.
        - customer_features (scipy.sparse.csr_matrix): TF-IDF features for customers.

        Returns:
        - similarities (np.ndarray): Cosine similarities between products and customers.
        """
        try:
            similarities = cosine_similarity(product_features, customer_features)
            return similarities
        except Exception as e:
            print(f"Error calculating similarities: {str(e)}")
            return None

    def recommend_products(self, customer_id, num_recommendations=5):
        """
        Recommend products to a customer based on their preferences and purchase history.

        Args:
        - customer_id (int): ID of the customer.
        - num_recommendations (int, optional): Number of recommendations to return. Defaults to 5.

        Returns:
        - recommended_products (list): List of recommended product names.
        """
        try:
            customer_features = self._build_customer_features()
            product_features = self._build_product_features()

            similarities = self._calculate_similarities(product_features, customer_features)

            if similarities is not None:
                customer_similarities = similarities[self.customer_purchases_df['customer_id'] == customer_id]
                recommended_product_indices = customer_similarities.argsort()[:, ::-1][:num_recommendations]
                recommended_products = self.products_df.iloc[recommended_product_indices[0]]['product_name'].tolist()
                return recommended_products
            else:
                return []
        except Exception as e:
            print(f"Error recommending products: {str(e)}")
            return []

def main():
    # Sample data
    products_df = pd.DataFrame({
        'product_id': [1, 2, 3],
        'product_name': ['LIGHTSHIFTER XL', 'SPORTS SHADES', 'TRAILBLAZER'],
        'description': ['Bollé LIGHTSHIFTER XL sunglasses', 'Bollé SPORTS SHADES for athletes', 'Bollé TRAILBLAZER for trail running']
    })

    customer_purchases_df = pd.DataFrame({
        'customer_id': [101, 101, 102],
        'purchase_history': ['LIGHTSHIFTER XL', 'SPORTS SHADES', 'TRAILBLAZER']
    })

    customer_preferences_df = pd.DataFrame({
        'customer_id': [101, 102],
        'preferences': ['sunglasses for cycling', 'shades for running']
    })

    engine = ProductRecommendationEngine(products_df, customer_purchases_df, customer_preferences_df)
    recommended_products = engine.recommend_products(101)

    print("Recommended products:")
    for product in recommended_products:
        print(product)

if __name__ == "__main__":
    main()
```
