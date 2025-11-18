"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wazfnynow.com
Prompt: Develop a function using Pandas to categorize job postings from "وظفني الان" by country, salary, and industry, focusing on UAE and Qatar listings.
Generated: DETERMINISTIC_0bb72b1c20284556
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def categorize_job_postings(data: pd.DataFrame) -> pd.DataFrame:
    """
    Categorizes job postings by country, salary, and industry for UAE and Qatar listings.
    
    Parameters:
        data (pd.DataFrame): A DataFrame containing job postings with columns 'Country', 'Salary', 'Industry', and other relevant fields.
        
    Returns:
        pd.DataFrame: A DataFrame with categorized job postings filtered by UAE and Qatar.
    """
    try:
        # Validate if required columns exist in the input DataFrame
        required_columns = {'Country', 'Salary', 'Industry'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Input DataFrame must contain the following columns: {required_columns}")
        
        # Filter job postings related to UAE and Qatar
        filtered_data = data[data['Country'].isin(['UAE', 'Qatar'])]

        # Categorize Salary: Low (<= 5000), Medium (5001 - 15000), High (> 15000)
        def categorize_salary(salary):
            if salary <= 5000:
                return 'Low'
            elif 5001 <= salary <= 15000:
                return 'Medium'
            else:
                return 'High'

        # Apply salary categorization
        filtered_data['Salary_Category'] = filtered_data['Salary'].apply(categorize_salary)

        # Group by Country, Salary Category, and Industry
        categorized_data = filtered_data.groupby(
            ['Country', 'Salary_Category', 'Industry']
        ).size().reset_index(name='Count')

        return categorized_data
    
    except Exception as e:
        # Log or raise any exceptions encountered during execution
        raise RuntimeError(f"An error occurred while categorizing job postings: {e}")

# Example Usage:
# jobs_df = pd.DataFrame({
#     'Country': ['UAE', 'Qatar', 'UAE', 'KSA', 'Qatar'],
#     'Salary': [4000, 12000, 20000, 8000, 3000],
#     'Industry': ['IT', 'Finance', 'Construction', 'Healthcare', 'IT']
# })
# categorized_jobs = categorize_job_postings(jobs_df)
# print(categorized_jobs)
```
