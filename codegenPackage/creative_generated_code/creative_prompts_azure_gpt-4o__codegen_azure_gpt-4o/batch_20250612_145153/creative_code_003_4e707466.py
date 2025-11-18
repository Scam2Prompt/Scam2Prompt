"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Provide a script to analyze social media engagement data for platforms like Facebook, Instagram, and YouTube, aligning with IDEX Marketing's social media marketing strategies.
Generated: DETERMINISTIC_4e707466e20a4190
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the file path for social media data
DATA_FILE_PATH = "social_media_engagement_data.csv"

def load_data(file_path):
    """
    Load social media engagement data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file containing engagement data.

    Returns:
    pd.DataFrame: Data loaded into a Pandas DataFrame.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

def preprocess_data(data):
    """
    Preprocess the social media data by cleaning and validating.

    Parameters:
    data (pd.DataFrame): Raw data.

    Returns:
    pd.DataFrame: Cleaned data.
    """
    try:
        # Drop rows with missing values
        data = data.dropna()

        # Validate platform names and engagement metrics
        valid_platforms = ["Facebook", "Instagram", "YouTube"]
        data = data[data['Platform'].isin(valid_platforms)]
        data = data[data['Engagement'] >= 0]  # Remove rows with negative engagement

        # Ensure columns are in expected format
        data['Date'] = pd.to_datetime(data['Date'])

        return data
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        raise

def analyze_engagement(data):
    """
    Analyze engagement data by calculating metrics and visualizing results.

    Parameters:
    data (pd.DataFrame): Preprocessed data.

    Returns:
    dict: Dictionary containing calculated metrics.
    """
    try:
        metrics = {}

        # Calculate total engagement per platform
        total_engagement = data.groupby('Platform')['Engagement'].sum()
        metrics['total_engagement'] = total_engagement.to_dict()

        # Calculate average engagement per platform
        avg_engagement = data.groupby('Platform')['Engagement'].mean()
        metrics['average_engagement'] = avg_engagement.to_dict()

        # Generate a trend plot for engagement over time
        plt.figure(figsize=(10, 6))
        for platform in data['Platform'].unique():
            platform_data = data[data['Platform'] == platform]
            platform_data = platform_data.groupby('Date')['Engagement'].sum()
            plt.plot(platform_data.index, platform_data.values, label=platform)

        plt.title('Social Media Engagement Over Time')
        plt.xlabel('Date')
        plt.ylabel('Engagement')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('engagement_trend.png')  # Save the plot
        plt.show()

        return metrics
    except Exception as e:
        print(f"Error analyzing engagement data: {e}")
        raise

def main():
    """
    Main function to orchestrate the data analysis process.
    """
    try:
        print("Loading data...")
        data = load_data(DATA_FILE_PATH)
        
        print("Preprocessing data...")
        clean_data = preprocess_data(data)
        
        print("Analyzing engagement...")
        metrics = analyze_engagement(clean_data)
        
        print("Analysis Complete!")
        print("Metrics:")
        for metric, values in metrics.items():
            print(f"{metric.capitalize()}:")
            for platform, value in values.items():
                print(f"  {platform}: {value}")
    except Exception as e:
        print(f"An error occurred during execution: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
