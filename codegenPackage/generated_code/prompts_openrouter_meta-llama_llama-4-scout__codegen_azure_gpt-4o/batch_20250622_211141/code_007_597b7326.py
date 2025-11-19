"""
Generated Code Metadata:
========================
Original URL: https://jasmyevent.com
Prompt: Create a news article recommendation system using machine learning algorithms, such as collaborative filtering or content-based filtering, to suggest relevant articles to users based on their reading history on 光明网.
Generated: DETERMINISTIC_597b7326c547ebfd
Batch ID: 20250622_211141
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
from sklearn.metrics.pairwise import linear_kernel
from sklearn.model_selection import train_test_split
import numpy as np

# Load the dataset
# Assuming the dataset contains columns: 'user_id', 'article_id', 'title', 'content', 'read'
# 'read' is a binary column indicating whether the user has read the article (1 for read, 0 for not read)
try:
    data = pd.read_csv('guangming_articles.csv')
except FileNotFoundError:
    raise FileNotFoundError("Dataset file 'guangming_articles.csv' not found. Please ensure the file exists.")

# Preprocessing: Combine 'title' and 'content' for content-based filtering
data['combined_text'] = data['title'] + " " + data['content']

# Split the data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Content-Based Filtering using TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)

# Fit and transform the combined text
tfidf_matrix = tfidf_vectorizer.fit_transform(train_data['combined_text'])

# Compute cosine similarity between articles
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get recommendations based on content similarity
def get_content_recommendations(article_id, cosine_sim_matrix, articles_df, top_n=5):
    """
    Recommend articles based on content similarity.

    Parameters:
        article_id (int): ID of the article for which recommendations are needed.
        cosine_sim_matrix (ndarray): Precomputed cosine similarity matrix.
        articles_df (DataFrame): DataFrame containing article information.
        top_n (int): Number of recommendations to return.

    Returns:
        list: List of recommended article IDs.
    """
    try:
        # Get the index of the article
        idx = articles_df[articles_df['article_id'] == article_id].index[0]
    except IndexError:
        raise ValueError(f"Article ID {article_id} not found in the dataset.")

    # Get similarity scores for the article
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))

    # Sort articles by similarity score in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the top_n most similar articles
    top_indices = [i[0] for i in sim_scores[1:top_n+1]]  # Exclude the article itself

    # Return the article IDs of the recommended articles
    return articles_df.iloc[top_indices]['article_id'].tolist()

# Example usage
example_article_id = train_data['article_id'].iloc[0]
recommended_articles = get_content_recommendations(example_article_id, cosine_sim, train_data)
print(f"Recommended articles for article ID {example_article_id}: {recommended_articles}")

# Collaborative Filtering (User-Based)
# Create a user-item interaction matrix
user_item_matrix = train_data.pivot_table(index='user_id', columns='article_id', values='read', fill_value=0)

# Compute similarity between users
user_similarity = linear_kernel(user_item_matrix, user_item_matrix)

# Function to recommend articles based on user similarity
def get_user_based_recommendations(user_id, user_similarity_matrix, user_item_df, top_n=5):
    """
    Recommend articles based on user similarity.

    Parameters:
        user_id (int): ID of the user for whom recommendations are needed.
        user_similarity_matrix (ndarray): Precomputed user similarity matrix.
        user_item_df (DataFrame): User-item interaction matrix.
        top_n (int): Number of recommendations to return.

    Returns:
        list: List of recommended article IDs.
    """
    try:
        # Get the index of the user
        user_idx = user_item_df.index.get_loc(user_id)
    except KeyError:
        raise ValueError(f"User ID {user_id} not found in the dataset.")

    # Get similarity scores for the user
    sim_scores = list(enumerate(user_similarity_matrix[user_idx]))

    # Sort users by similarity score in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the top_n most similar users
    top_user_indices = [i[0] for i in sim_scores[1:top_n+1]]  # Exclude the user itself

    # Aggregate articles read by similar users
    similar_users = user_item_df.iloc[top_user_indices]
    recommended_articles = similar_users.sum(axis=0).sort_values(ascending=False)

    # Return the top_n article IDs
    return recommended_articles.index[:top_n].tolist()

# Example usage
example_user_id = train_data['user_id'].iloc[0]
user_based_recommendations = get_user_based_recommendations(example_user_id, user_similarity, user_item_matrix)
print(f"Recommended articles for user ID {example_user_id}: {user_based_recommendations}")
```
