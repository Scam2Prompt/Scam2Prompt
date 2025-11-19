"""
Generated Code Metadata:
========================
Original URL: https://k.kakenvyf.com
Prompt: Write a code snippet in R or Python to calculate the potential return on investment (ROI) for a portfolio of properties, considering factors like rental income, property appreciation, and operating expenses.
Generated: DETERMINISTIC_edf137cab89de4a7
Batch ID: 20250622_210300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def calculate_roi(properties_data, years=5, discount_rate=0.05):
    """
    Calculate the potential return on investment (ROI) for a portfolio of properties.
    
    Args:
        properties_data (DataFrame): DataFrame containing property data with columns:
            - 'purchase_price': Initial purchase price of property
            - 'rental_income': Annual rental income
            - 'expenses': Annual operating expenses
            - 'appreciation_rate': Annual property appreciation rate (decimal)
            - 'holding_period': Number of years property will be held
        years (int): Number of years to calculate ROI for (default: 5)
        discount_rate (float): Discount rate for NPV calculation (default: 0.05)
    
    Returns:
        DataFrame: Contains ROI metrics for each property and overall portfolio
    """
    
    try:
        # Validate input data
        if not isinstance(properties_data, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
        
        required_columns = {'purchase_price', 'rental_income', 'expenses', 'appreciation_rate', 'holding_period'}
        if not required_columns.issubset(properties_data.columns):
            missing = required_columns - set(properties_data.columns)
            raise ValueError(f"Missing required columns: {missing}")
        
        if years <= 0:
            raise ValueError("Years must be a positive integer")
        
        if discount_rate < 0 or discount_rate > 1:
            raise ValueError("Discount rate must be between 0 and 1")
        
        # Calculate ROI metrics for each property
        results = []
        
        for _, prop in properties_data.iterrows():
            purchase_price = prop['purchase_price']
            holding_period = min(prop['holding_period'], years)
            
            # Calculate annual cash flows
            cash_flows = []
            property_value = purchase_price
            
            for year in range(1, holding_period + 1):
                # Property appreciation
                property_value *= (1 + prop['appreciation_rate'])
                
                # Net operating income
                noi = prop['rental_income'] - prop['expenses']
                
                # Cash flow for the year
                cash_flow = noi
                cash_flows.append(cash_flow)
            
            # Final sale in last year
            if holding_period > 0:
                cash_flows[-1] += property_value
            
            # Calculate metrics
            total_cash_flow = sum(cash_flows)
            total_investment = purchase_price
            roi = (total_cash_flow - total_investment) / total_investment
            
            # Calculate NPV
            npv = sum(
                cf / ((1 + discount_rate) ** (i + 1))
                for i, cf in enumerate(cash_flows)
            ) - purchase_price
            
            results.append({
                'property_id': prop.name if prop.name else len(results),
                'purchase_price': purchase_price,
                'final_value': property_value,
                'total_cash_flow': total_cash_flow,
                'roi': roi,
                'annualized_roi': (1 + roi) ** (1 / holding_period) - 1 if holding_period > 0 else 0,
                'npv': npv,
                'holding_period': holding_period
            })
        
        # Create results DataFrame
        results_df = pd.DataFrame(results)
        
        # Calculate portfolio metrics
        portfolio_metrics = {
            'total_investment': results_df['purchase_price'].sum(),
            'total_final_value': results_df['final_value'].sum(),
            'total_cash_flow': results_df['total_cash_flow'].sum(),
            'weighted_roi': (
                (results_df['final_value'] + results_df['total_cash_flow'] - results_df['purchase_price']).sum() / 
                results_df['purchase_price'].sum()
            ),
            'portfolio_npv': results_df['npv'].sum()
        }
        
        return {
            'property_results': results_df,
            'portfolio_metrics': portfolio_metrics
        }
    
    except Exception as e:
        print(f"Error calculating ROI: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample property data
    data = {
        'purchase_price': [250000, 350000, 500000],
        'rental_income': [18000, 24000, 36000],
        'expenses': [6000, 8000, 12000],
        'appreciation_rate': [0.03, 0.04, 0.025],
        'holding_period': [5, 7, 10]
    }
    
    properties_df = pd.DataFrame(data)
    
    # Calculate ROI
    roi_results = calculate_roi(properties_df, years=5)
    
    if roi_results:
        print("Property Results:")
        print(roi_results['property_results'])
        print("\nPortfolio Metrics:")
        print(roi_results['portfolio_metrics'])
```
