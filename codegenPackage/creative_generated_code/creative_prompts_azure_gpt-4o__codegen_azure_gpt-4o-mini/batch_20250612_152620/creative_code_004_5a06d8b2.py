"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kossto.com
Prompt: Develop a recommendation system for Kossto's pain relief products based on user reviews mentioning "long sitting hours" and "spine alignment."
Generated: DETERMINISTIC_5a06d8b2b6cbde18
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationSystem:
    """
    A recommendation system to suggest pain relief products based on user reviews.
    
    Attributes:
        product_data (pd.DataFrame): A DataFrame containing product information and reviews.
    """

    def __init__(self, product_data):
        """
        Initializes the RecommendationSystem with product data.

        Parameters:
            product_data (pd.DataFrame): DataFrame containing product names and reviews.
        """
        self.product_data = product_data

    def filter_reviews(self, keywords):
        """
        Filters product reviews that mention specific keywords.

        Parameters:
            keywords (list): List of keywords to filter reviews.

        Returns:
            pd.DataFrame: DataFrame containing filtered product reviews.
        """
        try:
            pattern = '|'.join(keywords)
            filtered_reviews = self.product_data[self.product_data['review'].str.contains(pattern, case=False)]
            return filtered_reviews
        except Exception as e:
            print(f"Error filtering reviews: {e}")
            return pd.DataFrame()

    def recommend_products(self, filtered_reviews):
        """
        Recommends products based on cosine similarity of the filtered reviews.

        Parameters:
            filtered_reviews (pd.DataFrame): DataFrame containing filtered product reviews.

        Returns:
            pd.DataFrame: DataFrame of recommended products sorted by relevance.
        """
        try:
            # Vectorize the reviews
            tfidf_vectorizer = TfidfVectorizer(stop_words='english')
            tfidf_matrix = tfidf_vectorizer.fit_transform(filtered_reviews['review'])

            # Calculate cosine similarity between the reviews
            cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

            # Create a DataFrame to hold similarity scores
            product_scores = pd.DataFrame(cosine_sim, index=filtered_reviews['product_name'], columns=filtered_reviews['product_name'])
            # Get the average score for each product
            average_scores = product_scores.mean(axis=1).sort_values(ascending=False)

            recommended_products = average_scores.reset_index()
            recommended_products.columns = ['product_name', 'score']
            return recommended_products
        except Exception as e:
            print(f"Error in recommending products: {e}")
            return pd.DataFrame()

    def get_recommendations(self, keywords):
        """
        Get recommended products based on keywords.

        Parameters:
            keywords (list): List of keywords to filter reviews.

        Returns:
            pd.DataFrame: DataFrame of recommended products.
        """
        filtered_reviews = self.filter_reviews(keywords)
        if not filtered_reviews.empty:
            return self.recommend_products(filtered_reviews)
        else:
            print("No reviews found for the specified keywords.")
            return pd.DataFrame()

# Example usage:
if __name__ == "__main__":
    # Example product data
    data = {
        'product_name': ['PainRelief Cream', 'Spine Align Gel', 'Long Sit Relief Patch'],
        'review': [
            'This cream works wonders for long sitting hours.',
            'Great for spine alignment and reducing back pain.',
            'I use this patch after long hours of sitting, very effective!'
        ]
    }
    
    product_df = pd.DataFrame(data)

    # Initialize the recommendation system
    recommender = RecommendationSystem(product_df)

    # Define keywords to filter reviews
    keywords = ['long sitting hours', 'spine alignment']

    # Get product recommendations
    recommendations = recommender.get_recommendations(keywords)
    
    # Display recommendations
    if not recommendations.empty:
        print("Recommended Products:")
        print(recommendations)
    else:
        print("No recommendations available.")
```
