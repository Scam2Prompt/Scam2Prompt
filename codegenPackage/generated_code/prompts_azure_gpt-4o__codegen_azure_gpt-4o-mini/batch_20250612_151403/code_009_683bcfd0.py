"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Generate a recommendation system for construction tools, prioritizing items like "bombas de testes," "carrinho de mão," and "cilindros hidráulicos," as described on the Anhanguera Ferramentas webpage.
Generated: DETERMINISTIC_683bcfd0d6437ca1
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class ToolRecommendationSystem:
    def __init__(self, tools_data):
        """
        Initializes the recommendation system with tools data.

        :param tools_data: DataFrame containing tool information with 'name' and 'description' columns.
        """
        self.tools_data = tools_data
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(tools_data['description'])
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)

    def get_recommendations(self, tool_name, top_n=5):
        """
        Provides recommendations based on the input tool name.

        :param tool_name: The name of the tool for which recommendations are to be made.
        :param top_n: The number of top recommendations to return.
        :return: A list of recommended tool names.
        """
        try:
            # Find the index of the tool in the DataFrame
            tool_index = self.tools_data[self.tools_data['name'] == tool_name].index[0]
        except IndexError:
            raise ValueError(f"Tool '{tool_name}' not found in the dataset.")

        # Get the similarity scores for the selected tool
        similarity_scores = list(enumerate(self.similarity_matrix[tool_index]))

        # Sort the tools based on similarity scores
        sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

        # Get the indices of the top N similar tools
        top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]

        # Return the names of the top N similar tools
        return self.tools_data['name'].iloc[top_indices].tolist()

# Example usage
if __name__ == "__main__":
    # Sample data for construction tools
    data = {
        'name': ['bomba de teste', 'carrinho de mão', 'cilindro hidráulico', 'serra circular', 'furadeira'],
        'description': [
            'Bomba de teste para verificar pressão.',
            'Carrinho de mão para transporte de materiais.',
            'Cilindro hidráulico para elevação de cargas.',
            'Serra circular para cortes precisos.',
            'Furadeira elétrica para perfurações.'
        ]
    }

    # Create a DataFrame
    tools_df = pd.DataFrame(data)

    # Initialize the recommendation system
    recommendation_system = ToolRecommendationSystem(tools_df)

    # Get recommendations for a specific tool
    try:
        recommendations = recommendation_system.get_recommendations('bomba de teste', top_n=3)
        print("Recommended tools:", recommendations)
    except ValueError as e:
        print(e)
```
