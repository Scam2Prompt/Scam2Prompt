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
from sklearn.metrics.pairwise import cosine_similarity

# Load product data
# Assume we have a CSV file with columns: 'product_id', 'product_name', 'product_description', 'category'
try:
    product_data = pd.read_csv('products.csv')
except FileNotFoundError:
    raise FileNotFoundError("The 'products.csv' file was not found. Please ensure the file exists in the correct location.")

# Check if required columns exist
required_columns = {'product_id', 'product_name', 'product_description', 'category'}
if not required_columns.issubset(product_data.columns):
    raise ValueError(f"The CSV file must contain the following columns: {required_columns}")

# Combine relevant text fields for recommendation
product_data['combined_features'] = product_data['product_name'] + " " + product_data['product_description'] + " " + product_data['category']

# Vectorize the combined features using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(product_data['combined_features'])

# Function to recommend products based on a given product_id
def recommend_products(product_id, num_recommendations=5):
    """
    Recommend products based on similarity to the given product_id.

    Args:
        product_id (int): The ID of the product to base recommendations on.
        num_recommendations (int): The number of recommendations to return.

    Returns:
        list: A list of recommended product IDs.
    """
    if product_id not in product_data['product_id'].values:
        raise ValueError(f"Product ID {product_id} not found in the dataset.")

    # Get the index of the product in the dataset
    product_index = product_data.index[product_data['product_id'] == product_id][0]

    # Compute cosine similarity between the selected product and all others
    cosine_similarities = cosine_similarity(tfidf_matrix[product_index], tfidf_matrix).flatten()

    # Get indices of the most similar products (excluding the input product itself)
    similar_indices = cosine_similarities.argsort()[-(num_recommendations + 1):-1][::-1]

    # Return the product IDs of the recommended products
    recommended_product_ids = product_data.iloc[similar_indices]['product_id'].tolist()
    return recommended_product_ids

# Example usage
if __name__ == "__main__":
    try:
        # Replace with a valid product_id from your dataset
        input_product_id = 101
        recommendations = recommend_products(input_product_id, num_recommendations=5)
        print(f"Recommended products for product ID {input_product_id}: {recommendations}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
