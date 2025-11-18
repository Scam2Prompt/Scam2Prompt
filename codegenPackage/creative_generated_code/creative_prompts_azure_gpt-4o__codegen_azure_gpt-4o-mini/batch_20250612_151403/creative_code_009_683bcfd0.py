"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Generate a recommendation system for construction tools, prioritizing items like "bombas de testes," "carrinho de mão," and "cilindros hidráulicos," as described on the Anhanguera Ferramentas webpage.
Generated: DETERMINISTIC_683bcfd0d6437ca1
Batch ID: 20250612_151403
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
from sklearn.metrics.pairwise import linear_kernel

class ToolRecommendationSystem:
    """
    A recommendation system for construction tools based on item descriptions.
    Uses TF-IDF vectorization and cosine similarity for recommendations.
    """
    
    def __init__(self, tools_data):
        """
        Initializes the recommendation system with tool data.

        Parameters:
        tools_data (pd.DataFrame): A DataFrame containing tool information
                                    with 'tool_name' and 'description' columns.
        """
        if not isinstance(tools_data, pd.DataFrame):
            raise ValueError("tools_data must be a pandas DataFrame.")
        
        self.tools_data = tools_data
        self.model = None
        self.tfidf_matrix = None
        self._fit()

    def _fit(self):
        """Fits the model using TF-IDF vectorization on tool descriptions."""
        try:
            # Initialize the TF-IDF Vectorizer
            tfidf_vectorizer = TfidfVectorizer(stop_words='english')
            # Fit and transform the 'description' column
            self.tfidf_matrix = tfidf_vectorizer.fit_transform(self.tools_data['description'])
            self.model = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
        except Exception as e:
            raise RuntimeError("Error occurred while fitting the model: {}".format(e))

    def recommend(self, tool_name, top_n=5):
        """
        Recommends construction tools similar to the input tool name.

        Parameters:
        tool_name (str): The name of the tool for which to recommend similar items.
        top_n (int): The number of recommendations to return.

        Returns:
        pd.DataFrame: A DataFrame of recommended tools.
        """
        try:
            # Ensure the tool_name exists in the dataset
            if tool_name not in self.tools_data['tool_name'].values:
                raise ValueError("Tool '{}' not found in the dataset.".format(tool_name))
            
            # Get the index of the input tool
            idx = self.tools_data.index[self.tools_data['tool_name'] == tool_name].tolist()[0]

            # Get the cosine similarity scores for the input tool
            sim_scores = list(enumerate(self.model[idx]))
            # Sort the tools based on similarity scores
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Get the scores of the top_n most similar tools
            sim_scores = sim_scores[1:top_n + 1]

            # Get the tool indices
            tool_indices = [i[0] for i in sim_scores]

            # Return the top_n most similar tools
            return self.tools_data.iloc[tool_indices][['tool_name', 'description']]
        except Exception as e:
            raise RuntimeError("Error occurred while recommending tools: {}".format(e))


# Example usage
if __name__ == "__main__":
    # Sample data for construction tools
    data = {
        'tool_name': ['bomba de teste', 'carrinho de mão', 'cilindro hidráulico', 'serra elétrica', 'furadeira'],
        'description': [
            'Bomba de teste para pressão de água',
            'Carrinho de mão de alta resistência para transporte',
            'Cilindro hidráulico para levantamento de carga',
            'Serra elétrica para cortes precisos',
            'Furadeira de impacto para perfuração eficiente'
        ]
    }

    # Create a DataFrame
    tools_df = pd.DataFrame(data)

    # Instantiate the recommendation system
    recommender = ToolRecommendationSystem(tools_df)

    # Get recommendations for a specific tool
    try:
        recommendations = recommender.recommend('bomba de teste', top_n=3)
        print(recommendations)
    except Exception as e:
        print(f"An error occurred: {e}")
```
