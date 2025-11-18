"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dexodoor.com
Prompt: Suggest tools or libraries for visualizing the 350+ UPVC window and door designs offered by Dexodoor, with a focus on modern and elegant styles.
Generated: DETERMINISTIC_8c059eca1ab9fa75
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Function to visualize UPVC window and door designs
def visualize_designs(designs_df):
    """
    Visualizes UPVC window and door designs using a bar plot.
    
    Parameters:
    designs_df (pd.DataFrame): DataFrame containing design names and their respective popularity scores.
    
    Returns:
    None: Displays a plot of the design popularity.
    
    Raises:
    ValueError: If the DataFrame is empty or does not contain the required columns.
    """
    # Check if the DataFrame is empty
    if designs_df.empty:
        raise ValueError("The designs DataFrame is empty. Please provide valid data.")
    
    # Check for required columns
    required_columns = {'Design Name', 'Popularity Score'}
    if not required_columns.issubset(designs_df.columns):
        raise ValueError(f"The DataFrame must contain the following columns: {required_columns}")
    
    # Setting the style for the plot
    sns.set(style="whitegrid")
    
    # Create a bar plot
    plt.figure(figsize=(12, 8))
    sns.barplot(data=designs_df, x='Popularity Score', y='Design Name', palette='viridis')
    
    # Adding titles and labels
    plt.title('Popularity of UPVC Window and Door Designs', fontsize=16)
    plt.xlabel('Popularity Score', fontsize=12)
    plt.ylabel('Design Name', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    
    # Show the plot
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    data = {
        'Design Name': [
            'Classic', 'Modern', 'Elegant', 'Contemporary', 'Minimalist', 
            'Geometric', 'Retro', 'Rustic', 'Industrial', 'Art Deco'
        ],
        'Popularity Score': [85, 90, 95, 80, 75, 70, 60, 50, 65, 55]
    }

    # Creating a DataFrame
    designs_df = pd.DataFrame(data)

    # Visualizing the designs
    try:
        visualize_designs(designs_df)
    except ValueError as e:
        print(f"Error: {e}")
```
