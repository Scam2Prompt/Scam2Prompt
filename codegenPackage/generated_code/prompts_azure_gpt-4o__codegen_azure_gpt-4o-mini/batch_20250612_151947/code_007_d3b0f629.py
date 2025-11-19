"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Write code to visualize the frequency of articles published in different categories like "Social Impact Investors" and "Stars Making a Social Impact" using Matplotlib.
Generated: DETERMINISTIC_d3b0f629e6c231d9
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import pandas as pd

# Sample data representing the frequency of articles in different categories
data = {
    'Category': ['Social Impact Investors', 'Stars Making a Social Impact', 'Social Entrepreneurs', 'Impact Measurement'],
    'Frequency': [25, 15, 30, 10]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Function to visualize article frequency by category
def visualize_article_frequency(df):
    """
    Visualizes the frequency of articles published in different categories using a bar chart.

    Parameters:
    df (pd.DataFrame): DataFrame containing 'Category' and 'Frequency' columns.

    Raises:
    ValueError: If the DataFrame does not contain the required columns.
    """
    # Check if the required columns are in the DataFrame
    if not all(col in df.columns for col in ['Category', 'Frequency']):
        raise ValueError("DataFrame must contain 'Category' and 'Frequency' columns.")

    # Set the figure size for better visibility
    plt.figure(figsize=(10, 6))

    # Create a bar chart
    plt.bar(df['Category'], df['Frequency'], color='skyblue')

    # Add title and labels
    plt.title('Frequency of Articles Published by Category', fontsize=16)
    plt.xlabel('Category', fontsize=14)
    plt.ylabel('Number of Articles', fontsize=14)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Add grid for easier visualization
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the plot
    plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
    plt.show()

# Call the function to visualize the data
if __name__ == "__main__":
    try:
        visualize_article_frequency(df)
    except Exception as e:
        print(f"An error occurred: {e}")
```
