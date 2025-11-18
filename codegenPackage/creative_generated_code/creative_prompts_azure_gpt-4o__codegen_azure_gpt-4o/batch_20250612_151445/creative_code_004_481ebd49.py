"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: Write a script to analyze monthly install growth (e.g., 300%+ MoM growth) for a rewards-based gaming app like Cosmic Rewards.
Generated: DETERMINISTIC_481ebd493b039738
Batch ID: 20250612_151445
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

def analyze_growth(data):
    """
    Analyzes month-over-month (MoM) install growth for a gaming app.

    Parameters:
        data (pd.DataFrame): A DataFrame containing two columns:
                             'Month' (datetime or string in yyyy-mm format)
                             and 'Installs' (integer representing the total installs).

    Returns:
        pd.DataFrame: A DataFrame with original data, MoM growth percentages,
                      and a flag for high growth months (e.g., > 300% growth).
    """
    try:
        # Ensure 'Month' column is datetime type for proper sorting and comparison
        data['Month'] = pd.to_datetime(data['Month'], format='%Y-%m')
        
        # Sort the data by month in ascending order
        data = data.sort_values(by='Month')
        
        # Calculate Month-over-Month growth percentage
        data['MoM_Growth_%'] = data['Installs'].pct_change() * 100
        
        # Flag months with high growth (300%+ growth)
        data['High_Growth'] = np.where(data['MoM_Growth_%'] > 300, True, False)
        
        return data
    
    except Exception as e:
        # Handle any exceptions that occur during processing
        print(f"An error occurred while analyzing growth: {e}")
        return None

# Sample input data for testing (replace this with actual data in production)
if __name__ == "__main__":
    # Example data for testing
    sample_data = {
        'Month': ['2023-01', '2023-02', '2023-03', '2023-04'],
        'Installs': [1000, 3000, 12000, 50000]
    }

    # Convert the sample data into a DataFrame
    df = pd.DataFrame(sample_data)
    
    # Perform the analysis
    result = analyze_growth(df)
    
    # Print the result if successful
    if result is not None:
        print("Growth Analysis Result:")
        print(result)
```
