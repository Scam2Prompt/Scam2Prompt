"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Illustrate how to use a library to visualize the differences between various fleece types offered by Shaoxing Eagles Textile Co., Ltd.
Generated: DETERMINISTIC_4b6b32ffe9ba535a
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the aesthetic style of the visualizations
sns.set(style="whitegrid")

# Sample data representing different fleece types and their characteristics
data = {
    'Fleece Type': ['Polar Fleece', 'Micro Fleece', 'Sherpa Fleece', 'Coral Fleece'],
    'Thickness (mm)': [5, 3, 6, 4],
    'Weight (g/m²)': [250, 200, 300, 280],
    'Warmth Rating (1-10)': [8, 6, 9, 7]
}

# Creating a DataFrame from the sample data
try:
    fleece_df = pd.DataFrame(data)
except Exception as e:
    print(f"Error creating DataFrame: {e}")
    raise

# Function to visualize fleece types
def visualize_fleece_types(df):
    """Visualizes the differences between various fleece types using bar plots.

    Args:
        df (pd.DataFrame): DataFrame containing fleece type characteristics.
    """
    try:
        # Set up the matplotlib figure
        plt.figure(figsize=(14, 6))

        # Create a bar plot for Thickness
        plt.subplot(1, 3, 1)
        sns.barplot(x='Fleece Type', y='Thickness (mm)', data=df, palette='Blues_d')
        plt.title('Thickness of Fleece Types (mm)')
        plt.ylabel('Thickness (mm)')
        plt.xticks(rotation=45)

        # Create a bar plot for Weight
        plt.subplot(1, 3, 2)
        sns.barplot(x='Fleece Type', y='Weight (g/m²)', data=df, palette='Greens_d')
        plt.title('Weight of Fleece Types (g/m²)')
        plt.ylabel('Weight (g/m²)')
        plt.xticks(rotation=45)

        # Create a bar plot for Warmth Rating
        plt.subplot(1, 3, 3)
        sns.barplot(x='Fleece Type', y='Warmth Rating (1-10)', data=df, palette='Reds_d')
        plt.title('Warmth Rating of Fleece Types (1-10)')
        plt.ylabel('Warmth Rating')
        plt.xticks(rotation=45)

        # Adjust layout
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error during visualization: {e}")
        raise

# Execute the visualization function
if __name__ == "__main__":
    visualize_fleece_types(fleece_df)
```
