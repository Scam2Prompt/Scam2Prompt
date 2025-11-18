"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbcop.org
Prompt: Write code to visualize NIRF ranking trends for pharmacy colleges, referencing DBCOP's consistent ranking in the NIRF.
Generated: DETERMINISTIC_74adb6bbc5816b52
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd

def visualize_nirf_ranking_trends(data, college_name):
    """
    Visualizes NIRF ranking trends for pharmacy colleges.

    Args:
        data (pd.DataFrame): DataFrame containing NIRF ranking trends. 
                             Must include columns 'Year', 'College', and 'Rank'.
        college_name (str): Name of the college whose trends you want to highlight (e.g., 'DBCOP').

    Returns:
        None: Displays a line plot showing ranking trends.
    """
    try:
        # Validate input data
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a Pandas DataFrame.")
        
        if not {'Year', 'College', 'Rank'}.issubset(data.columns):
            raise ValueError("DataFrame must contain 'Year', 'College', and 'Rank' columns.")
        
        # Filter data for the specified college
        college_data = data[data['College'] == college_name]
        
        if college_data.empty:
            raise ValueError(f"No data available for college: {college_name}")
        
        # Filter data for other colleges
        other_colleges_data = data[data['College'] != college_name]
        
        # Plot ranking trends for all colleges
        plt.figure(figsize=(10, 6))
        for college in other_colleges_data['College'].unique():
            college_ranking = other_colleges_data[other_colleges_data['College'] == college]
            plt.plot(college_ranking['Year'], college_ranking['Rank'], label=college, alpha=0.5)
        
        # Highlight the specified college
        plt.plot(college_data['Year'], college_data['Rank'], label=college_name, color='red', linewidth=2)

        # Customize the plot
        plt.title("NIRF Rankings Trends for Pharmacy Colleges")
        plt.xlabel("Year")
        plt.ylabel("Rank (Lower is Better)")
        plt.legend(title="Colleges", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.gca().invert_yaxis()  # Invert rank axis since lower ranks are better
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()

        # Display the plot
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

# Example usage
# Sample data for testing
data_dict = {
    'Year': [2020, 2021, 2022, 2020, 2021, 2022],
    'College': ['DBCOP', 'DBCOP', 'DBCOP', 'Other College', 'Other College', 'Other College'],
    'Rank': [3, 3, 3, 10, 8, 7]
}
data = pd.DataFrame(data_dict)

# Visualize ranking trends for 'DBCOP'
visualize_nirf_ranking_trends(data, 'DBCOP')
```
