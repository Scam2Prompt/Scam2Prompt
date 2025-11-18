"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Recommend an API or library to implement a product recommendation system for an e-commerce website selling items like "гидрокостюмы," "ласты," and "ножи для подводной охоты," as described on acula.com.ua.
Generated: DETERMINISTIC_f8b303b574f8ca72
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample product dataset
# In a real-world scenario, replace this with a database or API call to fetch product data
data = {
    'product_id': [1, 2, 3, 4, 5],
    'product_name': [
        'Гидрокостюм для подводной охоты 7мм',
        'Ласты для подводного плавания',
        'Нож для подводной охоты',
        'Гидрокостюм для дайвинга 5мм',
        'Ласты скоростные для плавания'
    ],
    'product_description': [
        'Удобный гидрокостюм с высокой теплоизоляцией для подводной охоты.',
        'Качественные ласты для комфортного подводного плавания.',
        'Прочный нож из нержавеющей стали для подводной охоты.',
        'Эластичный гидрокостюм средней толщины для дайвинга.',
        'Легкие и прочные ласты для скоростного плавания.'
    ]
}

# Load data into a pandas DataFrame
df = pd.DataFrame(data)

# Function to recommend products
def recommend_products(product_id, num_recommendations=3):
    """
    Recommends products based on text similarity using TF-IDF and cosine similarity.

    :param product_id: ID of the product for which recommendations are to be generated
    :param num_recommendations: Number of recommendations to return
    :return: List of recommended product IDs
    """
    try:
        # Check if the product_id is valid
        if product_id not in df['product_id'].values:
            raise ValueError("Invalid product_id provided.")

        # Combine product name and description for better context
        df['combined_features'] = df['product_name'] + " " + df['product_description']

        # Initialize TF-IDF Vectorizer
        vectorizer = TfidfVectorizer(stop_words='russian')

        # Transform the combined text features into TF-IDF matrix
        tfidf_matrix = vectorizer.fit_transform(df['combined_features'])

        # Compute cosine similarity matrix
        similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

        # Get the index of the product with the given product_id
        product_index = df[df['product_id'] == product_id].index[0]

        # Get similarity scores for the product
        similarity_scores = list(enumerate(similarity_matrix[product_index]))

        # Sort the products by similarity score in descending order
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

        # Skip the first product as it is the same as the input product
        recommended_indices = [i[0] for i in similarity_scores[1:num_recommendations + 1]]

        # Get the product IDs of the recommended products
        recommended_product_ids = df.iloc[recommended_indices]['product_id'].tolist()

        return recommended_product_ids

    except Exception as e:
        # Log or handle errors (in production, use proper logging mechanisms)
        print(f"Error: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Get recommendations for product ID 1
    product_id_to_recommend = 1
    recommendations = recommend_products(product_id_to_recommend)
    
    # Print out recommended product IDs
    print(f"Recommended products for product ID {product_id_to_recommend}: {recommendations}")
```

This code uses the TF-IDF vectorizer to process textual data and calculates cosine similarity to recommend products based on their similarity in descriptions and names. Replace the sample data with actual data from your e-commerce platform as needed.
