"""
Generated Code Metadata:
========================
Original URL: https://creocollective.io
Prompt: "Write a Python script to analyze marketing campaign data from various channels, including social media, email, and lead generation, using libraries like Pandas and NumPy."
Generated: DETERMINISTIC_2d6f2ab596342594
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np

# Define a function to load campaign data from a CSV file
def load_campaign_data(file_path):
    """
    Load marketing campaign data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the campaign data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If there is an error parsing the file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse the file '{file_path}': {e}")
        return None

# Define a function to analyze campaign data
def analyze_campaign_data(data):
    """
    Analyze marketing campaign data.

    Args:
        data (pd.DataFrame): A DataFrame containing the campaign data.

    Returns:
        dict: A dictionary containing the analysis results.
    """
    # Check if the data is not None
    if data is None:
        return None

    # Check if required columns exist
    required_columns = ['channel', 'impressions', 'clicks', 'conversions', 'cost']
    if not all(column in data.columns for column in required_columns):
        print("Error: The data is missing required columns.")
        return None

    # Calculate key performance indicators (KPIs)
    kpi_data = data.groupby('channel')[['impressions', 'clicks', 'conversions', 'cost']].sum().reset_index()

    # Calculate click-through rate (CTR)
    kpi_data['ctr'] = kpi_data['clicks'] / kpi_data['impressions']

    # Calculate conversion rate
    kpi_data['conversion_rate'] = kpi_data['conversions'] / kpi_data['clicks']

    # Calculate cost per click (CPC)
    kpi_data['cpc'] = kpi_data['cost'] / kpi_data['clicks']

    # Calculate cost per conversion
    kpi_data['cpa'] = kpi_data['cost'] / kpi_data['conversions']

    # Return the analysis results
    return kpi_data.to_dict(orient='records')

# Define a function to print analysis results
def print_analysis_results(results):
    """
    Print the analysis results.

    Args:
        results (dict): A dictionary containing the analysis results.
    """
    if results is not None:
        for result in results:
            print(f"Channel: {result['channel']}")
            print(f"Impressions: {result['impressions']}")
            print(f"Clicks: {result['clicks']}")
            print(f"Conversions: {result['conversions']}")
            print(f"Cost: {result['cost']:.2f}")
            print(f"CTR: {result['ctr']:.4f}")
            print(f"Conversion Rate: {result['conversion_rate']:.4f}")
            print(f"CPC: {result['cpc']:.2f}")
            print(f"CPA: {result['cpa']:.2f}")
            print("-" * 50)

# Main function
def main():
    # Load campaign data from CSV files
    social_media_data = load_campaign_data('social_media_data.csv')
    email_data = load_campaign_data('email_data.csv')
    lead_generation_data = load_campaign_data('lead_generation_data.csv')

    # Analyze campaign data
    social_media_results = analyze_campaign_data(social_media_data)
    email_results = analyze_campaign_data(email_data)
    lead_generation_results = analyze_campaign_data(lead_generation_data)

    # Print analysis results
    print("Social Media Results:")
    print_analysis_results(social_media_results)
    print("\nEmail Results:")
    print_analysis_results(email_results)
    print("\nLead Generation Results:")
    print_analysis_results(lead_generation_results)

if __name__ == "__main__":
    main()
```
