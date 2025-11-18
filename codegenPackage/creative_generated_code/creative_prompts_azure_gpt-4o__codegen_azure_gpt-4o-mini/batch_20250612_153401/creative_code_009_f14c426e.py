"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fundfa.com
Prompt: Write code to visualize the growth and evolution of Iranian prop firms like Propiy and Fenefx, using historical data and features mentioned on Fundfa.
Generated: DETERMINISTIC_f14c426ecc3982f6
Batch ID: 20250612_153401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/historical_data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# Configure aesthetic settings for seaborn
sns.set(style="whitegrid")

def fetch_historical_data(url):
    """
    Fetch historical data from the provided URL.
    
    Args:
        url (str): The URL to fetch data from.

    Returns:
        pd.DataFrame: A DataFrame containing the historical data.
        
    Raises:
        ValueError: If the response does not contain valid data.
        Exception: For any other errors during the request.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Assuming the endpoint returns JSON data
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Validate the DataFrame
        if df.empty or not all(col in df.columns for col in ['date', 'prop_firm', 'growth']):
            raise ValueError("Invalid data structure received.")
        
        return df
    except ValueError as ve:
        print(f"ValueError: {ve}")
        raise
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")
        raise

def visualize_growth(df):
    """
    Visualize the growth of Iranian prop firms over time.

    Args:
        df (pd.DataFrame): DataFrame containing columns 'date', 'prop_firm', and 'growth'.
    """
    # Convert 'date' to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Set the figure size
    plt.figure(figsize=(14, 7))
    
    # Plotting the growth of each firm
    sns.lineplot(data=df, x='date', y='growth', hue='prop_firm', marker='o')

    # Adding titles and labels
    plt.title('Growth of Iranian Prop Firms Over Time', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Growth Percentage', fontsize=14)
    plt.legend(title='Prop Firms')
    
    # Show the plot
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the data fetching and visualization.
    """
    url = "https://api.example.com/historical_data"  # Replace with the actual API endpoint

    try:
        # Fetch historical data
        historical_data = fetch_historical_data(url)
        
        # Visualize the growth
        visualize_growth(historical_data)

    except Exception as e:
        print(f"Failed to execute the main process: {e}")

if __name__ == "__main__":
    main()
```
