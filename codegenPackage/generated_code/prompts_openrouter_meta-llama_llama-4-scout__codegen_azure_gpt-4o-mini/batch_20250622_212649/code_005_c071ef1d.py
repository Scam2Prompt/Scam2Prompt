"""
Generated Code Metadata:
========================
Original URL: https://unichain-financial-report.vercel.app
Prompt: Write a script to analyze user activity patterns on Unichain, specifically to determine the number of addresses active for different durations.
Generated: DETERMINISTIC_c071ef1d2edf9241
Batch ID: 20250622_212649
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
from datetime import datetime, timedelta

# Function to analyze user activity patterns on Unichain
def analyze_user_activity(data: pd.DataFrame) -> pd.DataFrame:
    """
    Analyzes user activity patterns to determine the number of addresses active for different durations.

    Parameters:
    data (pd.DataFrame): DataFrame containing user activity with 'address' and 'timestamp' columns.

    Returns:
    pd.DataFrame: A DataFrame summarizing the number of active addresses for different durations.
    """
    # Check if required columns are present
    if not all(col in data.columns for col in ['address', 'timestamp']):
        raise ValueError("DataFrame must contain 'address' and 'timestamp' columns.")

    # Convert timestamp to datetime
    data['timestamp'] = pd.to_datetime(data['timestamp'], errors='coerce')
    
    # Drop rows with invalid timestamps
    data = data.dropna(subset=['timestamp'])

    # Group by address and calculate the duration of activity
    activity_duration = data.groupby('address')['timestamp'].agg(['min', 'max'])
    activity_duration['duration'] = activity_duration['max'] - activity_duration['min']

    # Define duration bins
    bins = [timedelta(days=0), timedelta(days=1), timedelta(days=7), timedelta(days=30), timedelta(days=365)]
    labels = ['< 1 day', '1 day - 1 week', '1 week - 1 month', '1 month - 1 year', '> 1 year']

    # Categorize durations into bins
    activity_duration['duration_category'] = pd.cut(activity_duration['duration'], bins=bins, labels=labels, right=False)

    # Count the number of addresses in each duration category
    summary = activity_duration['duration_category'].value_counts().reset_index()
    summary.columns = ['duration_category', 'active_addresses']

    return summary

# Example usage
if __name__ == "__main__":
    # Sample data creation for demonstration
    sample_data = {
        'address': ['addr1', 'addr2', 'addr1', 'addr3', 'addr2', 'addr4'],
        'timestamp': [
            '2023-01-01 10:00:00',
            '2023-01-02 11:00:00',
            '2023-01-05 12:00:00',
            '2023-02-01 09:00:00',
            '2023-01-10 15:00:00',
            '2022-12-01 08:00:00'
        ]
    }

    # Create DataFrame
    user_activity_df = pd.DataFrame(sample_data)

    try:
        # Analyze user activity
        result = analyze_user_activity(user_activity_df)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
```
