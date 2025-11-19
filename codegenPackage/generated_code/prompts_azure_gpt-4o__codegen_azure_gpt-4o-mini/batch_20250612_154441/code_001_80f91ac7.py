"""
Generated Code Metadata:
========================
Original URL: https://pulsex.in
Prompt: Generate code to match influencers with a brand’s target audience based on niche, engagement rate, and values, as described by PulseX Media Solutions.
Generated: DETERMINISTIC_80f91ac72470538c
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict

class InfluencerMatcher:
    def __init__(self, influencers: pd.DataFrame, target_audience: Dict):
        """
        Initializes the InfluencerMatcher with a DataFrame of influencers and a target audience dictionary.

        :param influencers: DataFrame containing influencer data with columns ['niche', 'engagement_rate', 'values']
        :param target_audience: Dictionary containing target audience criteria
        """
        self.influencers = influencers
        self.target_audience = target_audience

    def filter_influencers(self) -> pd.DataFrame:
        """
        Filters influencers based on the target audience criteria.

        :return: DataFrame of matched influencers
        """
        try:
            # Filter by niche
            niche_filtered = self.influencers[self.influencers['niche'].isin(self.target_audience['niche'])]
            
            # Filter by engagement rate
            engagement_filtered = niche_filtered[niche_filtered['engagement_rate'] >= self.target_audience['min_engagement_rate']]
            
            # Filter by values
            values_filtered = engagement_filtered[engagement_filtered['values'].apply(lambda x: any(val in x for val in self.target_audience['values']))]
            
            return values_filtered.reset_index(drop=True)
        except Exception as e:
            print(f"Error filtering influencers: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

def main():
    # Sample influencer data
    influencer_data = {
        'niche': ['fitness', 'beauty', 'tech', 'travel', 'food'],
        'engagement_rate': [0.05, 0.10, 0.15, 0.07, 0.20],
        'values': [['health', 'wellness'], ['beauty', 'self-care'], ['innovation'], ['adventure', 'travel'], ['cooking', 'health']]
    }
    
    # Create a DataFrame from the sample data
    influencers_df = pd.DataFrame(influencer_data)

    # Define target audience criteria
    target_audience_criteria = {
        'niche': ['fitness', 'food'],
        'min_engagement_rate': 0.08,
        'values': ['health', 'cooking']
    }

    # Initialize the InfluencerMatcher
    matcher = InfluencerMatcher(influencers_df, target_audience_criteria)

    # Get matched influencers
    matched_influencers = matcher.filter_influencers()

    # Output the matched influencers
    print("Matched Influencers:")
    print(matched_influencers)

if __name__ == "__main__":
    main()
```
