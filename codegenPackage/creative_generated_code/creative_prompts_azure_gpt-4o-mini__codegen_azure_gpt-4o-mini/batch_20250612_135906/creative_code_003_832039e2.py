"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancerh.com
Prompt: Create a code snippet that utilizes the historical data capabilities of Balance RH to analyze salary trends over the past five years.
Generated: DETERMINISTIC_832039e2c535c52e
Batch ID: 20250612_135906
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
from datetime import datetime, timedelta
from balance_rh_api import BalanceRHClient  # Hypothetical API client for Balance RH

def fetch_salary_data(start_date, end_date):
    """
    Fetch salary historical data from Balance RH API within the specified date range.

    :param start_date: The start date for data retrieval (datetime).
    :param end_date: The end date for data retrieval (datetime).
    :return: A DataFrame containing salary data.
    """
    client = BalanceRHClient()  # Initialize the API client
    try:
        # Fetch data from the API
        salary_data = client.get_salary_data(start_date=start_date, end_date=end_date)
        return pd.DataFrame(salary_data)
    except Exception as e:
        print(f"Error fetching salary data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def analyze_salary_trends(data):
    """
    Analyze salary trends from the provided salary DataFrame.

    :param data: A DataFrame containing salary data.
    :return: A DataFrame with analyzed trends.
    """
    if data.empty:
        print("No data to analyze.")
        return pd.DataFrame()  # Return empty DataFrame if no data

    # Convert date column to datetime format
    data['date'] = pd.to_datetime(data['date'])
    
    # Group by year and calculate average salary
    trend = data.groupby(data['date'].dt.year)['salary'].mean().reset_index()
    trend.columns = ['Year', 'Average Salary']
    
    return trend

def plot_salary_trends(trend_data):
    """
    Plot the salary trends over the years.

    :param trend_data: A DataFrame containing analyzed salary trends.
    """
    if trend_data.empty:
        return  # No data to plot

    plt.figure(figsize=(10, 5))
    plt.plot(trend_data['Year'], trend_data['Average Salary'], marker='o')
    plt.title('Average Salary Trends Over the Last 5 Years')
    plt.xlabel('Year')
    plt.ylabel('Average Salary')
    plt.xticks(trend_data['Year'])
    plt.grid()
    plt.tight_layout()
    plt.show()

def main():
    # Define the date range for the last 5 years
    end_date = datetime.now()
    start_date = end_date - timedelta(days=5 * 365)

    # Fetch salary data
    salary_data = fetch_salary_data(start_date, end_date)

    # Analyze salary trends
    salary_trends = analyze_salary_trends(salary_data)

    # Plot the trends
    plot_salary_trends(salary_trends)

if __name__ == "__main__":
    main()
```
