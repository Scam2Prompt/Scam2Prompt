"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aatmanamjewels.com
Prompt: Illustrate how to implement a product recommendation system for a jewelry website, using the unique features of Atmanam Jewels as a reference.
Generated: DETERMINISTIC_baedc78f428c5801
Batch ID: 20250612_162051
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
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load the jewelry product dataset (mock dataset for demonstration purposes)
# Columns: product_id, price, material, style, gemstone, popularity
data = {
    'product_id': [1, 2, 3, 4, 5],
    'price': [100, 200, 250, 150, 300],
    'material': ['gold', 'silver', 'gold', 'platinum', 'silver'],
    'style': ['classic', 'modern', 'vintage', 'classic', 'modern'],
    'gemstone': ['diamond', 'ruby', 'emerald', 'sapphire', 'diamond'],
    'popularity': [4.5, 4.8, 3.9, 4.7, 4.2]
}

# Convert dataset to DataFrame
df = pd.DataFrame(data)

# Preprocessing: One-hot encode categorical features and normalize numerical features
categorical_features = ['material', 'style', 'gemstone']
numerical_features = ['price', 'popularity']

# One-hot encoding
df_encoded = pd.get_dummies(df, columns=categorical_features)

# Normalize numerical features
scaler = StandardScaler()
df_encoded[numerical_features] = scaler.fit_transform(df_encoded[numerical_features])

# Prepare feature matrix for model training
X = df_encoded.drop(columns=['product_id'])

# Initialize and train the recommendation model using k-Nearest Neighbors
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(X)

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Endpoint to recommend similar products based on a given product ID.

    Request JSON body:
    {
        "product_id": <int>
    }

    Response JSON:
    {
        "recommendations": [
            {"product_id": <int>, "similarity_score": <float>},
            ...
        ]
    }
    """
    try:
        # Parse request data
        request_data = request.get_json()
        product_id = request_data.get('product_id')

        # Validate input
        if product_id not in df['product_id'].values:
            return jsonify({"error": "Invalid product_id"}), 400

        # Find the index of the input product ID
        product_index = df[df['product_id'] == product_id].index[0]

        # Fetch the feature vector for the input product
        product_vector = X.iloc[product_index].values.reshape(1, -1)

        # Perform recommendation using k-NN
        distances, indices = knn.kneighbors(product_vector, n_neighbors=4)  # Including the product itself

        # Prepare recommendation results, excluding the input product
        recommendations = []
        for dist, idx in zip(distances[0][1:], indices[0][1:]):  # Skip the first result (self-match)
            recommendations.append({
                "product_id": int(df.iloc[idx]['product_id']),
                "similarity_score": float(1 - dist)  # Convert distance to similarity score
            })

        return jsonify({"recommendations": recommendations})

    except Exception as e:
        # Handle unexpected exceptions
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
