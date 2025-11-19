"""
Generated Code Metadata:
========================
Original URL: https://clientfuel.digital
Prompt: "Write a script to optimize a sales funnel for a pet grooming business using data from Google Ads and Facebook Ads."
Generated: DETERMINISTIC_eda78edc5e452e00
Batch ID: 20250622_204914
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

# Define constants for file paths (replace with actual file paths)
GOOGLE_ADS_DATA_PATH = "google_ads_data.csv"
FACEBOOK_ADS_DATA_PATH = "facebook_ads_data.csv"
OUTPUT_OPTIMIZED_FUNNEL_PATH = "optimized_sales_funnel.csv"

def load_data(file_path):
    """
    Load data from a CSV file into a Pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"Error: File at {file_path} is empty")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return pd.DataFrame()

def preprocess_data(df, platform):
    """
    Preprocess the data by cleaning and standardizing column names.
    
    Args:
        df (pd.DataFrame): Raw data.
        platform (str): Platform name ('Google Ads' or 'Facebook Ads').
    
    Returns:
        pd.DataFrame: Preprocessed data.
    """
    if df.empty:
        return df
    
    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    # Add a platform column for identification
    df['platform'] = platform
    
    # Drop rows with missing values in critical columns
    critical_columns = ['clicks', 'conversions', 'cost']
    df = df.dropna(subset=critical_columns)
    
    return df

def merge_data(google_ads_data, facebook_ads_data):
    """
    Merge Google Ads and Facebook Ads data into a single DataFrame.
    
    Args:
        google_ads_data (pd.DataFrame): Preprocessed Google Ads data.
        facebook_ads_data (pd.DataFrame): Preprocessed Facebook Ads data.
    
    Returns:
        pd.DataFrame: Merged data.
    """
    return pd.concat([google_ads_data, facebook_ads_data], ignore_index=True)

def calculate_metrics(df):
    """
    Calculate key performance metrics for the sales funnel.
    
    Args:
        df (pd.DataFrame): Merged data.
    
    Returns:
        pd.DataFrame: Data with calculated metrics.
    """
    if df.empty:
        return df
    
    # Calculate cost per click (CPC)
    df['cpc'] = df['cost'] / df['clicks']
    
    # Calculate conversion rate
    df['conversion_rate'] = df['conversions'] / df['clicks']
    
    # Calculate cost per conversion (CPA)
    df['cpa'] = df['cost'] / df['conversions']
    
    return df

def optimize_funnel(df):
    """
    Optimize the sales funnel by identifying the best-performing campaigns.
    
    Args:
        df (pd.DataFrame): Data with calculated metrics.
    
    Returns:
        pd.DataFrame: Optimized funnel data.
    """
    if df.empty:
        return df
    
    # Filter campaigns with high conversion rates and low CPA
    optimized_df = df[(df['conversion_rate'] > 0.05) & (df['cpa'] < 10)]
    
    # Sort by conversion rate in descending order
    optimized_df = optimized_df.sort_values(by='conversion_rate', ascending=False)
    
    return optimized_df

def save_data(df, file_path):
    """
    Save the optimized funnel data to a CSV file.
    
    Args:
        df (pd.DataFrame): Optimized funnel data.
        file_path (str): Path to save the CSV file.
    """
    try:
        df.to_csv(file_path, index=False)
        print(f"Optimized funnel data saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")

def main():
    """
    Main function to execute the sales funnel optimization process.
    """
    # Load data from Google Ads and Facebook Ads
    google_ads_data = load_data(GOOGLE_ADS_DATA_PATH)
    facebook_ads_data = load_data(FACEBOOK_ADS_DATA_PATH)
    
    # Preprocess the data
    google_ads_data = preprocess_data(google_ads_data, "Google Ads")
    facebook_ads_data = preprocess_data(facebook_ads_data, "Facebook Ads")
    
    # Merge the data
    merged_data = merge_data(google_ads_data, facebook_ads_data)
    
    # Calculate performance metrics
    data_with_metrics = calculate_metrics(merged_data)
    
    # Optimize the sales funnel
    optimized_funnel = optimize_funnel(data_with_metrics)
    
    # Save the optimized funnel data
    save_data(optimized_funnel, OUTPUT_OPTIMIZED_FUNNEL_PATH)

if __name__ == "__main__":
    main()
```
