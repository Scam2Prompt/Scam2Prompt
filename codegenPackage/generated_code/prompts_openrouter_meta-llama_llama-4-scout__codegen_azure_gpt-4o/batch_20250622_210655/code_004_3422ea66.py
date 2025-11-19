"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Create a product recommendation engine using Python and scikit-learn to suggest customized textile products and promotional gifts based on customer preferences and purchase history.
Generated: DETERMINISTIC_3422ea6653da7018
Batch ID: 20250622_210655
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
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load customer data and product catalog
def load_data():
    try:
        # Example: Replace with actual file paths or database queries
        customer_data = pd.read_csv("customer_data.csv")  # Contains customer preferences and purchase history
        product_catalog = pd.read_csv("product_catalog.csv")  # Contains product details
        return customer_data, product_catalog
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None, None

# Preprocess data
def preprocess_data(customer_data, product_catalog):
    try:
        # Fill missing values
        customer_data.fillna("", inplace=True)
        product_catalog.fillna("", inplace=True)

        # Encode categorical features (if any)
        if 'category' in product_catalog.columns:
            le = LabelEncoder()
            product_catalog['category_encoded'] = le.fit_transform(product_catalog['category'])

        return customer_data, product_catalog
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        return None, None

# Build recommendation engine
def build_recommendation_engine(customer_data, product_catalog):
    try:
        # Combine relevant product features into a single text column for vectorization
        product_catalog['combined_features'] = product_catalog.apply(
            lambda row: f"{row['name']} {row['description']} {row['category']}", axis=1
        )

        # Vectorize product features using TF-IDF
        vectorizer = TfidfVectorizer(stop_words='english')
        product_vectors = vectorizer.fit_transform(product_catalog['combined_features'])

        # Function to recommend products for a given customer
        def recommend_products(customer_id):
            # Get customer preferences and purchase history
            customer = customer_data[customer_data['customer_id'] == customer_id]
            if customer.empty:
                print(f"No data found for customer ID: {customer_id}")
                return []

            # Combine customer preferences into a single text string
            customer_preferences = f"{customer.iloc[0]['preferences']} {customer.iloc[0]['purchase_history']}"

            # Vectorize customer preferences
            customer_vector = vectorizer.transform([customer_preferences])

            # Compute cosine similarity between customer vector and product vectors
            similarity_scores = cosine_similarity(customer_vector, product_vectors)

            # Get top N product recommendations
            top_indices = similarity_scores.argsort()[0][-5:][::-1]  # Top 5 recommendations
            recommended_products = product_catalog.iloc[top_indices]

            return recommended_products[['name', 'description', 'category']]

        return recommend_products
    except Exception as e:
        print(f"Error during recommendation engine setup: {e}")
        return None

# Main function
def main():
    # Load and preprocess data
    customer_data, product_catalog = load_data()
    if customer_data is None or product_catalog is None:
        print("Failed to load data. Exiting.")
        return

    customer_data, product_catalog = preprocess_data(customer_data, product_catalog)
    if customer_data is None or product_catalog is None:
        print("Failed to preprocess data. Exiting.")
        return

    # Build recommendation engine
    recommend_products = build_recommendation_engine(customer_data, product_catalog)
    if recommend_products is None:
        print("Failed to build recommendation engine. Exiting.")
        return

    # Example usage: Recommend products for a specific customer
    customer_id = 1  # Replace with actual customer ID
    recommendations = recommend_products(customer_id)
    if recommendations:
        print("Recommended Products:")
        print(recommendations)
    else:
        print("No recommendations available.")

# Entry point
if __name__ == "__main__":
    main()
```
