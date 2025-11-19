"""
Generated Code Metadata:
========================
Original URL: https://relivo.se
Prompt: Write code to create a visualization comparing the nutritional profile of Relivo with other supplements, highlighting its unique combination of ingredients.
Generated: DETERMINISTIC_b38dd4b4b62f601f
Batch ID: 20250612_151459
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

# Set the style for seaborn
sns.set(style="whitegrid")

# Define a function to create a nutritional profile comparison
def plot_nutritional_comparison(data, supplement_name):
    """
    Plots a bar chart comparing the nutritional profile of a given supplement
    with other supplements.

    Parameters:
    data (pd.DataFrame): DataFrame containing nutritional information.
    supplement_name (str): The name of the supplement to highlight.

    Returns:
    None
    """
    try:
        # Check if the required columns are present in the DataFrame
        required_columns = ['Supplement', 'Nutrient', 'Amount']
        if not all(col in data.columns for col in required_columns):
            raise ValueError("DataFrame must contain 'Supplement', 'Nutrient', and 'Amount' columns.")

        # Pivot the DataFrame to get nutrients as rows and supplements as columns
        pivot_data = data.pivot(index='Nutrient', columns='Supplement', values='Amount')

        # Create a bar plot
        plt.figure(figsize=(12, 8))
        ax = pivot_data.plot(kind='bar', alpha=0.7)

        # Highlight the specified supplement
        for bar in ax.patches:
            if bar.get_x() + bar.get_width() / 2 == pivot_data.columns.get_loc(supplement_name):
                bar.set_color('orange')  # Highlight color for the specified supplement

        # Set plot title and labels
        plt.title(f'Nutritional Profile Comparison: {supplement_name} vs Other Supplements', fontsize=16)
        plt.xlabel('Nutrients', fontsize=14)
        plt.ylabel('Amount per Serving', fontsize=14)
        plt.xticks(rotation=45)
        plt.legend(title='Supplements', bbox_to_anchor=(1.05, 1), loc='upper left')

        # Show the plot
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for nutritional comparison
    data = {
        'Supplement': ['Relivo', 'Relivo', 'Supplement A', 'Supplement A', 'Supplement B', 'Supplement B'],
        'Nutrient': ['Protein', 'Fiber', 'Protein', 'Fiber', 'Protein', 'Fiber'],
        'Amount': [20, 5, 15, 3, 25, 4]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Call the function to plot the comparison
    plot_nutritional_comparison(df, 'Relivo')
```
