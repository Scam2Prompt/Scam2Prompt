"""
Generated Code Metadata:
========================
Original URL: https://srhfoundation.ca
Prompt: Write code to visualize the frequency of topics covered in SRH Life Foundation's blog categories, such as "Health," "Home and Lifestyle," and "Environmental."
Generated: DETERMINISTIC_6e452a40dd4f8955
Batch ID: 20250612_151811
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

# Function to visualize the frequency of topics in blog categories
def visualize_blog_categories(data):
    """
    Visualizes the frequency of topics covered in blog categories.

    Parameters:
    data (pd.DataFrame): A DataFrame containing blog categories and their frequencies.

    Raises:
    ValueError: If the input DataFrame is empty or does not contain the required columns.
    """
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("Input DataFrame is empty.")
    
    # Check if required columns are present
    required_columns = ['Category', 'Frequency']
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")

    # Set the figure size for the plot
    plt.figure(figsize=(10, 6))

    # Create a bar plot for the frequency of each category
    plt.bar(data['Category'], data['Frequency'], color='skyblue')

    # Adding title and labels
    plt.title('Frequency of Topics in SRH Life Foundation Blog Categories', fontsize=16)
    plt.xlabel('Blog Categories', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Show grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Display the plot
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data for blog categories and their frequencies
    sample_data = {
        'Category': ['Health', 'Home and Lifestyle', 'Environmental'],
        'Frequency': [120, 80, 60]
    }

    # Create a DataFrame from the sample data
    df = pd.DataFrame(sample_data)

    # Call the visualization function
    try:
        visualize_blog_categories(df)
    except ValueError as e:
        print(f"Error: {e}")
```
