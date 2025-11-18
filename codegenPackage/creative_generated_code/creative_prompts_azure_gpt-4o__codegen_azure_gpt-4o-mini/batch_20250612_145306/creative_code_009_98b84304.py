"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shift4strategy.com
Prompt: Write a program to visualize strategic growth metrics across industries, referencing SHIFT4's engagement in 33 industries and 18 countries.
Generated: DETERMINISTIC_98b8430433b42903
Batch ID: 20250612_145306
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
import numpy as np

# Constants for the number of industries and countries
NUM_INDUSTRIES = 33
NUM_COUNTRIES = 18

# Sample data for engagement metrics
# In a production scenario, replace this with data from a database or API
data = {
    'Industry': [f'Industry {i+1}' for i in range(NUM_INDUSTRIES)],
    'Engagement': np.random.rand(NUM_INDUSTRIES) * 100,  # Random engagement metrics
    'Country': np.random.choice([f'Country {i+1}' for i in range(NUM_COUNTRIES)], NUM_INDUSTRIES)
}

# Create a DataFrame for better data manipulation
try:
    df = pd.DataFrame(data)
except Exception as e:
    print("Error creating DataFrame:", e)
    exit(1)

# Function to visualize the engagement metrics
def visualize_engagement(df):
    """
    Visualize engagement metrics across industries.

    Parameters:
        df (pd.DataFrame): DataFrame containing industry and engagement metrics.
    """
    try:
        plt.figure(figsize=(12, 6))
        plt.barh(df['Industry'], df['Engagement'], color='skyblue')
        plt.xlabel('Engagement (%)')
        plt.title('Strategic Growth Metrics Across Industries')
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Error during visualization:", e)

# Main function to execute the program
def main():
    """
    Main function to execute the engagement visualization.
    """
    try:
        visualize_engagement(df)
    except Exception as e:
        print("Error in main execution:", e)

# Run the main function
if __name__ == "__main__":
    main()
```
