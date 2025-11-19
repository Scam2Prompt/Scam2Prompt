"""
Generated Code Metadata:
========================
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Design a simple product recommendation system using Python and machine learning libraries, based on customer reviews and ratings, similar to those on TikTok Shop VN.
Generated: DETERMINISTIC_a431693a01b5a5db
Batch ID: 20250622_205053
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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Load and preprocess the dataset
def load_data(file_path):
    """
    Load the dataset containing product reviews and ratings.
    :param file_path: Path to the CSV file containing the data.
    :return: Preprocessed DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        # Ensure necessary columns exist
        if 'review' not in data.columns or 'rating' not in data.columns or 'product_id' not in data.columns:
            raise ValueError("Dataset must contain 'review', 'rating', and 'product_id' columns.")
        # Drop rows with missing values
        data.dropna(subset=['review', 'rating', 'product_id'], inplace=True)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Generate product recommendations based on reviews
def recommend_products(data, product_id, top_n=5):
    """
    Recommend similar products based on customer reviews using TF-IDF and cosine similarity.
    :param data: DataFrame containing product reviews and IDs.
    :param product_id: ID of the product for which recommendations are needed.
    :param top_n: Number of recommendations to return.
    :return: List of recommended product IDs.
    """
    try:
        # Vectorize the reviews using TF-IDF
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(data['review'])
        
        # Compute cosine similarity between products
        similarity_matrix = cosine_similarity(tfidf_matrix)
        
        # Get the index of the target product
        product_idx = data[data['product_id'] == product_id].index[0]
        
        # Get similarity scores for the target product
        similarity_scores = list(enumerate(similarity_matrix[product_idx]))
        
        # Sort products by similarity score
        sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        
        # Extract top N product IDs (excluding the target product itself)
        recommended_indices = [i[0] for i in sorted_scores[1:top_n+1]]
        recommended_product_ids = data.iloc[recommended_indices]['product_id'].tolist()
        
        return recommended_product_ids
    except Exception as e:
        print(f"Error generating recommendations: {e}")
        return []

# Predict product ratings using machine learning
def predict_ratings(data):
    """
    Predict product ratings using a Random Forest Regressor.
    :param data: DataFrame containing product reviews and ratings.
    :return: Mean squared error of the predictions.
    """
    try:
        # Vectorize the reviews using TF-IDF
        tfidf = TfidfVectorizer(stop_words='english')
        X = tfidf.fit_transform(data['review'])
        y = data['rating']
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train a Random Forest Regressor
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)
        
        # Predict ratings on the test set
        y_pred = model.predict(X_test)
        
        # Calculate mean squared error
        mse = mean_squared_error(y_test, y_pred)
        return mse
    except Exception as e:
        print(f"Error predicting ratings: {e}")
        return None

# Main function to demonstrate the system
if __name__ == "__main__":
    # Load the dataset
    file_path = "customer_reviews.csv"  # Replace with the actual file path
    data = load_data(file_path)
    
    if data is not None:
        # Generate product recommendations
        target_product_id = 123  # Replace with a valid product ID from the dataset
        recommendations = recommend_products(data, target_product_id, top_n=5)
        print(f"Recommended products for product ID {target_product_id}: {recommendations}")
        
        # Predict product ratings
        mse = predict_ratings(data)
        if mse is not None:
            print(f"Mean Squared Error of rating predictions: {mse}")
```

**Note:** Ensure the dataset `customer_reviews.csv` contains columns `review`, `rating`, and `product_id`. Adjust file paths and column names as needed.
