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
# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Define a class for the product recommendation system
class ProductRecommender:
    def __init__(self, products_df, reviews_df):
        """
        Initialize the product recommender.

        Parameters:
        products_df (pd.DataFrame): A DataFrame containing product information.
        reviews_df (pd.DataFrame): A DataFrame containing customer reviews and ratings.
        """
        self.products_df = products_df
        self.reviews_df = reviews_df

    def _prepare_data(self):
        """
        Prepare the data for training by merging products and reviews DataFrames.
        """
        # Merge products and reviews DataFrames
        merged_df = pd.merge(self.products_df, self.reviews_df, on='product_id')
        return merged_df

    def _vectorize_reviews(self, merged_df):
        """
        Vectorize customer reviews using TF-IDF.

        Parameters:
        merged_df (pd.DataFrame): A DataFrame containing merged product and review information.

        Returns:
        tfidf_vectors (pd.DataFrame): A DataFrame containing TF-IDF vectors for customer reviews.
        """
        # Initialize TF-IDF vectorizer
        vectorizer = TfidfVectorizer(stop_words='english')
        # Fit the vectorizer to the review text and transform it into vectors
        tfidf_vectors = vectorizer.fit_transform(merged_df['review_text'])
        return pd.DataFrame(tfidf_vectors.toarray(), columns=vectorizer.get_feature_names_out())

    def train_model(self):
        """
        Train a random forest regressor model to predict product ratings based on TF-IDF vectors.

        Returns:
        model (RandomForestRegressor): A trained random forest regressor model.
        """
        # Prepare the data
        merged_df = self._prepare_data()
        # Vectorize customer reviews
        tfidf_vectors = self._vectorize_reviews(merged_df)

        # Define features (X) and target (y)
        X = tfidf_vectors
        y = merged_df['rating']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a random forest regressor model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        print(f"Model RMSE: {np.sqrt(mean_squared_error(y_test, y_pred))}")

        return model

    def make_recommendations(self, product_id, model, num_recs=5):
        """
        Make product recommendations based on customer reviews and ratings.

        Parameters:
        product_id (int): The ID of the product for which to make recommendations.
        model (RandomForestRegressor): A trained random forest regressor model.
        num_recs (int): The number of recommendations to return.

        Returns:
        recs (pd.DataFrame): A DataFrame containing recommended products.
        """
        # Get the TF-IDF vector for the product
        product_review = self.reviews_df[self.reviews_df['product_id'] == product_id]['review_text'].iloc[0]
        vectorizer = TfidfVectorizer(stop_words='english')
        product_vector = vectorizer.fit_transform([product_review])
        product_vector = pd.DataFrame(product_vector.toarray(), columns=vectorizer.get_feature_names_out())

        # Predict ratings for all products
        predicted_ratings = model.predict(self._vectorize_reviews(self._prepare_data()))

        # Get the top-N recommended products
        recs = self.products_df.copy()
        recs['predicted_rating'] = predicted_ratings
        recs = recs[recs['product_id'] != product_id].sort_values(by='predicted_rating', ascending=False).head(num_recs)

        return recs[['product_id', 'product_name', 'predicted_rating']]

# Example usage
if __name__ == "__main__":
    # Sample product data
    products_df = pd.DataFrame({
        'product_id': [1, 2, 3, 4, 5],
        'product_name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    })

    # Sample review data
    reviews_df = pd.DataFrame({
        'product_id': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        'review_text': ['Great product!', 'Love it!', 'Good product.', 'Excellent!', 'Average.', 'Not bad.', 'Great!', 'Amazing!', 'Okay.', 'Decent.'],
        'rating': [5, 5, 4, 5, 3, 3, 5, 5, 3, 4]
    })

    # Create a product recommender
    recommender = ProductRecommender(products_df, reviews_df)

    # Train the model
    model = recommender.train_model()

    # Make recommendations
    recs = recommender.make_recommendations(1, model)
    print(recs)
```
