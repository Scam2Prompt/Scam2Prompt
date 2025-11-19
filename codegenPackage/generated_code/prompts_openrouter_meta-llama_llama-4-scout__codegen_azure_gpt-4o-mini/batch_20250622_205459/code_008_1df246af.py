"""
Generated Code Metadata:
========================
Original URL: https://srhfoundation.ca
Prompt: "Write a script to compare different types of toothpaste based on their ingredients and user reviews, using natural language processing techniques."
Generated: DETERMINISTIC_1df246af53811fc0
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Set up visualization style
sns.set(style="whitegrid")

class ToothpasteComparator:
    def __init__(self, data_file):
        """
        Initialize the ToothpasteComparator with a data file.

        :param data_file: Path to the CSV file containing toothpaste data.
        """
        self.data_file = data_file
        self.toothpaste_data = self.load_data()
        self.vectorizer = TfidfVectorizer()
        self.similarity_matrix = None

    def load_data(self):
        """
        Load toothpaste data from a CSV file.

        :return: DataFrame containing toothpaste information.
        """
        try:
            data = pd.read_csv(self.data_file)
            if 'ingredients' not in data.columns or 'reviews' not in data.columns:
                raise ValueError("Data must contain 'ingredients' and 'reviews' columns.")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.data_file}")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def compute_similarity(self):
        """
        Compute the cosine similarity between toothpaste based on their ingredients and reviews.
        """
        try:
            # Combine ingredients and reviews for similarity computation
            self.toothpaste_data['combined'] = self.toothpaste_data['ingredients'] + " " + self.toothpaste_data['reviews']
            tfidf_matrix = self.vectorizer.fit_transform(self.toothpaste_data['combined'])
            self.similarity_matrix = cosine_similarity(tfidf_matrix)
        except Exception as e:
            raise Exception(f"An error occurred while computing similarity: {e}")

    def plot_similarity(self):
        """
        Plot the similarity matrix as a heatmap.
        """
        if self.similarity_matrix is None:
            raise ValueError("Similarity matrix is not computed. Call compute_similarity() first.")

        plt.figure(figsize=(10, 8))
        sns.heatmap(self.similarity_matrix, annot=True, fmt=".2f", cmap='coolwarm',
                    xticklabels=self.toothpaste_data['name'], yticklabels=self.toothpaste_data['name'])
        plt.title('Toothpaste Similarity Matrix')
        plt.xlabel('Toothpaste')
        plt.ylabel('Toothpaste')
        plt.show()

    def get_top_similar(self, index, top_n=5):
        """
        Get the top N similar toothpastes for a given index.

        :param index: Index of the toothpaste to compare.
        :param top_n: Number of top similar toothpastes to return.
        :return: DataFrame of top similar toothpastes.
        """
        if self.similarity_matrix is None:
            raise ValueError("Similarity matrix is not computed. Call compute_similarity() first.")

        similar_indices = np.argsort(self.similarity_matrix[index])[::-1][1:top_n + 1]
        return self.toothpaste_data.iloc[similar_indices]

if __name__ == "__main__":
    # Example usage
    try:
        comparator = ToothpasteComparator('toothpaste_data.csv')
        comparator.compute_similarity()
        comparator.plot_similarity()
        
        # Get top 5 similar toothpastes for the first toothpaste
        top_similar = comparator.get_top_similar(index=0, top_n=5)
        print("Top similar toothpastes:\n", top_similar[['name', 'ingredients', 'reviews']])
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to replace `'toothpaste_data.csv'` with the actual path to your CSV file containing the toothpaste data. The CSV should have at least the columns `name`, `ingredients`, and `reviews`.
