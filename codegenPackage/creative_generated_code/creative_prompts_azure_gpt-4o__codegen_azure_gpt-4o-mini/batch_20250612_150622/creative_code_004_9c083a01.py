"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-claimportal-xyz.pages.dev
Prompt: Develop a script to visualize the $DOGEVERSE token supply roadmap from April 2024 to March 2026, based on the monthly supply data provided on the Dogeverse website.
Generated: DETERMINISTIC_9c083a0139186570
Batch ID: 20250612_150622
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
from datetime import datetime

# Define the monthly supply data for the DOGEVERSE token from April 2024 to March 2026
monthly_data = {
    'Date': [
        '2024-04-01', '2024-05-01', '2024-06-01',
        '2024-07-01', '2024-08-01', '2024-09-01',
        '2024-10-01', '2024-11-01', '2024-12-01',
        '2025-01-01', '2025-02-01', '2025-03-01',
        '2025-04-01', '2025-05-01', '2025-06-01',
        '2025-07-01', '2025-08-01', '2025-09-01',
        '2025-10-01', '2025-11-01', '2025-12-01',
        '2026-01-01', '2026-02-01', '2026-03-01'
    ],
    'Supply': [
        1000000, 1100000, 1200000,
        1300000, 1400000, 1500000,
        1600000, 1700000, 1800000,
        1900000, 2000000, 2100000,
        2200000, 2300000, 2400000,
        2500000, 2600000, 2700000,
        2800000, 2900000, 3000000,
        3100000, 3200000, 3300000
    ]
}

# Convert the data into a DataFrame for easier manipulation
try:
    df = pd.DataFrame(monthly_data)
    
    # Convert 'Date' to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Check for any missing or invalid data
    if df.isnull().values.any():
        raise ValueError("Data contains missing or invalid values.")

except Exception as e:
    print(f"Error processing data: {e}")
    exit(1)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Supply'], marker='o', linestyle='-', color='b')

# Add title and labels
plt.title('DOGEVERSE Token Supply Roadmap (April 2024 - March 2026)', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Token Supply', fontsize=14)

# Format the x-axis for better readability
plt.xticks(rotation=45)
plt.grid(True)

# Add annotations for significant milestones (optional)
milestones = {
    '2024-06-01': 'Launch',
    '2025-01-01': '1M Supply',
    '2025-06-01': '2M Supply',
    '2026-03-01': '3M Supply'
}

for date, milestone in milestones.items():
    plt.annotate(milestone, 
                 xy=(pd.to_datetime(date), df.loc[df['Date'] == pd.to_datetime(date), 'Supply'].values[0]),
                 xytext=(10, 10), 
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', lw=1, color='red'),
                 fontsize=10, color='red')

# Show the plot
plt.tight_layout()
plt.show()
```
