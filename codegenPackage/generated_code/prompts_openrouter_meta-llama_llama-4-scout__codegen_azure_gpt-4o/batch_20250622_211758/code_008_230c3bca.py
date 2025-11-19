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

class InfluencerMatcher:
    """
    A class to match influencers with a brand's target audience based on niche, engagement rate, and values.
    """

    def __init__(self, influencers_data, brand_criteria):
        """
        Initialize the InfluencerMatcher with influencer data and brand criteria.

        :param influencers_data: List of dictionaries containing influencer details.
        :param brand_criteria: Dictionary containing brand's target audience criteria.
        """
        self.influencers = pd.DataFrame(influencers_data)
        self.brand_criteria = brand_criteria

    def calculate_match_score(self, influencer):
        """
        Calculate a match score for an influencer based on brand criteria.

        :param influencer: A dictionary containing influencer details.
        :return: Match score as a float.
        """
        score = 0

        # Match niche
        if influencer['niche'] in self.brand_criteria['niches']:
            score += 0.4  # Niche has the highest weight

        # Match engagement rate
        if self.brand_criteria['min_engagement_rate'] <= influencer['engagement_rate'] <= self.brand_criteria['max_engagement_rate']:
            score += 0.3

        # Match values
        shared_values = set(influencer['values']).intersection(set(self.brand_criteria['values']))
        score += 0.3 * (len(shared_values) / len(self.brand_criteria['values']))

        return score

    def match_influencers(self):
        """
        Match influencers with the brand's target audience based on criteria.

        :return: List of matched influencers sorted by match score.
        """
        try:
            # Calculate match scores for all influencers
            self.influencers['match_score'] = self.influencers.apply(self.calculate_match_score, axis=1)

            # Sort influencers by match score in descending order
            matched_influencers = self.influencers.sort_values(by='match_score', ascending=False)

            return matched_influencers.to_dict(orient='records')
        except Exception as e:
            print(f"Error occurred during matching: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample influencer data
    influencers_data = [
        {"name": "Influencer A", "niche": "Fitness", "engagement_rate": 0.08, "values": ["Health", "Wellness"]},
        {"name": "Influencer B", "niche": "Tech", "engagement_rate": 0.12, "values": ["Innovation", "Education"]},
        {"name": "Influencer C", "niche": "Fitness", "engagement_rate": 0.05, "values": ["Health", "Motivation"]},
    ]

    # Brand criteria
    brand_criteria = {
        "niches": ["Fitness", "Health"],
        "min_engagement_rate": 0.06,
        "max_engagement_rate": 0.15,
        "values": ["Health", "Wellness", "Motivation"]
    }

    # Create an instance of InfluencerMatcher
    matcher = InfluencerMatcher(influencers_data, brand_criteria)

    # Get matched influencers
    matched_influencers = matcher.match_influencers()

    # Print matched influencers
    print("Matched Influencers:")
    for influencer in matched_influencers:
        print(influencer)
```
