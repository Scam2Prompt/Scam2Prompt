"""
Generated Code Metadata:
========================
Original URL: https://notclosn.top
Prompt: Write Python code to analyze user interaction data from an online educational platform, focusing on engagement metrics like session duration and page views, as described in the КарьераОнлайн program.
Generated: DETERMINISTIC_14770c2b86dab9b0
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from datetime import datetime

def load_data(file_path):
    """
    Load user interaction data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("File is empty. Please check the file contents.")
        return None
    except pd.errors.ParserError:
        print("Error parsing file. Please check the file format.")
        return None

def calculate_session_duration(data):
    """
    Calculate session duration in minutes.

    Args:
        data (pd.DataFrame): User interaction data.

    Returns:
        pd.DataFrame: Data with added session duration column.
    """
    # Ensure datetime columns are in datetime format
    data['start_time'] = pd.to_datetime(data['start_time'])
    data['end_time'] = pd.to_datetime(data['end_time'])

    # Calculate session duration
    data['session_duration'] = (data['end_time'] - data['start_time']).dt.total_seconds() / 60

    return data

def calculate_page_views(data):
    """
    Calculate page views per session.

    Args:
        data (pd.DataFrame): User interaction data.

    Returns:
        pd.DataFrame: Data with added page views column.
    """
    # Group by session and count page views
    page_views = data.groupby('session_id')['page_id'].count().reset_index()
    page_views.columns = ['session_id', 'page_views']

    # Merge page views with original data
    data = pd.merge(data, page_views, on='session_id')

    return data

def analyze_engagement(data):
    """
    Analyze engagement metrics.

    Args:
        data (pd.DataFrame): User interaction data.

    Returns:
        dict: Engagement metrics (average session duration, average page views).
    """
    # Calculate average session duration
    avg_session_duration = data['session_duration'].mean()

    # Calculate average page views
    avg_page_views = data['page_views'].mean()

    return {
        'average_session_duration': avg_session_duration,
        'average_page_views': avg_page_views
    }

def main():
    # Load data
    file_path = 'user_interaction_data.csv'  # Replace with actual file path
    data = load_data(file_path)

    if data is not None:
        # Calculate session duration
        data = calculate_session_duration(data)

        # Calculate page views
        data = calculate_page_views(data)

        # Analyze engagement metrics
        engagement_metrics = analyze_engagement(data)

        # Print engagement metrics
        print("Engagement Metrics:")
        print(f"Average Session Duration: {engagement_metrics['average_session_duration']:.2f} minutes")
        print(f"Average Page Views: {engagement_metrics['average_page_views']:.2f}")

if __name__ == "__main__":
    main()
```
