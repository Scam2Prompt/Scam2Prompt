"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.in
Prompt: Write a function in Python that analyzes the engagement rates of micro and macro-influencers based on data from a marketing campaign.
Generated: DETERMINISTIC_aa3480b039236bc2
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def analyze_engagement_rates(data):
    """
    Analyze engagement rates for micro and macro-influencers from a marketing campaign.

    Parameters:
        data (pd.DataFrame): A DataFrame containing influencer data with columns:
                             - 'influencer_type': Type of influencer ('micro' or 'macro')
                             - 'followers': Number of followers
                             - 'likes': Number of likes on posts
                             - 'comments': Number of comments on posts
                             - 'impressions': Number of impressions on posts

    Returns:
        pd.DataFrame: A DataFrame summarizing average engagement rates for both types of influencers.
    
    Raises:
        ValueError: If the input data is not a DataFrame or it lacks required columns.
    """
    
    # Check if input is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")
    
    required_columns = ['influencer_type', 'followers', 'likes', 'comments', 'impressions']
    
    # Check if required columns are present in DataFrame
    for col in required_columns:
        if col not in data.columns:
            raise ValueError(f"Input data must contain the column: '{col}'.")

    # Calculate engagement rate for each influencer
    data['engagement_rate'] = (data['likes'] + data['comments']) / data['impressions'] * 100

    # Group by influencer type and calculate average engagement rates
    engagement_summary = data.groupby('influencer_type')['engagement_rate'].mean().reset_index()

    # Rename columns for clarity
    engagement_summary.columns = ['Influencer Type', 'Average Engagement Rate (%)']

    return engagement_summary

# Example usage
if __name__ == "__main__":
    # Sample data creation
    sample_data = {
        'influencer_type': ['micro', 'macro', 'micro', 'macro'],
        'followers': [15000, 200000, 12000, 500000],
        'likes': [300, 1500, 200, 3000],
        'comments': [50, 200, 30, 400],
        'impressions': [10000, 100000, 8000, 200000]
    }

    # Create a DataFrame
    df = pd.DataFrame(sample_data)

    try:
        # Analyze engagement rates
        result = analyze_engagement_rates(df)
        print(result)

    except ValueError as e:
        print(f"Error analyzing engagement rates: {e}")
```
