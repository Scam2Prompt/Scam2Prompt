"""
Generated Code Metadata:
========================
Original URL: https://bee-property.com
Prompt: Generate code to optimize property listings on platforms like Airbnb by analyzing and improving visibility through metadata and keyword strategies, as outlined by Bee Property.
Generated: DETERMINISTIC_12430f7d2e290886
Batch ID: 20250612_153224
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PropertyListingOptimizer:
    def __init__(self, listings_df, metadata_columns, keywords):
        """
        Initialize the PropertyListingOptimizer class.

        Args:
        - listings_df (pd.DataFrame): DataFrame containing property listings.
        - metadata_columns (list): List of metadata columns to consider.
        - keywords (list): List of relevant keywords for optimization.
        """
        self.listings_df = listings_df
        self.metadata_columns = metadata_columns
        self.keywords = keywords

    def _preprocess_metadata(self):
        """
        Preprocess metadata by concatenating relevant columns and cleaning text.
        """
        # Concatenate metadata columns into a single string
        self.listings_df['metadata'] = self.listings_df[self.metadata_columns].apply(lambda row: ' '.join(row), axis=1)

        # Clean text data
        self.listings_df['metadata'] = self.listings_df['metadata'].apply(lambda x: x.lower())
        self.listings_df['metadata'] = self.listings_df['metadata'].apply(lambda x: x.replace('\n', ' ').replace('\r', ''))

    def _calculate_tfidf(self):
        """
        Calculate TF-IDF scores for metadata and keywords.
        """
        # Initialize TF-IDF vectorizer
        vectorizer = TfidfVectorizer(stop_words='english')

        # Fit TF-IDF vectorizer to metadata and transform into matrix
        tfidf_matrix = vectorizer.fit_transform(self.listings_df['metadata'])

        # Get feature names (keywords)
        feature_names = vectorizer.get_feature_names_out()

        # Filter keywords and get their indices
        keyword_indices = [np.where(feature_names == keyword)[0][0] for keyword in self.keywords if keyword in feature_names]

        return tfidf_matrix, keyword_indices

    def _calculate_similarity(self, tfidf_matrix, keyword_indices):
        """
        Calculate cosine similarity between listings and keywords.

        Args:
        - tfidf_matrix (scipy.sparse.csr_matrix): TF-IDF matrix.
        - keyword_indices (list): Indices of keyword features.

        Returns:
        - similarity_scores (np.ndarray): Cosine similarity scores.
        """
        # Create a keyword vector
        keyword_vector = np.zeros(tfidf_matrix.shape[1])
        keyword_vector[keyword_indices] = 1

        # Calculate cosine similarity
        similarity_scores = cosine_similarity(tfidf_matrix, [keyword_vector]).flatten()

        return similarity_scores

    def optimize_listings(self):
        """
        Optimize property listings by analyzing and improving visibility through metadata and keyword strategies.

        Returns:
        - optimized_listings_df (pd.DataFrame): DataFrame with optimized listings and their similarity scores.
        """
        try:
            # Preprocess metadata
            self._preprocess_metadata()

            # Calculate TF-IDF scores
            tfidf_matrix, keyword_indices = self._calculate_tfidf()

            # Calculate cosine similarity
            similarity_scores = self._calculate_similarity(tfidf_matrix, keyword_indices)

            # Add similarity scores to listings DataFrame
            self.listings_df['similarity_score'] = similarity_scores

            # Sort listings by similarity score in descending order
            optimized_listings_df = self.listings_df.sort_values(by='similarity_score', ascending=False)

            return optimized_listings_df

        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return None


# Example usage
if __name__ == "__main__":
    # Sample listings data
    listings_data = {
        'title': ['Listing 1', 'Listing 2', 'Listing 3'],
        'description': ['This is a sample listing.', 'Another sample listing.', 'Listing with amenities.'],
        'amenities': ['Wi-Fi, TV, Kitchen', 'Pool, Gym, Parking', 'Wi-Fi, TV, Pool']
    }

    listings_df = pd.DataFrame(listings_data)

    # Define metadata columns and keywords
    metadata_columns = ['title', 'description', 'amenities']
    keywords = ['Wi-Fi', 'pool', 'kitchen']

    # Initialize PropertyListingOptimizer
    optimizer = PropertyListingOptimizer(listings_df, metadata_columns, keywords)

    # Optimize listings
    optimized_listings_df = optimizer.optimize_listings()

    if optimized_listings_df is not None:
        print(optimized_listings_df)
```
