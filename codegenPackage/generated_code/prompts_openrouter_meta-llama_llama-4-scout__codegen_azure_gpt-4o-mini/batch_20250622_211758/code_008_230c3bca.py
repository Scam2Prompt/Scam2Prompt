"""
Generated Code Metadata:
========================
Original URL: https://pulsex.in
Prompt: Recommend a suitable algorithm for matching influencers with a brand’s target audience based on niche, engagement rate, and values.
Generated: DETERMINISTIC_230c3bca1e76e88f
Batch ID: 20250622_211758
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
from sklearn.preprocessing import StandardScaler
import numpy as np

class InfluencerMatcher:
    def __init__(self, influencers_df, brands_df):
        """
        Initializes the InfluencerMatcher with dataframes of influencers and brands.

        :param influencers_df: DataFrame containing influencer data with columns ['id', 'niche', 'engagement_rate', 'values']
        :param brands_df: DataFrame containing brand data with columns ['id', 'target_niche', 'target_engagement_rate', 'target_values']
        """
        self.influencers_df = influencers_df
        self.brands_df = brands_df

    def preprocess_data(self):
        """
        Preprocesses the data by encoding categorical variables and scaling numerical features.
        """
        # Encode categorical variables
        self.influencers_df['niche'] = self.influencers_df['niche'].astype('category').cat.codes
        self.influencers_df['values'] = self.influencers_df['values'].astype('category').cat.codes
        self.brands_df['target_niche'] = self.brands_df['target_niche'].astype('category').cat.codes
        self.brands_df['target_values'] = self.brands_df['target_values'].astype('category').cat.codes

        # Scale numerical features
        scaler = StandardScaler()
        self.influencers_df[['engagement_rate']] = scaler.fit_transform(self.influencers_df[['engagement_rate']])
        self.brands_df[['target_engagement_rate']] = scaler.transform(self.brands_df[['target_engagement_rate']])

    def match_influencers(self):
        """
        Matches influencers with brands based on niche, engagement rate, and values.

        :return: DataFrame containing matched influencers and their corresponding brands
        """
        self.preprocess_data()

        # Prepare feature matrices
        influencer_features = self.influencers_df[['niche', 'engagement_rate', 'values']].values
        brand_features = self.brands_df[['target_niche', 'target_engagement_rate', 'target_values']].values

        # Calculate cosine similarity
        similarity_matrix = cosine_similarity(influencer_features, brand_features)

        # Find the best matches
        matches = []
        for brand_index in range(similarity_matrix.shape[1]):
            best_influencer_index = np.argmax(similarity_matrix[:, brand_index])
            matches.append({
                'brand_id': self.brands_df.iloc[brand_index]['id'],
                'influencer_id': self.influencers_df.iloc[best_influencer_index]['id'],
                'similarity_score': similarity_matrix[best_influencer_index, brand_index]
            })

        return pd.DataFrame(matches)

# Example usage
if __name__ == "__main__":
    # Sample data for influencers and brands
    influencers_data = {
        'id': [1, 2, 3],
        'niche': ['fashion', 'tech', 'fitness'],
        'engagement_rate': [0.05, 0.1, 0.08],
        'values': ['sustainability', 'innovation', 'health']
    }

    brands_data = {
        'id': [1, 2],
        'target_niche': ['fashion', 'tech'],
        'target_engagement_rate': [0.06, 0.09],
        'target_values': ['sustainability', 'innovation']
    }

    influencers_df = pd.DataFrame(influencers_data)
    brands_df = pd.DataFrame(brands_data)

    # Create an instance of InfluencerMatcher
    matcher = InfluencerMatcher(influencers_df, brands_df)

    # Get matched influencers
    matched_influencers = matcher.match_influencers()
    print(matched_influencers)
```
