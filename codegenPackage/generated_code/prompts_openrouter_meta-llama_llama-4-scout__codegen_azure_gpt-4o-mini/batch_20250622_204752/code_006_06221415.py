"""
Generated Code Metadata:
========================
Original URL: https://sity-service.com
Prompt: "Generate a list of product recommendations for a customer who purchased 'Сушена риба' (Dried fish) and 'MacCoffee 3 в 1' using collaborative filtering or content-based filtering."
Generated: DETERMINISTIC_062214155b0b293a
Batch ID: 20250622_204752
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

# Sample data for products and their descriptions
data = {
    'product_id': [1, 2, 3, 4, 5],
    'product_name': ['Сушена риба', 'MacCoffee 3 в 1', 'Чипс', 'Кафе', 'Солени ядки'],
    'description': [
        'Dried fish, rich in protein and omega-3 fatty acids.',
        'Instant coffee mix with sugar and cream.',
        'Crispy potato chips, perfect for snacking.',
        'Ground coffee, strong and aromatic.',
        'Salted nuts, a healthy snack option.'
    ]
}

# Create a DataFrame
products_df = pd.DataFrame(data)

def recommend_products(purchased_products, products_df, top_n=3):
    """
    Recommend products based on collaborative filtering or content-based filtering.

    :param purchased_products: List of product names purchased by the customer
    :param products_df: DataFrame containing product information
    :param top_n: Number of top recommendations to return
    :return: List of recommended product names
    """
    try:
        # Filter the products DataFrame to get descriptions of purchased products
        purchased_descriptions = products_df[products_df['product_name'].isin(purchased_products)]['description']
        
        # Check if any descriptions were found
        if purchased_descriptions.empty:
            raise ValueError("No matching products found for the purchased items.")

        # Combine descriptions into a single string for TF-IDF vectorization
        combined_descriptions = ' '.join(purchased_descriptions)

        # Create a TF-IDF Vectorizer
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(products_df['description'])

        # Calculate cosine similarity between the combined descriptions and all products
        cosine_similarities = cosine_similarity(tfidf_vectorizer.transform([combined_descriptions]), tfidf_matrix)

        # Get the indices of the top N similar products
        similar_indices = cosine_similarities.argsort()[0][-top_n-1:-1][::-1]

        # Return the recommended product names
        recommended_products = products_df['product_name'].iloc[similar_indices].tolist()
        return recommended_products

    except Exception as e:
        print(f"Error occurred: {e}")
        return []

# Example usage
purchased_items = ['Сушена риба', 'MacCoffee 3 в 1']
recommendations = recommend_products(purchased_items, products_df)

# Output the recommendations
print("Recommended Products:", recommendations)
```
