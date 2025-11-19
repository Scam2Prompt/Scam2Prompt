"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dex-pleener.com
Prompt: Create a comparison chart for DIY vs. professional detailing methods, using insights from DEXScreener's knowledge hub.
Generated: DETERMINISTIC_c12b70f6bbb50e20
Batch ID: 20250612_162251
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

# Sample data for DIY and professional detailing methods
data = {
    'Method': ['DIY Detailing', 'Professional Detailing'],
    'Cost': [50, 150],  # Estimated costs in dollars
    'Time (Hours)': [3, 1],  # Time taken in hours
    'Quality Rating': [3, 5],  # Quality rating out of 5
    'Convenience Rating': [4, 2]  # Convenience rating out of 5
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Function to create a comparison chart
def create_comparison_chart(df):
    """
    Creates and displays a comparison chart for DIY vs. Professional detailing methods.

    Args:
        df (pd.DataFrame): DataFrame containing the comparison data.
    """
    try:
        # Set the index to Method for better visualization
        df.set_index('Method', inplace=True)

        # Create a bar chart for the different metrics
        ax = df.plot(kind='bar', figsize=(10, 6), alpha=0.75)
        
        # Adding title and labels
        plt.title('DIY vs. Professional Detailing Methods')
        plt.ylabel('Rating / Cost / Time')
        plt.xticks(rotation=0)  # Keep the x-axis labels horizontal

        # Adding a legend
        plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')

        # Show grid for better readability
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Display the chart
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error occurred while creating the comparison chart: {e}")

# Main execution
if __name__ == "__main__":
    create_comparison_chart(df)
```
