"""
Generated Code Metadata:
========================
Original URL: https://balancerh.com
Prompt: Create a code snippet that utilizes the historical data capabilities of Balance RH to analyze salary trends over the past five years.
Generated: DETERMINISTIC_832039e2c535c52e
Batch ID: 20250612_135906
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
from datetime import datetime, timedelta

# Define a function to retrieve historical data from Balance RH
def get_historical_data(api_key, company_id, start_date, end_date):
    """
    Retrieves historical data from Balance RH API.

    Args:
        api_key (str): Balance RH API key
        company_id (str): Company ID
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format

    Returns:
        pandas.DataFrame: Historical data
    """
    try:
        # Replace with actual API call
        # For demonstration purposes, a sample DataFrame is used
        data = {
            'date': pd.date_range(start=start_date, end=end_date),
            'salary': np.random.randint(50000, 150000, size=(end_date - start_date).days + 1)
        }
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Error retrieving historical data: {e}")
        return None

# Define a function to analyze salary trends
def analyze_salary_trends(historical_data):
    """
    Analyzes salary trends.

    Args:
        historical_data (pandas.DataFrame): Historical data

    Returns:
        dict: Salary trend analysis
    """
    try:
        # Calculate monthly average salaries
        historical_data['month'] = historical_data['date'].dt.to_period('M')
        monthly_avg_salaries = historical_data.groupby('month')['salary'].mean().reset_index()

        # Calculate overall average salary
        overall_avg_salary = historical_data['salary'].mean()

        # Calculate year-over-year (YoY) salary growth
        monthly_avg_salaries['year'] = monthly_avg_salaries['month'].dt.year
        yoy_growth = monthly_avg_salaries.pivot(index='month', columns='year', values='salary')

        return {
            'monthly_avg_salaries': monthly_avg_salaries,
            'overall_avg_salary': overall_avg_salary,
            'yoy_growth': yoy_growth
        }
    except Exception as e:
        print(f"Error analyzing salary trends: {e}")
        return None

# Main function
def main():
    api_key = "your_api_key"
    company_id = "your_company_id"
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=365*5)).strftime('%Y-%m-%d')

    historical_data = get_historical_data(api_key, company_id, start_date, end_date)
    if historical_data is not None:
        trend_analysis = analyze_salary_trends(historical_data)
        if trend_analysis is not None:
            print("Monthly Average Salaries:")
            print(trend_analysis['monthly_avg_salaries'])
            print("\nOverall Average Salary:")
            print(trend_analysis['overall_avg_salary'])
            print("\nYear-over-Year (YoY) Salary Growth:")
            print(trend_analysis['yoy_growth'])

if __name__ == "__main__":
    main()
```
