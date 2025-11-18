"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Suggest a library or framework for building a product recommendation engine for a site similar to "Poly-Market.hu," focusing on furniture and home appliances.
Generated: DETERMINISTIC_b965ba71d558b82f
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code using the `scikit-learn` library to build a product recommendation engine. This example demonstrates collaborative filtering with matrix factorization using Singular Value Decomposition (SVD). 

```python
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from surprise import SVD, Dataset, Reader
from surprise.model_selection import cross_validate

# Function to build and evaluate a product recommendation engine
def build_recommendation_engine():
    """
    Build a product recommendation engine using collaborative filtering (SVD).
    Focuses on furniture and home appliances data.

    Returns:
        None
    """
    try:
        # Sample dataset: Replace with actual data from your site
        # Data format: user_id, product_id, rating
        data = {
            "user_id": [1, 2, 3, 1, 2, 3, 4],
            "product_id": [101, 101, 101, 102, 102, 103, 103],
            "rating": [5, 3, 4, 2, 5, 4, 1]
        }

        # Load data into a pandas DataFrame
        df = pd.DataFrame(data)

        # Surprise requires data to be in a specific format
        reader = Reader(rating_scale=(1, 5))  # Rating scale from 1 to 5
        dataset = Dataset.load_from_df(df[['user_id', 'product_id', 'rating']], reader)

        # Train-test split
        trainset, testset = train_test_split(df, test_size=0.2, random_state=42)

        # Build and train the SVD model
        model = SVD()
        cross_validate(model, dataset, cv=5, verbose=True)

        # Generate recommendations (example for user_id = 1)
        user_id = 1
        user_products = df[df["user_id"] == user_id]["product_id"].unique()
        all_products = df["product_id"].unique()

        # Get list of products not yet rated by the user
        products_to_rate = [p for p in all_products if p not in user_products]

        recommendations = []
        for product_id in products_to_rate:
            pred = model.predict(user_id, product_id)
            recommendations.append((product_id, pred.est))

        # Sort recommendations by predicted rating (descending)
        recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)

        # Display top 5 recommendations
        print(f"Top recommendations for user {user_id}:")
        for product_id, rating in recommendations[:5]:
            print(f"Product ID: {product_id}, Predicted Rating: {rating:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the recommendation engine
if __name__ == "__main__":
    build_recommendation_engine()
```
