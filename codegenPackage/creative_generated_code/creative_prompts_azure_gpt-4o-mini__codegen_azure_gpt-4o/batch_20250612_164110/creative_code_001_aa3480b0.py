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

def analyze_engagement_rate(data: pd.DataFrame) -> dict:
    """
    Analyzes the engagement rates of micro and macro-influencers based on provided data.

    Parameters:
    - data (pd.DataFrame): A DataFrame containing influencer data with the following columns:
        - 'influencer_type': Type of the influencer ('micro' or 'macro')
        - 'engagement_rate': Engagement rate of the influencer (float)

    Returns:
    - dict: A dictionary containing average engagement rates for micro and macro influencers.
    """

    # Validate input
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    
    required_columns = {'influencer_type', 'engagement_rate'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"DataFrame must contain the following columns: {required_columns}")
    
    try:
        # Filter data for micro and macro influencers
        micro_influencers = data[data['influencer_type'] == 'micro']
        macro_influencers = data[data['influencer_type'] == 'macro']

        # Calculate average engagement rates
        micro_avg = micro_influencers['engagement_rate'].mean()
        macro_avg = macro_influencers['engagement_rate'].mean()

        # Handle cases where mean is NaN (no data for a type of influencer)
        if pd.isna(micro_avg):
            micro_avg = 0.0
        if pd.isna(macro_avg):
            macro_avg = 0.0

        # Return results in a dictionary
        return {
            'micro_average_engagement_rate': round(micro_avg, 2),
            'macro_average_engagement_rate': round(macro_avg, 2)
        }
    except Exception as e:
        # Catch unexpected errors
        raise RuntimeError(f"An error occurred while analyzing engagement rates: {e}")

# Example usage:
# data = pd.DataFrame({
#     'influencer_type': ['micro', 'macro', 'micro', 'macro', 'micro'],
#     'engagement_rate': [4.5, 3.2, 5.0, 2.8, 4.8]
# })
# result = analyze_engagement_rate(data)
# print(result)
```
