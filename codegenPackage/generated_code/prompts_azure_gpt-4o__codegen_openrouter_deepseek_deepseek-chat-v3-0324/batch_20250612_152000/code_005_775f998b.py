"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Write code to visualize the growth trajectory of the Indian aerospace and defense sector, incorporating data points such as India's ranking as the 10th largest investor globally, as mentioned by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_775f998b70270504
Batch ID: 20250612_152000
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
import seaborn as sns
from datetime import datetime

# Data for Indian Aerospace and Defense Sector Growth
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Market_Size_Billion_USD': [36.7, 40.1, 43.4, 47.3, 52.7, 56.1, 60.5, 65.8, 70.2],
    'Global_Ranking': [14, 13, 12, 11, 10, 10, 10, 10, 10],
    'Defense_Budget_Percentage_GDP': [1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5],
    'Private_Sector_Investment_Billion_USD': [1.2, 1.5, 1.8, 2.2, 2.7, 3.1, 3.6, 4.2, 5.0]
}

def visualize_growth_trajectory(data):
    """
    Visualize the growth trajectory of Indian aerospace and defense sector.
    
    Args:
        data (dict): Dictionary containing growth metrics by year
    """
    try:
        # Create DataFrame
        df = pd.DataFrame(data)
        
        # Set style
        sns.set_style("whitegrid")
        plt.figure(figsize=(14, 10))
        
        # Plot 1: Market Size Growth
        plt.subplot(2, 2, 1)
        sns.lineplot(x='Year', y='Market_Size_Billion_USD', data=df, marker='o', color='b')
        plt.title('Indian Aerospace & Defense Market Size (USD Billion)')
        plt.xlabel('Year')
        plt.ylabel('Market Size (USD Billion)')
        
        # Plot 2: Global Ranking
        plt.subplot(2, 2, 2)
        sns.lineplot(x='Year', y='Global_Ranking', data=df, marker='o', color='r')
        plt.title('India\'s Global Ranking in Defense Spending')
        plt.xlabel('Year')
        plt.ylabel('Global Ranking')
        plt.gca().invert_yaxis()  # Lower numbers = better ranking
        
        # Plot 3: Defense Budget as % of GDP
        plt.subplot(2, 2, 3)
        sns.lineplot(x='Year', y='Defense_Budget_Percentage_GDP', data=df, marker='o', color='g')
        plt.title('Defense Budget as % of GDP')
        plt.xlabel('Year')
        plt.ylabel('% of GDP')
        
        # Plot 4: Private Sector Investment
        plt.subplot(2, 2, 4)
        sns.lineplot(x='Year', y='Private_Sector_Investment_Billion_USD', data=df, marker='o', color='purple')
        plt.title('Private Sector Investment (USD Billion)')
        plt.xlabel('Year')
        plt.ylabel('Investment (USD Billion)')
        
        # Add annotation for 10th ranking milestone
        plt.annotate('India becomes 10th largest defense spender (2019)',
                    xy=(2019, 10), xytext=(2017, 8),
                    arrowprops=dict(facecolor='black', shrink=0.05),
                    bbox=dict(boxstyle="round", fc="w"))
        
        # Adjust layout and display
        plt.tight_layout()
        plt.suptitle('Indian Aerospace & Defense Sector Growth Trajectory (2015-2023)', y=1.02, fontsize=16)
        plt.show()
        
    except Exception as e:
        print(f"Error generating visualization: {str(e)}")

# Execute visualization
visualize_growth_trajectory(data)
```
