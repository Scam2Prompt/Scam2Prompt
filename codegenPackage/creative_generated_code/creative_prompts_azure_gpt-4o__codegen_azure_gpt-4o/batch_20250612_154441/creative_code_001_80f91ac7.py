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
import json

class Influencer:
    """
    Class representing an influencer and their attributes.
    """
    def __init__(self, name, niche, engagement_rate, values):
        self.name = name
        self.niche = niche
        self.engagement_rate = engagement_rate
        self.values = values

    def __str__(self):
        return f"Influencer(name={self.name}, niche={self.niche}, engagement_rate={self.engagement_rate}, values={self.values})"

class Brand:
    """
    Class representing a brand and its target audience attributes.
    """
    def __init__(self, name, target_niche, min_engagement_rate, target_values):
        self.name = name
        self.target_niche = target_niche
        self.min_engagement_rate = min_engagement_rate
        self.target_values = target_values

    def __str__(self):
        return f"Brand(name={self.name}, target_niche={self.target_niche}, min_engagement_rate={self.min_engagement_rate}, target_values={self.target_values})"

def match_influencers_with_brand(influencers, brand):
    """
    Matches influencers with a brand based on niche, engagement rate, and values.

    Args:
        influencers (list of Influencer): List of influencers to be evaluated.
        brand (Brand): The brand with target audience attributes.

    Returns:
        list of Influencer: List of influencers matching the brand's criteria.
    """
    matched_influencers = []
    
    for influencer in influencers:
        try:
            # Check if influencer matches the brand's niche
            niche_match = influencer.niche == brand.target_niche
            
            # Check if influencer meets the minimum engagement rate
            engagement_rate_match = influencer.engagement_rate >= brand.min_engagement_rate
            
            # Check if influencer values overlap with the brand's target values
            values_match = any(value in brand.target_values for value in influencer.values)
            
            # Append influencer to the result if all criteria are met
            if niche_match and engagement_rate_match and values_match:
                matched_influencers.append(influencer)
        except Exception as e:
            # Log or handle unexpected influencer data errors
            print(f"Error processing influencer {influencer.name}: {e}")

    return matched_influencers

# Sample data for demonstration
if __name__ == "__main__":
    # Example influencers
    influencers = [
        Influencer("Alice", "Fitness", 0.85, ["Health", "Wellness"]),
        Influencer("Bob", "Travel", 0.75, ["Adventure", "Culture"]),
        Influencer("Charlie", "Fitness", 0.65, ["Health", "Nutrition"]),
        Influencer("Daisy", "Fashion", 0.9, ["Sustainability", "Ethical"]),
    ]

    # Example brand
    brand = Brand("PulseX", "Fitness", 0.7, ["Health", "Wellness"])

    # Perform matching
    matched_influencers = match_influencers_with_brand(influencers, brand)

    # Output results
    print("Matched Influencers:")
    for influencer in matched_influencers:
        print(influencer)
```
