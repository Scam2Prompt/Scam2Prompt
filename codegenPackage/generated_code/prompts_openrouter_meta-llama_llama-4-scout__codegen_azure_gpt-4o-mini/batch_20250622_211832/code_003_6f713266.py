"""
Generated Code Metadata:
========================
Original URL: https://norwegianget.net
Prompt: "Create a Python script to build a simple novel recommendation system based on genres and reader preferences, inspired by the variety of novels listed on NorwegianGet."
Generated: DETERMINISTIC_6f71326684b726de
Batch ID: 20250622_211832
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

class NovelRecommendationSystem:
    def __init__(self, novels_data):
        """
        Initializes the recommendation system with a DataFrame of novels.

        :param novels_data: DataFrame containing novel information with 'title', 'genre', and 'description' columns.
        """
        self.novels_data = novels_data
        self.tfidf_matrix = None
        self.cosine_sim = None
        self._fit()

    def _fit(self):
        """
        Fits the TF-IDF vectorizer to the novel descriptions and computes the cosine similarity matrix.
        """
        # Create TF-IDF vectorizer
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        
        # Fit and transform the descriptions
        self.tfidf_matrix = tfidf_vectorizer.fit_transform(self.novels_data['description'])
        
        # Compute cosine similarity matrix
        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)

    def recommend(self, title, num_recommendations=5):
        """
        Recommends novels based on the given title.

        :param title: The title of the novel to base recommendations on.
        :param num_recommendations: The number of recommendations to return.
        :return: A list of recommended novel titles.
        """
        try:
            # Get the index of the novel that matches the title
            idx = self.novels_data.index[self.novels_data['title'] == title].tolist()[0]
        except IndexError:
            raise ValueError(f"Novel titled '{title}' not found in the database.")

        # Get the pairwise similarity scores of all novels with that novel
        sim_scores = list(enumerate(self.cosine_sim[idx]))

        # Sort the novels based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the most similar novels
        sim_scores = sim_scores[1:num_recommendations + 1]

        # Get the novel indices
        novel_indices = [i[0] for i in sim_scores]

        # Return the top recommended novels
        return self.novels_data['title'].iloc[novel_indices].tolist()

def load_novels_data(file_path):
    """
    Loads novels data from a CSV file.

    :param file_path: Path to the CSV file containing novel data.
    :return: DataFrame containing the novels data.
    """
    try:
        novels_data = pd.read_csv(file_path)
        if not all(col in novels_data.columns for col in ['title', 'genre', 'description']):
            raise ValueError("CSV must contain 'title', 'genre', and 'description' columns.")
        return novels_data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The provided CSV file is empty.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the data: {e}")

if __name__ == "__main__":
    # Load novels data from a CSV file
    file_path = 'novels.csv'  # Update this path to your CSV file
    novels_data = load_novels_data(file_path)

    # Create the recommendation system
    recommender = NovelRecommendationSystem(novels_data)

    # Example usage: Get recommendations for a specific novel
    try:
        title_to_recommend = "The Great Gatsby"  # Change this to a title in your dataset
        recommendations = recommender.recommend(title_to_recommend)
        print(f"Recommendations for '{title_to_recommend}':")
        for rec in recommendations:
            print(f"- {rec}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occurred: {e}")
```
