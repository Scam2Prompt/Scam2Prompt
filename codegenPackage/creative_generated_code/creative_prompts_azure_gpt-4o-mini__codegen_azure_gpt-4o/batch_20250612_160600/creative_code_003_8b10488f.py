"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livivid.com
Prompt: How can I develop a product recommendation system for a website like livivid.com that sells unique handmade items, including hemp clothing and accessories?
Generated: DETERMINISTIC_8b10488f06abe040
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load product data
# Assume the data is in a CSV file with columns: 'product_id', 'product_name', 'description'
try:
    product_data = pd.read_csv('products.csv')
except FileNotFoundError:
    raise Exception("The products.csv file was not found. Please ensure the file exists in the correct location.")

# Check if required columns are present
required_columns = ['product_id', 'product_name', 'description']
if not all(col in product_data.columns for col in required_columns):
    raise Exception("The input CSV file must contain the following columns: 'product_id', 'product_name', 'description'.")

# Fill missing descriptions with empty strings
product_data['description'] = product_data['description'].fillna("")

# Generate TF-IDF matrix for product descriptions
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(product_data['description'])

# Calculate cosine similarity between products based on their descriptions
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_recommendations(product_id, num_recommendations=5):
    """
    Get product recommendations based on a given product ID.

    Args:
        product_id (int): The ID of the product to base recommendations on.
        num_recommendations (int): The number of product recommendations to return.

    Returns:
        list: A list of product IDs recommended.
    """
    # Ensure the product ID exists
    if product_id not in product_data['product_id'].values:
        raise ValueError(f"Product ID {product_id} not found in the dataset.")

    # Find the index of the given product ID
    product_idx = product_data.index[product_data['product_id'] == product_id][0]

    # Get similarity scores for the product
    similarity_scores = list(enumerate(cosine_sim[product_idx]))

    # Sort products by similarity scores in descending order
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get indices of the top recommendations (excluding the input product itself)
    top_indices = [i[0] for i in similarity_scores[1:num_recommendations + 1]]

    # Return the product IDs of the recommended products
    return product_data.iloc[top_indices]['product_id'].tolist()

# Example usage
if __name__ == "__main__":
    try:
        # Input product ID for which recommendations are needed
        input_product_id = 101  # Replace with a valid product ID
        recommendations = get_recommendations(input_product_id, num_recommendations=5)
        print(f"Recommended products for product ID {input_product_id}: {recommendations}")
    except Exception as e:
        print(f"Error: {e}")
```

### Notes:
Ensure that the `products.csv` file is in the same directory as the script and contains the required columns: `product_id`, `product_name`, and `description`. This code uses content-based filtering based on product descriptions. For real-world scenarios, additional features such as user behavior data can be integrated for improved recommendations.
