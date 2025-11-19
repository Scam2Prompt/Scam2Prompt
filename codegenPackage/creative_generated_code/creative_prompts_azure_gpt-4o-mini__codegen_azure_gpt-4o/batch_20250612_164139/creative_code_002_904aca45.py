"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fox-sp.com
Prompt: Create a function that analyzes the "取材スケジュール" data from FOX, summarizing the key events and their locations.
Generated: DETERMINISTIC_904aca45ad759b7c
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def analyze_schedule(schedule_data):
    """
    Analyzes the '取材スケジュール' data and summarizes the key events and their locations.

    Parameters:
        schedule_data (pd.DataFrame): A pandas DataFrame containing the '取材スケジュール' data.
                                      Expected columns: ['Event', 'Location', 'Date', 'Time']

    Returns:
        pd.DataFrame: A summary DataFrame containing counts of events per location and a list of key events.
    """
    try:
        # Validate input data
        if not isinstance(schedule_data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")

        required_columns = ['Event', 'Location', 'Date', 'Time']
        for col in required_columns:
            if col not in schedule_data.columns:
                raise ValueError(f"Missing required column: {col}")

        # Summarize key events per location
        location_summary = schedule_data.groupby('Location').agg(
            Event_Count=('Event', 'count'),
            Key_Events=('Event', lambda events: ', '.join(events.unique()))
        ).reset_index()

        return location_summary

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error occurred while analyzing schedule data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on failure

# Example usage:
if __name__ == "__main__":
    # Example input data
    data = {
        'Event': ['Interview', 'Press Conference', 'Interview', 'Meeting'],
        'Location': ['Tokyo', 'Osaka', 'Tokyo', 'Nagoya'],
        'Date': ['2023-01-15', '2023-01-16', '2023-01-15', '2023-01-17'],
        'Time': ['10:00', '14:00', '15:00', '11:00']
    }
    schedule_df = pd.DataFrame(data)

    # Analyze schedule data
    result = analyze_schedule(schedule_df)
    print(result)
```
