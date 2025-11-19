"""
Generated Code Metadata:
========================
Original URL: https://liquidlauncher.app
Prompt: Create a timeline visualization of computer hardware evolution using data points from LiquidLauncher’s article on the journey through computer hardware development.
Generated: DETERMINISTIC_a87b0ae2d6fe0b83
Batch ID: 20250612_153925
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

# Define the data for the timeline of computer hardware evolution
data = {
    'Year': [1945, 1951, 1965, 1971, 1981, 1995, 2006, 2020],
    'Event': [
        'ENIAC: First general-purpose electronic computer',
        'UNIVAC: First commercially available computer',
        'Moore\'s Law: Transistor count doubles every 2 years',
        'Intel 4004: First microprocessor',
        'IBM PC: Standardized personal computing',
        'Windows 95: Major OS release for personal computers',
        'Dual-core processors: Introduction of multi-core CPUs',
        'Rise of AI and Quantum Computing: New frontiers in hardware'
    ]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Function to create a timeline visualization
def create_timeline(df):
    """
    Creates a timeline visualization of computer hardware evolution.

    Parameters:
    df (DataFrame): DataFrame containing the timeline data with 'Year' and 'Event' columns.
    """
    try:
        # Set the figure size
        plt.figure(figsize=(10, 6))

        # Plotting the timeline
        plt.plot(df['Year'], [1] * len(df), "ro")  # Red dots for each event
        plt.yticks([])  # Hide y-axis ticks

        # Adding event labels to the timeline
        for i, row in df.iterrows():
            plt.text(row['Year'], 1.02, row['Event'], rotation=45, ha='right', fontsize=10)

        # Set title and labels
        plt.title('Timeline of Computer Hardware Evolution', fontsize=14)
        plt.xlabel('Year', fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.7)

        # Show the plot
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred while creating the timeline: {e}")

# Main execution
if __name__ == "__main__":
    create_timeline(df)
```
