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
import heapq
from typing import List, Dict, Tuple

class Influencer:
    """
    Represents an influencer with relevant attributes for brand matching.
    """
    def __init__(self, name: str, niche: str, engagement_rate: float, values: List[str]):
        self.name = name
        self.niche = niche
        self.engagement_rate = engagement_rate
        self.values = values

class Brand:
    """
    Represents a brand with target audience criteria.
    """
    def __init__(self, name: str, target_niche: str, min_engagement: float, desired_values: List[str]):
        self.name = name
        self.target_niche = target_niche
        self.min_engagement = min_engagement
        self.desired_values = desired_values

def match_influencers_to_brand(brand: Brand, influencers: List[Influencer], top_n: int = 5) -> List[Tuple[Influencer, float]]:
    """
    Matches influencers to a brand based on niche, engagement rate, and values.
    Returns top_n influencers sorted by a weighted match score.

    Args:
        brand: Brand object with target audience criteria.
        influencers: List of Influencer objects to match against.
        top_n: Number of top matches to return. Defaults to 5.

    Returns:
        List of tuples containing matched Influencer and their match score, sorted by score.
    """
    if not influencers:
        raise ValueError("Influencers list cannot be empty.")
    
    matched_influencers = []

    for influencer in influencers:
        # Skip if niche doesn't match
        if influencer.niche.lower() != brand.target_niche.lower():
            continue
        
        # Skip if engagement rate is below threshold
        if influencer.engagement_rate < brand.min_engagement:
            continue
        
        # Calculate values match score (percentage of shared values)
        shared_values = set(influencer.values) & set(brand.desired_values)
        values_score = len(shared_values) / len(brand.desired_values) if brand.desired_values else 0
        
        # Calculate weighted match score (50% engagement, 50% values)
        engagement_weight = 0.5
        values_weight = 0.5
        match_score = (influencer.engagement_rate * engagement_weight) + (values_score * values_weight)
        
        matched_influencers.append((influencer, match_score))
    
    # Return top_n matches sorted by score (descending)
    top_matches = heapq.nlargest(top_n, matched_influencers, key=lambda x: x[1])
    return top_matches

# Example usage
if __name__ == "__main__":
    # Sample brand
    brand = Brand(
        name="EcoFriendly Apparel",
        target_niche="sustainable fashion",
        min_engagement=3.5,
        desired_values=["sustainability", "ethical production", "vegan"]
    )

    # Sample influencers
    influencers = [
        Influencer(
            name="EcoWarrior",
            niche="sustainable fashion",
            engagement_rate=4.2,
            values=["sustainability", "ethical production", "vegan"]
        ),
        Influencer(
            name="GreenLife",
            niche="sustainable fashion",
            engagement_rate=3.8,
            values=["sustainability", "zero waste"]
        ),
        Influencer(
            name="Fashionista",
            niche="luxury fashion",
            engagement_rate=5.0,
            values=["luxury", "exclusivity"]
        )
    ]

    try:
        matches = match_influencers_to_brand(brand, influencers)
        print(f"Top matches for {brand.name}:")
        for influencer, score in matches:
            print(f"- {influencer.name}: Score {score:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
