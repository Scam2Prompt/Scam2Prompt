"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: "Create a Python script to analyze the effectiveness of marketing campaigns for a small business, using metrics similar to those considered by NMKT."
Generated: DETERMINISTIC_0e9c6a0dfd0ce229
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

# Define constants for metrics thresholds
ROI_THRESHOLD = 1.5  # Minimum acceptable Return on Investment
CTR_THRESHOLD = 0.02  # Minimum acceptable Click-Through Rate
CONVERSION_RATE_THRESHOLD = 0.05  # Minimum acceptable Conversion Rate

def load_campaign_data(file_path):
    """
    Load marketing campaign data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing campaign data.
        
    Returns:
        pd.DataFrame: DataFrame containing the campaign data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return None

def calculate_metrics(data):
    """
    Calculate key performance metrics for marketing campaigns.
    
    Args:
        data (pd.DataFrame): DataFrame containing campaign data.
        
    Returns:
        pd.DataFrame: DataFrame with calculated metrics.
    """
    try:
        # Ensure required columns exist
        required_columns = ['Spend', 'Revenue', 'Clicks', 'Impressions', 'Conversions']
        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"Missing required column: {col}")
        
        # Calculate metrics
        data['ROI'] = data['Revenue'] / data['Spend']  # Return on Investment
        data['CTR'] = data['Clicks'] / data['Impressions']  # Click-Through Rate
        data['ConversionRate'] = data['Conversions'] / data['Clicks']  # Conversion Rate
        
        return data
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return None

def evaluate_campaigns(data):
    """
    Evaluate the effectiveness of marketing campaigns based on predefined thresholds.
    
    Args:
        data (pd.DataFrame): DataFrame containing campaign data with calculated metrics.
        
    Returns:
        pd.DataFrame: DataFrame with evaluation results.
    """
    try:
        # Add evaluation columns
        data['EffectiveROI'] = data['ROI'] >= ROI_THRESHOLD
        data['EffectiveCTR'] = data['CTR'] >= CTR_THRESHOLD
        data['EffectiveConversionRate'] = data['ConversionRate'] >= CONVERSION_RATE_THRESHOLD
        
        # Overall effectiveness
        data['OverallEffective'] = data[['EffectiveROI', 'EffectiveCTR', 'EffectiveConversionRate']].all(axis=1)
        
        return data
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return None

def main():
    """
    Main function to execute the script.
    """
    # File path to the campaign data CSV
    file_path = 'campaign_data.csv'
    
    # Load campaign data
    campaign_data = load_campaign_data(file_path)
    if campaign_data is None:
        return
    
    # Calculate metrics
    campaign_data = calculate_metrics(campaign_data)
    if campaign_data is None:
        return
    
    # Evaluate campaigns
    campaign_data = evaluate_campaigns(campaign_data)
    if campaign_data is None:
        return
    
    # Display results
    print("Campaign Analysis Results:")
    print(campaign_data[['CampaignName', 'ROI', 'CTR', 'ConversionRate', 'OverallEffective']])
    
    # Save results to a new CSV file
    output_file = 'campaign_analysis_results.csv'
    try:
        campaign_data.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error: Failed to save results - {e}")

if __name__ == "__main__":
    main()
```
