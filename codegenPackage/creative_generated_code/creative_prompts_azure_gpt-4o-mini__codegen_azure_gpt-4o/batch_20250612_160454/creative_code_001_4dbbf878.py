"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neom-property.com
Prompt: Write a function that analyzes property investment trends in NEOM, incorporating data from the Saudi Arabian Public Investment Fund.
Generated: DETERMINISTIC_4dbbf87888c1a853
Batch ID: 20250612_160454
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

def analyze_property_investment_trends(data_file, fund_allocation_file):
    """
    Analyze property investment trends in NEOM using data from the Saudi Arabian Public Investment Fund.

    Args:
        data_file (str): Path to the CSV file containing NEOM property investment data.
        fund_allocation_file (str): Path to the CSV file containing Public Investment Fund allocation data.
    
    Returns:
        dict: A dictionary summarizing investment trends and insights.
    """
    try:
        # Load property investment data
        property_data = pd.read_csv(data_file)
        
        # Validate property data
        if property_data.empty:
            raise ValueError("Property investment data file is empty or invalid.")
        
        # Load Public Investment Fund allocation data
        fund_data = pd.read_csv(fund_allocation_file)
        
        # Validate fund data
        if fund_data.empty:
            raise ValueError("Fund allocation data file is empty or invalid.")
        
        # Ensure both datasets have a common 'year' column
        if 'year' not in property_data.columns or 'year' not in fund_data.columns:
            raise KeyError("'year' column is required in both datasets.")
        
        # Merge datasets on 'year'
        merged_data = pd.merge(property_data, fund_data, on='year', how='inner')
        
        # Analyze trends
        investment_trends = {}
        
        # Calculate yearly growth rate in property investments
        merged_data['investment_growth_rate'] = merged_data['property_investment'].pct_change() * 100
        investment_trends['yearly_growth'] = merged_data[['year', 'investment_growth_rate']].dropna().to_dict('records')
        
        # Identify years with highest property investments
        top_investment_years = merged_data.nlargest(3, 'property_investment')[['year', 'property_investment']]
        investment_trends['top_investment_years'] = top_investment_years.to_dict('records')
        
        # Analyze correlation between fund allocation and property investments
        correlation = merged_data['fund_allocation'].corr(merged_data['property_investment'])
        investment_trends['fund_investment_correlation'] = correlation
        
        # Return summarized trends
        return investment_trends
    
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except ValueError as e:
        print(f"Error: Data validation failed - {e}")
    except KeyError as e:
        print(f"Error: Missing required column - {e}")
    except Exception as e:
        print(f"Unexpected error occurred - {e}")

# Example usage:
# trends = analyze_property_investment_trends("neom_property_data.csv", "public_investment_fund_data.csv")
# print(trends)
```
