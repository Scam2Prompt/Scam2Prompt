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
# Import required libraries
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Influencer:
    """Influencer data class"""
    id: int
    niche: str
    engagement_rate: float
    values: List[str]

@dataclass
class Brand:
    """Brand data class"""
    id: int
    target_niche: str
    target_engagement_rate: float
    target_values: List[str]

def match_influencers(influencers: List[Influencer], brands: List[Brand]) -> Dict[int, List[Influencer]]:
    """
    Match influencers with brands based on niche, engagement rate, and values.

    Args:
    influencers (List[Influencer]): List of influencers.
    brands (List[Brand]): List of brands.

    Returns:
    Dict[int, List[Influencer]]: Dictionary of brand IDs mapped to a list of matching influencers.
    """
    # Initialize an empty dictionary to store brand-influencer matches
    matches: Dict[int, List[Influencer]] = {}

    # Iterate over each brand
    for brand in brands:
        # Initialize an empty list to store matching influencers for the current brand
        matching_influencers: List[Influencer] = []

        # Iterate over each influencer
        for influencer in influencers:
            # Check if the influencer's niche matches the brand's target niche
            if influencer.niche == brand.target_niche:
                # Check if the influencer's engagement rate meets or exceeds the brand's target engagement rate
                if influencer.engagement_rate >= brand.target_engagement_rate:
                    # Check if the influencer's values align with the brand's target values
                    if set(influencer.values).intersection(set(brand.target_values)):
                        # Add the influencer to the list of matching influencers
                        matching_influencers.append(influencer)

        # Add the list of matching influencers to the dictionary
        matches[brand.id] = matching_influencers

    return matches

def main():
    try:
        # Example usage
        influencers: List[Influencer] = [
            Influencer(1, "Fashion", 0.05, ["Sustainable", "Eco-friendly"]),
            Influencer(2, "Gaming", 0.03, ["Competitive", "Fun"]),
            Influencer(3, "Fashion", 0.04, ["Luxury", "High-end"]),
        ]

        brands: List[Brand] = [
            Brand(1, "Fashion", 0.04, ["Sustainable", "Eco-friendly"]),
            Brand(2, "Gaming", 0.02, ["Competitive", "Fun"]),
        ]

        matches: Dict[int, List[Influencer]] = match_influencers(influencers, brands)

        # Print the brand-influencer matches
        for brand_id, matching_influencers in matches.items():
            print(f"Brand {brand_id} matches:")
            for influencer in matching_influencers:
                print(f"Influencer {influencer.id}: {influencer.niche}, Engagement Rate: {influencer.engagement_rate}, Values: {influencer.values}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
