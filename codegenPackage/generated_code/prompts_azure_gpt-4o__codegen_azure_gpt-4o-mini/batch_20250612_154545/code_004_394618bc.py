"""
Generated Code Metadata:
========================
Original URL: https://publicvibeindia.blogspot.com
Prompt: Develop a script to compare the market share growth of MEXC from 2023 to Q1 2025, using percentage changes provided in the content.
Generated: DETERMINISTIC_394618bc77aecd8d
Batch ID: 20250612_154545
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

# Define a function to calculate percentage change
def calculate_percentage_change(start_value, end_value):
    """
    Calculate the percentage change between two values.

    Parameters:
    start_value (float): The initial value.
    end_value (float): The final value.

    Returns:
    float: The percentage change from start_value to end_value.
    """
    try:
        if start_value == 0:
            raise ValueError("Start value cannot be zero for percentage change calculation.")
        return ((end_value - start_value) / start_value) * 100
    except Exception as e:
        print(f"Error calculating percentage change: {e}")
        return None

# Market share data for MEXC (example values)
market_share_data = {
    'Year': ['2023', '2024', 'Q1 2025'],
    'Market Share (%)': [5.0, 7.5, 10.0]  # Example market share values
}

# Create a DataFrame
df = pd.DataFrame(market_share_data)

# Calculate percentage changes
df['Percentage Change (%)'] = df['Market Share (%)'].pct_change() * 100

# Display the DataFrame
print("Market Share Data:")
print(df)

# Plotting the market share growth
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Market Share (%)'], marker='o', linestyle='-', color='b')
plt.title('MEXC Market Share Growth (2023 - Q1 2025)')
plt.xlabel('Year')
plt.ylabel('Market Share (%)')
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

# Output the percentage changes
for i in range(1, len(df)):
    year = df['Year'][i]
    change = df['Percentage Change (%)'][i]
    if change is not None:
        print(f"Percentage change from {df['Year'][i-1]} to {year}: {change:.2f}%")
```
