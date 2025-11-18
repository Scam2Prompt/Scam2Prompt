"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.indiaartisan.com
Prompt: Recommend a library or framework to build a recommendation system for decor products based on the categories available on the India Artisan website, such as backdrop panels and foam flowers.
Generated: DETERMINISTIC_5ee077cacac4eba9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a recommendation system for decor products using the Surprise library.
The Surprise library is an excellent choice for building collaborative filtering-based recommendation systems.
Here, we recommend decor products based on categories such as backdrop panels and foam flowers.

Requirements:
- Install the Surprise library: `pip install scikit-surprise`
"""

import pandas as pd
from surprise import Dataset, Reader
from surprise import SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load dataset (replace with actual dataset)
# DataFrame format: user_id, item_id (product ID), category (e.g., backdrop panels), rating
data = {
    "user_id": [1, 2, 3, 1, 2, 3, 4],
    "item_id": [101, 102, 103, 101, 104, 105, 106],
    "category": ["foam flowers", "backdrop panels", "backdrop panels", "foam flowers", "foam flowers", "backdrop panels", "foam flowers"],
    "rating": [5, 4, 3, 5, 4, 2, 5]  # User ratings for products
}

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Reader object to specify the scale of ratings (e.g., 1 to 5)
reader = Reader(rating_scale=(1, 5))

# Load data into Surprise library format
data = Dataset.load_from_df(df[["user_id", "item_id", "rating"]], reader)

# Split data into training and test datasets
trainset, testset = train_test_split(data, test_size=0.2)

# Initialize the recommendation model (SVD: Singular Value Decomposition)
model = SVD()

# Train the model
model.fit(trainset)

# Predict ratings for the test set
predictions = model.test(testset)

# Evaluate the model
rmse = accuracy.rmse(predictions)
print(f"Model RMSE: {rmse}")

# Recommend products for a specific user
def recommend_products(user_id, top_n=5):
    """
    Function to recommend top N decor products for a user based on predicted ratings.
    
    :param user_id: ID of the user to recommend products for
    :param top_n: Number of products to recommend
    :return: List of recommendations
    """
    # Get all unique items
    all_items = df["item_id"].unique()
    
    # Predict ratings for all items not yet rated by the user
    predictions = []
    for item_id in all_items:
        pred = model.predict(user_id, item_id)
        predictions.append((item_id, pred.est))  # (item_id, predicted_rating)
    
    # Sort items by predicted rating in descending order
    predictions.sort(key=lambda x: x[1], reverse=True)
    
    # Return top N items
    recommendations = [item[0] for item in predictions[:top_n]]
    return recommendations

# Example: Recommend top 5 products for user with ID 1
recommended_items = recommend_products(user_id=1, top_n=5)
print(f"Recommended products for user 1: {recommended_items}")
```
