"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Generate Python code to visualize trends in e-commerce review topics for baby products, leveraging Consensys's insights on category landscape and consumer language clusters.
Generated: DETERMINISTIC_15a03d7626a5e225
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from wordcloud import WordCloud

# Sample e-commerce review data for baby products
review_data = {
    "review": [
        "Love this baby monitor, so easy to use and great value!",
        "The stroller is so lightweight and easy to maneuver.",
        "The baby clothes are adorable, but run small.",
        "The breast pump is so comfortable and efficient.",
        "The crib is sturdy and looks great in our nursery.",
        "The baby food is organic and my baby loves it.",
        "The baby carrier is so convenient for running errands.",
        "The diapers are eco-friendly and work great.",
        "The baby gym is so much fun for tummy time.",
        "The nursery decor is beautiful and calming."
    ],
    "category": [
        "Baby Monitors",
        "Strollers",
        "Baby Clothes",
        "Breast Pumps",
        "Cribs",
        "Baby Food",
        "Baby Carriers",
        "Diapers",
        "Baby Gyms",
        "Nursery Decor"
    ]
}

# Create a DataFrame from the review data
df = pd.DataFrame(review_data)

# Define a function to perform K-means clustering on review text
def cluster_reviews(reviews, n_clusters):
    """
    Perform K-means clustering on review text.

    Args:
        reviews (list): List of review text.
        n_clusters (int): Number of clusters.

    Returns:
        labels (list): Cluster labels for each review.
    """
    # Create a TF-IDF vectorizer to transform text into vectors
    vectorizer = TfidfVectorizer(stop_words="english")

    # Fit the vectorizer to the review text and transform into vectors
    vectors = vectorizer.fit_transform(reviews)

    # Perform K-means clustering on the vectors
    kmeans = KMeans(n_clusters=n_clusters)
    labels = kmeans.fit_predict(vectors)

    return labels

# Define a function to visualize review topics using word clouds
def visualize_review_topics(reviews, labels):
    """
    Visualize review topics using word clouds.

    Args:
        reviews (list): List of review text.
        labels (list): Cluster labels for each review.
    """
    # Create a dictionary to store review text by cluster label
    review_dict = {}
    for review, label in zip(reviews, labels):
        if label not in review_dict:
            review_dict[label] = []
        review_dict[label].append(review)

    # Create a word cloud for each cluster
    for label, review_list in review_dict.items():
        # Join review text into a single string
        review_text = " ".join(review_list)

        # Create a word cloud
        wordcloud = WordCloud(width=800, height=400).generate(review_text)

        # Display the word cloud
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title(f"Review Topic {label}")
        plt.show()

# Perform K-means clustering on review text
n_clusters = 5
labels = cluster_reviews(df["review"], n_clusters)

# Visualize review topics using word clouds
visualize_review_topics(df["review"], labels)

# Define a function to analyze category landscape
def analyze_category_landscape(df):
    """
    Analyze category landscape.

    Args:
        df (DataFrame): DataFrame containing review data.

    Returns:
        category_counts (Series): Count of reviews by category.
    """
    # Count reviews by category
    category_counts = df["category"].value_counts()

    return category_counts

# Analyze category landscape
category_counts = analyze_category_landscape(df)

# Display category landscape
plt.figure(figsize=(10, 6))
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Category Landscape")
plt.show()

# Define a function to analyze consumer language clusters
def analyze_consumer_language_clusters(reviews, labels):
    """
    Analyze consumer language clusters.

    Args:
        reviews (list): List of review text.
        labels (list): Cluster labels for each review.

    Returns:
        cluster_text (dict): Dictionary of cluster labels to review text.
    """
    # Create a dictionary to store review text by cluster label
    cluster_text = {}
    for review, label in zip(reviews, labels):
        if label not in cluster_text:
            cluster_text[label] = []
        cluster_text[label].append(review)

    return cluster_text

# Analyze consumer language clusters
cluster_text = analyze_consumer_language_clusters(df["review"], labels)

# Display consumer language clusters
for label, review_list in cluster_text.items():
    print(f"Cluster {label}:")
    for review in review_list:
        print(review)
    print()
```
