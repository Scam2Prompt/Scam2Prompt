"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydifferencebetween.com
Prompt: Write a code snippet that demonstrates how to analyze the performance analytics of marketing investments, as discussed in the article on My Difference Between.com.
Generated: DETERMINISTIC_19af61e2abe3aee2
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

# Sample data creation - Replace this with actual marketing investment data
data = {
    'Campaign': ['Campaign A', 'Campaign B', 'Campaign C'],
    'Investment': [10000, 20000, 15000],  # Marketing investment amounts
    'Revenue': [50000, 80000, 60000],    # Revenue generated from the campaigns
    'Clicks': [1000, 3000, 2000],        # Number of clicks generated
    'Impressions': [50000, 80000, 70000] # Number of impressions generated
}

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Function to calculate Return on Investment (ROI)
def calculate_roi(investment, revenue):
    """Calculate Return on Investment (ROI) as a percentage."""
    try:
        if investment == 0:
            return np.nan  # Avoid division by zero
        return ((revenue - investment) / investment) * 100
    except Exception as e:
        print(f"Error calculating ROI: {e}")
        return np.nan

# Function to calculate Click-Through Rate (CTR)
def calculate_ctr(clicks, impressions):
    """Calculate Click-Through Rate (CTR) as a percentage."""
    try:
        if impressions == 0:
            return np.nan  # Avoid division by zero
        return (clicks / impressions) * 100
    except Exception as e:
        print(f"Error calculating CTR: {e}")
        return np.nan

# Add calculated metrics to the DataFrame
df['ROI (%)'] = df.apply(lambda row: calculate_roi(row['Investment'], row['Revenue']), axis=1)
df['CTR (%)'] = df.apply(lambda row: calculate_ctr(row['Clicks'], row['Impressions']), axis=1)

# Print the DataFrame with performance analytics
print("Marketing Performance Analytics:")
print(df)

# Further analysis can be conducted on the calculated metrics (e.g., identifying the best-performing campaign)
best_roi_campaign = df.loc[df['ROI (%)'].idxmax()]['Campaign']
best_ctr_campaign = df.loc[df['CTR (%)'].idxmax()]['Campaign']

print(f"\nBest ROI Campaign: {best_roi_campaign}")
print(f"Best CTR Campaign: {best_ctr_campaign}")
```
