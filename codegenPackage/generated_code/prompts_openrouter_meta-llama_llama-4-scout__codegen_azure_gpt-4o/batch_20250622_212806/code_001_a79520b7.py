"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Write a Python code snippet to compare the properties of HASTELLOY C-276 and HASTELLOY X alloys.
Generated: DETERMINISTIC_a79520b7e6f7d190
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd

# Define the properties of HASTELLOY C-276 and HASTELLOY X alloys
# Data is stored in dictionaries for easy comparison
alloy_properties = {
    "HASTELLOY C-276": {
        "Density (g/cm³)": 8.9,
        "Melting Point (°C)": 1325,
        "Corrosion Resistance": "Excellent",
        "Tensile Strength (MPa)": 690,
        "Applications": ["Chemical Processing", "Pollution Control", "Marine Environments"]
    },
    "HASTELLOY X": {
        "Density (g/cm³)": 8.22,
        "Melting Point (°C)": 1260,
        "Corrosion Resistance": "Good",
        "Tensile Strength (MPa)": 750,
        "Applications": ["Aerospace", "Gas Turbines", "Industrial Furnaces"]
    }
}

# Convert the dictionary to a pandas DataFrame for better visualization
try:
    alloy_df = pd.DataFrame(alloy_properties).T  # Transpose for better readability
    print("Comparison of HASTELLOY C-276 and HASTELLOY X alloys:")
    print(alloy_df)
except Exception as e:
    print(f"An error occurred while processing alloy data: {e}")

# Save the comparison to a CSV file for further analysis
try:
    alloy_df.to_csv("alloy_comparison.csv", index=True)
    print("Comparison data has been saved to 'alloy_comparison.csv'.")
except Exception as e:
    print(f"An error occurred while saving alloy data to CSV: {e}")
```
