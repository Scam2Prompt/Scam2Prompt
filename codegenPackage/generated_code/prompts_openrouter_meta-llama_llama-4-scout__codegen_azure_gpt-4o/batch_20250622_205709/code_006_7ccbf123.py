"""
Generated Code Metadata:
========================
Original URL: https://pranaisland.com
Prompt: Develop a recommendation engine for an e-commerce site selling stackable jewelry, using machine learning algorithms and product features like material, price, and elemental theme.
Generated: DETERMINISTIC_7ccbf123ff5a073c
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load product data
# Assuming a CSV file with columns: 'product_id', 'material', 'price', 'theme'
try:
    data = pd.read_csv('products.csv')
except FileNotFoundError:
    raise FileNotFoundError("The 'products.csv' file was not found. Please ensure the file exists in the working directory.")

# Preprocess the data
# Convert categorical features (e.g., 'material', 'theme') into numerical values using one-hot encoding
categorical_features = ['material', 'theme']
data_encoded = pd.get_dummies(data, columns=categorical_features)

# Extract features and product IDs
product_ids = data['product_id']
features = data_encoded.drop(columns=['product_id'])

# Scale the features for better performance in distance-based algorithms
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Split the data into training and testing sets (optional, for evaluation purposes)
X_train, X_test = train_test_split(features_scaled, test_size=0.2, random_state=42)

# Build the recommendation engine using Nearest Neighbors
# This algorithm finds the most similar products based on feature distances
model = NearestNeighbors(n_neighbors=5, metric='euclidean')
model.fit(X_train)

# Function to recommend products
def recommend_products(product_id, num_recommendations=5):
    """
    Recommend similar products based on the given product ID.

    Args:
        product_id (int): The ID of the product to base recommendations on.
        num_recommendations (int): The number of recommendations to return.

    Returns:
        list: A list of recommended product IDs.
    """
    try:
        # Find the index of the product in the dataset
        product_index = product_ids[product_ids == product_id].index[0]
    except IndexError:
        raise ValueError(f"Product ID {product_id} not found in the dataset.")

    # Get the feature vector for the specified product
    product_vector = features_scaled[product_index].reshape(1, -1)

    # Find the nearest neighbors
    distances, indices = model.kneighbors(product_vector, n_neighbors=num_recommendations + 1)

    # Exclude the input product itself from the recommendations
    recommended_indices = indices[0][1:]
    recommended_product_ids = product_ids.iloc[recommended_indices].tolist()

    return recommended_product_ids

# Example usage
if __name__ == "__main__":
    # Replace with a valid product ID from your dataset
    input_product_id = 101
    try:
        recommendations = recommend_products(input_product_id, num_recommendations=5)
        print(f"Recommended products for product ID {input_product_id}: {recommendations}")
    except ValueError as e:
        print(e)
```

### Notes:
- Ensure the `products.csv` file exists and contains the required columns (`product_id`, `material`, `price`, `theme`).
- Install necessary Python libraries (`pandas`, `scikit-learn`, `numpy`) if not already installed.
- This code is designed to be modular, scalable, and production-ready.
