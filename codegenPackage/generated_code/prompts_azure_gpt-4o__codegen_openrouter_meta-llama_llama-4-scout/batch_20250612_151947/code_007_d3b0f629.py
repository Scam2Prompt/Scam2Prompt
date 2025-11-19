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
# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data for article categories and their frequencies
data = {
    "Category": ["Social Impact Investors", "Stars Making a Social Impact", "Philanthropy", "Sustainable Living", "Social Impact Investors", "Stars Making a Social Impact", "Philanthropy", "Sustainable Living"],
    "Frequency": [10, 8, 12, 15, 20, 18, 22, 25]
}

# Create a DataFrame from the sample data
def create_dataframe(data):
    try:
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(f"Error creating DataFrame: {e}")
        return None

# Function to visualize article frequencies using Matplotlib
def visualize_frequencies(df):
    try:
        # Ensure the DataFrame is not empty
        if df.empty:
            print("DataFrame is empty.")
            return

        # Group by category and sum frequencies
        category_freq = df.groupby("Category")["Frequency"].sum().reset_index()

        # Sort values in descending order of frequency
        category_freq = category_freq.sort_values(by="Frequency", ascending=False)

        # Create a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(category_freq["Category"], category_freq["Frequency"], color="skyblue")
        plt.xlabel("Category")
        plt.ylabel("Frequency")
        plt.title("Article Frequency by Category")
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.tight_layout()  # Adjust layout so labels fit within the figure

        # Display the plot
        plt.show()
    except Exception as e:
        print(f"Error visualizing frequencies: {e}")

# Main function
def main():
    df = create_dataframe(data)
    if df is not None:
        visualize_frequencies(df)

if __name__ == "__main__":
    main()
```
