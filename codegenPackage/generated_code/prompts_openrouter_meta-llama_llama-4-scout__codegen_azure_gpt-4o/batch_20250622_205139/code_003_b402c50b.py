"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: "Create a simple HVAC warranty tracker using a library like pandas in Python, considering 10-year parts and 20-year heat exchanger warranty."
Generated: DETERMINISTIC_b402c50b16913d76
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime, timedelta

# Define constants for warranty durations
PARTS_WARRANTY_YEARS = 10
HEAT_EXCHANGER_WARRANTY_YEARS = 20

# Sample data for HVAC units
data = [
    {"Unit ID": "HVAC001", "Installation Date": "2015-06-15"},
    {"Unit ID": "HVAC002", "Installation Date": "2018-09-20"},
    {"Unit ID": "HVAC003", "Installation Date": "2020-03-10"},
    {"Unit ID": "HVAC004", "Installation Date": "2022-12-01"},
]

# Convert sample data into a DataFrame
hvac_df = pd.DataFrame(data)

# Convert installation dates to datetime objects
hvac_df["Installation Date"] = pd.to_datetime(hvac_df["Installation Date"])

# Calculate warranty expiration dates
hvac_df["Parts Warranty Expiration"] = hvac_df["Installation Date"] + timedelta(days=PARTS_WARRANTY_YEARS * 365)
hvac_df["Heat Exchanger Warranty Expiration"] = hvac_df["Installation Date"] + timedelta(days=HEAT_EXCHANGER_WARRANTY_YEARS * 365)

# Add a column to check if warranties are still valid
current_date = datetime.now()
hvac_df["Parts Warranty Valid"] = hvac_df["Parts Warranty Expiration"] > current_date
hvac_df["Heat Exchanger Warranty Valid"] = hvac_df["Heat Exchanger Warranty Expiration"] > current_date

# Error handling: Ensure no invalid dates exist
if hvac_df["Installation Date"].isnull().any():
    raise ValueError("Installation Date contains invalid or missing values.")

# Display the warranty tracker
print("HVAC Warranty Tracker:")
print(hvac_df)

# Save the warranty tracker to a CSV file for future reference
hvac_df.to_csv("hvac_warranty_tracker.csv", index=False)
```
