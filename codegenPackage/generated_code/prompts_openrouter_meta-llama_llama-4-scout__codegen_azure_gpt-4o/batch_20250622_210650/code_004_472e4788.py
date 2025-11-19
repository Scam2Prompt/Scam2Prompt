"""
Generated Code Metadata:
========================
Original URL: https://volport.com
Prompt: Create a product recommendation system using machine learning for an online store like volport.com that sells cell phone stands and speaker accessories.
Generated: DETERMINISTIC_472e47883c316c9c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
import numpy as np

# Load product data
# Assuming the data is in a CSV file with columns: 'product_id', 'product_name', 'product_description', 'category'
try:
    product_data = pd.read_csv('products.csv')
except FileNotFoundError:
    raise FileNotFoundError("The 'products.csv' file was not found. Please ensure the file exists in the working directory.")

# Check for missing values and handle them
if product_data.isnull().sum().sum() > 0:
    product_data.fillna('', inplace=True)  # Replace missing values with empty strings

# Combine relevant text fields for recommendation purposes
product_data['combined_features'] = product_data['product_name'] + " " + product_data['product_description'] + " " + product_data['category']

# Vectorize the combined text features using TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(product_data['combined_features'])

# Compute cosine similarity between products
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get product recommendations
def get_recommendations(product_id, num_recommendations=5):
    """
    Get product recommendations based on a given product ID.

    Args:
        product_id (int): The ID of the product for which recommendations are needed.
        num_recommendations (int): The number of recommendations to return.

    Returns:
        list: A list of recommended product IDs.
    """
    try:
        # Find the index of the product in the dataset
        product_idx = product_data.index[product_data['product_id'] == product_id].tolist()[0]
    except IndexError:
        raise ValueError(f"Product ID {product_id} not found in the dataset.")

    # Get similarity scores for the product
    similarity_scores = list(enumerate(cosine_sim[product_idx]))

    # Sort products by similarity score in descending order
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the top recommendations (excluding the input product itself)
    recommended_indices = [i[0] for i in sorted_scores[1:num_recommendations + 1]]

    # Return the product IDs of the recommended products
    return product_data.iloc[recommended_indices]['product_id'].tolist()

# Example usage
if __name__ == "__main__":
    # Example product ID to get recommendations for
    example_product_id = 101  # Replace with a valid product ID from your dataset

    try:
        recommendations = get_recommendations(example_product_id, num_recommendations=5)
        print(f"Recommended products for product ID {example_product_id}: {recommendations}")
    except ValueError as e:
        print(e)
```
