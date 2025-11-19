"""
Generated Code Metadata:
========================
Original URL: https://shift4strategy.com
Prompt: Write a program to visualize strategic growth metrics across industries, referencing SHIFT4's engagement in 33 industries and 18 countries.
Generated: DETERMINISTIC_98b8430433b42903
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define a function to visualize growth metrics
def visualize_growth_metrics(industry_data):
    """
    Visualize strategic growth metrics across industries.

    Args:
        industry_data (dict): A dictionary containing industry data.
            Each key is an industry, and each value is another dictionary
            with 'growth_rate' and 'country_count' keys.

    Returns:
        None
    """

    # Create a pandas DataFrame from the industry data
    df = pd.DataFrame({
        'Industry': list(industry_data.keys()),
        'Growth Rate': [data['growth_rate'] for data in industry_data.values()],
        'Country Count': [data['country_count'] for data in industry_data.values()]
    })

    # Sort the DataFrame by growth rate in descending order
    df = df.sort_values(by='Growth Rate', ascending=False)

    # Create a figure and axis object
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Plot growth rates as a bar chart
    ax[0].bar(df['Industry'], df['Growth Rate'])
    ax[0].set_title('Growth Rates Across Industries')
    ax[0].set_xlabel('Industry')
    ax[0].set_ylabel('Growth Rate')
    ax[0].tick_params(axis='x', rotation=90)

    # Plot country counts as a scatter plot
    ax[1].scatter(df['Industry'], df['Country Count'])
    ax[1].set_title('Country Count Across Industries')
    ax[1].set_xlabel('Industry')
    ax[1].set_ylabel('Country Count')
    ax[1].tick_params(axis='x', rotation=90)

    # Layout so plots do not overlap
    fig.tight_layout()

    # Show the plot
    plt.show()

# Define industry data for SHIFT4
industry_data = {
    'E-commerce': {'growth_rate': 0.25, 'country_count': 10},
    'Retail': {'growth_rate': 0.15, 'country_count': 8},
    'Food Service': {'growth_rate': 0.30, 'country_count': 12},
    'Travel': {'growth_rate': 0.20, 'country_count': 15},
    'Software': {'growth_rate': 0.40, 'country_count': 18},
    'Hardware': {'growth_rate': 0.10, 'country_count': 5},
    'Financial Services': {'growth_rate': 0.35, 'country_count': 10},
    'Healthcare': {'growth_rate': 0.28, 'country_count': 8},
    'Education': {'growth_rate': 0.22, 'country_count': 12},
    'Real Estate': {'growth_rate': 0.18, 'country_count': 10},
    'Manufacturing': {'growth_rate': 0.12, 'country_count': 8},
    'Logistics': {'growth_rate': 0.25, 'country_count': 15},
    'Construction': {'growth_rate': 0.08, 'country_count': 10},
    'Media': {'growth_rate': 0.20, 'country_count': 12},
    'Telecommunications': {'growth_rate': 0.30, 'country_count': 18},
    'Energy': {'growth_rate': 0.15, 'country_count': 10},
    'Government': {'growth_rate': 0.10, 'country_count': 8},
    'Non-Profit': {'growth_rate': 0.12, 'country_count': 5},
    'Arts and Entertainment': {'growth_rate': 0.18, 'country_count': 10},
    'Sports': {'growth_rate': 0.22, 'country_count': 8},
    'Hospitality': {'growth_rate': 0.25, 'country_count': 12},
    'Pharmaceuticals': {'growth_rate': 0.35, 'country_count': 15},
    'Biotechnology': {'growth_rate': 0.40, 'country_count': 10},
    'Automotive': {'growth_rate': 0.10, 'country_count': 8},
    'Aerospace': {'growth_rate': 0.15, 'country_count': 10},
    'Defense': {'growth_rate': 0.12, 'country_count': 5},
    'IT Services': {'growth_rate': 0.30, 'country_count': 18},
    'Consulting': {'growth_rate': 0.25, 'country_count': 12},
    'Marketing': {'growth_rate': 0.20, 'country_count': 10},
    'Advertising': {'growth_rate': 0.18, 'country_count': 8},
    'Media and Entertainment': {'growth_rate': 0.22, 'country_count': 15},
}

# Add 13 more industries to meet the 33 industry requirement
industry_data['Agriculture'] = {'growth_rate': 0.08, 'country_count': 10}
industry_data['Banking'] = {'growth_rate': 0.12, 'country_count': 8}
industry_data['Chemicals'] = {'growth_rate': 0.10, 'country_count': 5}
industry_data['Electronics'] = {'growth_rate': 0.25, 'country_count': 12}
industry_data['Environmental Services'] = {'growth_rate': 0.18, 'country_count': 10}
industry_data['Facilities Management'] = {'growth_rate': 0.15, 'country_count': 8}
industry_data['Insurance'] = {'growth_rate': 0.20, 'country_count': 15}
industry_data['Metals and Mining'] = {'growth_rate': 0.12, 'country_count': 10}
industry_data['Paper and Packaging'] = {'growth_rate': 0.10, 'country_count': 5}
industry_data['Private Equity'] = {'growth_rate': 0.25, 'country_count': 12}
industry_data['Professional Services'] = {'growth_rate': 0.22, 'country_count': 10}
industry_data['Real Estate Investment Trusts'] = {'growth_rate': 0.18, 'country_count': 8}
industry_data['Securities and Commodity Exchanges'] = {'growth_rate': 0.30, 'country_count': 18}

# Call the function to visualize growth metrics
visualize_growth_metrics(industry_data)
```
