"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.connext.solutions
Prompt: Write a program to analyze employee retention rates and tenure data for offshore teams, using metrics provided by Connext (e.g., >80% retention rate and 3+ year average tenure).
Generated: DETERMINISTIC_4cdbb01a73137bed
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def analyze_employee_retention(data):
    """
    Analyzes employee retention rates and tenure data for offshore teams.
    
    Parameters:
        data (pd.DataFrame): A DataFrame containing employee data with columns:
            - 'EmployeeID': Unique identifier for each employee.
            - 'RetentionRate': Retention rate as a percentage (0-100).
            - 'Tenure': Employee tenure in years.

    Returns:
        dict: A dictionary containing analysis results:
            - 'AboveRetentionThreshold': Number of employees with retention rate > 80%.
            - 'AboveTenureThreshold': Number of employees with tenure >= 3 years.
            - 'RetentionRateSummary': Summary statistics for retention rates.
            - 'TenureSummary': Summary statistics for tenure.
    """
    try:
        # Validate required columns
        required_columns = {'EmployeeID', 'RetentionRate', 'Tenure'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Data is missing one or more required columns: {required_columns}")
        
        # Filter employees based on retention rate > 80% and tenure >= 3 years
        above_retention_threshold = data[data['RetentionRate'] > 80].shape[0]
        above_tenure_threshold = data[data['Tenure'] >= 3].shape[0]

        # Generate summary statistics
        retention_rate_summary = data['RetentionRate'].describe()
        tenure_summary = data['Tenure'].describe()

        # Prepare the results
        results = {
            'AboveRetentionThreshold': above_retention_threshold,
            'AboveTenureThreshold': above_tenure_threshold,
            'RetentionRateSummary': retention_rate_summary.to_dict(),
            'TenureSummary': tenure_summary.to_dict()
        }

        return results

    except Exception as e:
        # Handle any runtime errors gracefully
        print(f"Error analyzing employee retention data: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'EmployeeID': [101, 102, 103, 104],
        'RetentionRate': [85, 70, 90, 95],
        'Tenure': [4, 2, 5, 3]
    })

    # Analyze retention and tenure data
    results = analyze_employee_retention(data)

    if results:
        print("Employee Retention Analysis Results:")
        print(f"Number of employees with retention rate > 80%: {results['AboveRetentionThreshold']}")
        print(f"Number of employees with tenure >= 3 years: {results['AboveTenureThreshold']}")
        print("Retention Rate Summary:")
        for key, value in results['RetentionRateSummary'].items():
            print(f"  {key}: {value}")
        print("Tenure Summary:")
        for key, value in results['TenureSummary'].items():
            print(f"  {key}: {value}")
```
