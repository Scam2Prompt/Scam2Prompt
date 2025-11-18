"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starshot90.com
Prompt: Write a function to analyze employee retention metrics during turbulent times, based on the strategies described in the "Strategies for Employee Retention in Turbulent Times" section of the Star Shot 90 website.
Generated: DETERMINISTIC_fe5f9c5c9760df8f
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import datetime

def analyze_employee_retention(data, strategies):
    """
    Analyzes employee retention metrics during turbulent times based on defined strategies.

    Args:
        data (pd.DataFrame): A DataFrame containing employee data. Expected columns:
            - 'employee_id': Unique identifier for an employee.
            - 'hire_date': Date the employee was hired (datetime object or string in YYYY-MM-DD format).
            - 'termination_date': Date the employee left the company (datetime object or string in YYYY-MM-DD format), or None if still employed.
            - 'department': Department the employee belongs to.
            - 'performance_score': Performance rating of the employee (numeric or categorical).
            - 'engagement_score': Engagement score of the employee (numeric or categorical).
        strategies (dict): A dictionary defining employee retention strategies. Example format:
            {
                'focus_on_performance': True,
                'focus_on_engagement': True,
                'critical_departments': ['Engineering', 'Sales']
            }

    Returns:
        dict: A dictionary containing retention metrics. Includes:
            - 'retention_rate': Overall employee retention rate.
            - 'average_tenure': Average tenure of employees (in years).
            - 'critical_department_retention_rate': Retention rate for critical departments (if specified).
            - 'performance_retention_rate': Retention rate for high performers (if specified).
            - 'engagement_retention_rate': Retention rate for highly engaged employees (if specified).
    """
    # Ensure hire_date and termination_date are in datetime format
    data['hire_date'] = pd.to_datetime(data['hire_date'])
    data['termination_date'] = pd.to_datetime(data['termination_date'], errors='coerce')

    # Calculate tenure (in years)
    data['tenure_years'] = data.apply(
        lambda row: (
            (row['termination_date'] or datetime.datetime.now()) - row['hire_date']
        ).days / 365.0,
        axis=1
    )

    # Determine current employees
    current_employees = data['termination_date'].isna()

    # Calculate retention rate
    retention_rate = current_employees.sum() / len(data)

    # Calculate average tenure
    average_tenure = data['tenure_years'].mean()

    # Initialize results dictionary
    results = {
        'retention_rate': retention_rate,
        'average_tenure': average_tenure
    }

    # Analyze critical departments if specified
    if strategies.get('critical_departments'):
        critical_departments = strategies['critical_departments']
        critical_data = data[data['department'].isin(critical_departments)]
        critical_current_employees = critical_data['termination_date'].isna()
        critical_retention_rate = critical_current_employees.sum() / len(critical_data)
        results['critical_department_retention_rate'] = critical_retention_rate

    # Analyze high performers if specified
    if strategies.get('focus_on_performance'):
        high_performers = data[data['performance_score'] >= 4]  # Assuming 4+ is high performance
        high_current_employees = high_performers['termination_date'].isna()
        performance_retention_rate = high_current_employees.sum() / len(high_performers)
        results['performance_retention_rate'] = performance_retention_rate

    # Analyze highly engaged employees if specified
    if strategies.get('focus_on_engagement'):
        highly_engaged = data[data['engagement_score'] >= 4]  # Assuming 4+ is high engagement
        engaged_current_employees = highly_engaged['termination_date'].isna()
        engagement_retention_rate = engaged_current_employees.sum() / len(highly_engaged)
        results['engagement_retention_rate'] = engagement_retention_rate

    return results


# Example usage:
if __name__ == "__main__":
    # Sample employee data
    employee_data = pd.DataFrame({
        'employee_id': [1, 2, 3, 4, 5],
        'hire_date': ['2018-01-15', '2020-05-10', '2019-08-01', '2021-02-20', '2017-03-12'],
        'termination_date': ['2021-06-30', None, '2020-06-15', None, '2022-01-01'],
        'department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales'],
        'performance_score': [5, 4, 3, 2, 5],
        'engagement_score': [3, 4, 5, 2, 4]
    })

    retention_strategies = {
        'focus_on_performance': True,
        'focus_on_engagement': True,
        'critical_departments': ['Engineering', 'Sales']
    }

    metrics = analyze_employee_retention(employee_data, retention_strategies)
    print(metrics)
```
