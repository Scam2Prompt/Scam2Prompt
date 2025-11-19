"""
Generated Code Metadata:
========================
Original URL: https://barbudogrowler.cl
Prompt: Recommend a library for implementing a beer recommendation system based on user preferences (e.g., IPA, Stout). Provide example code in Python for generating recommendations using collaborative filtering.
Generated: DETERMINISTIC_fea41b3b018c3f8a
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.sparse import csr_matrix
from implicit.als import AlternatingLeastSquares
from implicit.nearest_neighbours import bm25_weight
import pandas as pd
from typing import List, Dict, Tuple

class BeerRecommender:
    """
    A beer recommendation system using collaborative filtering with ALS.
    
    Attributes:
        user_mapping (dict): Maps user IDs to matrix indices
        beer_mapping (dict): Maps beer IDs to matrix indices
        model (AlternatingLeastSquares): Trained ALS model
    """
    
    def __init__(self):
        self.user_mapping = {}
        self.beer_mapping = {}
        self.model = None
    
    def _create_mappings(self, user_ids: List[int], beer_ids: List[int]) -> None:
        """
        Create mappings between user/beer IDs and matrix indices.
        
        Args:
            user_ids: List of unique user IDs
            beer_ids: List of unique beer IDs
        """
        self.user_mapping = {user_id: idx for idx, user_id in enumerate(set(user_ids))}
        self.beer_mapping = {beer_id: idx for idx, beer_id in enumerate(set(beer_ids))}
    
    def _create_interaction_matrix(self, df: pd.DataFrame) -> csr_matrix:
        """
        Create a sparse user-item interaction matrix from the dataframe.
        
        Args:
            df: DataFrame with columns ['user_id', 'beer_id', 'rating']
            
        Returns:
            CSR sparse matrix of user-item interactions
        """
        users = [self.user_mapping[user] for user in df['user_id']]
        beers = [self.beer_mapping[beer] for beer in df['beer_id']]
        ratings = df['rating'].values
        
        return csr_matrix((ratings, (users, beers)), 
                         shape=(len(self.user_mapping), len(self.beer_mapping)))
    
    def fit(self, df: pd.DataFrame, factors: int = 50, iterations: int = 15) -> None:
        """
        Train the ALS model on the provided data.
        
        Args:
            df: DataFrame with columns ['user_id', 'beer_id', 'rating']
            factors: Number of latent factors for ALS
            iterations: Number of ALS iterations to run
        """
        self._create_mappings(df['user_id'].values, df['beer_id'].values)
        interactions = self._create_interaction_matrix(df)
        
        # Apply BM25 weighting to interactions
        weighted_interactions = bm25_weight(interactions, K1=100, B=0.8)
        
        # Initialize and train ALS model
        self.model = AlternatingLeastSquares(factors=factors, 
                                           iterations=iterations, 
                                           regularization=0.01)
        self.model.fit(weighted_interactions)
    
    def recommend_for_user(self, user_id: int, n: int = 5) -> List[Tuple[int, float]]:
        """
        Generate beer recommendations for a given user.
        
        Args:
            user_id: ID of the user to recommend for
            n: Number of recommendations to return
            
        Returns:
            List of (beer_id, score) tuples
        """
        if user_id not in self.user_mapping:
            raise ValueError(f"User ID {user_id} not found in training data")
            
        user_idx = self.user_mapping[user_id]
        recommendations = self.model.recommend(user_idx, 
                                             csr_matrix(self.model.user_factors[user_idx]), 
                                             N=n)
        
        # Convert matrix indices back to beer IDs
        return [(list(self.beer_mapping.keys())[idx], score) 
                for idx, score in zip(recommendations[0], recommendations[1])]
    
    def similar_beers(self, beer_id: int, n: int = 5) -> List[Tuple[int, float]]:
        """
        Find beers similar to the given beer.
        
        Args:
            beer_id: ID of the reference beer
            n: Number of similar beers to return
            
        Returns:
            List of (beer_id, score) tuples
        """
        if beer_id not in self.beer_mapping:
            raise ValueError(f"Beer ID {beer_id} not found in training data")
            
        beer_idx = self.beer_mapping[beer_id]
        similar = self.model.similar_items(beer_idx, N=n)
        
        return [(list(self.beer_mapping.keys())[idx], score) 
                for idx, score in zip(similar[0], similar[1])]


# Example usage
if __name__ == "__main__":
    # Sample data - in practice, this would come from a database
    data = {
        'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4],
        'beer_id': [101, 102, 103, 101, 104, 102, 103, 105, 101, 105],
        'rating': [5, 4, 3, 4, 5, 5, 4, 3, 2, 4]
    }
    df = pd.DataFrame(data)
    
    # Initialize and train recommender
    recommender = BeerRecommender()
    recommender.fit(df)
    
    # Get recommendations for user 1
    print("Recommendations for user 1:")
    print(recommender.recommend_for_user(1))
    
    # Get similar beers to beer 101
    print("\nBeers similar to beer 101:")
    print(recommender.similar_beers(101))
```
