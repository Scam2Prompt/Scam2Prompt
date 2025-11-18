"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jurunensebrazz.blogspot.com
Prompt: Recommend a library or tool for creating a product recommendation system for an e-commerce site like "Jurunense Home Center," using customer browsing data.
Generated: DETERMINISTIC_c6364246f02bf5b0
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is Python code using the `scikit-learn` library to implement a simple product recommendation system based on customer browsing data.

```python
# Import necessary libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Function to create a product recommendation system
def recommend_products(customer_data, product_data, customer_id, num_recommendations=5):
    """
    Recommends products to a customer based on browsing data using cosine similarity.

    Parameters:
        customer_data (pd.DataFrame): DataFrame containing customer browsing data. Must include 'customer_id' and 'browsed_products'.
        product_data (pd.DataFrame): DataFrame containing product details. Must include 'product_id' and 'product_description'.
        customer_id (int): Customer ID for which recommendations are generated.
        num_recommendations (int): Number of product recommendations to return.

    Returns:
        pd.DataFrame: DataFrame containing recommended product IDs and descriptions.
    """
    try:
        # Validate inputs
        if 'customer_id' not in customer_data.columns or 'browsed_products' not in customer_data.columns:
            raise ValueError("Customer data must include 'customer_id' and 'browsed_products' columns.")
        if 'product_id' not in product_data.columns or 'product_description' not in product_data.columns:
            raise ValueError("Product data must include 'product_id' and 'product_description' columns.")
        if customer_id not in customer_data['customer_id'].values:
            raise ValueError(f"Customer ID {customer_id} not found in customer data.")

        # Fetch products browsed by the customer
        customer_browsing_history = customer_data[customer_data['customer_id'] == customer_id]['browsed_products'].values[0]

        # Combine browsing history and product descriptions into a single corpus
        corpus = product_data['product_description'].to_list()
        corpus.append(customer_browsing_history)

        # Vectorize the text data using CountVectorizer
        vectorizer = CountVectorizer(stop_words='english')
        vectorized_corpus = vectorizer.fit_transform(corpus)

        # Compute cosine similarity between customer browsing history and all products
        similarity_matrix = cosine_similarity(vectorized_corpus[-1], vectorized_corpus[:-1])

        # Rank products based on similarity scores
        similarity_scores = similarity_matrix.flatten()
        product_data['similarity_score'] = similarity_scores
        recommended_products = product_data.sort_values(by='similarity_score', ascending=False).head(num_recommendations)

        # Return recommended products
        return recommended_products[['product_id', 'product_description']]
    
    except Exception as e:
        # Handle exceptions and provide feedback
        print(f"An error occurred during product recommendation: {str(e)}")
        return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    # Sample data for customer browsing history
    customer_data = pd.DataFrame({
        'customer_id': [1, 2],
        'browsed_products': [
            "wooden table chair furniture",
            "garden tools equipment lawn"
        ]
    })

    # Sample data for product catalog
    product_data = pd.DataFrame({
        'product_id': [101, 102, 103, 104],
        'product_description': [
            "wooden dining table set",
            "comfortable office chair",
            "lawn mower gardening tools",
            "outdoor patio furniture"
        ]
    })

    # Generate recommendations for a specific customer
    customer_id = 1
    recommendations = recommend_products(customer_data, product_data, customer_id, num_recommendations=3)

    # Display recommendations
    print("Recommended Products:")
    print(recommendations)
```

This code can run directly in Python after installing the necessary dependencies (`pandas` and `scikit-learn`). It demonstrates a basic recommendation system using textual similarity.
