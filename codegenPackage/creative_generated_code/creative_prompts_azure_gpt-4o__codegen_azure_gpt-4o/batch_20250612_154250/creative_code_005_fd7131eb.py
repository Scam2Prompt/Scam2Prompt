"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://octavepartners.com
Prompt: Write code to analyze business performance metrics and suggest optimization strategies, inspired by the business advisory services offered by Octave Partners.
Generated: DETERMINISTIC_fd7131eb73972cda
Batch ID: 20250612_154250
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

def analyze_business_performance(data):
    """
    Analyze business performance metrics and suggest optimization strategies.

    :param data: pandas DataFrame containing business metrics.
                 Expected columns: 'Revenue', 'Cost', 'Profit', 'CustomerSatisfaction', 'EmployeeRetention'
    :return: Dictionary containing analysis results and optimization suggestions.
    """
    try:
        # Validate input data
        required_columns = ['Revenue', 'Cost', 'Profit', 'CustomerSatisfaction', 'EmployeeRetention']
        if not all(col in data.columns for col in required_columns):
            raise ValueError("Input data must contain the following columns: "
                             + ", ".join(required_columns))

        # Initialize results dictionary
        results = {}

        # Basic metrics analysis
        results['AverageRevenue'] = data['Revenue'].mean()
        results['AverageCost'] = data['Cost'].mean()
        results['AverageProfit'] = data['Profit'].mean()
        results['CustomerSatisfactionMedian'] = data['CustomerSatisfaction'].median()
        results['EmployeeRetentionMedian'] = data['EmployeeRetention'].median()

        # Profit margin analysis
        data['ProfitMargin'] = (data['Profit'] / data['Revenue']) * 100
        results['AverageProfitMargin'] = data['ProfitMargin'].mean()

        # Strategy suggestions based on metrics
        suggestions = []

        # Suggestion for reducing costs
        if results['AverageCost'] > results['AverageRevenue'] * 0.5:
            suggestions.append("Consider cost-cutting strategies to improve profitability.")

        # Suggestion for improving customer satisfaction
        if results['CustomerSatisfactionMedian'] < 70:
            suggestions.append("Focus on improving customer satisfaction through better service or product quality.")

        # Suggestion for enhancing employee retention
        if results['EmployeeRetentionMedian'] < 80:
            suggestions.append("Invest in employee engagement initiatives to improve retention.")

        # Suggestion for optimizing profit margin
        if results['AverageProfitMargin'] < 20:
            suggestions.append("Explore ways to increase revenue or reduce costs to improve profit margins.")

        # Add suggestions to results
        results['Suggestions'] = suggestions

        return results

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return {"Error": str(ve)}

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"Error": str(e)}


# Example Usage
if __name__ == "__main__":
    # Sample business performance metrics
    sample_data = pd.DataFrame({
        'Revenue': [100000, 120000, 130000, 110000],
        'Cost': [60000, 70000, 80000, 65000],
        'Profit': [40000, 50000, 50000, 45000],
        'CustomerSatisfaction': [75, 80, 65, 70],
        'EmployeeRetention': [85, 90, 78, 82]
    })

    # Analyze and get suggestions
    analysis_results = analyze_business_performance(sample_data)
    print("Analysis Results and Suggestions:")
    for key, value in analysis_results.items():
        print(f"{key}: {value}")
```
