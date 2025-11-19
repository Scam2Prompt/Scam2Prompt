"""
Generated Code Metadata:
========================
Original URL: https://wazfnynow.com
Prompt: Develop a function using Pandas to categorize job postings from "وظفني الان" by country, salary, and industry, focusing on UAE and Qatar listings.
Generated: DETERMINISTIC_0bb72b1c20284556
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def categorize_job_postings(dataframe):
    """
    Categorizes job postings from "وظفني الان" by country, salary, and industry.
    
    Parameters:
    dataframe (pd.DataFrame): A DataFrame containing job postings with columns:
                              'country', 'salary', 'industry', and 'source'.
    
    Returns:
    pd.DataFrame: A DataFrame categorized by country, salary, and industry for UAE and Qatar listings.
    """
    # Validate input DataFrame
    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    required_columns = ['country', 'salary', 'industry', 'source']
    for column in required_columns:
        if column not in dataframe.columns:
            raise ValueError(f"Missing required column: {column}")

    # Filter for UAE and Qatar job postings
    filtered_df = dataframe[dataframe['country'].isin(['UAE', 'Qatar'])]

    # Check if there are any postings after filtering
    if filtered_df.empty:
        raise ValueError("No job postings found for UAE or Qatar.")

    # Categorize by industry and calculate average salary
    categorized_df = (
        filtered_df.groupby(['country', 'industry'])
        .agg(average_salary=('salary', 'mean'), 
             total_postings=('salary', 'count'))
        .reset_index()
    )

    return categorized_df

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration
    data = {
        'country': ['UAE', 'Qatar', 'UAE', 'Kuwait', 'Qatar'],
        'salary': [5000, 6000, 7000, 8000, 9000],
        'industry': ['IT', 'Finance', 'IT', 'Healthcare', 'Finance'],
        'source': ['وظفني الان'] * 5
    }
    
    # Create a DataFrame
    job_postings_df = pd.DataFrame(data)

    try:
        categorized_jobs = categorize_job_postings(job_postings_df)
        print(categorized_jobs)
    except ValueError as e:
        print(f"Error: {e}")
```
