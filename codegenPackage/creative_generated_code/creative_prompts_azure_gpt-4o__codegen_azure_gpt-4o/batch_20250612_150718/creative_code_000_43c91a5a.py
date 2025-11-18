"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydifferencebetween.com
Prompt: Write a Python script to analyze performance analytics data and generate marketing investment return insights, referencing best practices discussed in business articles.
Generated: DETERMINISTIC_43c91a5a7b8990d4
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

# Define constants for marketing channels and thresholds
MARKETING_CHANNELS = ['Social Media', 'Email', 'SEO', 'PPC', 'Affiliate']
ROI_THRESHOLD = 1.2  # Return on Investment threshold for good performance

# Function to read and validate input data
def load_data(file_path):
    """
    Load performance analytics data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing analytics data.
    
    Returns:
        pd.DataFrame: Loaded and validated DataFrame.
    """
    try:
        # Load the data into a DataFrame
        data = pd.read_csv(file_path)
        
        # Basic validation checks
        required_columns = ['Channel', 'Investment', 'Revenue']
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Missing required column: {column}")
        
        return data
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the data: {str(e)}")

# Function to calculate performance metrics
def calculate_metrics(data):
    """
    Calculate ROI and other metrics for each marketing channel.
    
    Args:
        data (pd.DataFrame): DataFrame with investment and revenue data.
    
    Returns:
        pd.DataFrame: DataFrame with calculated metrics.
    """
    try:
        # Calculate ROI (Revenue / Investment)
        data['ROI'] = np.where(data['Investment'] > 0, data['Revenue'] / data['Investment'], np.nan)
        
        # Categorize performance based on ROI threshold
        data['Performance'] = np.where(data['ROI'] >= ROI_THRESHOLD, 'Good', 'Poor')
        
        return data
    except Exception as e:
        raise Exception(f"An error occurred while calculating metrics: {str(e)}")

# Function to generate insights based on metrics
def generate_insights(data):
    """
    Generate actionable marketing investment return insights.
    
    Args:
        data (pd.DataFrame): DataFrame with calculated metrics.
    
    Returns:
        str: Insights report.
    """
    try:
        insights = []
        
        # Aggregate insights by channel performance
        for channel in MARKETING_CHANNELS:
            channel_data = data[data['Channel'] == channel]
            if not channel_data.empty:
                avg_roi = channel_data['ROI'].mean()
                insights.append(f"Channel: {channel}, Average ROI: {avg_roi:.2f}")
        
        # Add summary insights
        good_channels = data[data['Performance'] == 'Good']['Channel'].unique()
        poor_channels = data[data['Performance'] == 'Poor']['Channel'].unique()
        
        insights.append("\nSummary:")
        insights.append(f"Channels performing well (ROI >= {ROI_THRESHOLD}): {', '.join(good_channels)}")
        insights.append(f"Channels underperforming: {', '.join(poor_channels)}")
        
        return "\n".join(insights)
    except Exception as e:
        raise Exception(f"An error occurred while generating insights: {str(e)}")

# Main function to execute the script
def main():
    """
    Main function to execute performance analytics and generate insights.
    """
    try:
        # File path to the analytics data
        file_path = 'analytics_data.csv'  # Update with actual file path
        
        # Load the performance analytics data
        data = load_data(file_path)
        
        # Calculate metrics for the data
        metrics_data = calculate_metrics(data)
        
        # Generate marketing investment return insights
        insights = generate_insights(metrics_data)
        
        # Print insights
        print("Marketing Investment Return Insights:")
        print(insights)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
