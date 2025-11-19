"""
Generated Code Metadata:
========================
Original URL: https://publicvibeindia.blogspot.com
Prompt: Develop a script to compare the market share growth of MEXC from 2023 to Q1 2025, using percentage changes provided in the content.
Generated: DETERMINISTIC_394618bc77aecd8d
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt

def compare_market_share_growth(data):
    """
    Compares the market share growth of MEXC from 2023 to Q1 2025 using percentage changes.
    
    Args:
        data (dict): Dictionary containing the market share percentages for each period.
                     Example: {'2023': 5.2, '2024': 6.8, 'Q1_2025': 7.5}
    
    Returns:
        pd.DataFrame: DataFrame with the market share data and growth calculations.
    """
    try:
        # Create DataFrame from input data
        df = pd.DataFrame.from_dict(data, orient='index', columns=['Market Share (%)'])
        df.index.name = 'Period'
        df.reset_index(inplace=True)
        
        # Calculate growth percentage from 2023 to each subsequent period
        base_2023 = df[df['Period'] == '2023']['Market Share (%)'].values[0]
        df['Growth from 2023 (%)'] = ((df['Market Share (%)'] - base_2023) / base_2023) * 100
        
        # Calculate quarter-over-quarter growth (for Q1 2025)
        if 'Q1_2025' in data and '2024' in data:
            qoq_growth = ((data['Q1_2025'] - data['2024']) / data['2024']) * 100
            df['QoQ Growth (%)'] = 0.0  # Initialize column
            df.loc[df['Period'] == 'Q1_2025', 'QoQ Growth (%)'] = qoq_growth
        
        return df
    
    except Exception as e:
        print(f"Error processing market share data: {str(e)}")
        return None

def plot_growth_comparison(df):
    """
    Plots the market share growth comparison.
    
    Args:
        df (pd.DataFrame): DataFrame containing market share and growth data.
    """
    try:
        if df is None:
            raise ValueError("No data provided for plotting")
            
        plt.figure(figsize=(10, 6))
        
        # Plot market share
        plt.subplot(2, 1, 1)
        plt.bar(df['Period'], df['Market Share (%)'], color='skyblue')
        plt.title('MEXC Market Share Comparison (2023-Q1 2025)')
        plt.ylabel('Market Share (%)')
        
        # Plot growth from 2023
        plt.subplot(2, 1, 2)
        periods = df['Period'][df['Period'] != '2023']  # Exclude base year
        growth = df['Growth from 2023 (%)'][df['Period'] != '2023']
        plt.bar(periods, growth, color='lightgreen')
        plt.title('Growth from 2023 (%)')
        plt.ylabel('Growth Percentage (%)')
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error generating plot: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample data (replace with actual market share percentages)
    market_share_data = {
        '2023': 5.2,
        '2024': 6.8,
        'Q1_2025': 7.5
    }
    
    # Compare growth
    result_df = compare_market_share_growth(market_share_data)
    
    if result_df is not None:
        print("Market Share Growth Comparison:")
        print(result_df)
        
        # Plot results
        plot_growth_comparison(result_df)
```
