"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.in
Prompt: Create a script to automate influencer selection for campaigns based on engagement metrics and audience alignment, inspired by PulseX Media's FAQ section.
Generated: DETERMINISTIC_6fc799d69701f389
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

class InfluencerSelector:
    """
    A class to automate influencer selection for campaigns based on engagement metrics
    and audience alignment.

    Attributes:
        influencers_df (pd.DataFrame): DataFrame containing influencer data.
    """

    def __init__(self, influencers_data):
        """
        Initializes the InfluencerSelector object.

        Args:
            influencers_data (list of dicts): List of dictionaries containing influencer data.
                                              Each dictionary must include:
                                              'name', 'engagement_rate', 'audience_demographics'.
        """
        self.influencers_df = pd.DataFrame(influencers_data)

    def filter_influencers(self, min_engagement_rate=5.0, required_demographics=None):
        """
        Filters influencers based on engagement rate and audience demographics.

        Args:
            min_engagement_rate (float): Minimum engagement rate required for selection.
            required_demographics (list of str): List of required audience demographics.

        Returns:
            pd.DataFrame: Filtered DataFrame of influencers meeting the criteria.
        """
        try:
            # Filter based on engagement rate
            filtered_df = self.influencers_df[self.influencers_df['engagement_rate'] >= min_engagement_rate]

            # Filter based on audience demographics (if provided)
            if required_demographics:
                filtered_df = filtered_df[
                    filtered_df['audience_demographics'].apply(
                        lambda audience: any(demo in audience for demo in required_demographics)
                    )
                ]

            return filtered_df
        except KeyError as e:
            raise ValueError(f"Missing required column in influencers data: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred during filtering: {e}")

    def rank_influencers(self, filtered_df):
        """
        Ranks influencers by engagement rate in descending order.

        Args:
            filtered_df (pd.DataFrame): DataFrame of filtered influencers.

        Returns:
            pd.DataFrame: Ranked DataFrame of influencers.
        """
        try:
            return filtered_df.sort_values(by='engagement_rate', ascending=False).reset_index(drop=True)
        except KeyError as e:
            raise ValueError(f"Missing required column for ranking: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred during ranking: {e}")


# Example Usage
if __name__ == "__main__":
    # Sample influencer data
    influencers_data = [
        {"name": "Influencer A", "engagement_rate": 7.5, "audience_demographics": ["tech", "gaming"]},
        {"name": "Influencer B", "engagement_rate": 4.3, "audience_demographics": ["fashion", "lifestyle"]},
        {"name": "Influencer C", "engagement_rate": 8.9, "audience_demographics": ["gaming", "travel"]},
        {"name": "Influencer D", "engagement_rate": 5.1, "audience_demographics": ["tech", "education"]},
    ]

    # Initialize selector
    selector = InfluencerSelector(influencers_data)

    # Filter influencers
    filtered_influencers = selector.filter_influencers(
        min_engagement_rate=5.0, 
        required_demographics=["tech", "gaming"]
    )

    # Rank influencers
    ranked_influencers = selector.rank_influencers(filtered_influencers)

    # Display results
    print("Filtered and Ranked Influencers:")
    print(ranked_influencers)
```

This script automates influencer selection for campaigns based on engagement metrics and audience alignment. It uses pandas for data manipulation, includes error handling, and follows best practices for readability and maintainability.
