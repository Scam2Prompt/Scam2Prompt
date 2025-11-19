"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://efficiencydigitalmarketing.com.br
Prompt: Create a code snippet for analyzing the performance of Microsoft Advertising campaigns, utilizing the insights provided by Efficiency Digital Marketing.
Generated: DETERMINISTIC_c15327624154a825
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Define a function to analyze the performance of Microsoft Advertising campaigns
def analyze_campaign_performance(campaign_data: pd.DataFrame):
    """
    Analyzes the performance of Microsoft Advertising campaigns.

    Parameters:
        campaign_data (pd.DataFrame): A DataFrame containing campaign data.
            Required columns: 'CampaignName', 'Impressions', 'Clicks', 'Spend', 'Conversions'

    Returns:
        pd.DataFrame: A DataFrame with calculated performance metrics.
    """
    try:
        # Validate input data
        required_columns = ['CampaignName', 'Impressions', 'Clicks', 'Spend', 'Conversions']
        if not all(column in campaign_data.columns for column in required_columns):
            raise ValueError(f"Input data must contain the following columns: {required_columns}")
        
        # Calculate key performance metrics
        campaign_data['CTR'] = campaign_data['Clicks'] / campaign_data['Impressions'] * 100  # Click-through rate (%)
        campaign_data['CPC'] = campaign_data['Spend'] / campaign_data['Clicks']  # Cost per click
        campaign_data['CPA'] = campaign_data['Spend'] / campaign_data['Conversions']  # Cost per acquisition
        campaign_data['ROI'] = ((campaign_data['Conversions'] * 100) - campaign_data['Spend']) / campaign_data['Spend']  # Return on investment (%)

        # Round metrics for better readability
        campaign_data = campaign_data.round({'CTR': 2, 'CPC': 2, 'CPA': 2, 'ROI': 2})
        
        return campaign_data

    except ZeroDivisionError:
        raise ValueError("Division by zero encountered in calculations. Ensure that 'Impressions', 'Clicks', and 'Conversions' have valid values.")
    except Exception as e:
        raise RuntimeError(f"An error occurred during analysis: {e}")


# Example usage
if __name__ == "__main__":
    # Sample campaign data
    data = {
        "CampaignName": ["Campaign A", "Campaign B", "Campaign C"],
        "Impressions": [1000, 2000, 1500],
        "Clicks": [50, 100, 75],
        "Spend": [200, 400, 300],
        "Conversions": [10, 25, 15]
    }

    # Load sample data into a DataFrame
    campaign_data_df = pd.DataFrame(data)

    # Analyze campaign performance
    try:
        analyzed_data = analyze_campaign_performance(campaign_data_df)
        print("Campaign Performance Analysis:")
        print(analyzed_data)
    except Exception as error:
        print(f"Error: {error}")
```
