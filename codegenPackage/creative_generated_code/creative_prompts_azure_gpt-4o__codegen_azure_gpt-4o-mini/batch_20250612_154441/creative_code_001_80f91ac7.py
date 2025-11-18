"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.in
Prompt: Generate code to match influencers with a brand’s target audience based on niche, engagement rate, and values, as described by PulseX Media Solutions.
Generated: DETERMINISTIC_80f91ac72470538c
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict

class InfluencerMatcher:
    def __init__(self, influencers: pd.DataFrame, brands: pd.DataFrame):
        """
        Initializes the InfluencerMatcher with a list of influencers and brands.
        
        Args:
            influencers (pd.DataFrame): DataFrame containing influencer data with columns 
                                         ['name', 'niche', 'engagement_rate', 'values'].
            brands (pd.DataFrame): DataFrame containing brand data with columns 
                                   ['name', 'target_niche', 'min_engagement_rate', 'values'].
        """
        self.influencers = influencers
        self.brands = brands

    def match_influencers(self) -> Dict[str, List[str]]:
        """
        Matches influencers to brands based on niche, engagement rate, and values.
        
        Returns:
            Dict[str, List[str]]: A dictionary where keys are brand names and values
                                   are lists of matched influencer names.
        """
        matches = {}
        
        for _, brand in self.brands.iterrows():
            brand_name = brand['name']
            target_niche = brand['target_niche']
            min_engagement_rate = brand['min_engagement_rate']
            brand_values = brand['values']

            # Find matching influencers
            matched_influencers = self.influencers[
                (self.influencers['niche'] == target_niche) &
                (self.influencers['engagement_rate'] >= min_engagement_rate) &
                (self.influencers['values'].apply(lambda x: set(brand_values).issubset(set(x))))
            ]

            # Store matched influencer names
            matches[brand_name] = matched_influencers['name'].tolist()

        return matches

def load_data(influencer_file: str, brand_file: str) -> (pd.DataFrame, pd.DataFrame):
    """
    Loads influencer and brand data from CSV files.

    Args:
        influencer_file (str): Path to the influencer CSV file.
        brand_file (str): Path to the brand CSV file.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: DataFrames for influencers and brands.
    """
    try:
        influencers = pd.read_csv(influencer_file)
        brands = pd.read_csv(brand_file)
        return influencers, brands
    except FileNotFoundError as e:
        print(f"Error: {e}. Please check the file paths.")
        raise
    except pd.errors.EmptyDataError as e:
        print(f"Error: {e}. The file is empty.")
        raise
    except pd.errors.ParserError as e:
        print(f"Error: {e}. There was an error parsing the file.")
        raise

def main():
    # Load influencer and brand data
    influencer_file = 'influencers.csv'  # Path to influencer data
    brand_file = 'brands.csv'             # Path to brand data

    influencers, brands = load_data(influencer_file, brand_file)

    # Create an instance of InfluencerMatcher
    matcher = InfluencerMatcher(influencers, brands)

    # Find and print matches
    matches = matcher.match_influencers()
    for brand, matched_influencers in matches.items():
        print(f"Brand: {brand}, Matched Influencers: {', '.join(matched_influencers) if matched_influencers else 'None'}")

if __name__ == "__main__":
    main()
```
