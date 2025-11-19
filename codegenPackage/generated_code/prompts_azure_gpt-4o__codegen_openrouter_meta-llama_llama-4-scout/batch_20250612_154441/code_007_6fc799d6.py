"""
Generated Code Metadata:
========================
Original URL: https://pulsex.in
Prompt: Create a script to automate influencer selection for campaigns based on engagement metrics and audience alignment, inspired by PulseX Media's FAQ section.
Generated: DETERMINISTIC_6fc799d69701f389
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# influencer_selector.py

import pandas as pd

class Influencer:
    """Represents an influencer with their metrics and audience data."""

    def __init__(self, id, engagement_rate, audience_size, audience_demographics):
        """
        Initializes an Influencer object.

        Args:
            id (str): Unique identifier for the influencer.
            engagement_rate (float): Engagement rate of the influencer.
            audience_size (int): Size of the influencer's audience.
            audience_demographics (dict): Demographics of the influencer's audience.
        """
        self.id = id
        self.engagement_rate = engagement_rate
        self.audience_size = audience_size
        self.audience_demographics = audience_demographics

class Campaign:
    """Represents a campaign with its target audience and engagement requirements."""

    def __init__(self, id, target_audience_demographics, min_engagement_rate, min_audience_size):
        """
        Initializes a Campaign object.

        Args:
            id (str): Unique identifier for the campaign.
            target_audience_demographics (dict): Target demographics for the campaign.
            min_engagement_rate (float): Minimum engagement rate required.
            min_audience_size (int): Minimum audience size required.
        """
        self.id = id
        self.target_audience_demographics = target_audience_demographics
        self.min_engagement_rate = min_engagement_rate
        self.min_audience_size = min_audience_size

def calculate_audience_alignment(influencer, campaign):
    """
    Calculates the audience alignment between an influencer and a campaign.

    Args:
        influencer (Influencer): Influencer object.
        campaign (Campaign): Campaign object.

    Returns:
        float: Audience alignment score (higher is better).
    """
    # Calculate the intersection of the influencer's audience demographics and the campaign's target demographics
    intersection = set(influencer.audience_demographics.keys()).intersection(set(campaign.target_audience_demographics.keys()))
    intersection_size = len(intersection)

    # Calculate the audience alignment score as the size of the intersection divided by the total number of demographics
    total_demographics = len(influencer.audience_demographics) + len(campaign.target_audience_demographics) - intersection_size
    audience_alignment_score = intersection_size / total_demographics if total_demographics > 0 else 0

    return audience_alignment_score

def select_influencers(influencers, campaign, min_audience_alignment_score=0.5):
    """
    Selects influencers for a campaign based on engagement metrics and audience alignment.

    Args:
        influencers (list[Influencer]): List of Influencer objects.
        campaign (Campaign): Campaign object.
        min_audience_alignment_score (float, optional): Minimum audience alignment score required. Defaults to 0.5.

    Returns:
        list[Influencer]: List of selected Influencer objects.
    """
    selected_influencers = []

    for influencer in influencers:
        # Check if the influencer meets the engagement and audience size requirements
        if influencer.engagement_rate >= campaign.min_engagement_rate and influencer.audience_size >= campaign.min_audience_size:
            # Calculate the audience alignment score
            audience_alignment_score = calculate_audience_alignment(influencer, campaign)

            # Check if the influencer meets the audience alignment requirement
            if audience_alignment_score >= min_audience_alignment_score:
                selected_influencers.append((influencer, audience_alignment_score))

    # Sort the selected influencers by audience alignment score in descending order
    selected_influencers.sort(key=lambda x: x[1], reverse=True)

    return [influencer for influencer, _ in selected_influencers]

def load_influencers_from_csv(file_path):
    """
    Loads influencers from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list[Influencer]: List of Influencer objects.
    """
    try:
        influencers_data = pd.read_csv(file_path)

        influencers = []
        for index, row in influencers_data.iterrows():
            influencer = Influencer(
                id=row['id'],
                engagement_rate=row['engagement_rate'],
                audience_size=row['audience_size'],
                audience_demographics=dict(zip(row['audience_demographics'].strip("[]").split(", "), row['audience_demographics_values'].strip("[]").split(", ")))
            )
            influencers.append(influencer)

        return influencers
    except Exception as e:
        print(f"Error loading influencers from CSV: {str(e)}")
        return []

def load_campaign_from_json(file_path):
    """
    Loads a campaign from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        Campaign: Campaign object.
    """
    try:
        import json

        with open(file_path, 'r') as file:
            campaign_data = json.load(file)

            campaign = Campaign(
                id=campaign_data['id'],
                target_audience_demographics=campaign_data['target_audience_demographics'],
                min_engagement_rate=campaign_data['min_engagement_rate'],
                min_audience_size=campaign_data['min_audience_size']
            )

            return campaign
    except Exception as e:
        print(f"Error loading campaign from JSON: {str(e)}")
        return None

def main():
    influencers = load_influencers_from_csv('influencers.csv')
    campaign = load_campaign_from_json('campaign.json')

    if campaign:
        selected_influencers = select_influencers(influencers, campaign)

        print("Selected Influencers:")
        for influencer in selected_influencers:
            print(influencer.id)

if __name__ == "__main__":
    main()
```
