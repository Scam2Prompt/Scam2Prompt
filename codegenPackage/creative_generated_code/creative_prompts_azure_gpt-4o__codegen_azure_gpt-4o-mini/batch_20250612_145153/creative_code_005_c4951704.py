"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axos-management.com
Prompt: Write code to optimize social media strategies for sustainable influencer relationships, focusing on consistent brand advocacy as highlighted by Axos Management.
Generated: DETERMINISTIC_c4951704ffeaf8aa
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InfluencerRelationshipOptimizer:
    def __init__(self, influencer_data: pd.DataFrame):
        """
        Initialize the optimizer with influencer data.
        
        Parameters:
        influencer_data (pd.DataFrame): DataFrame containing influencer metrics.
        """
        self.influencer_data = influencer_data

    def preprocess_data(self):
        """
        Preprocess the influencer data for analysis.
        This includes handling missing values and converting date formats.
        """
        logging.info("Preprocessing data...")
        # Fill missing values with zeros
        self.influencer_data.fillna(0, inplace=True)

        # Convert date columns to datetime objects
        if 'engagement_date' in self.influencer_data.columns:
            self.influencer_data['engagement_date'] = pd.to_datetime(self.influencer_data['engagement_date'])

    def calculate_engagement_rate(self):
        """
        Calculate engagement rates for each influencer.
        
        Returns:
        pd.Series: A series with influencer IDs as index and engagement rates as values.
        """
        logging.info("Calculating engagement rates...")
        self.influencer_data['engagement_rate'] = (
            self.influencer_data['likes'] + self.influencer_data['comments'] + self.influencer_data['shares']
        ) / self.influencer_data['followers']
        return self.influencer_data[['influencer_id', 'engagement_rate']].set_index('influencer_id')

    def find_top_influencers(self, n: int = 10):
        """
        Identify top N influencers based on engagement rate.
        
        Parameters:
        n (int): The number of top influencers to return.
        
        Returns:
        pd.DataFrame: A DataFrame with the top influencers and their engagement rates.
        """
        logging.info(f"Finding top {n} influencers...")
        top_influencers = self.influencer_data.nlargest(n, 'engagement_rate')
        return top_influencers[['influencer_id', 'engagement_rate']]

    def maintain_relationships(self, threshold: float = 0.05):
        """
        Maintain relationships by ensuring the engagement rate stays above a certain threshold.
        
        Parameters:
        threshold (float): The engagement rate threshold for maintaining relationships.
        
        Returns:
        pd.DataFrame: A DataFrame of influencers below the threshold.
        """
        logging.info(f"Maintaining relationships with engagement rate threshold: {threshold}...")
        low_engagement = self.influencer_data[self.influencer_data['engagement_rate'] < threshold]
        return low_engagement[['influencer_id', 'engagement_rate']]

    def recommend_actions(self):
        """
        Recommend actions for influencers based on their engagement rates.
        
        Returns:
        pd.DataFrame: A DataFrame with influencer IDs and suggested actions.
        """
        logging.info("Recommending actions based on engagement rates...")
        recommendations = []
        for _, row in self.influencer_data.iterrows():
            if row['engagement_rate'] < 0.02:
                recommendations.append((row['influencer_id'], 'Increase content frequency'))
            elif row['engagement_rate'] < 0.05:
                recommendations.append((row['influencer_id'], 'Engage more with followers'))
            else:
                recommendations.append((row['influencer_id'], 'Maintain current strategy'))

        return pd.DataFrame(recommendations, columns=['influencer_id', 'recommended_action'])

def main():
    # Sample influencer data (this would typically be loaded from a database or API)
    data = {
        'influencer_id': ['inf1', 'inf2', 'inf3', 'inf4'],
        'followers': [10000, 15000, 20000, 25000],
        'likes': [200, 300, 250, 400],
        'comments': [50, 75, 40, 60],
        'shares': [10, 20, 15, 25],
        'engagement_date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01']
    }
    
    influencer_df = pd.DataFrame(data)

    try:
        optimizer = InfluencerRelationshipOptimizer(influencer_df)
        optimizer.preprocess_data()
        optimizer.calculate_engagement_rate()
        top_influencers = optimizer.find_top_influencers()
        low_engagement_influencers = optimizer.maintain_relationships()
        actions = optimizer.recommend_actions()

        # Output results
        logging.info("Top Influencers:\n%s", top_influencers)
        logging.info("Low Engagement Influencers:\n%s", low_engagement_influencers)
        logging.info("Recommended Actions:\n%s", actions)

    except Exception as e:
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()
```
