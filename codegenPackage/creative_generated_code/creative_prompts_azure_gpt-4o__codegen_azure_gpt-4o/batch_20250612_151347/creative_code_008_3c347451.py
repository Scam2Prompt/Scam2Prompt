"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evamobi.com
Prompt: Write a script to evaluate promotional effectiveness for mobile apps, including re-engagement strategies and remarketing setups, as described in Evamobi's services.
Generated: DETERMINISTIC_3c3474516cea4411
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime, timedelta

# Function to evaluate promotional effectiveness
def evaluate_promotions(data, promotion_start_date, promotion_end_date):
    """
    Evaluates the effectiveness of promotional campaigns for mobile apps.

    Parameters:
    data (pd.DataFrame): User engagement data with columns ['user_id', 'date', 'activity_type']
    promotion_start_date (str): Start date of the promotion in 'YYYY-MM-DD' format
    promotion_end_date (str): End date of the promotion in 'YYYY-MM-DD' format

    Returns:
    pd.DataFrame: Summary of promotion effectiveness with columns:
                  ['total_users', 'reengaged_users', 'new_users', 'conversion_rate']
    """
    try:
        # Convert strings to datetime objects
        promotion_start_date = datetime.strptime(promotion_start_date, '%Y-%m-%d')
        promotion_end_date = datetime.strptime(promotion_end_date, '%Y-%m-%d')
        
        # Ensure input dates are valid
        if promotion_start_date > promotion_end_date:
            raise ValueError("Promotion start date cannot be after promotion end date.")
        
        # Data filtering for the promotion period
        data['date'] = pd.to_datetime(data['date'])
        promotion_data = data[(data['date'] >= promotion_start_date) & (data['date'] <= promotion_end_date)]
        
        # Calculate metrics
        total_users = data['user_id'].nunique()  # Total unique users in the dataset
        reengaged_users = promotion_data[promotion_data['activity_type'] == 'reengagement']['user_id'].nunique()
        new_users = promotion_data[promotion_data['activity_type'] == 'new']['user_id'].nunique()
        if total_users > 0:
            conversion_rate = (reengaged_users + new_users) / total_users * 100  # Conversion rate percentage
        else:
            conversion_rate = 0
        
        # Create summary dataframe
        summary = pd.DataFrame({
            'total_users': [total_users],
            'reengaged_users': [reengaged_users],
            'new_users': [new_users],
            'conversion_rate': [conversion_rate]
        })
        
        return summary

    except Exception as e:
        # Log error and return empty dataframe
        print(f"Error evaluating promotions: {e}")
        return pd.DataFrame()

# Function to set up remarketing strategies
def setup_remarketing(data, remarketing_window_days):
    """
    Sets up remarketing strategies based on user inactivity.

    Parameters:
    data (pd.DataFrame): User engagement data with columns ['user_id', 'date', 'activity_type']
    remarketing_window_days (int): Number of days of inactivity to trigger remarketing

    Returns:
    pd.DataFrame: List of users to remarket with columns ['user_id']
    """
    try:
        # Convert dates to datetime objects
        data['date'] = pd.to_datetime(data['date'])
        
        # Find the latest activity date for each user
        latest_activity = data.groupby('user_id')['date'].max().reset_index()
        latest_activity.rename(columns={'date': 'last_active_date'}, inplace=True)
        
        # Identify users who have been inactive for longer than the remarketing window
        current_date = datetime.now()
        remarketing_users = latest_activity[
            (current_date - latest_activity['last_active_date']) > timedelta(days=remarketing_window_days)
        ]
        
        # Return a list of user IDs to remarket
        return remarketing_users[['user_id']]

    except Exception as e:
        # Log error and return empty dataframe
        print(f"Error setting up remarketing: {e}")
        return pd.DataFrame()

# Example usage of the functions
if __name__ == "__main__":
    # Sample user engagement data
    sample_data = pd.DataFrame({
        'user_id': [1, 2, 3, 4, 5, 1, 2, 3],
        'date': ['2023-10-01', '2023-10-01', '2023-10-02', '2023-10-02', '2023-10-03', '2023-10-03', '2023-10-05', '2023-10-05'],
        'activity_type': ['new', 'new', 'new', 'reengagement', 'new', 'reengagement', 'reengagement', 'new']
    })
    
    # Evaluate promotions
    promotion_summary = evaluate_promotions(sample_data, '2023-10-01', '2023-10-05')
    print("Promotion Summary:")
    print(promotion_summary)
    
    # Set up remarketing
    remarketing_list = setup_remarketing(sample_data, remarketing_window_days=3)
    print("\nRemarketing User List:")
    print(remarketing_list)
```
