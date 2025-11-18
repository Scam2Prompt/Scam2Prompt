"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Create a script to analyze and visualize the impact of different risk levels on savings returns, as described in the "Sur-Mesure" formula on pipelinefinanceconseil.com. Include graphs to illustrate high-risk versus low-risk scenarios.
Generated: DETERMINISTIC_c891d4cbff7cb179
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for the plots
sns.set(style="whitegrid")

def calculate_returns(principal, rate_of_return, years):
    """
    Calculate future value of an investment based on principal,
    annual rate of return, and number of years.
    
    :param principal: Initial amount of money invested
    :param rate_of_return: Annual rate of return (in decimal form)
    :param years: Number of years the money is invested for
    :return: Future value of the investment
    """
    try:
        future_value = principal * (1 + rate_of_return) ** years
        return future_value
    except Exception as e:
        print(f"Error in calculating returns: {e}")
        return None

def analyze_risk_levels(principal, years):
    """
    Analyze the impact of different risk levels on savings returns.
    
    :param principal: Initial investment amount
    :param years: Number of years to analyze
    :return: DataFrame containing returns for different risk levels
    """
    # Define risk levels and their corresponding rates of return
    risk_levels = {
        "Low Risk": 0.03,      # 3% annual return
        "Moderate Risk": 0.06, # 6% annual return
        "High Risk": 0.10      # 10% annual return
    }
    
    results = []

    # Calculate future value for each risk level
    for risk, rate in risk_levels.items():
        future_value = calculate_returns(principal, rate, years)
        results.append({"Risk Level": risk, "Future Value": future_value})

    return pd.DataFrame(results)

def plot_returns(returns_df):
    """
    Plot the future values of investments for different risk levels.
    
    :param returns_df: DataFrame containing risk levels and their future values
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(data=returns_df, x='Risk Level', y='Future Value', palette='viridis')
    plt.title('Impact of Risk Levels on Savings Returns')
    plt.xlabel('Risk Level')
    plt.ylabel('Future Value ($)')
    plt.yscale('log')  # Use logarithmic scale for better visualization
    plt.grid(axis='y')
    plt.show()

def main():
    """
    Main function to execute the analysis and visualization of savings returns.
    """
    # User inputs
    try:
        principal = float(input("Enter the principal amount ($): "))
        years = int(input("Enter the number of years: "))
        
        if principal < 0 or years < 0:
            raise ValueError("Principal and years must be non-negative.")
        
        # Analyze the impact of different risk levels
        returns_df = analyze_risk_levels(principal, years)
        
        # Plot the results
        plot_returns(returns_df)
        
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
