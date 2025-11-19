"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Create a product recommendation system using Python and machine learning libraries, based on the product categories and customer reviews on acula.com.ua.
Generated: DETERMINISTIC_aaabc1aaf57bb2dc
Batch ID: 20250622_211342
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load data (replace 'data.csv' with the actual dataset file from acula.com.ua)
# Ensure the dataset contains columns: 'product_id', 'category', 'review'
try:
    data = pd.read_csv('data.csv')
except FileNotFoundError:
    raise FileNotFoundError("The dataset file 'data.csv' was not found. Please provide the correct file.")

# Check for missing values and handle them
if data.isnull().sum().sum() > 0:
    data = data.dropna()  # Drop rows with missing values

# Encode product categories
label_encoder = LabelEncoder()
data['category_encoded'] = label_encoder.fit_transform(data['category'])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    data['review'], data['category_encoded'], test_size=0.2, random_state=42
)

# Vectorize customer reviews using TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Train a Random Forest Classifier for category prediction
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train_tfidf, y_train)

# Evaluate the model
accuracy = rf_classifier.score(X_test_tfidf, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# Function to recommend products based on a given review
def recommend_products(review, top_n=5):
    """
    Recommend products based on a given review.

    Parameters:
    - review (str): The customer review text.
    - top_n (int): Number of top recommendations to return.

    Returns:
    - recommendations (list): List of recommended product IDs.
    """
    try:
        # Transform the review using the trained TF-IDF vectorizer
        review_tfidf = tfidf_vectorizer.transform([review])
        
        # Predict the category of the review
        predicted_category = rf_classifier.predict(review_tfidf)[0]
        
        # Filter products in the predicted category
        category_products = data[data['category_encoded'] == predicted_category]
        
        # Compute similarity scores between the review and product reviews
        similarity_scores = cosine_similarity(review_tfidf, tfidf_vectorizer.transform(category_products['review']))
        
        # Get top N product recommendations
        top_indices = np.argsort(similarity_scores[0])[::-1][:top_n]
        recommendations = category_products.iloc[top_indices]['product_id'].tolist()
        
        return recommendations
    except Exception as e:
        print(f"Error in recommendation system: {e}")
        return []

# Example usage
example_review = "I love the quality and durability of this product."
recommended_products = recommend_products(example_review)
print("Recommended Products:", recommended_products)
```

This code assumes the existence of a dataset (`data.csv`) with columns `product_id`, `category`, and `review`. It uses TF-IDF for text vectorization, a Random Forest Classifier for category prediction, and cosine similarity for product recommendations. Proper error handling and comments are included to ensure clarity and robustness.
